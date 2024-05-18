from typing import Text, Dict, Tuple, List
from ghi_chep_hang_ngay import GhiChepHangNgay
from cong_viec import CongViec, get_task,get_ghi_chep_trong_ngay
from constant import (
    IDX_TEN_NHAN_VIEN,
    CV,
    START_INDEX,
    DI_TRE,
    VE_SOM,
    NGHI_PHEP
)
import pandas as pd
from collections import defaultdict
import traceback

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
        return list(self.dict_ghi_chep_cong_viec.keys())
    
    def get_so_gio_cong(self):
        tong_gio_gio_cong = 0.0
        for v in self.dict_ghi_chep_cong_viec.values():
            for cv in v.values():
                # print(f'{k}-{ban_ve}-{cv[0]}')
                cong_viec :CongViec = cv[0]
                ten_cong_viec = cong_viec.ten_cong_viec
                if ten_cong_viec.strip().lower() in [DI_TRE, VE_SOM, NGHI_PHEP]:
                    continue
                try:
                    tang_ca = cong_viec.ghi_ghep_hang_ngay[0].tang_ca
                    hanh_chinh = cong_viec.ghi_ghep_hang_ngay[0].hanh_chanh
                    if tang_ca is not None:
                        tong_gio_gio_cong+= tang_ca.gio
                    if hanh_chinh is not None:
                        tong_gio_gio_cong+= hanh_chinh.gio
                except Exception as e:
                    print("##### ERROR ####")
                    print(f"- Công việc: {ten_cong_viec}")
                    traceback.print_exc()
        return tong_gio_gio_cong
            


    def get_so_gio_nghi_phep(self):
        nghi_phep : dict = self.dict_ghi_chep_cong_viec[NGHI_PHEP]
        lst_ngay_nghi_phep = []
        lst_gio_nghi_phep = []
        for v in nghi_phep.values():
            cv = v[0]
            for _cv in cv.ghi_ghep_hang_ngay:
                ngay_ve_som = _cv.ngay
                gio_ve_som = _cv.hanh_chanh.TSN_nghi

                lst_ngay_nghi_phep.append(ngay_ve_som)
                lst_gio_nghi_phep.append(gio_ve_som)

        # print(f'lst_ngay_ve_som: {lst_ngay_nghi_phep}')
        # print(f'lst_gio_ve_som: {lst_gio_nghi_phep}')
        hour = 0.0
        if lst_gio_nghi_phep:
            hour = sum(lst_gio_nghi_phep)
        # print(f'Sum hour : {hour}')
        return hour, lst_ngay_nghi_phep, lst_gio_nghi_phep 

    def get_so_phut_di_tre(self):
        di_tre = self.dict_ghi_chep_cong_viec.get(DI_TRE, {})
        # di_tre.update(self.dict_ghi_chep_cong_viec.get('Đi trể', {}))
        lst_minutes = []
        for cong_viec in di_tre.values():
            cv = cong_viec[0]
            for _v in cv.ghi_ghep_hang_ngay:
                lst_minutes.append(_v.hanh_chanh.TSN_nghi)
        # lst_minutes = [v[0].ghi_ghep_hang_ngay[0].hanh_chanh.TSN_nghi for v in di_tre.values()]
        minutes = 0
        if lst_minutes:
            minutes = sum(lst_minutes)
        return minutes

    def get_so_gio_ve_som(self):
        ve_som : dict = self.dict_ghi_chep_cong_viec[VE_SOM]
        lst_ngay_ve_som = []
        lst_gio_ve_som = []
        for v in ve_som.values():
            cv = v
            for _cv in cv:
                ngay_ve_som = _cv.ghi_ghep_hang_ngay[0].ngay
                gio_ve_som = _cv.ghi_ghep_hang_ngay[0].hanh_chanh.TSN_nghi

                lst_ngay_ve_som.append(ngay_ve_som)
                lst_gio_ve_som.append(gio_ve_som)

        hour = 0.0
        if lst_ngay_ve_som:
            hour = sum(lst_gio_ve_som)
        return hour, lst_ngay_ve_som, lst_gio_ve_som

    def get_so_ban_ve_hoan_thanh(self):
        pass

    def get_so_cong_viec_chua_hoan_thanh(self):
        pass

    def get_so_gio_tang_ca(self):
        tong_gio_tang_ca = 0.0
        lst_ngay_tang_ca = []
        lst_gio_tang_ca = []
        lst_cong_viec = []
        lst_ban_ve = []
        for k, v in self.dict_ghi_chep_cong_viec.items():
            for ban_ve, cv in v.items():
                # print(f'{k}-{ban_ve}-{cv[0]}')
                cong_viec :CongViec = cv[0]
                tang_ca = cong_viec.ghi_ghep_hang_ngay[0].tang_ca
                if tang_ca is not None:
                    gio_tang_ca = tang_ca.gio
                    ngay_tang_ca = cong_viec.ghi_ghep_hang_ngay[0].ngay

                    tong_gio_tang_ca+= gio_tang_ca
                    lst_ngay_tang_ca.append(ngay_tang_ca)
                    lst_gio_tang_ca.append(gio_tang_ca)
                    lst_cong_viec.append(cong_viec.ten_cong_viec)
                    lst_ban_ve.append(cong_viec.ban_ve)
        return tong_gio_tang_ca, lst_ngay_tang_ca, lst_gio_tang_ca, lst_cong_viec, lst_ban_ve
            

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
        # ghi_chep_hang_ngay = get_ghi_chep_trong_ngay(df = df)
        if cv:
            ten_cv = cv.ten_cong_viec
            if cv.ban_ve is not None: 
                ban_ve = cv.ban_ve
            else: # Trễ, sớm, phép, vệ sinh,...
                ban_ve = str(idx)
            dict_ghi_chep_cong_viec[ten_cv][ban_ve].append(cv)
    # Tạo một ghi chép công việc cho nhận viên trong 1 tháng
    return NhanVien(
        msnv= manv,
        ho_ten= ten_nv,
        dict_ghi_chep_cong_viec= dict_ghi_chep_cong_viec
    )




if __name__ == "__main__":
    print("dataset/nhan_vien.py")