#!/usr/bin/env python3
# coding:UTF-8

from LSBSteg import LSBSteg
import cv2
import tkinter as tk
from tkinter import filedialog

win = tk.Tk()
win.title("图片文字隐写")
width = 350
height = 200
screenwidth = win.winfo_screenwidth()  
screenheight = win.winfo_screenheight() 
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth-width)/2, (screenheight-height)/2)   
win.geometry(alignstr)
win["background"]="#F0F0F0"
win.resizable(width=False, height=False)

times=1

def select_Path():
    file_path = filedialog.askopenfilename()
    path.set(file_path)

def get_file(b_located):
    global path
    frame=tk.Frame(b_located,bg="#F0F0F0")
    path=tk.StringVar()
    tk.Label(frame,text="ImgPath:",bg="#F0F0F0").pack(side="left")
    tk.Entry(frame,textvariable=path,state="disabled").pack(side="left")
    tk.Frame(frame,width=5,bg="#F0F0F0").pack(side="left")
    tk.Button(frame,text="Select",command=select_Path).pack(side="left")
    frame.pack()
    
def b_encode():
    global b_text
    global b_warning
    global times
    global b_frame
    if times!=1:
        b_frame.pack_forget()
    times+=1
    b_frame=tk.Frame(win,bg="#F0F0F0")
    b_warning=tk.StringVar()
    b_warning.set("The picture must be png")
    tk.Label(b_frame,textvariable=b_warning,bg="#F0F0F0").pack()
    get_file(b_frame)
    tk.Label(b_frame,pady=1,text="Text to be encoded:",bg="#F0F0F0").pack()
    b_text=tk.Text(b_frame,height=3,width=40,wrap="word")
    b_text.pack()
    tk.Frame(b_frame,height=5,bg="#F0F0F0").pack()
    tk.Button(b_frame,text="Encode",padx=2,pady=2,command=r_encode).pack()
    b_frame.pack()

def r_encode():
    if str(path.get()[-4::])==".png":
        steg = LSBSteg(cv2.imread(path.get()))
        img_encoded = steg.encode_text(b_text.get("0.0","end"))
        cv2.imwrite(str(path.get()[:-4:]) + ".encoded.png", img_encoded)
        b_warning.set("The encoded picture is done (in the original folder)")
    else:
        b_warning.set("It's not a png picture")

def b_decode():
    global times
    global b_frame
    global b_warning
    global b_text
    if times!=1:
        b_frame.pack_forget()
    times+=1
    b_frame=tk.Frame(win,bg="#F0F0F0")
    b_warning=tk.StringVar()
    b_warning.set("The picture must be png")
    tk.Label(b_frame,textvariable=b_warning,bg="#F0F0F0").pack()
    get_file(b_frame)
    tk.Label(b_frame,pady=1,text="The decoded text:",bg="#F0F0F0").pack()
    b_text=tk.Text(b_frame,height=3,width=40,wrap="word",state="disabled")
    b_text.pack()
    tk.Frame(b_frame,height=5,bg="#F0F0F0").pack()
    tk.Button(b_frame,text="Decode",padx=2,pady=2,command=r_decode).pack()
    b_frame.pack()

def r_decode():
    if str(path.get()[-4::])==".png":
        im = cv2.imread(path.get())
        detext = LSBSteg(im).decode_text()
        b_text.config(state="normal")
        b_text.insert("0.0",detext)
    else:
        b_warning.set("It's not a png picture")

tk.Frame(win,height=10,bg="#F0F0F0").pack()
frametop=tk.Frame(win,bg="#F0F0F0")
tk.Button(frametop,text="Encode",padx=6,pady=4,command=b_encode).pack(side="left")
tk.Frame(frametop,width=50,bg="#F0F0F0").pack(side="left")
tk.Button(frametop,text="Decode",padx=6,pady=4,command=b_decode).pack(side="left")
frametop.pack()

win.mainloop()
