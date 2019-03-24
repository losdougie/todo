from flask import Flask, render_template
import os

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
            "todo_list.html", title="File Not Found", list_data=["Cannot find file."]
        )
    with open(filename, "r") as f:
        for line in f:
            file_text.append(line.strip())
    return render_template("todo_list.html", title=title, list_data=file_text)


@app.route("/temp")
def show_template():
    title = "Template"
    test = "Test"
    return render_template("todo_list.html", title=title, list_data=test)

if __name__ == "__main__":
    app.run(debug=True)
