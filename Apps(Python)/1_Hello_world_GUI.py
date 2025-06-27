import tkinter as tk

# Creates the main window
w = tk.Tk()
w.title("Hello App")
w.geometry("200x100")  # Sets size of window (width x height)

# Creates a label widget
label = tk.Label(w, text="Hello, World!", font=("Calibri", 16))

# Packs the label into the window
label.pack(pady=20)
                                                                                                               
# Start the GUI event loop
w.mainloop()