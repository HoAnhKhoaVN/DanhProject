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

        # region 1: Lấy dữ liệu
        self.data : ToanBoData = load_pickle(fn = data_path)
        lst_nam = self.data.get_danh_sach_nam()
        # endregion


        # region 2: Configure window
        self.title("Danh Product")
        self.geometry(f"{1100}x{580}") # Chỉnh kích thước màn hình
        # endregion


        # region 3: Tạo một sidebar để chọn tháng và năm
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

            # region Truy xuất dữ liệu
        self.bt_truy_xuat = customtkinter.CTkButton(
            self.sidebar_frame, 
            command=self.sidebar_button_event,
            text= "Truy xuất"
            )
        self.bt_truy_xuat.grid(row=9, column=0, padx=20, pady=10)
            # endregion

        # endregion
        
        
        # region 4: Create slider and progressbar frame
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

            # region 4.1: Logo Kết quả công việc
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

            # region 4.2: Tải danh sách nhân viên
                
                # region 4.2.1: Nhãn `Mã nhân viên``
        self.nhan_vien_label = customtkinter.CTkLabel(self.hor_frame, text="Mã nhân viên:", anchor="w")
        self.nhan_vien_label.grid(row=4, column=1, padx=20, pady=(10, 0))
                # endregion
        
                # region 4.2.2: Option Menu
        self.nhan_vien_optionemenu = customtkinter.CTkOptionMenu(
            self.hor_frame, 
            values= self.data.get_danh_sach_nhan_vien(
                nam= self.nam_optionemenu.get(),
                thang= self.thang_optionemenu.get()
            )
        )
        self.nhan_vien_optionemenu.grid(row=4, column=2, padx=20, pady=(10, 20))
                # endregion

                # region 4.2.3: Xem danh sách nhân viên
        self.bt_xem_chi_tiet_cong_viec = customtkinter.CTkButton(
            self.hor_frame, 
            command=self.button_xem_nhan_vien,
            text= "Xem nhân viên"
        )
        self.bt_xem_chi_tiet_cong_viec.grid(row=4, column=3, padx=20, pady=10)
                # endregion
        # endregion
            
            # region Label các công việc
        self.cac_cong_viec_label = customtkinter.CTkLabel(self.hor_frame, text=f"Các công việc: ", anchor="w")
        self.cac_cong_viec_label.grid(row=8, column=1, padx=20, pady=(10, 0))
            # endregion

            # region options công việc
        self.nhan_vien = None
        self.ho_ten_nv = None
        self.ma_so_nv = None
        self.cac_cong_viec_trong_thang = ""
        self.so_cong_viec_trong_thang = None
        self.so_ngay_cong = 30
        self.so_ngay_tre = None
        self.so_ngay_ve_som = None
        self.so_ngay_tang_ca = None
        self.so_ngay_nghi_phep = None

        # region Label Họ tên
        self.ho_ten_label = customtkinter.CTkLabel(self.hor_frame, text=f"Họ Tên: {self.ho_ten_nv}", anchor="w")
        self.ho_ten_label.grid(row=5, column=1, padx=20, pady=(10, 0))
        # endregion

        # region Số ngày công
        self.so_ngay_cong_label = customtkinter.CTkLabel(self.hor_frame, text=f"Số ngày công: {self.so_ngay_cong}", anchor="w")
        self.so_ngay_cong_label.grid(row=6, column=1, padx=20, pady=(10, 0))
        # endregion

        # region số công việc
        self.tang_ca_label = customtkinter.CTkLabel(self.hor_frame, text=f"Tăng ca: {self.so_ngay_tang_ca}", anchor="w")
        self.tang_ca_label.grid(row=5, column=3, padx=20, pady=(10, 0))
        # endregion

        # region Trễ
        self.tre_label = customtkinter.CTkLabel(self.hor_frame, text=f"Trễ: {self.so_ngay_tre}", anchor="w")
        self.tre_label.grid(row=5, column=2, padx=20, pady=(10, 0))
        # endregion

        # region Sớm
        self.som_label = customtkinter.CTkLabel(self.hor_frame, text=f"Sớm: {self.so_ngay_ve_som}", anchor="w")
        self.som_label.grid(row=6, column=2, padx=20, pady=(10, 0))
        # endregion

        # region Phép
        self.phep_label = customtkinter.CTkLabel(self.hor_frame, text=f"Phép: {self.so_ngay_nghi_phep}", anchor="w")
        self.phep_label.grid(row=6, column=3, padx=20, pady=(10, 0))
        # endregion

        self.cac_cong_viec_optionemenu = customtkinter.CTkOptionMenu(
            self.hor_frame, 
            values= self.cac_cong_viec_trong_thang
        )
        self.cac_cong_viec_optionemenu.grid(row=8, column=2, padx=20, pady=(10, 20))
            # endregion

            # region nút "Xem chi tiết công việc"
        self.bt_xem_chi_tiet_cong_viec = customtkinter.CTkButton(
            self.hor_frame, 
            command=self.button_xem_chi_tiet,
            text= "Xem chi tiết công việc"
        )
        self.bt_xem_chi_tiet_cong_viec.grid(row=8, column=3, padx=20, pady=10)

            # endregion
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


        # # region create tabview
        # self.tabview = customtkinter.CTkTabview(self, width=250)
        # self.tabview.grid(row=0, column=3, padx=(20, 0), pady=(20, 0), sticky="nsew")
        # self.tabview.add("CTkTabview")
        # self.tabview.add("Tab 2")
        # self.tabview.add("Tab 3")
        # self.tabview.tab("CTkTabview").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs
        # self.tabview.tab("Tab 2").grid_columnconfigure(0, weight=1)

        # self.optionmenu_1 = customtkinter.CTkOptionMenu(self.tabview.tab("CTkTabview"), dynamic_resizing=False,
        #                                                 values=["Value 1", "Value 2", "Value Long Long Long"])
        # self.optionmenu_1.grid(row=0, column=3, padx=20, pady=(20, 10))
        # self.combobox_1 = customtkinter.CTkComboBox(self.tabview.tab("CTkTabview"),
        #                                             values=["Value 1", "Value 2", "Value Long....."])
        # self.combobox_1.grid(row=1, column=3, padx=20, pady=(10, 10))
        # self.string_input_button = customtkinter.CTkButton(self.tabview.tab("CTkTabview"), text="Open CTkInputDialog",
        #                                                    command=self.open_input_dialog_event)
        # self.string_input_button.grid(row=2, column=3, padx=20, pady=(10, 10))
        # self.label_tab_2 = customtkinter.CTkLabel(self.tabview.tab("Tab 2"), text="CTkLabel on Tab 2")
        # self.label_tab_2.grid(row=0, column=3, padx=20, pady=20)

        # # endregion

        
    def sidebar_button_event(self):
        # region Logo Kết quả công việc
        self.logo_label.configure(text = f"Kết quả làm việc {self.thang_optionemenu.get().zfill(2)}/{self.nam_optionemenu.get()}")
        # endregion

        # region Tải danh sách nhân viên
        self.nhan_vien_optionemenu.configure(
            values= self.data.get_danh_sach_nhan_vien(
                nam= self.nam_optionemenu.get(),
                thang= self.thang_optionemenu.get())
        )
        # endregion


        # region Lấy danh sách công việc của nhân viên đầu tiên để hiển thị
        self.nhan_vien : NhanVien = self.data.get_thong_tin_nhan_vien(
            nam = self.nam_optionemenu.get(),
            thang= self.thang_optionemenu.get(),
            ma_nhan_vien= self.nhan_vien_optionemenu.get()
        )
        self.ho_ten_nv = self.nhan_vien.get_ho_ten()
        self.ma_so_nv = self.nhan_vien.get_msnv()
        self.cac_cong_viec_trong_thang = self.nhan_vien.get_cac_cong_viec_trong_thang()
        self.so_cong_viec_trong_thang = self.nhan_vien.get_so_cong_viec_trong_thang()
        self.so_ngay_cong = 30
        self.so_ngay_tre = self.nhan_vien.get_so_ngay_di_tre()
        self.so_ngay_ve_som = self.nhan_vien.get_so_ngay_ve_som()
        self.so_ngay_tang_ca = self.nhan_vien.get_so_ngay_tang_ca()
        self.so_ngay_nghi_phep = self.nhan_vien.get_so_ngay_nghi_phep()

        self.cac_cong_viec_optionemenu.configure(
            values = self.cac_cong_viec_trong_thang
        )
        # endregion

    def button_xem_chi_tiet(self):
        text = ''
        cv = self.cac_cong_viec_optionemenu.get()
        ban_ve = list(self.nhan_vien.dict_ghi_chep_cong_viec[cv].keys())
        # print(f"{cv}:{ban_ve}")
        text+=f"***** {cv} ****\n"
        for bv in ban_ve:
            cong_viec = self.nhan_vien.dict_ghi_chep_cong_viec[cv][bv][0]
            cong_doan = cong_viec.cong_doan
            nha_may = cong_viec.nha_may
            # so_luong = cong_viec.so_luong
            # don_vi = cong_viec.don_vi

            so_ngay_lam = len(cong_viec.ghi_ghep_hang_ngay)
            lst_ngay_cong = [cong_viec.ghi_ghep_hang_ngay[ngay_lam].ngay for ngay_lam in range(so_ngay_lam)]

            text+=(f"""
1. Bản vẽ: {bv}
2. Công đoạn: {cong_doan}
3. Nhà máy : {nha_may}
4. Số ngày làm: {so_ngay_lam}
5: Danh sách ngày làm: {', '.join(lst_ngay_cong)}
""")
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

    def button_xem_nhan_vien(self):
        self.ho_ten_label.configure(text=f"Họ Tên: {self.ho_ten_nv}")
        self.so_ngay_cong_label.configure(text=f"Số ngày công: {self.so_ngay_cong}")
        self.tang_ca_label.configure(text=f"Tăng ca: {self.so_ngay_tang_ca}")
        self.tre_label.configure(text=f"Trễ: {self.so_ngay_tre}")
        self.som_label.configure(text=f"Sớm: {self.so_ngay_ve_som}")
        self.phep_label.configure(text=f"Phép: {self.so_ngay_nghi_phep}")
if __name__ == "__main__":
    app = App()
    app.mainloop()
    # data = load_pickle(fn = 'full_data_v3.plk' )
    # print(data)