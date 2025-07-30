import os
import sys
import shutil
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
    """Converts tags to hierarchical format and returns paths"""
    hierarchical_tags = []
    tag_paths = []
    
    for tag in tags:
        if tag in TAG_TO_PATH:
            path = TAG_TO_PATH[tag]
            tag_paths.append(path)
            
            parts = path.split('/')[1:-1]  

            print(f"{tag} parts: {parts}")
            if parts[0] not in hierarchical_tags:
                hierarchical_tags.append(parts[0])

            # Agregar tag específico
            specific_tag = tag.replace('-', '-')
            hierarchical_tags.append(specific_tag)

    return sorted(hierarchical_tags), sorted(tag_paths)

def create_problem_structure(platform, contest, problem_name, difficulty, tags):
    base_path = f"platforms/{platform}"
    if contest and contest != "practice":
        problem_path = f"{base_path}/contests/{contest}/{problem_name}"
    else:
        problem_path = f"{base_path}/practice/{problem_name}"
    
    os.makedirs(problem_path, exist_ok=True)

    # Obtain hierarchical tags and file paths
    hierarchical_tags, topic_paths = get_hierarchical_tags(tags)

    topic_links = []
    for path in topic_paths:
        topic_name = path.split('/')[-1].replace('.md', '')
        topic_links.append(f"[[{path.replace('.md', '')}|{topic_name}]]")
    
    readme_content = f"""---
platform: {platform.title()}
contest: {contest if contest and contest != "practice" else 'Practice'}
difficulty: {difficulty if difficulty else 0}
date: {datetime.now().strftime('%Y-%m-%d')}
tags:
{('\n').join(f'  - {tag}' for tag in hierarchical_tags)}
---
# [{problem_name.replace('-', ' ').title()}](link)

## 📓 Related Topics
{('\n').join(f'- {link}' for link in topic_links) if topic_links else '[Topic 1] [Topic 2]'}

## 📖 Description
[Brief summary of the problem]

## 💡 Approach
[Your approach and why it works]

## ⚡ Complexity
- **Time:** O(?)
- **Space:** O(?)

## 🔍 Key Points
- [Important insight 1]
- [Important insight 2]

## 🔗 Related Problems
- [Similar Problem 1]
- [Similar Problem 2]

## 🔄 Versions
- `solution.cpp` - Main solution 
"""

    with open(f"{problem_path}/{problem_name.replace('-', ' ')}.md", "w", encoding='utf-8') as f:
        f.write(readme_content)
    
    shutil.copy("templates/template.cpp", f"{problem_path}/solution.cpp")
    
    for topic_path in topic_paths:
        create_topic_if_not_exists(topic_path)
    
    print(f"✅ Problema creado: {problem_path}")
    print(f"📝 README: {problem_path}/README.md")
    print(f"💻 Código: {problem_path}/solution.cpp")
    print(f"🏷️ Tags jerárquicos: {' '.join(hierarchical_tags)}")
    print(f"📚 Temas vinculados: {len(topic_paths)}")

def create_topic_if_not_exists(topic_path):
    """Creates a hierarchical topic file if it does not exist"""
    if os.path.exists(topic_path):
        return

    os.makedirs(os.path.dirname(topic_path), exist_ok=True)

    parts = topic_path.split('/')
    topic_name = parts[-1].replace('.md', '')
    category = parts[1] if len(parts) > 1 else 'general'
    subcategory = parts[2] if len(parts) > 2 else None
    
    specific_tag = f"#{topic_name}"
    
    parent_topic = f"[[topics/{category}/{category.title().replace('-', ' ')}|{category.title()}]]"
    
    topic_content = f"""# {topic_name}

**Parent Topic:** {parent_topic}

## 🎯 Definition
[Algorithm/technique definition]

## 🔑 Key Concepts
- **Concept 1:** [Explanation]
- **Concept 2:** [Explanation]
- **Complexity:** O(?) time, O(?) space

## 💻 Implementation Template
```cpp
// Basic template for {topic_name}
// Add implementation here
```

## 🎯 Use Cases
- [Use case 1]
- [Use case 2]

## 🔗 Related Concepts
- [Related Concept 1]
- [Related Concept 2]

## 🧠 Solved Problems
### Easy (800 - 1200)
```dataview
TABLE platform, difficulty, date
FROM {specific_tag}
WHERE contains(file.path, "platforms/") AND difficulty >= 800 AND difficulty <= 1200
SORT date DESC
```

### Medium (1200-1600)
```dataview
TABLE platform, difficulty, date
FROM {specific_tag}
WHERE contains(file.path, "platforms/") AND difficulty > 1200 AND difficulty <= 1600
SORT date DESC
```

### Hard (1600+)
```dataview
TABLE platform, difficulty, date
FROM {specific_tag}
WHERE contains(file.path, "platforms/") AND difficulty > 1600
SORT date DESC
```

## 🎯 Personal Status
- **Mastery Level:** ?/10
- **Problems Solved:** 
```dataview
TABLE rows.length as "Total"
FROM {specific_tag}
WHERE contains(file.path, "platforms/")
```

- **Last Practice:** 
```dataview
TABLE platform, date
FROM {specific_tag}
WHERE contains(file.path, "platforms/")
SORT date DESC
LIMIT 1
```

## 📚 Study Resources
- [Resource 1](URL)
- [Resource 2](URL)

## 🏆 Important Variations
- **Variation 1:** [Description]
- **Variation 2:** [Description]
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
        print("Uso: python create_problem.py <platform> <contest> <problem_name> <difficulty> [tag1] [tag2]...")
        print("Ejemplo: python create_problem.py codeforces div2-850 A-watermelon bfs implementation")
        print("\nPara ver todos los tags disponibles:")
        print("python create_problem.py --list-tags")
        sys.exit(1)
    
    platform = sys.argv[1]
    contest = sys.argv[2]
    problem_name = sys.argv[3]
    difficulty = sys.argv[4] if len(sys.argv) > 4 and sys.argv[4].isdigit() else None
    tags = sys.argv[5:] if len(sys.argv) > 5 else []

    if not tags:
        print("⚠️  Advertencia: No se especificaron tags. Se creará el problema sin enlaces automáticos a temas.")
        response = input("¿Continuar? (y/N): ")
        if response.lower() != 'y':
            sys.exit(0)

    create_problem_structure(platform, contest, problem_name, difficulty, tags)