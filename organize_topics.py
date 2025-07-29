import os
import re
from create_problem import TAG_TO_PATH  
from pathlib import Path

def scan_existing_problems():
    """Escanea problemas existentes y sugiere reorganización"""
    platforms_dir = Path("platforms")
    if not platforms_dir.exists():
        print("❌ Directorio platforms/ no encontrado")
        return
    
    problems_found = []
    
    # Buscar todos los README.md en platforms/
    for readme_path in platforms_dir.rglob("README.md"):
        try:
            with open(readme_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
            # Extraer información del problema
            problem_info = {
                'path': str(readme_path),
                'name': readme_path.parent.name,
                'tags': extract_tags_from_content(content),
                'topics': extract_topics_from_content(content)
            }
            problems_found.append(problem_info)
            
        except Exception as e:
            print(f"⚠️  Error leyendo {readme_path}: {e}")
    
    print(f"📊 Encontrados {len(problems_found)} problemas")
    
    # Analizar tags más comunes
    all_tags = []
    for problem in problems_found:
        all_tags.extend(problem['tags'])
    
    tag_count = {}
    for tag in all_tags:
        tag_count[tag] = tag_count.get(tag, 0) + 1
    
    print("\n🏷️ Tags más comunes:")
    for tag, count in sorted(tag_count.items(), key=lambda x: x[1], reverse=True)[:10]:
        print(f"   {tag}: {count} problemas")
    
    # Sugerir archivos de temas faltantes
    suggest_missing_topics(tag_count.keys())

def extract_tags_from_content(content):
    """Extrae tags de un archivo markdown"""
    tags = []
    
    # Buscar tags con formato #tag
    hash_tags = re.findall(r'#([a-zA-Z0-9\-/_]+)', content)
    tags.extend(hash_tags)
    
    # Buscar tags en sección específica
    tags_section = re.search(r'## 🏷️ Tags\s*\n(.*?)(?=\n##|\Z)', content, re.DOTALL)
    if tags_section:
        section_content = tags_section.group(1)
        # Extraer tags adicionales
        additional_tags = re.findall(r'`([^`]+)`', section_content)
        tags.extend(additional_tags)
    
    return list(set(tags))  # Remover duplicados

def extract_topics_from_content(content):
    """Extrae enlaces a temas de un archivo markdown"""
    topics = []
    
    # Buscar enlaces tipo [[topic]]
    wiki_links = re.findall(r'\[\[([^\]|]+)(?:\|[^\]]+)?\]\]', content)
    topics.extend(wiki_links)
    
    return topics

def suggest_missing_topics(existing_tags):
    """Sugiere archivos de temas que podrían faltar"""
    print("\n📚 Archivos de temas sugeridos:")
    
    for tag in existing_tags:
        if tag in TAG_TO_PATH:
            topic_path = TAG_TO_PATH[tag]
            if not os.path.exists(topic_path):
                print(f"   ❌ Faltante: {topic_path}")
            else:
                print(f"   ✅ Existe: {topic_path}")

def create_index_files():
    """Crea archivos índice para las carpetas principales"""
    topic_dirs = [
        "topics/graphs",
        "topics/dynamic-programming", 
        "topics/data-structures",
        "topics/mathematics",
        "topics/strings",
        "topics/search-and-sort",
        "topics/techniques"
    ]
    
    for topic_dir in topic_dirs:
        index_path = f"{topic_dir}/{topic_dir.split('/')[-1].replace('-', ' ').title()}.md"
        if not os.path.exists(index_path):
            print(f"📄 Creando índice: {index_path}")
            create_index_file(topic_dir, index_path)

def create_index_file(topic_dir, index_path):
    """Crea un archivo índice para una categoría"""
    category_name = topic_dir.split('/')[-1].replace('-', ' ').title()
    
    # Escanear subcarpetas
    subdirs = []
    if os.path.exists(topic_dir):
        for item in os.listdir(topic_dir):
            item_path = os.path.join(topic_dir, item)
            if os.path.isdir(item_path):
                subdirs.append(item)
    
    # Crear contenido del índice
    content = f"""# {category_name}

        #{topic_dir.split('/')[-1]} #algorithm #competitive-programming

        ## 🎯 Definición
        [Descripción general de {category_name.lower()}]

        ## 🗺️ Mapa de Conceptos

    """
    
    # Agregar enlaces a subcategorías
    for subdir in sorted(subdirs):
        subdir_title = subdir.replace('-', ' ').title()
        content += f"### {subdir_title}\n"
        
        # Buscar archivos .md en la subcarpeta
        subdir_path = os.path.join(topic_dir, subdir)
        if os.path.exists(subdir_path):
            for file in os.listdir(subdir_path):
                if file.endswith('.md'):
                    file_name = file.replace('.md', '')
                    relative_path = f"topics/{topic_dir.split('/')[-1]}/{subdir}/{file_name}"
                    content += f"- [[{relative_path}|{file_name}]]\n"
        content += "\n"
    
    content += f"""
        ## 📊 Estadísticas Generales
        ```dataview
        TABLE rows.length as "Problemas"
        FROM #{topic_dir.split('/')[-1]} AND #competitive-programming 
        WHERE contains(file.path, "platforms/")
        GROUP BY file.tags
        SORT rows.length DESC
        \```

        ## 🧠 Todos los Problemas
        ```dataview
        TABLE 
            file.name as "Problema",
            plataforma as "Plataforma", 
            dificultad as "Dificultad",
            fecha as "Fecha"
        FROM #{topic_dir.split('/')[-1]} AND #competitive-programming 
        WHERE contains(file.path, "platforms/")
        SORT fecha DESC
        \```
    """
    
    # Crear directorio si no existe
    os.makedirs(os.path.dirname(index_path), exist_ok=True)
    
    # Escribir archivo
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == "--scan":
        scan_existing_problems()
    elif len(sys.argv) > 1 and sys.argv[1] == "--create-indexes":
        create_index_files()
    else:
        print("Uso:")
        print("  python organize_topics.py --scan          # Escanear problemas existentes")
        print("  python organize_topics.py --create-indexes # Crear archivos índice")
