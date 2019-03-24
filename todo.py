import json
import os

def get_todo(file):
    with open(file, "r") as f:
        todo_dict = json.load(f)
        return todo_dict.get("todo_list")

def write_todo(data, file):
    try:
        with open(file, "w") as f:
            json.dump(data, f, indent=4)
        return True
    except:
        return False