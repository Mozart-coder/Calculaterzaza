import tkinter as tk

list_cal = []
list_total = []

def plusf():
    nu1 = float(num_box.get())
    list_cal.append(nu1)

    output_label2.configure(text = "(plus)")

def subf():
    nu1 = float(num_box.get())
    nu1 = 0 - nu1
    list_cal.append(nu1)

    output_label2.configure(text="(minus)")


def multiplyf():
    nu1 = float(num_box.get())
    nu2 = list_cal[-1]*nu1
    list_cal.pop()
    list_cal.append(nu2)

    output_label2.configure(text="(multiply)")
    
def dividef():
    nu1 = float(num_box.get())
    nu2 = list_cal[-1]/nu1
    list_cal.pop()
    list_cal.append(nu2)

    output_label2.configure(text="(divide)")

def Calculate():
    result = 0
    for i in list_cal:
        result += i

    output1 = '' 
    for i in list_cal:
        if i == list_cal[-1]:
            output1 += str(i)
        else :
            output1 += str(i) + '+' 
    output1 += " = " + str(result) 
    output_label.configure(text=output1)

    list_total.append(result) # เก็บข้อมูลผลลัพท์
    output2 = ''
    for m in list_total:
        output2 += "result " + " : " + str(m) + "\n"
    re_label.configure(text=output2);list_cal.clear()


def plusresultf():
    plusresult = 0
    for sum in list_total:
        plusresult += sum

    output3 = ''
    for i in list_total:
        if i == list_total[-1]:
            output3 += str(i)
        else :
            output3 += str(i) + '+' 
    output3 += " = " + str(plusresult) 
    re_label.configure(text=output3)


#ลบออก
def clear():
    list_cal.clear()

    output_label.configure(text="")
    output_label2.configure(text='')

#ลบประวัติออกหมด
def clearall():
    list_cal.clear()
    list_total.clear()

    output_label.configure(text="")
    output_label2.configure(text='')
    re_label.configure(text="")


window = tk.Tk()
window.title("Calculater")
window.minsize(350,600)

title_label = tk.Label(master=window,text = "input number")
title_label.pack()

output_label = tk.Label(master=window)
output_label.pack()

num_box = tk.Entry(master=window) #กล่องข้อความ # ใช่โปรแกรมป้องกันใส่ str
num_box.pack()

output_label2 = tk.Label(master=window)
output_label2.pack()

sum_button = tk.Button(master=window,text="+" , command = plusf,width =7,height = 1)
sum_button.pack(pady=5)

sub_button = tk.Button(master=window, text='-',command= subf,width =7,height = 1)
sub_button.pack(pady=5)

multiply_button = tk.Button(master=window,text="x",command=multiplyf,width =7,height = 1)
multiply_button.pack(pady=5)

divide_button = tk.Button(master=window,text = "/",command = dividef,width =7,height = 1)
divide_button.pack(pady=5)

sumre_button = tk.Button(master=window,text="sum all result",command=plusresultf)
sumre_button.pack(pady=5)

C_button = tk.Button(master=window,text="C",command = clear,width =7,height = 1)
C_button.pack(pady=5)

CE_button = tk.Button(master=window,text="CE",command = clearall,width =7,height = 1)
CE_button.pack(pady=5)

enter_button = tk.Button(master=window,text="Enter", command = Calculate,width = 15,height = 2)
enter_button.pack(pady=5)

re_label = tk.Label(master=window)
re_label.pack(pady=5)

window.mainloop()

#กดแล้วลบข้อมูลในกล่อง
#กรณี input ข้อมูลที่ไม่ใช่ตัวเลข