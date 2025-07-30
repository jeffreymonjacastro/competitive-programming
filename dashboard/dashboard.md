 🏆 Dashboard de Programación Competitiva

## 📊 Resumen Hoy
**Problemas resueltos hoy:**
```dataview
TABLE platform, difficulty 
FROM #cp
WHERE date = date(today)
```

## 🎯 Por Tema (Top 5)

```dataview
TABLE length(rows) as Problems
FROM #cp 
WHERE contains(file.path, "platforms/")
FLATTEN filter(
	file.tags, (t) => 
	t != "#cp" AND
	t != "#codeforces"
) as tags
GROUP BY tags
SORT length(rows) DESC
LIMIT 5
```

## 🔄 Necesitan Repaso
```dataview
LIST file.name
FROM #competitive-programming AND #needs-review
WHERE contains(file.path, "platforms/")
LIMIT 10
\```

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