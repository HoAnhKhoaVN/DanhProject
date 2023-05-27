from pickle import dump, load
from typing import Text, Any

def load_pickle(fn: Text):
    with open(fn, "rb") as f:
        data = load(f)
    return data

def dump_pickle(
        fn: Text,
        obj: Any,
    ):
    with open(fn, "wb") as f:
        dump(obj, f)
    
def check_cay_thu_muc(root: Text)-> bool:
    pass

def chuan_hoa_cay_thu_muc(root: Text)-> None:
    # Có thể lưu cache lại để nếu đã có rồi thì chỉ các excel mới thôi
    pass

if __name__ == "__main__":
    print("file utils.py")