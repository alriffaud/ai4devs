#!/usr/bin/env python3
"""Main entry point for CLI tool for AI Copilot Productivity Sprint."""
import argparse
import json
import os
import time

CONFIG_FILE = 'config.json'
TIMELOG_FILE = 'time_log.json'

# Prompt: "Generate a function to load or initialize config."
def load_config(path=CONFIG_FILE):
    """Load existing configuration or create default one."""
    if not os.path.exists(path):
        default = {'tasks': []}
        with open(path, 'w') as f:
            json.dump(default, f, indent=2)
        return default
    with open(path) as f:
        return json.load(f)

# Prompt: "Generate a function to save config back to file."
def save_config(config, path=CONFIG_FILE):
    with open(path, 'w') as f:
        json.dump(config, f, indent=2)

# Prompt: "Generate parser for add-task, log-time, report commands."
def create_parser():
    parser = argparse.ArgumentParser(description="Productivity Sprint CLI Tool")
    sub = parser.add_subparsers(dest='command')

    parser_add = sub.add_parser('add-task', help='Add a new task')
    parser_add.add_argument('--id', type=int, required=True, help='Task ID')
    parser_add.add_argument('--desc', type=str, required=True, help='Task description')
    parser_add.add_argument('--estimate', type=int, required=True, help='Time estimate in minutes')

    parser_log = sub.add_parser('log-time', help='Log time for a task')
    parser_log.add_argument('--id', type=int, required=True, help='Task ID')
    parser_log.add_argument('--time', type=int, required=True, help='Time spent in minutes')

    parser_rep = sub.add_parser('report', help='Generate report')

    return parser

# Prompt: "Generate function to log time into a JSON log file."
def log_time_entry(task_id, minutes):
    entry = {'id': task_id, 'time': minutes, 'timestamp': time.time()}
    logs = []
    if os.path.exists(TIMELOG_FILE):
        with open(TIMELOG_FILE) as f:
            logs = json.load(f)
    logs.append(entry)
    with open(TIMELOG_FILE, 'w') as f:
        json.dump(logs, f, indent=2)

# Prompt: "Generate report function to compare estimates vs actuals."
def generate_report(config, time_logs):
    report = []
    for t in config.get('tasks', []):
        actual = sum(e['time'] for e in time_logs if e['id']==t['id'])
        report.append({
            'id': t['id'],
            'description': t['desc'],
            'estimate': t['estimate'],
            'actual': actual
        })
    print(json.dumps(report, indent=2))

def main():
    config = load_config()
    parser = create_parser()
    args = parser.parse_args()

    if args.command == 'add-task':
        # AI suggestion: ensure no duplicate IDs
        new_task = {'id': args.id, 'desc': args.desc, 'estimate': args.estimate}
        config['tasks'] = [t for t in config.get('tasks', []) if t['id']!=args.id] + [new_task]
        save_config(config)
        print(f"Task {args.id} added.")
    elif args.command == 'log-time':
        log_time_entry(args.id, args.time)
        print(f"Logged {args.time} minutes for task {args.id}.")
    elif args.command == 'report':
        logs = []
        if os.path.exists(TIMELOG_FILE):
            with open(TIMELOG_FILE) as f:
                logs = json.load(f)
        generate_report(config, logs)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
