from constant import DATANAME, DI_TRE
from utils import load_pickle


if __name__ == "__main__":
    data = load_pickle(fn = DATANAME)
    ngay_cong : dict = data.dict_ghi_chep_cac_nam['2024'].dict_ghi_chep_12_thang['3'].dict_nhan_vien['4431'].dict_ghi_chep_cong_viec[DI_TRE]
    print(f'Về sớm: {ngay_cong}')

    exit()