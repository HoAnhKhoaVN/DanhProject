from toan_bo_data import ToanBoData
from utils import dump_pickle

def load_toan_bo_data():
    x = ToanBoData(root="Data")
    dump_pickle(
        fn = "full_data_v3.plk",
        obj= x   
    )

if __name__ == "__main__":
    print("file main.py")
    load_toan_bo_data()
   