from typing import Text, List
from utils import load_pickle, dump_pickle
from tqdm import tqdm
import os
from constant import SEP, DATANAME, DATAPATH
from ghi_chep_nam import get_ghi_chep_hang_nam, GhiChepNam
from ghi_chep_thang import get_ghi_chep_hang_tháng
from nhan_vien import NhanVien


def get_toan_bo_data(root: Text):
    # Tạo dict với các năm
    dict_ghi_chep_cac_nam = {}

    for fn in tqdm(os.listdir(path= root), desc = "Ghi chép hàng năm: "):
        nam = fn.split(SEP)[-1] # năm có dạng Y-2023
        year_path = os.path.join(root, fn)
        dict_ghi_chep_cac_nam[nam] = get_ghi_chep_hang_nam(year_fd= year_path)

    # Trả về kết quả
    return dict_ghi_chep_cac_nam

class ToanBoData:
    def __init__(
        self,
        root : Text = DATAPATH,
        cache_path : Text = DATANAME,
        update_whole : bool = False,
        # update_
    ) -> None:
        if not os.path.exists(root) :
            self.root = root
            self.dict_ghi_chep_cac_nam = dict()
        else:
            self.root = root
            if update_whole or not cache_path:
                self.dict_ghi_chep_cac_nam = get_toan_bo_data(self.root)
            elif cache_path:
                self.auto_add_data()
                

    def load_cache(
            self,
            cache_file: Text,
        ):
        return load_pickle(cache_file)
    
    def update(
        self,
        lst_path: List[Text],
    ):
        for path in tqdm(lst_path, desc = 'Cập nhật file từ Upload'):
            year, month  = path.split('\\')[-2:]
            year = year.split('-')[-1]
            month = month.split('.')[0].split('-')[-1]
            if year not in self.dict_ghi_chep_cac_nam:
                self.dict_ghi_chep_cac_nam[year] = GhiChepNam(nam = year, dict_ghi_chep_12_thang={})
            self.dict_ghi_chep_cac_nam[year].dict_ghi_chep_12_thang[month] = get_ghi_chep_hang_tháng(path)
        
    
    def auto_add_data(
        self,
        cache_path: Text = DATANAME
        ):
        self.dict_ghi_chep_cac_nam = self.load_cache(cache_path).dict_ghi_chep_cac_nam
        # region Lấy danh sách các năm và từ điển tháng theo năm
        lst_year = self.dict_ghi_chep_cac_nam.keys()
        dict_year_2_month = {y: self.dict_ghi_chep_cac_nam[y].dict_ghi_chep_12_thang.keys() for y in lst_year}
        # endregion

        # region So sánh xem có năm nào mới hông?
        lst_tmp_year= list(map(lambda fn : fn.split(SEP)[-1], os.listdir(path = self.root)))
        lst_new_year= list(set(lst_tmp_year) - set(lst_year)) # Chỉ thêm các năm trong đây thôi
        # endregion

        # region xac dinh cac file bi xoa
        lst_delete_year = list(set(lst_year) - set(lst_tmp_year))
        for year in lst_delete_year:
            self.dict_ghi_chep_cac_nam.pop(year)

        # endregion


        # region So sánh các tháng mới
        dict_new_year_2_month = dict()
        for y in lst_year:
            lst_month = os.listdir(
                path= os.path.join(self.root, f'Y-{y}')
            )
            lst_tmp_month = list(map(lambda fn : fn.split(".")[0].split("-")[1], lst_month))
            lst_original_month = dict_year_2_month[y]

            lst_new_month = list(set(lst_tmp_month) - set(lst_original_month))
            dict_new_year_2_month[y] = lst_new_month

            lst_delete_month = list(set(lst_original_month) - set(lst_tmp_month))
            for month in lst_delete_month:
                self.dict_ghi_chep_cac_nam[y].dict_ghi_chep_12_thang.pop(month)
        # endregion

        # region Thêm ghi chép năm cho các năm mới
        lst_year_path= list(map(lambda y: os.path.join(self.root, f'Y-{y}'),lst_new_year))
        for nam, year_path in tqdm(zip(lst_new_year, lst_year_path), desc = "Thêm ghi chép năm cho các năm mới: "):
            self.dict_ghi_chep_cac_nam[nam] = get_ghi_chep_hang_nam(year_fd= year_path)
        # endregion

        # region Thêm ghi chép tháng cho các tháng mới
        print(f"dict_new_year_2_month.items(): {dict_new_year_2_month.items()}")
        for year, months in dict_new_year_2_month.items():
            for month in tqdm(months, desc = "Thêm ghi chép tháng cho các tháng mới"):
                year_fd = os.path.join(self.root, f'Y-{year}')
                excel_file = os.path.join(year_fd, f'T-{month}.xls')
                self.dict_ghi_chep_cac_nam[year].dict_ghi_chep_12_thang[month] = get_ghi_chep_hang_tháng(excel_file)
        # endregion


    def thong_ke(self):
        pass


    def ve_so_do(self):
        pass

    def get_danh_sach_nam(self):
        return list(self.dict_ghi_chep_cac_nam.keys()) 
    
    def get_danh_sach_thang(
        self,
        nam: Text
    ):  
        lst_nam = self.get_danh_sach_nam()
        if nam not in lst_nam:
            return []
        return list(self.dict_ghi_chep_cac_nam[nam].dict_ghi_chep_12_thang.keys())

    def get_danh_sach_nhan_vien(
        self,
        nam: Text,
        thang: Text
    ):  
        # Kiểm tra năm
        lst_nam = self.get_danh_sach_nam()
        if nam not in lst_nam:
            return []
        
        # Kiểm tra tháng
        lst_thang = self.get_danh_sach_thang(nam)
        if thang not in lst_thang:
            return []
        
        return list(self.dict_ghi_chep_cac_nam[nam].dict_ghi_chep_12_thang[thang].dict_nhan_vien.keys())
    
    def get_thong_tin_nhan_vien(
        self,
        nam: Text,
        thang: Text,
        ma_nhan_vien: Text
    )-> NhanVien:
        thang = str(int(thang))
        return self.dict_ghi_chep_cac_nam[nam].dict_ghi_chep_12_thang[thang].dict_nhan_vien[ma_nhan_vien]
        

def load_toan_bo_data():
    x = ToanBoData(root= DATAPATH , cache_path= DATANAME)
    dump_pickle(
        fn = DATANAME,
        obj= x   
    )
        
if __name__ == "__main__":
    print("Hello")

    data :ToanBoData = load_pickle(fn = 'DATA.plk' )

    print(data.__dict__)
    print(
        data.get_danh_sach_nam(),
        data.get_danh_sach_thang('2023'),
        data.get_danh_sach_nhan_vien(
            nam= '2023',
            thang= '1'
        )
    )



    