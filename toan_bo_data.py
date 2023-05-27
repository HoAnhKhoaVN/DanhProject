from typing import Text, List
from utils import load_pickle, dump_pickle
from tqdm import tqdm
import os
from constant import SEP
from ghi_chep_nam import get_ghi_chep_hang_nam


def get_toan_bo_data(root: Text):
    # Tạo dict với các năm
    dict_ghi_chep_cac_nam = {}

    for fn in tqdm(os.listdir(path= root), desc = "Ghi chép hàng năm: "):
        nam = fn.split(SEP)[-1] # năm có dạng Y-2023
        year_path = os.path.join(root, fn)
        dict_ghi_chep_cac_nam[nam] = get_ghi_chep_hang_nam(year_fd= year_path)

    # Trả về kết quả
    return dict_ghi_chep_cac_nam

class ToanBoData:
    def __init__(
        self,
        root : Text = None,
        cache_path : Text = None
    ) -> None:
        assert root, "Không tìm thấy tên thư mục chứa dữ liệu"
        self.root = root
        if cache_path:
            self.dict_ghi_chep_cac_nam = self.load_cache(cache_path)
        else:
            self.dict_ghi_chep_cac_nam = get_toan_bo_data(self.root)


    def load_cache(
            self,
            cache_file: Text,
        ):
        return load_pickle(cache_file)

    def thong_ke(self):
        pass


    def ve_so_do(self):
        pass

if __name__ == "__main__":
    print("Hello")

    