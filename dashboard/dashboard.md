# Dashboard
## 📊 Today
```dataview
TABLE platform, status, difficulty 
FROM #cp
WHERE date = date(today) 
```

## 🎯 Top 5 most solved topics
```dataview
TABLE length(rows) as Problems
FROM #cp 
FLATTEN filter(
	file.tags, (t) => 
	t != "#cp" AND
	t != "#codeforces"
) as tags
GROUP BY tags
SORT length(rows) DESC
LIMIT 5
```

## 🔄 Needs Review Problems
```dataview
TABLE platform, difficulty
FROM #cp 
WHERE status = "🟣review"
LIMIT 10
```

## 📈 Progreso por Dificultad
```dataview
TABLE 
    rows.length as "Cantidad",
    round(rows.length / 50 * 100, 1) + "%" as "Progreso"
FROM #competitive-programming 
WHERE contains(file.path, "platforms/")
GROUP BY choice(contains(tags, "#easy"), "Fácil", choice(contains(tags, "#medium"), "Medio", "Difícil"))
\```

## 📊 Estadísticas por Plataforma

```dataview
TABLE 
    rows.length as "Problemas",
    length(filter(rows.file.tags, (t) => contains(t, "#solved"))) as "Resueltos",
    round(length(filter(rows.file.tags, (t) => contains(t, "#solved"))) / rows.length * 100, 1) + "%" as "Tasa Éxito"
FROM #competitive-programming 
WHERE contains(file.path, "platforms/")
GROUP BY split(file.path, "/")[1]
SORT rows.length DESC
\```

## 🎯 Conceptos que necesitan más práctica

```dataview
TABLE 
    rows.length as "Problemas Totales",
    length(filter(rows.file.tags, (t) => contains(t, "#needs-review"))) as "Necesitan Repaso",
    choice(length(filter(rows.file.tags, (t) => contains(t, "#needs-review"))) / rows.length > 0.3, "🔴 Crítico", choice(length(filter(rows.file.tags, (t) => contains(t, "#needs-review"))) / rows.length > 0.1, "🟡 Atención", "🟢 Bien")) as "Estado"
FROM #competitive-programming 
WHERE contains(file.path, "platforms/") AND (startswith(file.tags[0], "#graphs") OR startswith(file.tags[0], "#dp") OR startswith(file.tags[0], "#math"))
GROUP BY split(filter(file.tags, (t) => contains(t, "/") AND !contains(t, "competitive-programming")), "/")[0]
SORT length(filter(rows.file.tags, (t) => contains(t, "#needs-review"))) DESC
\```