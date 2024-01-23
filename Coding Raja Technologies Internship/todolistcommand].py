#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
import json
from datetime import datetime, timedelta

# File to store tasks
TASKS_FILE = "tasks.json"

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            tasks = json.load(file)
        return tasks
    else:
        return {"tasks": []}

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=2)

def add_task(tasks, description, priority, due_date):
    task = {
        "description": description,
        "priority": priority,
        "due_date": due_date.strftime("%Y-%m-%d") if due_date else None
    }
    tasks["tasks"].append(task)
    save_tasks(tasks)

def list_tasks(tasks):
    if tasks["tasks"]:
        print("\nTask List:")
        for idx, task in enumerate(tasks["tasks"], start=1):
            print(f"{idx}. {task['description']} - Priority: {task['priority']}, Due Date: {task['due_date']}")
    else:
        print("\nNo tasks found.")

def main():
    tasks = load_tasks()

    while True:
        print("\n1. Add Task\n2. List Tasks\n3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            description = input("Enter task description: ")
            priority = input("Enter task priority (High/Medium/Low): ")
            
            due_date_str = input("Enter due date (YYYY-MM-DD) or press Enter for no due date: ")
            due_date = datetime.strptime(due_date_str, "%Y-%m-%d") if due_date_str else None

            add_task(tasks, description, priority, due_date)
            print("Task added successfully!")

        elif choice == "2":
            list_tasks(tasks)

        elif choice == "3":
            print("Exiting the application. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()


# In[ ]:




