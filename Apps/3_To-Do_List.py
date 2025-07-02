import customtkinter as ctk

# Initialize window
app = ctk.CTk()
app.title("To-Do List")
app.geometry("300x400")

# Entry box for task
task_entry = ctk.CTkEntry(app, placeholder_text="Enter a task")
task_entry.pack(pady=10)

# Function to add task
def add_task():
    task = task_entry.get()
    if task:
        task_label = ctk.CTkLabel(app, text=task)
        task_label.pack()
        task_entry.delete(0, 'end')

# Add button
add_button = ctk.CTkButton(app, text="Add Task", command=add_task)
add_button.pack(pady=5)

# Run the GUI
app.mainloop()