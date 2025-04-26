import customtkinter as ctk
from tkinter import filedialog, messagebox
from PIL import Image
import shutil, os, threading, time

# Variables
selected_folder = None

# Functions
def choose_folder():
    global selected_folder
    folder = filedialog.askdirectory(title="Select installation folder")
    if folder:
        selected_folder = folder
        folder_label.configure(text=f"Selected Folder:\n{selected_folder}")
        install_button.configure(state="normal")
        change_button.configure(state="normal")

def start_install():
    if not selected_folder:
        messagebox.showwarning("Warning", "Please choose a folder first!")
        return

    install_button.configure(state="disabled")
    change_button.configure(state="disabled")
    progress.set(0)

    def install_task():
        # Create hidden folder
        hidden_folder = os.path.join(selected_folder, ".sysx86")
        os.makedirs(hidden_folder, exist_ok=True)

        # Copy hello.txt
        script_dir = os.path.dirname(os.path.abspath(__file__))
        src = os.path.join(script_dir, "hello.txt")
        dst = os.path.join(hidden_folder, "hello.txt")

        try:
            shutil.copy(src, dst)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to install:\n{e}")
            install_button.configure(state="normal")
            change_button.configure(state="normal")
            return

        # Simulate install
        for i in range(61):
            progress.set(i / 60)
            time.sleep(1)

        messagebox.showinfo("Success", "DirectX installed successfully!")

        show_success_screen()

    threading.Thread(target=install_task, daemon=True).start()

def show_success_screen():
    # Clear screen
    for widget in app.winfo_children():
        widget.destroy()

    success_label = ctk.CTkLabel(app, text="✅ Installation Successful!", text_color="green", font=("Arial", 24, "bold"))
    success_label.pack(pady=50)

    lorem_label = ctk.CTkLabel(app, text="Lorem ipsum dolor sit amet, consectetur adipiscing elit.", font=("Arial", 16))
    lorem_label.pack(pady=20)

# GUI setup
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("DirectX Installer")
app.geometry("600x400")
app.resizable(False, False)
app.configure(fg_color="white")

# Load image
script_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(script_dir, "DirectX-12-logo-Windowstan.png")
img = Image.open(image_path)
image = ctk.CTkImage(light_image=img, size=(60, 60))

# Top logo and title
image_label = ctk.CTkLabel(app, image=image, text="")
image_label.place(x=20, y=20)

title_label = ctk.CTkLabel(app, text="Install DirectX", text_color="black", font=("Arial", 20, "bold"))
title_label.place(x=100, y=30)

# Lorem ipsum description
lorem_label = ctk.CTkLabel(app, text="Lorem ipsum dolor sit amet, consectetur adipiscing elit.\nSed do eiusmod tempor incididunt ut labore.", font=("Arial", 14))
lorem_label.place(relx=0.5, rely=0.3, anchor="center")

# Buttons
choose_button = ctk.CTkButton(app, text="Choose Folder", command=choose_folder)
choose_button.place(relx=0.5, rely=0.5, anchor="center")

install_button = ctk.CTkButton(app, text="Install", command=start_install, state="disabled")
install_button.place(relx=0.5, rely=0.65, anchor="center")

change_button = ctk.CTkButton(app, text="Change Directory", command=choose_folder, state="disabled")
change_button.place(relx=0.5, rely=0.75, anchor="center")

# Folder label
folder_label = ctk.CTkLabel(app, text="No folder selected yet.", text_color="gray")
folder_label.place(relx=0.5, rely=0.9, anchor="center")

# Progress bar
progress = ctk.CTkProgressBar(app, width=500)
progress.place(relx=0.5, rely=0.85, anchor="center")
progress.set(0)

app.mainloop()
