from typing import Text, Dict, Tuple, List
from ghi_chep_hang_ngay import GhiChepHangNgay
from cong_viec import CongViec, get_task,get_ghi_chep_trong_ngay
from constant import (
    IDX_TEN_NHAN_VIEN,
    CV,
    START_INDEX,   
)
import pandas as pd
from collections import defaultdict

def create_list_defaultdict():
    """Tạo một defaultdict để có thể dump thành file pickle
    Sửa lỗi dựa: https://stackoverflow.com/questions/72339545/attributeerror-cant-pickle-local-object-locals-lambda
    """
    return defaultdict(list)

class NhanVien:
    def __init__(
        self,
        msnv: int,
        ho_ten: Text,
        dict_ghi_chep_cong_viec: Dict[Text, CongViec],
        dict_ghi_chep_theo_ngay: Dict[Tuple[Text,Text], List[GhiChepHangNgay]]
    ) -> None:
        self.msnv = msnv
        self.ho_ten = ho_ten
        self.dict_ghi_chep_cong_viec = dict_ghi_chep_cong_viec
        self.dict_ghi_chep_theo_ngay = dict_ghi_chep_theo_ngay

    def thong_ke(self):
        pass

    def get_ho_ten(self):
        return self.ho_ten

    def get_msnv(self):
        return self.msnv
    
    def get_so_cong_viec_trong_thang(self):
        return len(self.dict_ghi_chep_cong_viec)
    
    def get_cac_cong_viec_trong_thang(self):
        return list(self.dict_ghi_chep_cong_viec.keys())
    
    def get_so_ngay_cong(self):
        pass

    def get_so_ngay_nghi_phep(self):
        return len(self.dict_ghi_chep_cong_viec.get('Nghỉ phép', []))

    def get_so_ngay_di_tre(self):
        return len(self.dict_ghi_chep_cong_viec.get('Đi trễ', []))

    def get_so_ngay_ve_som(self):
        return len(self.dict_ghi_chep_cong_viec.get('Về sớm', []))

    def get_so_ban_ve_hoan_thanh(self):
        pass

    def get_so_cong_viec_chua_hoan_thanh(self):
        pass

    def get_so_ngay_tang_ca(self):
        pass

    def get_so_ngay_khong_lam(self):
        pass

    def get_so_ngay_hang_chanh(self):
        pass

    


def get_value_for_staff(
    manv: Text,
    df: pd.DataFrame
    )-> NhanVien:
    """Lấy giá trị cho một nhân viên trong tháng

    Args:
        manv (Text): Mã số nhân viên. Dùng để định danh nhân viên
        df (pd.DataFrame): DataFrame chứa ghi chép của 1 nhân viên

    Returns:
        NhanVien: Ghi chép cho nhân viên. Bao gồm:
        - msnv (Text): Mã số nhân viên
        - ho_ten (Text): Họ tên nhân viên
        - dict_ghi_chep_cong_viec (Dict[Text, List[GhiChepCongViec]]): Ghi chép công việc theo tên công việc
    """    
    # Lấy tên nhân viên
    ten_nv = df[CV][IDX_TEN_NHAN_VIEN]

    # Lấy số công việc nhân viên làm trong tháng
    dict_ghi_chep_cong_viec = defaultdict(create_list_defaultdict)
    N = len(df)
    for idx in range(START_INDEX,N):
        cv = get_task(idx = idx, df = df)
        ghi_chep_hang_ngay = get_ghi_chep_trong_ngay(df = df)
        if cv:
            ten_cv = cv.ten_cong_viec
            ban_ve = cv.ban_ve
            dict_ghi_chep_cong_viec[ten_cv][ban_ve].append(cv)
    # Tạo một ghi chép công việc cho nhận viên trong 1 tháng
    return NhanVien(
        msnv= manv,
        ho_ten= ten_nv,
        dict_ghi_chep_cong_viec= dict_ghi_chep_cong_viec
    )




if __name__ == "__main__":
    print("dataset/nhan_vien.py")