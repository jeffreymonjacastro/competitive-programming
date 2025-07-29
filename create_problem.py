import os
import sys
from datetime import datetime

TAG_TO_PATH = {
    # Graphs
    'bfs': 'topics/graphs/traversal/BFS.md',
    'dfs': 'topics/graphs/traversal/DFS.md',
    'dijkstra': 'topics/graphs/shortest-path/Dijkstra.md',
    'bellman-ford': 'topics/graphs/shortest-path/Bellman-Ford.md',
    'floyd-warshall': 'topics/graphs/shortest-path/Floyd-Warshall.md',
    'kruskal': 'topics/graphs/mst/Kruskal.md',
    'prim': 'topics/graphs/mst/Prim.md',
    'topological-sort': 'topics/graphs/special/Topological-Sort.md',

    # DP
    'dp': 'topics/dynamic-programming/Dynamic-Programming.md',
    'lis': 'topics/dynamic-programming/classic/LIS.md',
    'knapsack': 'topics/dynamic-programming/classic/Knapsack.md',
    'tree-dp': 'topics/dynamic-programming/tree-dp/Tree-DP.md',
    'digit-dp': 'topics/dynamic-programming/digit-dp/Digit-DP.md',
    'bitmask-dp': 'topics/dynamic-programming/bitmask-dp/Bitmask-DP.md',

    # Data Structures
    'segment-tree': 'topics/data-structures/trees/Segment-Tree.md',
    'fenwick-tree': 'topics/data-structures/trees/Fenwick-Tree.md',
    'dsu': 'topics/data-structures/disjoint-set/DSU.md',
    'trie': 'topics/data-structures/strings/Trie.md',
    
    # math
    'number-theory': 'topics/mathematics/number-theory/Number-Theory.md',
    'gcd': 'topics/mathematics/number-theory/GCD-LCM.md',
    'primes': 'topics/mathematics/number-theory/Prime-Numbers.md',
    'combinatorics': 'topics/mathematics/combinatorics/Combinatorics.md',
    'modular-arithmetic': 'topics/mathematics/number-theory/Modular-Arithmetic.md',

    # Strings
    'kmp': 'topics/strings/pattern-matching/KMP.md',
    'z-algorithm': 'topics/strings/pattern-matching/Z-Algorithm.md',
    'string-hashing': 'topics/strings/string-processing/String-Hashing.md',

    # Sorting and Searching
    'binary-search': 'topics/search-and-sort/binary-search/Binary-Search.md',
    'two-pointers': 'topics/search-and-sort/two-pointers/Two-Pointers.md',
    'sliding-window': 'topics/search-and-sort/two-pointers/Sliding-Window.md',
    'complete-search': 'topics/search-and-sort/complete-search/Complete-Search.md',

    # Prefix y Suffix
    'prefix-sum': 'topics/prefix-suffix/Prefix-Sum.md',
    'suffix-array': 'topics/prefix-suffix/Suffix-Array.md',
    'z-function': 'topics/prefix-suffix/Z-Function.md',

    # Techniques
    'greedy': 'topics/techniques/Greedy.md',
    'divide-conquer': 'topics/techniques/Divide-and-Conquer.md',
    'backtracking': 'topics/techniques/Backtracking.md',

    # Geometry
    'line-geometry': 'topics/geometry/Line-Geometry.md',
    'sweep-line': 'topics/geometry/Sweep-Line.md',
    'polygon-geometry': 'topics/geometry/Polygon-Geometry.md',
    'convex-hull': 'topics/geometry/Convex-Hull.md',

    # Miscellaneous
    'bitwise-operations': 'topics/miscellaneous/Bitwise-Operations.md',
    'hashing': 'topics/miscellaneous/Hashing.md',
    'games': 'topics/miscellaneous/Games.md',
}

def get_hierarchical_tags(tags):
    """Convierte tags simples a tags jerárquicos"""
    hierarchical_tags = []
    tag_paths = []
    
    for tag in tags:
        if tag in TAG_TO_PATH:
            path = TAG_TO_PATH[tag]
            tag_paths.append(path)
            
            # Crear tag jerárquico basado en la ruta
            parts = path.split('/')[1:-1]  # Excluir 'topics' y el archivo .md
            if parts:
                hierarchical_tag = '/'.join(parts).replace('-', '-')
                if hierarchical_tag not in hierarchical_tags:
                    hierarchical_tags.append(f"#{hierarchical_tag}")
            
            # Agregar tag específico
            specific_tag = tag.replace('-', '-')
            hierarchical_tags.append(f"#{specific_tag}")
    
    return hierarchical_tags, tag_paths

