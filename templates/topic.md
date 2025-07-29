# BFS (Breadth-First Search)

#graphs/search/bfs #algorithm #competitive-programming

**Tema padre:** [[topics/graphs/Graph Theory|Graph Theory]] > [[topics/graphs/search/Search|Búsqueda en Grafos]]

## 🎯 Definición
BFS es un algoritmo de búsqueda que explora todos los vértices a distancia k antes de explorar vértices a distancia k+1.

## 🔑 Conceptos Clave
- **Cola (Queue):** Estructura FIFO para mantener el orden de exploración
- **Visitados:** Array para evitar ciclos infinitos
- **Niveles:** Distancia desde el nodo fuente
- **Complejidad:** O(V + E) en tiempo, O(V) en espacio

## 💻 Implementación Template
```cpp
vector<int> bfs(int start, vector<vector<int>>& adj) {
    int n = adj.size();
    vector<int> dist(n, -1);
    queue<int> q;
    
    dist[start] = 0;
    q.push(start);
    
    while (!q.empty()) {
        int u = q.front();
        q.pop();
        
        for (int v : adj[u]) {
            if (dist[v] == -1) {
                dist[v] = dist[u] + 1;
                q.push(v);
            }
        }
    }
    
    return dist;
}
\```

## 🎯 Casos de Uso
- Camino más corto en grafos no ponderados
- Componentes conexas
- Detección de ciclos
- Coloreo de grafos bipartitos
- Laberinto con obstáculos

## 🔗 Conceptos Relacionados
- [[topics/graphs/search/DFS|DFS]] - Alternativa de búsqueda en profundidad
- [[topics/graphs/shortest-path/Dijkstra|Dijkstra]] - Extensión para grafos ponderados
- [[topics/data-structures/trees/Queue|Queue]] - Estructura de datos utilizada

## 🧠 Problemas Resueltos

### Fácil (800-1200)
```dataview
LIST file.name
FROM #graphs/search/bfs AND #competitive-programming 
WHERE contains(file.path, "platforms/") AND (contains(tags, "#easy") OR contains(tags, "#800") OR contains(tags, "#1000") OR contains(tags, "#1200"))
SORT fecha DESC
\```

### Medio (1200-1600)
```dataview
LIST file.name
FROM #graphs/search/bfs AND #competitive-programming 
WHERE contains(file.path, "platforms/") AND (contains(tags, "#medium") OR contains(tags, "#1400") OR contains(tags, "#1600"))
SORT fecha DESC
\```

### Difícil (1600+)
```dataview
LIST file.name
FROM #graphs/search/bfs AND #competitive-programming 
WHERE contains(file.path, "platforms/") AND (contains(tags, "#hard") OR contains(tags, "#1800") OR contains(tags, "#2000"))
SORT fecha DESC
\```

## 🎯 Estado Personal
- **Nivel de dominio:** 8/10
- **Problemas resueltos:** 
```dataview
TABLE rows.length as "Total"
FROM #graphs/search/bfs AND #competitive-programming 
WHERE contains(file.path, "platforms/")
\```
- **Última práctica:** 
```dataview
LIST file.name
FROM #graphs/search/bfs AND #competitive-programming 
WHERE contains(file.path, "platforms/")
SORT fecha DESC
LIMIT 1
\```
- **Necesita repaso:** #needs-review

## 📚 Problemas Para Practicar
- [ ] Codeforces - Maze (encontrar camino más corto)
- [ ] LeetCode - Word Ladder
- [ ] AtCoder - Grid Path Finding

## 🏆 Variaciones Importantes
- **Multi-source BFS:** Múltiples puntos de inicio
- **0-1 BFS:** Para grafos con pesos 0 y 1
- **BFS en matriz:** Navegación en grillas 2D
- **BFS con estados:** Cuando cada nodo tiene múltiples estados