import customtkinter as ctk

# Creates the main window
w = ctk.CTk()
w.title("Hello App")
w.geometry("200x100")  # Sets size of window (width x height)

# Creates a label widget (Corrected: CTkLabel instead of Label)
label = ctk.CTkLabel(w, text="Hello, World!", font=("Calibri", 16))

# Packs the label into the window
label.pack(pady=20)

# Start the GUI event loop
w.mainloop()