def create_problem_structure(platform, contest, problem_name, tags):
    # Crear estructura de directorios
    base_path = f"platforms/{platform}"
    if contest and contest != "practice":
        problem_path = f"{base_path}/contests/{contest}/{problem_name}"
    else:
        problem_path = f"{base_path}/practice/{problem_name}"
    
    os.makedirs(problem_path, exist_ok=True)
    
    # Obtener tags jerárquicos y rutas de archivos
    hierarchical_tags, topic_paths = get_hierarchical_tags(tags)
    
    # Crear enlaces a temas
    topic_links = []
    for path in topic_paths:
        # Convertir ruta a nombre legible para el enlace
        topic_name = path.split('/')[-1].replace('.md', '')
        topic_links.append(f"[[{path.replace('.md', '')}|{topic_name}]]")
    
    # Crear README template con sintaxis de Obsidian
    readme_content = f"""# {problem_name.replace('-', ' ').title()}
#{platform} #[dificultad] {' '.join(hierarchical_tags)}

**Plataforma:** {platform.title()}
**Contest:** {contest if contest and contest != "practice" else 'Practice'}
**Dificultad:** [Rating/Nivel]
**Fecha de resolución:** {datetime.now().strftime('%d/%m/%Y')}
**Tiempo empleado:** [HH:MM]

## 🔗 Enlaces
- **Problema:** [URL del problema]
- **Submission:** [URL de submission]

## 📓 Temas relacionados
{' '.join(topic_links) if topic_links else '[[Topic 1]] [[Topic 2]]'}

## 📖 Descripción
[Breve resumen del problema]

## 💡 Enfoque
[Tu approach y por qué funciona]

## ⚡ Complejidad
- **Tiempo:** O(?)
- **Espacio:** O(?)

## 🔍 Puntos Clave
- [Insight importante 1]
- [Insight importante 2]

## 📚 Conceptos Aprendidos
[Qué aprendiste resolviendo este problema]

## 🔗 Problemas Relacionados
- [[Problema Similar 1]]
- [[Problema Similar 2]]

## 🔄 Versiones
- `solution.cpp` - Solución principal
"""

    with open(f"{problem_path}/{problem_name.replace('-', ' ')}.md", "w", encoding='utf-8') as f:
        f.write(readme_content)
    
    # Crear archivo de solución
    solution_template = """#include <bits/stdc++.h>

using namespace std;
#define cpu()                  \
  ios::sync_with_stdio(false); \
  cin.tie(nullptr);
#define ll long long
#define lld long double
const int mod = 1e9 + 7;

ll binPow(ll a, ll b) {
  a %= mod;
  ll result = 1;
  while (b > 0) {
    if (b & 1LL)
      result = (result * a) % mod;
    a = (a * a) % mod;
    b >>= 1;
  }
  return result;
}

void solve() {}

int main() {
  cpu();
  int t;
  t = 1;
  // cin >> t;
  while (t--)
    solve();
  return 0;
}

"""
    
    with open(f"{problem_path}/solution.cpp", "w") as f:
        f.write(solution_template)
    
    # Crear archivos de temas si no existen
    for topic_path in topic_paths:
        create_topic_if_not_exists(topic_path)
    
    print(f"✅ Problema creado: {problem_path}")
    print(f"📝 README: {problem_path}/README.md")
    print(f"💻 Código: {problem_path}/solution.cpp")
    print(f"🏷️ Tags jerárquicos: {' '.join(hierarchical_tags)}")
    print(f"📚 Temas vinculados: {len(topic_paths)}")

