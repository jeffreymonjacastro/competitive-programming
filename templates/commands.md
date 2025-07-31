# Commands 

## Create new problem

Syntax:
```bash
python create_problem.py <platform> <contest_id> <problem_name> [difficulty] [tags...]
```
1. `<platform>`: The platform where the problem is hosted (e.g., `codeforces`, `atcoder`).
2. `<contest_id>`: The contest identifier (e.g., `850D2`, `B408`).
3. `<problem_name>`: The name of the problem (e.g., `A-shortest-path`).
4. `[difficulty]`: (Optional) The difficulty of the problem (e.g., `1800`).
5. `[tags...]`: (Optional) A list of tags associated with the problem (e.g., `bfs`, `graphs`).

Example: BFS problem in CodeForces with difficulty and tags
```bash
python create_problem.py codeforces 850D2 A-shortest-path 1800 bfs graphs 
```

This will create:

```
# - platforms/codeforces/contests/850D2/A-shortest-path/
# - topics/graphs/search/BFS.md (if it doesn't exist)
# - topics/graphs/Graph Theory.md (if it doesn't exist)
# - Automatic links between the problem and topics
```

Example: DP problem in AtCoder 
```bash
python create_problem.py atcoder 1200D3 B-Longest-Subsequence
```

This will only create the folder, the .md file, and the .cpp file

```
# - platforms/atcoder/contests/1200D3/B-Longest-Subsequence/
```

## View available tags
```bash
python create_problem.py --list-tags
```

Output:
```
# 🏷️ Available tags:
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

## Organize problems

### Scan existing problems and view statistics
```bash
python organize_topics.py --scan
```

### Create missing index files
```bash
python organize_topics.py --create-indexes
```

## Execution 

### C++

With input.txt file:

```bash
g++ -o solution solution.cpp  # Compile
Get-Content input.txt | .\solution.exe # Run with input redirection
```

With manual input:

```bash
g++ -o solution solution.cpp  # Compile
.\solution.exe  # Run
```

### Java

With input.txt file:

```bash
javac solution.java                    # Compile
Get-Content input.txt | java Solution  # Run with input redirection
```

With manual input:

```bash
javac solution.java  # Compile
java Solution         # Run
```

### Python

With input.txt file:

```bash
Get-Content input.txt | python solution.py  # Run with input redirection
```
With manual input:

```bash
python solution.py # Run
```

### JavaScript

With input.txt file:

```bash
Get-Content input.txt | node solution.js  # Run with input redirection
```

With manual input:

```bash
node solution.js  # Run
```