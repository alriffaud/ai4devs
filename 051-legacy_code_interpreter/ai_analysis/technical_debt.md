# Technical Debt and Code Smells

This document identifies **technical debt** and **code smells** within the legacy **code**.

## Smells Detected
1. Long methods (>50 lines) in `generate_report()`.
2. Duplicate code blocks for CSV and JSON parsing.
3. Poor naming conventions (`do_it()`, `process_data()`).

## Debt Metrics
- Estimated 4 hotspots with Cyclomatic complexity >10.
- Hard-coded file paths causing configuration issues.
