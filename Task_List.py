import tkinter as tk

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)

def delete_task():
    selected_task = listbox.curselection()
    if selected_task:
        listbox.delete(selected_task)

#Create main window
window = tk.Tk()
window.title("To-Do List")

#Create and pack widgets
entry = tk.Entry(window, width=30)
entry.pack(pady=10)

add_button = tk.Button(window, text=" Add Task", command=add_task)
add_button.pack(pady=5)

delete_button = tk.Button(window, text="Delete Task", command=delete_task)
delete_button.pack(pady=5)

listbox = tk.Listbox(window, selectmode=tk.SINGLE)
listbox.pack(pady=10)

#Start the main loop
window.mainloop()