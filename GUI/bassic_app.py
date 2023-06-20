import customtkinter
        
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Danh Product!!!")
        self.geometry("400x180")
        self.grid_columnconfigure(0, weight=1)
        print(help(self.grid_columnconfigure))
        self.grid_rowconfigure((0, 1), weight=1)
        print(help(self.grid_rowconfigure))

        self.checkbox_1 = customtkinter.CTkCheckBox(self, text="checkbox 1")
        self.checkbox_1.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="w")
        self.checkbox_2 = customtkinter.CTkCheckBox(self, text="checkbox 2")
        self.checkbox_2.grid(row=1, column=0, padx=10, pady=(10, 0), sticky="w")
        self.button = customtkinter.CTkButton(self, text="my button", command=self.button_callback)
        self.button.grid(row=3, column=0, padx=10, pady=10, sticky="ew")

    def button_callback(self):
        print("button pressed")

if __name__ == "__main__":
    app = App()
    app.mainloop()