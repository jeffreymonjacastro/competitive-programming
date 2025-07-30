# Progreso de Hoy

## ✅ Problemas Resueltos Hoy
```dataview
LIST file.name
FROM #competitive-programming 
WHERE contains(file.path, "platforms/") 
    AND fecha = date(today)
\```

## 🔄 Problemas Para Repasar
```dataview
TABLE file.name as "Problema", dificultad as "Dificultad"
FROM #competitive-programming 
WHERE contains(tags, "#needs-review")
LIMIT 5
\```