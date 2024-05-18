from typing import Text, List, Dict
from ghi_chep_hang_ngay import GhiChepHangNgay, get_value_ghi_chep_hang_ngay
import pandas as pd
from collections import defaultdict
from constant import (
    CHU_THICH,
    CV,
    BAN_VE,
    CONG_DOAN,
    NHA_MAY,
    SL,
    DVT,
    KHDTCT,
    PYC,
    TGDK,
    TGTT,
    TL,
    START_INDEX,
    HC_GIO,
    TC_GIO,
    TNS_NGHI,
    TC_TL,
    HC_TL,
    MAX_NUM_DAY,
    NGHI_PHEP,
    VE_SOM,
    DI_TRE
)

def preprocess_ten_cv(ten_cv: Text)-> Text:
    """_summary_

    Args:
        ten_cv (Text): _description_

    Returns:
        Text: _description_
    """
    if ten_cv.strip().lower() in ['nghỉ phép', 'nghĩ phép']:
        return NGHI_PHEP
    
    if ten_cv.strip().lower() in ['về sớm', 'sớm']:
        return VE_SOM
    
    if ten_cv.strip().lower() in ['đi trể', 'đi trễ']:
        return DI_TRE
    return ten_cv


class CongViec:
    def __init__(
        self,
        ten_cong_viec : Text,
        ban_ve: int,
        cong_doan: int,
        nha_may: int,
        so_luong: int,
        don_vi: Text,
        KH_DT_CT: Text,
        PYC: int,
        thoi_gian_du_kien: float,
        thoi_gian_thuc_te: float,
        ti_le: float,
        chu_thich: Text,
        ghi_ghep_hang_ngay: List[GhiChepHangNgay]
    ) -> None:
        self.ten_cong_viec = preprocess_ten_cv(ten_cong_viec)
        self.ban_ve = ban_ve
        self.cong_doan = cong_doan
        self.nha_may = nha_may
        self.so_luong =  so_luong
        self.don_vi = don_vi
        self.KH_DT_CT= KH_DT_CT
        self.PYC = PYC
        self.thoi_gian_du_kien = thoi_gian_du_kien
        self.thoi_gian_thuc_te = thoi_gian_thuc_te
        self.ti_le = ti_le
        self.chu_thich = chu_thich
        self.ghi_ghep_hang_ngay = ghi_ghep_hang_ngay

    def thong_ke(self):
        pass



def get_task(
    idx: int,
    df: pd.DataFrame
)-> CongViec:
    # region Kiểm tra xem có tên công việc không?
    # Nếu có thì mới tạo công việc
    ten_cong_viec = df[CV][idx]
    if not ten_cong_viec: 
        return None
    # endregion
    
    ban_ve = df[BAN_VE][idx]
    cong_doan = df[CONG_DOAN][idx]
    nha_may = df[NHA_MAY][idx]
    sl = df[SL][idx]
    dvt = df[DVT][idx]
    khdtct = df[KHDTCT][idx]
    pyc = df[PYC][idx]
    tgdk = df[TGDK][idx]
    tgtt = df[TGTT][idx]
    tl = df[TL][idx]
    chu_thich = df[CHU_THICH][idx]

    ghi_chep_hang_ngay = get_value_ghi_chep_hang_ngay(idx = idx, _df = df)
    # print(f'Tên công việc - ghi chép hằng ngày:{ten_cong_viec}- {ghi_chep_hang_ngay}')

    if ghi_chep_hang_ngay:
        cv = CongViec(
            ten_cong_viec= ten_cong_viec,
            ban_ve= ban_ve,
            cong_doan= cong_doan,
            nha_may= nha_may,
            so_luong= sl,
            don_vi= dvt,
            KH_DT_CT= khdtct,
            PYC= pyc,
            thoi_gian_du_kien= tgdk,
            thoi_gian_thuc_te= tgtt,
            chu_thich= chu_thich,
            ti_le= tl,
            ghi_ghep_hang_ngay= ghi_chep_hang_ngay
        )
        return cv
    return None

def get_gio_lam_hanh_chanh_trong_ngay(
        df: pd.DataFrame,
        ngay: int,
        ):
    # B1: Chuẩn bị các biến cần thiết
    lst_idx = []
    lst_time = []
    lst_ti_le_cong_viec = []
    ngay = str(ngay).zfill(2)
    start_idx = START_INDEX + 2

    # B2: 
    for idx , x in enumerate(df[f'{HC_GIO}{ngay}'].iloc[start_idx:]):
        if isinstance(x, (float, int)): # Kiểm tra xem 'x' đang xét có là số thực hay số nguyên không?
            _idx = idx+start_idx
            lst_idx.append(_idx)

            # Lấy tỉ lệ
            tl = df[f'{HC_TL}{ngay}'][_idx]

            lst_ti_le_cong_viec.append(tl)
            lst_time.append(x)

    return lst_idx, lst_time, lst_ti_le_cong_viec

