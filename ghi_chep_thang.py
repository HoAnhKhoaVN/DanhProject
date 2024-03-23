from typing import Text, Dict
from nhan_vien import NhanVien, get_value_for_staff
from constant import (
    NUM_DIGIT_IN_DAY,
    MAX_NUM_DAY,
    LST_FIELD_DAILY,
    OUTPUT_EXCEL,
    TNS,
    GIO_TL,
    COT_CO_DINH,
    CHU_THICH
    )
import os
import pandas as pd


class GhiChepThang:
    def __init__(
        self,
        thang: int,
        dict_nhan_vien: Dict[Text, NhanVien]
    ) -> None:
        self.thang = thang
        self.dict_nhan_vien = dict_nhan_vien

    def so_nhan_vien(self):
        return len(self.dict_nhan_vien)
    
    


def clear_dataframe(df: pd.DataFrame)-> pd.DataFrame:
    """Làm sạch data frame trước khi đưa vào dữ liệu

    Args:
        df (pd.DataFrame): DataFrame cần làm sạch

    Returns:
        pd.DataFrame: DataFrame đã làm sạch
    """
    # Bỏ tất cả các dòng chứa toàn bộ NULL
    df.dropna(how='all',inplace= True)
    df.where(pd.notnull(df), None, inplace= True)
    # Ghi nhận số ngày công
    ngay_cong = []
    for ngay in range(1, MAX_NUM_DAY + 1):
        for ncong in LST_FIELD_DAILY:
            if ncong != TNS:
                for cv in GIO_TL:
                    name = f"{ncong}__{cv}__{str(ngay).zfill(NUM_DIGIT_IN_DAY)}"
                    ngay_cong.append(name)
            else:
                name = f"{ncong}__{str(ngay).zfill(NUM_DIGIT_IN_DAY)}"
                ngay_cong.append(name)
    # Đổi tên các trường cho ngày công
    ten_cot_moi = COT_CO_DINH + ngay_cong + [CHU_THICH]
    column_name = dict(zip(df.columns, ten_cot_moi))
    df.rename(columns = column_name, inplace = True)
    # Reset lại index bắt đầu từ 0
    df.reset_index(inplace=True)

    return df

def get_ghi_chep_hang_tháng(
    file_excel: Text
    )->GhiChepThang:

    # Lấy dữ liệu tháng mấy vậy?
    thang = file_excel.split(os.sep)[-1].split('.')[0].split('-')[1]

    # Đọc file excel chưa thông tin của tháng
    df = pd.read_excel(file_excel,sheet_name=None, na_values="null")
    # Lấy ra danh sách nhân viên
    lst_ma_nhan_vien = [k for k in df.keys() if k.strip().isnumeric()]
    # Tạo ghi chép trong tháng cho từng nhân viên
    dict_nhan_vien = {}
    for manv in lst_ma_nhan_vien:
        temp_df : pd.DataFrame = clear_dataframe(df[manv])
        temp_df.to_excel(OUTPUT_EXCEL,sheet_name= 'demo') 
        nv = get_value_for_staff(
            manv= manv,
            df = temp_df
        )
        if nv:
            dict_nhan_vien[nv.msnv] = nv

    # Trả về ghi chép trong tháng
    return GhiChepThang(
        thang= thang,
        dict_nhan_vien= dict_nhan_vien
    )



if __name__ == "__main__":
        print("dataset/ghi_chep_thang.py")