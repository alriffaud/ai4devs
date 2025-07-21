# AI Prompting Notes

This document summarizes prompting **strategies**, **prompts**, **AI suggestions**, and **examples** during feature implementation.

## 1. Prompts
- **Configuration loading**  
  - Prompt: “Generate a function to load or initialize config file in Python.”  
- **Parser creation**  
  - Prompt: “Generate an argparse setup for commands add-task, log-time, report.”  
- **Time logging**  
  - Prompt: “Generate a function to append a time log entry into a JSON file.”

## 2. Strategies
- **Be specific**: Mention file formats (JSON), command names, and argument types.  
- **Incremental prompts**: Start with function signature, then request body details.  
- **Refinement loops**: After initial suggestion, clarify handling of edge cases (e.g., duplicate IDs).

## 3. AI Suggestions
| Step               | Suggestion Summary                                              |
|--------------------|-----------------------------------------------------------------|
| load_config        | Created default JSON structure and file if missing.            |
| create_parser      | Used subparsers for separate commands with required arguments. |
| log_time_entry     | Used timestamp and appended logs to JSON list.                 |
| generate_report    | Aggregated times and printed formatted JSON.                   |

## 4. Examples
### Example Prompt
> “Generate a report function that compares estimate vs actual times using Python.”

### Example AI Output
```python
def generate_report(config, logs):
    for t in config['tasks']:
        total = sum(l['time'] for l in logs if l['id']==t['id'])
        print(f"Task {t['id']}: estimate={t['estimate']}, actual={total}")
```

### Iteration
- **Refinement**: After seeing print-only output, prompted: “Format report as JSON array and pretty-print.”

*These notes document how different **prompts** led to diverse **AI suggestions**, and which **strategies** yielded the best results.*