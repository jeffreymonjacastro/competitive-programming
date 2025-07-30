# Graph Theory

#graphs #algorithm #competitive-programming

## 🎯 Definición
Los grafos son estructuras de datos que modelan relaciones entre objetos mediante vértices y aristas. Son fundamentales en programación competitiva.

## 🗺️ Mapa de Conceptos

### [[topics/graphs/search/BFS|Búsqueda en Grafos]]
- [[topics/graphs/search/BFS|BFS (Breadth-First Search)]]
- [[topics/graphs/search/DFS|DFS (Depth-First Search)]]
- [[topics/graphs/search/Bidirectional Search|Búsqueda Bidireccional]]

### [[topics/graphs/shortest-path/Single Source|Caminos Más Cortos]]
#### Fuente Única
- [[topics/graphs/shortest-path/Dijkstra|Algoritmo de Dijkstra]]
- [[topics/graphs/shortest-path/Bellman Ford|Algoritmo de Bellman-Ford]]
- [[topics/graphs/shortest-path/SPFA|SPFA]]

#### Todos los Pares
- [[topics/graphs/shortest-path/Floyd Warshall|Floyd-Warshall]]
- [[topics/graphs/shortest-path/Johnson Algorithm|Algoritmo de Johnson]]

### [[topics/graphs/mst/MST|Árbol de Expansión Mínima]]
- [[topics/graphs/mst/Kruskal|Algoritmo de Kruskal]]
- [[topics/graphs/mst/Prim|Algoritmo de Prim]]

### [[topics/graphs/flow/Max Flow|Flujo Máximo]]
- [[topics/graphs/flow/Ford Fulkerson|Ford-Fulkerson]]
- [[topics/graphs/flow/Dinic|Algoritmo de Dinic]]

### Algoritmos Especiales
- [[topics/graphs/special/Topological Sort|Ordenamiento Topológico]]
- [[topics/graphs/special/Strongly Connected Components|Componentes Fuertemente Conexas]]

## 📊 Estadísticas Generales
```dataview
TABLE rows.length as "Problemas"
FROM #graphs AND #competitive-programming 
WHERE contains(file.path, "platforms/")
GROUP BY file.tags
SORT rows.length DESC
```

## 🧠 Todos los Problemas de Grafos
```dataview
TABLE 
    file.name as "Problema",
    plataforma as "Plataforma", 
    dificultad as "Dificultad",
    fecha as "Fecha"
FROM #graphs AND #competitive-programming 
WHERE contains(file.path, "platforms/")
SORT fecha DESC
```

## 🎯 Estado de Aprendizaje
- [x] Representación de grafos
- [x] BFS/DFS básico
- [x] Dijkstra
- [ ] Algoritmos de flujo
- [ ] Grafos planares

## 📚 Recursos
- [CP-Algorithms Graph Theory](https://cp-algorithms.com/graph/)
- [USACO Guide - Graph Theory](https://usaco.guide/gold/shortest-paths/)