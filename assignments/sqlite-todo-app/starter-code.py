"""Starter code for the SQLite Todo App assignment."""

import sqlite3
from pathlib import Path

DATABASE_PATH = Path(__file__).with_name("todos.db")


def connect_database():
    """Return a connection to the local SQLite database."""
    return sqlite3.connect(DATABASE_PATH)


def initialize_database(connection):
    """Create the todos table if it does not already exist."""
    pass


def add_todo(connection, title):
    """Insert a todo and return its generated ID."""
    pass


def list_todos(connection):
    """Return todos ordered by ID."""
    pass


def set_completed(connection, todo_id, completed=True):
    """Set a todo's completion state and return whether it existed."""
    pass


def delete_todo(connection, todo_id):
    """Delete a todo and return whether it existed."""
    pass


def display_todos(connection):
    """Print all todos in a readable format."""
    todos = list_todos(connection)
    if not todos:
        print("No todos yet.")
        return

    for todo_id, title, completed in todos:
        marker = "x" if completed else " "
        print(f"{todo_id}. [{marker}] {title}")


def run():
    connection = connect_database()
    initialize_database(connection)

    try:
        while True:
            print("\n1. Add todo")
            print("2. List todos")
            print("3. Complete todo")
            print("4. Delete todo")
            print("5. Quit")
            choice = input("Choose an action: ").strip()

            if choice == "1":
                title = input("Todo title: ").strip()
                if title:
                    todo_id = add_todo(connection, title)
                    print(f"Added todo #{todo_id}")
                else:
                    print("Title cannot be empty.")
            elif choice == "2":
                display_todos(connection)
            elif choice == "3":
                todo_id = int(input("Todo ID: "))
                if set_completed(connection, todo_id):
                    print("Todo completed.")
                else:
                    print("Todo not found.")
            elif choice == "4":
                todo_id = int(input("Todo ID: "))
                if delete_todo(connection, todo_id):
                    print("Todo deleted.")
                else:
                    print("Todo not found.")
            elif choice == "5":
                break
            else:
                print("Invalid action.")
    finally:
        connection.close()


if __name__ == "__main__":
    run()
