from typing import Text, List
from constant import (
    MAX_NUM_DAY,
    NUM_DIGIT_IN_DAY,
    HC_GIO,
    HC_TL,
    TNS_NGHI, 
    TC_GIO,
    TC_TL
)
import pandas as pd


class TangCa:
    def __init__(
        self,
        gio: float,
        ti_le: float
    )-> None:
        self.gio = gio
        self.ti_le = ti_le

    def thong_ke(self):
        pass

    def is_null(self):
        pass
        

class HanhChanh:
    def __init__(
        self,
        gio: float,
        ti_le: float,
        TSN_nghi: float
    ) -> None:
        self.gio = gio
        self.ti_le = ti_le
        self.TSN_nghi = TSN_nghi

    def thong_ke(self):
        pass

    def is_null(self):
        pass


class GhiChepHangNgay:
    def __init__(
        self,
        ngay: Text,
        gio_HC: float,
        ti_le_HC: float,
        TSN_nghi_HC: float,
        gio_TC: float,
        ti_le_TC: float,
    ) -> None:
        self.ngay = ngay
        self.tang_ca = TangCa(gio_TC, ti_le_TC)
        self.hanh_chanh = HanhChanh(gio_HC, ti_le_HC, TSN_nghi_HC)

    def is_null(self):
        pass
    
    def thong_ke(self):
        pass

def get_value_ghi_chep_hang_ngay(
    idx: int,
    _df: pd.DataFrame
)-> List[GhiChepHangNgay]:
    """Ghi nhận ghi chép của công việc trong 1 tháng (luôn có 31 ngày cho dễ tính toán)

    Args:
        idx (int): số thứ tự của ngày từ 1 -> 31
        _df (pd.DataFrame): DataFrame chứa kết quả phân công.

    Returns:
        List[GhiChepHangNgay]: Danh sách ghi chép cho từng ngày
    """    
    lst_ghi_chep_hang_ngay = []
    for ngay in range(1,MAX_NUM_DAY):
        _ngay = str(ngay).zfill(NUM_DIGIT_IN_DAY)
        hc_gio = f"{HC_GIO}{_ngay}"
        hc_tl = f"{HC_TL}{_ngay}"
        tns_nghi = f"{TNS_NGHI}{_ngay}"
        tc_gio = f"{TC_GIO}{_ngay}"
        tc_tl = f"{TC_TL}{_ngay}"
        lst_ghi_chep_hang_ngay.append(
            GhiChepHangNgay(
                ngay= _ngay,
                gio_HC= _df[hc_gio][idx],
                ti_le_HC= _df[hc_tl][idx],
                TSN_nghi_HC= _df[tns_nghi][idx],
                gio_TC= _df[tc_gio][idx],
                ti_le_TC = _df[tc_tl][idx]
            )
        )
    return lst_ghi_chep_hang_ngay


if __name__ == "__main__":
    print("dataset/ghi_chep_hang_ngay.py")