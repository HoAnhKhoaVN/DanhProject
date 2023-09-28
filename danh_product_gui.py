import tkinter
import tkinter.messagebox
import customtkinter
from typing import Text

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"
from utils import load_pickle
from toan_bo_data import ToanBoData
from nhan_vien import NhanVien

class App(customtkinter.CTk):
    def __init__(
            self,
            data_path : Text = 'full_data_v3.plk'
        ):
        super().__init__()

        # region Lấy dữ liệu
        self.data : ToanBoData = load_pickle(fn = data_path)
        lst_nam = self.data.get_danh_sach_nam()
        # endregion


        # configure window
        self.title("Danh Product")
        self.geometry(f"{1100}x{580}") # Chỉnh kích thước màn hình


        # Tạo một sidebar để chọn tháng và năm
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")

        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Chọn tháng - năm", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        # region Chọn năm
        self.nam_label = customtkinter.CTkLabel(self.sidebar_frame, text="Năm:", anchor="w")
        self.nam_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.nam_optionemenu = customtkinter.CTkOptionMenu(
            self.sidebar_frame, 
            values=lst_nam
        )
        self.nam_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 20))
        # endregion
        # region Chọn tháng
        self.thang_label = customtkinter.CTkLabel(
            self.sidebar_frame, text="Chọn tháng:", anchor="w")
        self.thang_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.thang_optionemenu = customtkinter.CTkOptionMenu(
            self.sidebar_frame, 
            values = self.data.get_danh_sach_thang(nam = self.nam_optionemenu.get() )
        )
        self.thang_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 10))
        # endregion

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

        # region Logo Kết quả công việc
        self.logo_label = customtkinter.CTkLabel(
            self.hor_frame, 
            text=f"Kết quả làm việc {self.thang_optionemenu.get().zfill(2)}/{self.nam_optionemenu.get()}", 
            font=customtkinter.CTkFont(
                size=20,
                weight="bold",
            ),
            text_color='red'
        )
        self.logo_label.grid(row=3, column=2, padx=20, pady=(20, 10))
        # endregion

        # region Tải danh sách nhân viên
        self.nhan_vien_label = customtkinter.CTkLabel(self.hor_frame, text="Mã nhân viên:", anchor="w")
        self.nhan_vien_label.grid(row=4, column=1, padx=20, pady=(10, 0))
        self.nhan_vien_optionemenu = customtkinter.CTkOptionMenu(
            self.hor_frame, 
            values= self.data.get_danh_sach_nhan_vien(
                nam= self.nam_optionemenu.get(),
                thang= self.thang_optionemenu.get()
            )
        )
        self.nhan_vien_optionemenu.grid(row=4, column=2, padx=20, pady=(10, 20))
        # endregion

        # region Nút bấm để "Xem chi tiết"
        self.bt_xem_chi_tiet = customtkinter.CTkButton(
            self.hor_frame, 
            command=self.button_xem_chi_tiet,
            text= "Xem chi tiết"
        )
        self.bt_xem_chi_tiet.grid(row=4, column=3, padx=20, pady=10)


        # endregion

        # region Khu vực để hiển thị nội dung chi tiết cho 1 người
        self.textbox = customtkinter.CTkTextbox(self, width=350)
        self.textbox.grid(row=2, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")

        # endregion

        # # region Khung tìm kiếm
        # self.entry = customtkinter.CTkEntry(self, placeholder_text="CTkEntry")
        # self.entry.grid(row=8, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")

        # self.main_button_1 = customtkinter.CTkButton(master=self, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"))
        # self.main_button_1.grid(row=9, column=1, padx=(20, 20), pady=(20, 20), sticky="nsew")
        # # endregion


        # region create tabview
        self.tabview = customtkinter.CTkTabview(self, width=250)
        self.tabview.grid(row=0, column=3, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.tabview.add("CTkTabview")
        self.tabview.add("Tab 2")
        self.tabview.add("Tab 3")
        self.tabview.tab("CTkTabview").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs
        self.tabview.tab("Tab 2").grid_columnconfigure(0, weight=1)

        self.optionmenu_1 = customtkinter.CTkOptionMenu(self.tabview.tab("CTkTabview"), dynamic_resizing=False,
                                                        values=["Value 1", "Value 2", "Value Long Long Long"])
        self.optionmenu_1.grid(row=0, column=3, padx=20, pady=(20, 10))
        self.combobox_1 = customtkinter.CTkComboBox(self.tabview.tab("CTkTabview"),
                                                    values=["Value 1", "Value 2", "Value Long....."])
        self.combobox_1.grid(row=1, column=3, padx=20, pady=(10, 10))
        self.string_input_button = customtkinter.CTkButton(self.tabview.tab("CTkTabview"), text="Open CTkInputDialog",
                                                           command=self.open_input_dialog_event)
        self.string_input_button.grid(row=2, column=3, padx=20, pady=(10, 10))
        self.label_tab_2 = customtkinter.CTkLabel(self.tabview.tab("Tab 2"), text="CTkLabel on Tab 2")
        self.label_tab_2.grid(row=0, column=3, padx=20, pady=20)

        # endregion

        


        
    def sidebar_button_event(self):
        print(f"""
        - Tháng : {self.thang_optionemenu.get().zfill(2)}
        - Năm : {self.nam_optionemenu.get()}
        - Danh sách nhân viên: {self.data.get_danh_sach_nhan_vien(
            nam=self.nam_optionemenu.get(),
            thang= self.thang_optionemenu.get()
        )}
        """
        )
        # region Logo Kết quả công việc
        self.logo_label = customtkinter.CTkLabel(
            self.hor_frame, 
            text=f"Kết quả làm việc {self.thang_optionemenu.get().zfill(2)}/{self.nam_optionemenu.get()}", 
            font=customtkinter.CTkFont(
                size=20,
                weight="bold",
            ),
            text_color='red'
        )
        self.logo_label.grid(row=3, column=2, padx=20, pady=(20, 10))
        # endregion

        # region Tải danh sách nhân viên
        self.nhan_vien_label = customtkinter.CTkLabel(self.hor_frame, text="Mã nhân viên:", anchor="w")
        self.nhan_vien_label.grid(row=4, column=1, padx=20, pady=(10, 0))
        self.nhan_vien_optionemenu = customtkinter.CTkOptionMenu(
            self.hor_frame, 
            values= self.data.get_danh_sach_nhan_vien(
                nam= self.nam_optionemenu.get(),
                thang= self.thang_optionemenu.get()
            )
        )
        self.nhan_vien_optionemenu.grid(row=4, column=2, padx=20, pady=(10, 20))
        # endregion

    def button_xem_chi_tiet(self):
        nhan_vien : NhanVien = self.data.get_thong_tin_nhan_vien(
            nam = self.nam_optionemenu.get(),
            thang= self.thang_optionemenu.get(),
            ma_nhan_vien= self.nhan_vien_optionemenu.get()
        )

        ho_ten_nv = nhan_vien.get_ho_ten()
        ma_so_nv = nhan_vien.get_msnv()
        cac_cong_viec_trong_thang = nhan_vien.get_cac_cong_viec_trong_thang()
        so_cong_viec_trong_thang = nhan_vien.get_so_cong_viec_trong_thang()

        text = f'''
        - Mã số nhân viên: {ma_so_nv}
        - Họ tên: {ho_ten_nv}
        - Số công việc trong tháng : {so_cong_viec_trong_thang}
        - Số ngày đi trễ: {nhan_vien.get_so_ngay_di_tre()}
        - Số ngày về sớm: {nhan_vien.get_so_ngay_ve_som()}
        - Số ngày nghỉ phép: {nhan_vien.get_so_ngay_nghi_phep()}
        - Công việc:

        '''
        for cv in cac_cong_viec_trong_thang:
            text+=f'\t + {cv}\n'


        # Xóa toàn bộ văn bản trong textbox
        self.textbox.delete(
            index1="0.0",
            index2="end"
        )
         # Thêm văn bản mới vào đầu textbox
        self.textbox.insert("0.0", text= text)

    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
        print("CTkInputDialog:", dialog.get_input())


if __name__ == "__main__":
    app = App()
    app.mainloop()
    # data = load_pickle(fn = 'full_data_v3.plk' )
    # print(data)