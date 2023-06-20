import tkinter as tk
from tkinter import ttk
import customtkinter

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


# root window
root = tk.Tk()
root.geometry("240x100")
root.title('Login')
root.resizable(0, 0)

# configure the grid
root.columnconfigure(0, weight=1) # Chỉnh cột thứ 0 có kích thước là 1x
root.columnconfigure(1, weight=3) # Chỉnh cột thứ 1 có kích thước là 3x


# username
username_label = ttk.Label(root, text="Username:")
username_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5) # Thêm vào lưới ở dòng 0 cột 0

appearance_mode_optionemenu = customtkinter.CTkOptionMenu(root, values=["Light", "Dark", "System"])
appearance_mode_optionemenu.grid(column=1, row=0, sticky=tk.E, padx=5, pady=5)

# password
password_label = ttk.Label(root, text="Password:")
password_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)

password_entry = ttk.Entry(root,  show="*") # Hiển thị mật khẩu là *
password_entry.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)

# login button
login_button = ttk.Button(root, text="Login")
login_button.grid(column=1, row=3, sticky=tk.E, padx=5, pady=5)


root.mainloop() # Hiển thị của sổ
