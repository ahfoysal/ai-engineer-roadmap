# Phase 0 — Programming Foundations

**Goal:** Be fluent in Python and comfortable with the developer tools every AI engineer uses daily.
**Time:** 3–4 weeks (skip parts you know).

---

## 🎯 Outcomes
By the end you can: write clean Python, manipulate data structures, use Git/GitHub, work in the terminal, and run basic SQL queries.

## ✅ Checklist

### Python core
- [ ] Variables, types, f-strings, operators
- [ ] Control flow: `if/elif/else`, `for`, `while`, comprehensions
- [ ] Data structures: list, dict, set, tuple — and when to use each
- [ ] Functions, `*args/**kwargs`, default args, lambdas
- [ ] Modules, packages, `import`, virtual environments (`venv`, `uv`)
- [ ] File I/O, JSON, error handling (`try/except`)
- [ ] OOP: classes, methods, `__init__`, inheritance, dunder methods
- [ ] Iterators, generators, decorators (enough to read them)
- [ ] Type hints (`list[int]`, `Optional`, `dict[str, Any]`)

### Tooling
- [ ] Terminal basics: `cd`, `ls`, `grep`, pipes, env vars
- [ ] Git: `clone`, `add`, `commit`, `push`, `pull`, `branch`, `merge`, resolving conflicts
- [ ] GitHub: repos, PRs, README, `.gitignore`
- [ ] Jupyter / Colab notebooks
- [ ] Package management with `pip` and `uv`

### SQL (you'll need it for data)
- [ ] `SELECT`, `WHERE`, `ORDER BY`, `LIMIT`
- [ ] `JOIN` (inner/left), `GROUP BY`, aggregate functions
- [ ] Subqueries, basic CTEs

## 📚 Best resources
- **Python** — [Python for Everybody (free, Dr. Chuck)](https://www.py4e.com/) · [Automate the Boring Stuff (free book)](https://automatetheboringstuff.com/) · [CS50P (Harvard, free)](https://cs50.harvard.edu/python/)
- **Git** — [Git & GitHub crash course (freeCodeCamp)](https://www.youtube.com/watch?v=RGOj5yH7evk) · [Oh My Git! (game)](https://ohmygit.org/)
- **SQL** — [SQLBolt (free, interactive)](https://sqlbolt.com/) · [Mode SQL Tutorial](https://mode.com/sql-tutorial/)
- **Terminal** — [MIT Missing Semester](https://missing.csail.mit.edu/)

## 🛠️ Phase project
**Build a CLI data tool.** A Python command-line app that reads a CSV, computes summary stats, and writes a JSON report. Must use functions, type hints, error handling, and be committed to GitHub with a README.

## <a name="self-test"></a>🧪 Self-test (skip Phase 0 if you can do all of these)
1. Write a generator that yields Fibonacci numbers.
2. Explain the difference between a list and a tuple, and why dict keys must be hashable.
3. Clone a repo, make a branch, commit a change, open a PR.
4. Write a SQL query that joins two tables and groups by a column.

➡️ Next: [Phase 1 — Math & Statistics](01-math-stats.md)
