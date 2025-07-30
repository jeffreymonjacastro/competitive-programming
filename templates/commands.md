# Crear problema nuevo

Ejemplo: Problema de BFS en CodeForces con dificultad y tags
```bash
python create_problem.py codeforces 850D2 A-shortest-path 1800 bfs graphs 
```

Esto creará:

```
# - platforms/codeforces/contests/850D2/A-shortest-path/
# - topics/graphs/search/BFS.md (si no existe)
# - topics/graphs/Graph Theory.md (si no existe)
# - Enlaces automáticos entre el problema y los temas
```

Ejemplo: Problema de DP en AtCoder 
```bash
python create_problem.py atcoder 1200D3 B-Longest-Subsequence
```

Esto creará solamente la carpeta al archivo, el .md, el .cpp

```
# - platforms/atcoder/contests/1200D3/B-Longest-Subsequence/
```

# Ver Tags disponibles
```bash
python create_problem.py --list-tags
```

Salida:
```
# 🏷️ Tags disponibles:
# 
# 📂 Graphs:
#    • bfs
#    • dfs  
#    • dijkstra
#    • kruskal
# 
# 📂 Dynamic-programming:
#    • dp
#    • knapsack
#    • lis
```

# Organizar problemas

## Escanear problemas existentes y ver estadísticas
```bash
python organize_topics.py --scan
```

## Crear archivos índice faltantes
```bash
python organize_topics.py --create-indexes
```