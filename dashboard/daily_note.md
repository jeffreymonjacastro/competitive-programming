# Progreso de Hoy

## ✅ Problemas Resueltos Hoy
```dataview
TABLE platform, difficulty 
WHERE contains(file.path, "platforms/") AND date = date(today)
```

## 🔄 Problemas Para Repasar
```dataview
TABLE file.name as "Problema", dificultad as "Dificultad"
FROM #competitive-programming 
WHERE contains(tags, "#needs-review")
LIMIT 5
```