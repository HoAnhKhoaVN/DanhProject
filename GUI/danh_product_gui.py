import tkinter
import tkinter.messagebox
import customtkinter

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("Danh Product")
        self.geometry(f"{1100}x{580}") # Chỉnh kích thước màn hình


        # Tạo một sidebar để chọn tháng và năm
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")

        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Chọn tháng - năm", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.thang_label = customtkinter.CTkLabel(
            self.sidebar_frame, text="Chọn tháng:", anchor="w")
        self.thang_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.thang_optionemenu = customtkinter.CTkOptionMenu(
            self.sidebar_frame, 
            values = list(map(str,range(1,13)))
        )
        self.thang_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        self.nam_label = customtkinter.CTkLabel(self.sidebar_frame, text="Năm:", anchor="w")
        self.nam_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.nam_optionemenu = customtkinter.CTkOptionMenu(
            self.sidebar_frame, 
            values=['2022', '2023']
        )
        self.nam_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))


        self.bt_truy_xuat = customtkinter.CTkButton(
            self.sidebar_frame, 
            command=self.sidebar_button_event,
            text= "Truy xuất"
            )
        self.bt_truy_xuat.grid(row=9, column=0, padx=20, pady=10)

        # create slider and progressbar frame
        self.hor_frame = customtkinter.CTkFrame(
            self,
            width=350,
            # corner_radius= 0
        )
        
        self.hor_frame.grid(
            row=0,
            column=1,
            columnspan=2, 
            padx=(10, 0), 
            # pady=(10, 0), 
            sticky="nsew",
            rowspan=2
        )
        # self.hor_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(
            self.hor_frame, 
            text=f"Kết quả làm việc {self.thang_optionemenu.get().zfill(2)}/{self.nam_optionemenu.get()}", 
            font=customtkinter.CTkFont(
                size=20,
                weight="bold",
            ),
            text_color='red'
        )
        self.logo_label.grid(row=3, column=3, padx=20, pady=(20, 10))


        # self.main_button_1 = customtkinter.CTkButton(master=self, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"))
        # self.main_button_1.grid(row=3, column=3, padx=(20, 20), pady=(20, 20), sticky="nsew")
        


        
    def sidebar_button_event(self):
        print("Nút truy xuất được click")























        
if __name__ == "__main__":
    app = App()
    app.mainloop()