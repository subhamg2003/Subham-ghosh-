import json
import os
import tkinter as tk
from tkinter import messagebox

# Declare variables
tasks = None
task_list = None
description_entry = None
priority_entry = None
due_date_entry = None

# Function to load tasks from a JSON file
def load_tasks():
    if os.path.exists('tasks.json'):
        with open('tasks.json', 'r') as file:
            return json.load(file)
    else:
        return []
# Function to save tasks to a JSON file
def save_tasks(tasks):
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file, indent=4)

# Function to add a task
def add_task(description, priority, due_date):
    task = {
        'description': description,
        'priority': priority,
        'due_date': due_date,
        'completed': False
    }
    tasks.append(task)
    save_tasks(tasks)
    messagebox.showinfo("Task Added", f"Task added: {description}")
    description_entry.delete(0, tk.END)  # Clear the input fields
    priority_entry.delete(0, tk.END)
    due_date_entry.delete(0, tk.END)

# Function to remove a task
def remove_task(index):
    if index < 0 or index >= len(tasks):
        messagebox.showerror("Error", "Invalid task number.")
    else:
        removed_task = tasks.pop(index)
        save_tasks(tasks)
        messagebox.showinfo("Task Removed", f"Task removed: {removed_task['description']}")
        display_tasks()

# Function to mark a task as completed
def complete_task(index):
    if index < 0 or index >= len(tasks):
        messagebox.showerror("Error", "Invalid task number.")
    else:
        tasks[index]['completed'] = True
        save_tasks(tasks)
        messagebox.showinfo("Task Completed", f"Task marked as completed: {tasks[index]['description']}")
        display_tasks()

# Function to display tasks
def display_tasks():
    task_list.delete(0, tk.END)  # Clear the task list
    for i, task in enumerate(tasks):
        status = "Done" if task['completed'] else "Not Done"
        task_list.insert(tk.END, f"{i + 1}. {task['description']} (Priority: {task['priority']}, Due Date: {task['due_date']}, Status: {status}")

# Event handler for the Add Task button
def add_task_button_click():
    description = description_entry.get()
    priority = priority_entry.get()
    due_date = due_date_entry.get()
    add_task(description, priority, due_date)
    display_tasks()

# Event handler for the Remove Task button
def remove_task_button_click():
    index = task_list.curselection()
    if index:
        remove_task(index[0])

# Event handler for the Complete Task button
def complete_task_button_click():
    index = task_list.curselection()
    if index:
        complete_task(index[0])

# Main function
def main():
    global tasks
    global task_list
    global description_entry
    global priority_entry
    global due_date_entry

    tasks = load_tasks()

    # Create the main application window
    root = tk.Tk()
    root.title("Task Manager")
    root.geometry("800x600")
    root['background']= 'pink'
    # Create and configure the input fields
    description_label = tk.Label(root, text="Task Description:")
    description_label.pack()
    description_entry = tk.Entry(root)
    description_entry.pack()

    priority_label = tk.Label(root, text="Priority:")
    priority_label.pack()
    priority_entry = tk.Entry(root)
    priority_entry.pack()

    due_date_label = tk.Label(root, text="Due Date (YYYY-MM-DD):")
    due_date_label.pack()
    due_date_entry = tk.Entry(root)
    due_date_entry.pack()

    add_task_button = tk.Button(root, text="Add Task", command=add_task_button_click)
    add_task_button.pack()

    # Create and configure the task list
    task_list = tk.Listbox(root,width=80,height=20, selectmode=tk.SINGLE)
    task_list.pack()

    display_tasks()

    remove_task_button = tk.Button(root, text="Remove Task", command=remove_task_button_click)
    remove_task_button.pack()

    complete_task_button = tk.Button(root, text="Complete Task", command=complete_task_button_click)
    complete_task_button.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
