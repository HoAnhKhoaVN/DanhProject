from typing import Text, List, Dict
from ghi_chep_hang_ngay import GhiChepHangNgay, get_value_ghi_chep_hang_ngay
import pandas as pd
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
)


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
        self.ten_cong_viec = ten_cong_viec
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

if __name__ == "__main__":
    print("dataset/cong_viec.py")
