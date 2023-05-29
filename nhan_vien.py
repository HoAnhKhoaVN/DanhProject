from typing import Text, Dict
from cong_viec import CongViec, get_task
from constant import (
    IDX_TEN_NHAN_VIEN,
    CV,
    START_INDEX,   
)
import pandas as pd
from collections import defaultdict


class NhanVien:
    def __init__(
        self,
        msnv: int,
        ho_ten: Text,
        dict_ghi_chep_cong_viec: Dict[Text, CongViec]
    ) -> None:
        self.msnv = msnv
        self.ho_ten = ho_ten
        self.dict_ghi_chep_cong_viec = dict_ghi_chep_cong_viec

    def thong_ke(self):
        pass

    def get_ho_ten(self):
        return self.ho_ten

    def get_msnv(self):
        return self.msnv
    
    def get_so_cong_viec_trong_thang(self):
        return len(self.dict_ghi_chep_cong_viec)
    
    def get_cac_cong_viec_trong_thang(self):
        return self.dict_ghi_chep_cong_viec.keys()
    
    def get_so_ngay_cong(self):
        pass

    def get_so_ngay_nghi_phep(self):
        pass

    def get_so_ngay_di_tre(self):
        pass

    def get_so_ngay_ve_som(self):
        pass

    def get_so_ban_ve_hoan_thanh(self):
        pass

    def get_so_cong_viec_chua_hoan_thanh(self):
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
    dict_ghi_chep_cong_viec = defaultdict(list)
    N = len(df)
    for idx in range(START_INDEX,N):
        cv = get_task(idx = idx, df = df)
        if cv:
            ten_cv = cv.ten_cong_viec
            dict_ghi_chep_cong_viec[ten_cv].append(cv)
    # Tạo một ghi chép công việc cho nhận viên trong 1 tháng
    return NhanVien(
        msnv= manv,
        ho_ten= ten_nv,
        dict_ghi_chep_cong_viec= dict_ghi_chep_cong_viec
    )




if __name__ == "__main__":
    print("dataset/nhan_vien.py")