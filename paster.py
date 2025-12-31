import keyboard
import tkinter as tk
import sys, os

root = tk.Tk()
root.title("Paster")
root.geometry("400x200")
root.resizable(False, False)          
root.attributes("-topmost", True)
font_size = 15


# ---------- RESOURCE PATH ---------
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS  # PyInstaller temp dir
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# ---------- FUNCTIONS ----------

def countdown(count):
    if count == 3:
        btn.config(state=tk.DISABLED)

    if count >= 0:
        btn.config(text=str(count), font=("Arial", font_size, "bold"))
        root.after(1000, countdown, count - 1)
    else:
        btn.config(text="Paste", state=tk.NORMAL)
        keyboard.write(txt.get("1.0", "end-1c"))
        

def paste_input():
    countdown(3)

# ---------- UI LAYOUT ----------

frame = tk.Frame(root)
frame.pack(expand=True, padx=10, pady=10)

txt = tk.Text(
    frame,
    height=5,
    width=40,
    font=("Arial", 12)
)
txt.grid(row=0, column=0, pady=(0, 10))

btn = tk.Button(
    frame,
    text="Paste",
    font=("Arial", font_size, "bold"),
    width=10,
    height=1,
    command=paste_input
)
btn.grid(row=1, column=0, pady=(15, 0))

root.iconbitmap(resource_path("paster_logo.ico"))
root.mainloop()
