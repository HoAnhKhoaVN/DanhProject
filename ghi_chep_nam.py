from typing import Text, Dict
from ghi_chep_thang import GhiChepThang, get_ghi_chep_hang_tháng
import os
from tqdm import tqdm

class GhiChepNam:
    def __init__(
        self,
        nam: Text,
        dict_ghi_chep_12_thang: Dict[Text, GhiChepThang]
    ) -> None:
        self.nam = nam
        self.dict_ghi_chep_12_thang = dict_ghi_chep_12_thang
        
    def thong_ke(self):
        pass

def get_ghi_chep_hang_nam(
        year_fd: Text,
    )-> GhiChepNam:
    
    # Lấy năm từ tên thư mực
    nam = year_fd.split(os.sep)[-1].split('.')[0].replace('Y', '')

    # Lấy ghi chép của 12 tháng
    dict_ghi_chep_12_thang = {}
    for fn in tqdm(os.listdir(year_fd), desc= "Lấy ghi chép của 12 tháng"):
        thang = fn.split(".")[0].split("-")[1]
        excel_file = os.path.join(year_fd, fn)
        dict_ghi_chep_12_thang[thang] = get_ghi_chep_hang_tháng(excel_file)
    # Trả về ghi chep của một năm

    return GhiChepNam(
        nam = nam,
        dict_ghi_chep_12_thang= dict_ghi_chep_12_thang
    )





if __name__ == "__main__":
    print("dataset/cong_viec.py")
