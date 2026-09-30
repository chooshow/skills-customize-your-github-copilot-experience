# 📘 Assignment: SQLite Todo App

## 🎯 Objective

Learn how to persist application data with SQLite in Python. You will create a small todo application that initializes a database, performs CRUD operations, and keeps tasks available between program runs.

## 📝 Tasks

### 🛠️ Initialize the SQLite Database

#### Description
Complete the database setup so the program creates a SQLite database file and a `todos` table when it starts.

#### Requirements
Completed program should:

- Connect to the database path defined in the starter code
- Create a `todos` table if it does not already exist
- Store an integer `id`, a task `title`, and a boolean-style `completed` value
- Commit changes and close the connection correctly

### 🛠️ Implement Todo CRUD Operations

#### Description
Implement functions for adding, listing, updating, and deleting todo items. Use parameterized SQL queries for values supplied by the user.

#### Requirements
Completed program should:

- Add a todo and return its generated ID
- Return all todos in a predictable order
- Mark a selected todo as completed or incomplete
- Delete a selected todo and report whether it existed
- Preserve todo data after the program exits and starts again

### 🛠️ Build the Command-Line Workflow

#### Description
Connect the database functions to the provided command-line menu so a user can manage todos through repeated actions.

#### Requirements
Completed program should:

- Display the available actions and current todo list
- Accept commands to add, list, complete, and delete todos
- Handle an invalid command or unknown todo ID without crashing
- Close the database connection when the application ends

Example interaction:

```text
1. Add todo
2. List todos
3. Complete todo
4. Delete todo
5. Quit
Choose an action: 1
Todo title: Read about SQL
Added todo #1
```
