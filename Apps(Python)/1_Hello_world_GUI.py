import tkinter as tk

# Creates the main window
root = tk.Tk()
root.title("Hello App")
root.geometry("200x100")  # Sets size of window (width x height)

# Creates a label widget
label = tk.Label(root, text="Hello, World!", font=("Cabili", 16))

# Packs the label into the window
label.pack(pady=20)
                                                                                                               
# Start the GUI event loop
root.mainloop()