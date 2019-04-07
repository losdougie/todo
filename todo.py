import json
import os


def get_todo(file):
    with open(file, "r") as f:
        todo_dict = json.load(f)
        return todo_dict


def display_todo(file):
    todo_list = get_todo(file)
    completed_items = []
    for item in todo_list:
        status = todo_list[item].get("status")
        if status.lower() == "completed" or status.lower() == "done":
            completed_items.append(item)
    for item in completed_items:
        todo_list.pop(item)
        # del todo_list[item] # alternative way to delete item from a dict
    return todo_list


def update_todo(file, new_title, new_details, time="", status="not started"):
    current_list = get_todo(file)

    max_item_num = 1
    for item in current_list:
        current_item_num = int(item[4:])
        if current_item_num > max_item_num:
            max_item_num = current_item_num

    new_item = "todo{}".format(max_item_num + 1)

    current_list[new_item] = {
        "name": new_title,
        "details": new_details,
        "time": time,
        "status": status,
    }

    write_todo(current_list, file)


def write_todo(data, file):
    try:
        with open(file, "w") as f:
            json.dump(data, f, indent=4)
        return True
    except:
        return False
