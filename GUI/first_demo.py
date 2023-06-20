import tkinter as tk
def my_print():
    print("Hello!!")

if __name__ == "__main__":
    window = tk.Tk(screenName= "Main")
    lb_thang = tk.Label(master=window, text="Tháng: ")
    lb_thang.pack()

    et_thang = tk.Entry(master= window, width= 30)
    et_thang.pack()

    lb_nam = tk.Label(master=window, text="Năm: ")
    lb_nam.pack()

    et_nam = tk.Entry(master= window, width= 30, textvariable= "Năm: ")
    et_nam.pack()

    bt_hien_thi = tk.Button(master= window, text= "Hiện thị chi tiết")
    bt_hien_thi.pack()
    bt_hien_thi.config(command=my_print)
    window.mainloop()
        