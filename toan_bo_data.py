from typing import Text, List
from utils import load_pickle, dump_pickle
from tqdm import tqdm
import os
from constant import SEP
from ghi_chep_nam import get_ghi_chep_hang_nam
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
        root : Text = None,
        cache_path : Text = None
    ) -> None:
        assert root, "Không tìm thấy tên thư mục chứa dữ liệu"
        self.root = root
        if cache_path:
            self.dict_ghi_chep_cac_nam = self.load_cache(cache_path)
        else:
            self.dict_ghi_chep_cac_nam = get_toan_bo_data(self.root)


    def load_cache(
            self,
            cache_file: Text,
        ):
        return load_pickle(cache_file)

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
        return self.dict_ghi_chep_cac_nam[nam].dict_ghi_chep_12_thang[thang].dict_nhan_vien[ma_nhan_vien]
        
if __name__ == "__main__":
    print("Hello")

    data :ToanBoData = load_pickle(fn = 'full_data_v3.plk' )

    print(
        data.get_danh_sach_nam(),
        data.get_danh_sach_thang('2023'),
        data.get_danh_sach_nhan_vien(
            nam= '2023',
            thang= '1'
        )
    )



    