# Dashboard
## 📊 Today
```dataview
TABLE platform, status, difficulty 
FROM #cp
WHERE date = date(today) 
```

## 🔄 Needs Review Problems
```dataview
TABLE platform, difficulty
FROM #cp 
WHERE status = "🟣Review"
LIMIT 10
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

## 📈 Difficulty Progress
```dataview
TABLE length(rows) as Problems
FROM #cp 
WHERE status = "🟢Solved"
GROUP BY difficulty 
SORT difficulty ASC
```

## 📊 Platform Progress
```dataview
TABLE length(rows) as Problems
FROM #cp 
WHERE status = "🟢Solved"
GROUP BY platform
SORT Problems DESC
```
