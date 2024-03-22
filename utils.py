from pickle import dump, load
from typing import Text, Any
from collections import defaultdict
import os
# from tkinter.filedialog import askopenfile
from customtkinter import (
    HORIZONTAL,
    CTkLabel,
    CTkProgressBar,
    CTk
)
import time

def create_list_defaultdict():
    """Tạo một defaultdict để có thể dump thành file pickle
    Sửa lỗi dựa: https://stackoverflow.com/questions/72339545/attributeerror-cant-pickle-local-object-locals-lambda
    """
    return defaultdict(list)

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

def open_file():
    file_path = CTk.askopenfile(mode='r', filetypes=[('Image Files', '*jpeg')])
    if file_path is not None:
        pass


def uploadFiles(ws):
    pb1 = CTkProgressBar(
        ws, 
        orient=HORIZONTAL, 
        length=300, 
        mode='determinate'
        )
    pb1.grid(row=4, columnspan=3, pady=20)
    for i in range(5):
        ws.update_idletasks()
        pb1['value'] += 20
        time.sleep(1)
    pb1.destroy()
    CTkLabel(ws, text='File Uploaded Successfully!', foreground='green').grid(row=4, columnspan=3, pady=10)

def latest_change(filename):
    return max(os.path.getmtime(filename), os.path.getctime(filename))

if __name__ == "__main__":
    print("file utils.py")