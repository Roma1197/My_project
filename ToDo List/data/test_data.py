from datetime import datetime
import json

tasks = []
TASK_TEST = [
    {
        'id': 1,
        'title': 'Wash hands',
        'description': 'Wash hands and face with soap and',
        'priority': 5,
        'due_date': datetime(2022, 11, 1, 12, 37),
        'done': True
    },
    {
        'id': 2,
        'title': 'Wash face',
        'description': 'Wash face with soap and',
        'priority': 3,
        'due_date': datetime(2022, 11, 1, 12, 37),
        'done': True
    },
    {
        'id': 3,
        'title': 'Run',
        'description': 'Run five stadium circles',
        'priority': 2,
        'due_date': datetime(2022, 11, 1, 12, 37),
        'done': True
    },
    {
        'id': 4,
        'title': 'Feed the dog',
        'description': 'Feed the dog',
        'priority': 4,
        'due_date': datetime(2022, 11, 1, 12, 37),
        'done': True
    }
]