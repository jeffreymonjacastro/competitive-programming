---
state: full
tags:
  - greedy
  - algorithm
---
# competitive-programming
Competitive Programming codes &amp; learning


Hello World

```dataview
TABLE platform, contest, difficulty, status, date, tags
FROM #greedy 
```

```dataviewjs
let pages = dv.pages('#cp');

let results = [];
for (let page of pages) {
    let content = await dv.io.load(page.file.path);
    let match = content.match(/## 📖 Description\s*\n((?:(?!##).)*)/s);
    if (match) {
        results.push([
            dv.fileLink(page.file.path, false, page.file.name),
            match[1].trim()
        ]);
    }
}

dv.table(["Archivo", "Description"], results);
```
