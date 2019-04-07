from flask import Flask, render_template, url_for, request
import os
import todo

app = Flask(__name__)


@app.route("/")
def index():
    return "You have reached the index."


@app.route("/file/<file>")
def show_text_file(file):
    title = "ToDo"
    filename = file + ".txt"
    file_text = []
    if not os.path.isfile(filename):
        return render_template(
            "file_list.html", title="File Not Found", list_data=["Cannot find file."]
        )
    with open(filename, "r") as f:
        for line in f:
            file_text.append(line.strip())
    return render_template("todo_list.html", title=title, list_data=file_text)


@app.route("/todo", methods=["GET", "POST"])
def show_todo():
    todo_file = "todo.json"
    title = "ToDo List"
    if request.method == "POST":
        new_name = request.form["todo_name"]
        new_details = request.form["todo_details"]
        # go do something with the results
        print(new_name, ";", new_details)
        todo.update_todo(todo_file, new_name, new_details)
    return render_template(
        "todo_list.html", title=title, todo_data=todo.display_todo(todo_file)
    )


@app.route("/temp")
def show_template():
    title = "Template"
    test = "Test"
    return render_template("todo_list.html", title=title, list_data=test)


if __name__ == "__main__":
    app.run(debug=True)
