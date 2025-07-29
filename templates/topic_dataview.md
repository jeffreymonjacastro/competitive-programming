## 🔍 Vista Dinámica de Problemas

```dataview
TABLE 
    file.name as "Problema",
    plataforma as "Plataforma", 
    dificultad as "Dificultad",
    fecha as "Fecha"
FROM #competitive-programming 
WHERE contains(file.path, "platforms/") 
    AND (contains(tags, "#dp") OR contains(file.outlinks, this.file.link))
SORT fecha DESC
\```

```dataview
LIST
FROM #competitive-programming 
WHERE contains(tags, "#dp") AND contains(tags, "#needs-review")
\```