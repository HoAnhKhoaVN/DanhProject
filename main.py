from toan_bo_data import ToanBoData
from utils import dump_pickle, load_pickle
from cong_viec import CongViec
from ghi_chep_hang_ngay import HanhChanh, TangCa
from constant import (
    DATANAME,
    DATAPATH,
    NGHI_PHEP
)

def load_toan_bo_data(root= DATAPATH , cache_path= DATANAME):
    x = ToanBoData(root, cache_path)
    dump_pickle(
        fn = DATANAME,
        # fn = 'test.plk',
        obj= x   
    )

if __name__ == "__main__":
    print("file main.py")
    # data = load_toan_bo_data(root = 'dummy_data_2', cache_path= None)

    data = load_pickle(fn = DATANAME)
    # print(data.__dict__)
    # print(data.dict_ghi_chep_cac_nam['2023'].dict_ghi_chep_12_thang['1'].__dict__)
    # tong_gio_tang_ca = 0.0
    # lst_ngay_tang_ca = []
    # lst_gio_tang_ca = []
    # for k, v in data.dict_ghi_chep_cac_nam['2023'].dict_ghi_chep_12_thang['1'].dict_nhan_vien['3309'].dict_ghi_chep_cong_viec.items():
    #     for ban_ve, cv in v.items():
    #         print(f'{k}-{ban_ve}-{cv[0]}')
    #         cong_viec :CongViec = cv[0]
    #         tang_ca = cong_viec.ghi_ghep_hang_ngay[0].tang_ca
    #         if tang_ca is not None:
    #             gio_tang_ca = tang_ca.gio
    #             ngay_tang_ca = cong_viec.ghi_ghep_hang_ngay[0].ngay

    #             tong_gio_tang_ca+= gio_tang_ca
    #             lst_ngay_tang_ca.append(ngay_tang_ca)
    #             lst_gio_tang_ca.append(gio_tang_ca)
    # print(f'lst_ngay_tang_ca: {lst_ngay_tang_ca}')
    # print(f'lst_gio_tang_ca: {lst_gio_tang_ca}')
    # print(f'tong_gio_tang_ca: {tong_gio_tang_ca}')


            

            




    # lst_tang_ca = lst_minutes = [v[0].ghi_ghep_hang_ngay[0].tang_ca.gio for v in cv.values()]
    # print(f'lst_tang_ca: {lst_tang_ca}')
    # gio_tang_ca = 0.0
    # if lst_tang_ca:
    #     gio_tang_ca = sum(lst_tang_ca)
    # print(f'gio_tang_ca: {gio_tang_ca}')

    # print(f'Số phút đi trễ')
    # di_tre : dict = data.dict_ghi_chep_cac_nam['2023'].dict_ghi_chep_12_thang['1'].dict_nhan_vien['1602'].dict_ghi_chep_cong_viec['Đi trể']

    # cv = 'Đi trể'
    # # for v in di_tre.values():
    # #     print(f'v[0].ghi_ghep_hang_ngay: {v[0].ghi_ghep_hang_ngay[0].hanh_chanh.TSN_nghi}')
    # lst_minutes = [v[0].ghi_ghep_hang_ngay[0].hanh_chanh.TSN_nghi for v in di_tre.values()]
    # if lst_minutes:
    #     minutes = sum(lst_minutes)
    # print(f'lst_minutes: {minutes}')

    # print(f'số tăng ca')
        

    # print(f'Số phút về sớm')
    # ve_som : dict = data.dict_ghi_chep_cac_nam['2023'].dict_ghi_chep_12_thang['1'].dict_nhan_vien['3823'].dict_ghi_chep_cong_viec[VE_SOM]

    # cv = 'Đi trể'
    # # for v in di_tre.values():
    # #     print(f'v[0].ghi_ghep_hang_ngay: {v[0].ghi_ghep_hang_ngay[0].hanh_chanh.TSN_nghi}')
    # lst_ngay_ve_som = []
    # lst_gio_ve_som = []
    # for v in ve_som.values():
    #     cv = v[0]
    #     ngay_ve_som = cv.ghi_ghep_hang_ngay[0].ngay
    #     gio_ve_som = cv.ghi_ghep_hang_ngay[0].hanh_chanh.TSN_nghi

    #     lst_ngay_ve_som.append(ngay_ve_som)
    #     lst_gio_ve_som.append(gio_ve_som)

    # print(f'lst_ngay_ve_som: {lst_ngay_ve_som}')
    # print(f'lst_gio_ve_som: {lst_gio_ve_som}')
    # if lst_ngay_ve_som:
    #     hour = sum(lst_gio_ve_som)
    # print(f'Sum hour : {hour}')
        
    nghi_phep : dict = data.dict_ghi_chep_cac_nam['2023'].dict_ghi_chep_12_thang['1'].dict_nhan_vien['1883'].dict_ghi_chep_cong_viec[NGHI_PHEP]
    lst_ngay_nghi_phep = []
    lst_gio_nghi_phep = []
    for v in nghi_phep.values():
        cv = v[0]
        for _cv in cv.ghi_ghep_hang_ngay:
            ngay_ve_som = _cv.ngay
            gio_ve_som = _cv.hanh_chanh.TSN_nghi

            lst_ngay_nghi_phep.append(ngay_ve_som)
            lst_gio_nghi_phep.append(gio_ve_som)

    print(f'lst_ngay_ve_som: {lst_ngay_nghi_phep}')
    print(f'lst_gio_ve_som: {lst_gio_nghi_phep}')
    hour = 0.0
    if lst_gio_nghi_phep:
        hour = sum(lst_gio_nghi_phep)
    print(f'Sum hour : {hour}')
        

       