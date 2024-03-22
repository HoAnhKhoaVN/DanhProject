# from tkinter import *
# from tkinter.ttk import *
from tkinter.filedialog import askopenfile
import time
from customtkinter import (
    HORIZONTAL,
    CTkLabel,
    CTkProgressBar,
    CTk,
    CTkButton,
)

ws = CTk()
ws.title('PythonGuides')
ws.geometry('400x200') 


def open_file():
    file_path = askopenfile(mode='r', filetypes=[('Excel_97', '*xls'), ('Excel_97', '*xlsx')])
    if file_path is not None:
        pass


def uploadFiles():
    pb1 = CTkProgressBar(
        master = ws, 
        orientation=HORIZONTAL, 
        width=300, 
        mode='determinate'
        )
    pb1.grid(row=4, columnspan=3, pady=20)
    # for i in range(5):
    #     ws.update_idletasks()
    #     print(f'pb1: {pb1.__dict__}')
    #     pb1['value'] += 20
    #     time.sleep(1)
    pb1.destroy()
    CTkLabel(ws, text='File Uploaded Successfully!', fg_color='green').grid(row=4, columnspan=3, pady=10)
        
    
    
adhar = CTkLabel(
    ws, 
    text='Upload Government id in jpg format '
    )
adhar.grid(row=0, column=0, padx=10)

adharbtn = CTkButton(
    ws, 
    text ='Choose File', 
    command = lambda:open_file()
    ) 
adharbtn.grid(row=0, column=1)

dl = CTkLabel(
    ws, 
    text='Upload Driving License in jpg format '
    )
dl.grid(row=1, column=0, padx=10)

dlbtn = CTkButton(
    ws, 
    text ='Choose File ', 
    command = lambda:open_file()
    ) 
dlbtn.grid(row=1, column=1)

ms = CTkLabel(
    ws, 
    text='Upload Marksheet in jpg format '
    )
ms.grid(row=2, column=0, padx=10)

msbtn = CTkButton(
    ws, 
    text ='Choose File', 
    command = lambda:open_file()
    ) 
msbtn.grid(row=2, column=1)

upld = CTkButton(
    ws, 
    text='Upload Files', 
    command=uploadFiles
    )
upld.grid(row=3, columnspan=3, pady=10)


if __name__ == "__main__":
    ws.mainloop()