def create_topic_if_not_exists(topic_path):
    """Crea un archivo de tema jerárquico si no existe"""
    if os.path.exists(topic_path):
        return
    
    # Crear directorio si no existe
    os.makedirs(os.path.dirname(topic_path), exist_ok=True)
    
    # Determinar el tipo de archivo basado en la ruta
    parts = topic_path.split('/')
    topic_name = parts[-1].replace('.md', '')
    category = parts[1] if len(parts) > 1 else 'general'
    subcategory = parts[2] if len(parts) > 2 else None
    
    # Crear tag jerárquico
    if subcategory:
        main_tag = f"#{category}/{subcategory}"
        specific_tag = f"#{category}/{subcategory}/{topic_name.lower().replace(' ', '-')}"
    else:
        main_tag = f"#{category}"
        specific_tag = f"#{category}/{topic_name.lower().replace(' ', '-')}"
    
    # Determinar tema padre
    if subcategory:
        parent_topic = f"[[topics/{category}/{category.title().replace('-', ' ')}|{category.title()}]]"
    else:
        parent_topic = "[[Competitive Programming]]"
    
    topic_content = f"""# {topic_name}

**Tema padre:** {parent_topic}

## 🎯 Definición
[Definición del algoritmo/técnica]

## 🔑 Conceptos Clave
- **Concepto 1:** [Explicación]
- **Concepto 2:** [Explicación]
- **Complejidad:** O(?) tiempo, O(?) espacio

## 💻 Implementación Template
```cpp
// Template básico para {topic_name}
// Agregar implementación aquí
```

## 🎯 Casos de Uso
- [Caso de uso 1]
- [Caso de uso 2]

## 🔗 Conceptos Relacionados
- [[Concepto Relacionado 1]]
- [[Concepto Relacionado 2]]

## 🧠 Problemas Resueltos
### Fácil (800 - 1200)
```dataview
LIST file.name
FROM {specific_tag} AND #competitive-programming 
WHERE contains(file.path, "platforms/") AND (contains(tags, "#easy") OR contains(tags, "#800") OR contains(tags, "#1000") OR contains(tags, "#1200"))
SORT fecha DESC
```

### Medio (1200-1600)
```dataview
LIST file.name
FROM {specific_tag} AND #competitive-programming 
WHERE contains(file.path, "platforms/") AND (contains(tags, "#medium") OR contains(tags, "#1400") OR contains(tags, "#1600"))
SORT fecha DESC
```

### Difícil (1600+)
```dataview
LIST file.name
FROM {specific_tag} AND #competitive-programming 
WHERE contains(file.path, "platforms/") AND (contains(tags, "#hard") OR contains(tags, "#1800") OR contains(tags, "#2000"))
SORT fecha DESC
```

## 🎯 Estado Personal
- **Nivel de dominio:** ?/10
- **Problemas resueltos:** 
```dataview
TABLE rows.length as "Total"
FROM {specific_tag} AND #competitive-programming 
WHERE contains(file.path, "platforms/")
```

- **Última práctica:** 
```dataview
LIST file.name
FROM {specific_tag} AND #competitive-programming 
WHERE contains(file.path, "platforms/")
SORT fecha DESC
LIMIT 1
```

## 📚 Recursos de Estudio
- [Recurso 1](URL)
- [Recurso 2](URL)

## 🏆 Variaciones Importantes
- **Variación 1:** [Descripción]
- **Variación 2:** [Descripción]
"""
    
    with open(topic_path, "w", encoding='utf-8') as f:
        f.write(topic_content)
    print(f"📚 Tema creado: {topic_path}")

def list_available_tags():
    """Muestra todos los tags disponibles organizados por categoría"""
    print("\n🏷️ Tags disponibles:")
    
    categories = {}
    for tag, path in TAG_TO_PATH.items():
        category = path.split('/')[1]
        if category not in categories:
            categories[category] = []
        categories[category].append(tag)
    
    for category, tags in categories.items():
        print(f"\n📂 {category.title()}:")
        for tag in sorted(tags):
            print(f"   • {tag}")

if __name__ == "__main__":
    if sys.argv[1] == "--list-tags":
        list_available_tags()
        sys.exit(0)

    if len(sys.argv) < 4:
        print("Uso: python create_problem.py <platform> <contest> <problem_name> [tag1] [tag2]...")
        print("Ejemplo: python create_problem.py codeforces div2-850 A-watermelon bfs implementation")
        print("\nPara ver todos los tags disponibles:")
        print("python create_problem.py --list-tags")
        sys.exit(1)
    
    platform = sys.argv[1]
    contest = sys.argv[2]
    problem_name = sys.argv[3]
    tags = sys.argv[4:] if len(sys.argv) > 4 else []
    
    if not tags:
        print("⚠️  Advertencia: No se especificaron tags. Se creará el problema sin enlaces automáticos a temas.")
        response = input("¿Continuar? (y/N): ")
        if response.lower() != 'y':
            sys.exit(0)
    
    create_problem_structure(platform, contest, problem_name, tags)