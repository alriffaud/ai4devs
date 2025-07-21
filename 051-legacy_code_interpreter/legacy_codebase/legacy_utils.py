
## Challenges
"""
- Poor **structure** with mixed concerns in single file.  
- Minimal or missing docstrings.  
- Tight coupling between classes and helper functions.  
- No test suite.
---
"""

## Metrics
"""
- **Lines of code:** ~350  
- **Functions:** 12 top‑level functions  
- **Classes:** 2  
- **Average function length:** ~25 lines  
- **Cyclomatic complexity:** high in 4 functions (estimated > 10)
"""

## History
"""
- **Origin:** Developed in 2017 for internal reporting tool.  
- **Maintenance:** Last updated in 2018, no further refactoring.  
- **Contributors:** Single author; no code review history.
"""

## Pain Points
"""
- High **complexity** in `generate_report()` function: mixes I/O, formatting, and business logic.  
- Poor naming: e.g., `do_it()`, `process_data()` with vague descriptions.  
- Lack of configuration abstraction: hard‑coded file paths.  
- Duplicate code blocks handling CSV vs JSON.
"""

## Complexity
"""
- Functions with nested loops and conditionals up to 4 levels deep.  
- No modularization: all logic in one file.  
- Estimated maintainability index: very low.
"""
