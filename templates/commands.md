# Crear problema nuevo

Ejemplo: Problema de BFS en CodeForces
```bash
python create_problem.py codeforces div2-850 A-shortest-path bfs graphs
```

Esto creará:

```
# - platforms/codeforces/contests/div2-850/A-shortest-path/
# - topics/graphs/search/BFS.md (si no existe)  
# - topics/graphs/Graph Theory.md (si no existe)
# - Enlaces automáticos entre el problema y los temas
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