def get_gio_lam_tang_ca_trong_ngay(df: pd.DataFrame, ngay: int):
    # B1: Chuẩn bị các biến cần thiết
    lst_idx = []
    lst_time = []
    lst_ti_le_cong_viec = []
    ngay = str(ngay).zfill(2)
    start_idx = START_INDEX + 2

    # B2: 
    for idx , x in enumerate(df[f'{TC_GIO}{ngay}'].iloc[start_idx:]):
        if isinstance(x, (float, int)): # Kiểm tra xem 'x' đang xét có là số thực hay số nguyên không?
            _idx = idx+start_idx
            lst_idx.append(_idx)

            # Lấy tỉ lệ
            tl = df[f'{TC_TL}{ngay}'][_idx]

            lst_ti_le_cong_viec.append(tl)
            lst_time.append(x)

    return lst_idx, lst_time, lst_ti_le_cong_viec


def get_ngay_nghi(df: pd.DataFrame, ngay: int):
    # B1: Chuẩn bị các biến cần thiết
    lst_idx = []
    lst_time = []
    ngay = str(ngay).zfill(2)
    start_idx = START_INDEX + 2

    # B2: 
    for idx , x in enumerate(df[f'{TNS_NGHI}{ngay}'].iloc[start_idx:]):
        if isinstance(x, (float, int)): # Kiểm tra xem 'x' đang xét có là số thực hay số nguyên không?
            lst_idx.append(idx+start_idx)
            lst_time.append(x)

    return lst_idx, lst_time

def get_ghi_chep_trong_ngay(df: pd.DataFrame):
    result = {}
    la_ngay_nghi = False
    for ngay in range(1, MAX_NUM_DAY+1):
        tmp_dict = {}
        # B1: Kiểm tra có phải là ngày nghỉ không?
        lst_idx_nts, lst_gio_nts = get_ngay_nghi(
            df = df,
            ngay= ngay
        )

        lst_gio_ve_som = []
        lst_idx_ve_som= []
        if lst_idx_nts:
            # Lọc ra danh sách về sớm
            for i , time in enumerate(lst_gio_nts):
                if time < 8:
                    lst_idx_ve_som.append(lst_idx_nts[i])
                    lst_gio_ve_som.append(time)

            # Xóa các index về sớm ra khỏi nghỉ phép
            if lst_idx_ve_som:
                la_ve_som = True # Không phải là ngày nghỉ mà là đi về sớm
                # lst_idx_nghi = []    # Nếu đi về sớm thì không là ngày nghỉ nha
                # lst_gio_nghi = []
                # for i in lst_idx_nts:
                #     if i not in lst_idx_ve_som:
                #         lst_idx_nghi.append(i)
                #         lst_gio_nghi.append(lst_gio_nts[i])
            else:
                la_ve_som = False
                la_ngay_nghi= True
        else:
                la_ve_som = False
                la_ngay_nghi= False


        if la_ngay_nghi:# Là ngày nghỉ
            tmp_dict['gio_nghi'] = lst_gio_nts
        elif la_ve_som:
            tmp_dict['ve_som'] = lst_gio_ve_som

        lst_idx_hc, lst_gio_hc, lst_ti_le_hanh_chanh = get_gio_lam_hanh_chanh_trong_ngay(
            df = df,
            ngay= ngay
        )
        

        if lst_idx_hc:
            tmp_dict['idx_hanh_chanh'] = lst_idx_hc
            tmp_dict['gio_hanh_chanh'] = lst_gio_hc
            tmp_dict['ti_le_hanh_chanh'] = lst_ti_le_hanh_chanh
        

        lst_idx_tang_ca, lst_gio_tang_ca, lst_ti_le_tang_ca = get_gio_lam_tang_ca_trong_ngay(
            df = df,
            ngay= ngay
        )
        if lst_idx_tang_ca:
            tmp_dict['idx_tang_ca'] = lst_idx_tang_ca
            tmp_dict['gio_tang_ca'] = lst_gio_tang_ca
            tmp_dict['ti_le_tang_ca'] = lst_ti_le_tang_ca
    
        if tmp_dict:
            result[ngay] = tmp_dict
    return result





if __name__ == "__main__":
    print("dataset/cong_viec.py")
