import sqlite3

def main():
    db = sqlite3.connect("tasks.db")
    c = db.cursor()
    drop_task_table_query = "DROP TABLE IF EXISTS tasks"
    create_task_table_query = "CREATE TABLE tasks(name TEXT, status TEXT, priority INTEGER)"
    c.execute(drop_task_table_query)
    c.execute(create_task_table_query)
    db.commit()
    load_query = "INSERT INTO tasks(name, status, priority) VALUES (?,?,?)"
    load_values = ("task1", "working", 1)
                 #{"name": "task1", "status": "working", "priority": "1"}
    c.execute(load_query, load_values)
    db.commit()
    c.execute("SELECT * FROM tasks")
    print(c.fetchall())
    db.close()


if __name__ == "__main__":
    main()