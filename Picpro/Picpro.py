#!/usr/bin/env python3
# coding:UTF-8

from LSBSteg import LSBSteg
import cv2
import tkinter as tk
from tkinter import filedialog

win = tk.Tk()
win.title("Picpro")
width = 350
height = 200
screenwidth = win.winfo_screenwidth()  
screenheight = win.winfo_screenheight() 
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth-width)/2, (screenheight-height)/2)   
win.geometry(alignstr)
win["background"]="#F0F0F0"
win.resizable(width=False, height=False)

times=1

def back():
    frame_com.pack_forget()
    framemain.pack()

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
    frame_describe.pack_forget()
    if times!=1:
        b_frame.pack_forget()
    times+=1
    b_frame=tk.Frame(frame_com,bg="#F0F0F0")
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
    frame_describe.pack_forget()
    if times!=1:
        b_frame.pack_forget()
    times+=1
    b_frame=tk.Frame(frame_com,bg="#F0F0F0")
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
        img = cv2.imread(path.get())
        detext = LSBSteg(img).decode_text()
        b_text.config(state="normal")
        b_text.insert("0.0",detext)
    else:
        b_warning.set("It's not a png picture")

def j_to_p():
    global times
    global b_frame
    global b_warning
    global b_text
    if times!=1:
        b_frame.pack_forget()
    times+=1
    b_frame=tk.Frame(frame_com,bg="#F0F0F0")
    tk.Frame(b_frame,height=20,bg="#F0F0F0").pack()
    b_warning=tk.StringVar()
    b_warning.set("The picture must be jpg")
    tk.Label(b_frame,textvariable=b_warning,bg="#F0F0F0").pack()
    get_file(b_frame)
    tk.Frame(b_frame,height=15,bg="#F0F0F0").pack()
    tk.Button(b_frame,text="Convert",padx=3,pady=3,command=r_j_to_p).pack()
    b_frame.pack()

def r_j_to_p():
    if str(path.get()[-4::])==".jpg":
        img = cv2.imread(path.get())
        cv2.imwrite(str(path.get()[:-4:]) + ".png",img)
        b_warning.set("The picture is done (in the original folder)")
    else:
        b_warning.set("It's not a jpg picture")

def p_to_j():
    global times
    global b_frame
    global b_warning
    global b_text
    if times!=1:
        b_frame.pack_forget()
    times+=1
    b_frame=tk.Frame(frame_com,bg="#F0F0F0")
    tk.Frame(b_frame,height=20,bg="#F0F0F0").pack()
    b_warning=tk.StringVar()
    b_warning.set("The picture must be png")
    tk.Label(b_frame,textvariable=b_warning,bg="#F0F0F0").pack()
    get_file(b_frame)
    tk.Frame(b_frame,height=15,bg="#F0F0F0").pack()
    tk.Button(b_frame,text="Convert",padx=3,pady=3,command=r_p_to_j).pack()
    b_frame.pack()

def r_p_to_j():
    if str(path.get()[-4::])==".png":
        img = cv2.imread(path.get())
        cv2.imwrite(str(path.get()[:-4:]) + ".jpg",img)
        b_warning.set("The picture is done (in the original folder)")
    else:
        b_warning.set("It's not a png picture")

def anti_id():
    global times
    global b_frame
    global b_warning
    global b_text
    global b_mode
    frame_describe.pack_forget()
    if times!=1:
        b_frame.pack_forget()
    times+=1
    b_frame=tk.Frame(frame_com,bg="#F0F0F0")
    tk.Frame(b_frame,height=20,bg="#F0F0F0").pack()
    b_warning=tk.StringVar()
    b_warning.set("The picture must be jpg or png")
    tk.Label(b_frame,textvariable=b_warning,bg="#F0F0F0").pack()
    get_file(b_frame)
    tk.Frame(b_frame,height=15,bg="#F0F0F0").pack()
    c_frame=tk.Frame(b_frame,bg="#F0F0F0")
    b_mode=tk.StringVar()
    b_mode.set("NORMAL")
    tk.OptionMenu(c_frame,b_mode,"POOR","NORMAL","SUPER","ULTRA").pack(side="left")
    tk.Frame(c_frame,width=10,bg="#F0F0F0").pack(side="left")
    tk.Button(c_frame,text="Process",padx=3,pady=3,command=id_draw).pack(side="left")
    c_frame.pack()
    b_frame.pack()

def id_draw():
    if str(path.get()[-4::])==".png" or str(path.get()[-4::])==".jpg":
        img = cv2.imread(path.get())
        if b_mode.get()=="NORMAL":
            cont=60
        elif b_mode.get()=="POOR":
            cont=45
        elif b_mode.get()=="SUPER":
            cont=75
        elif b_mode.get()=="ULTRA":
            cont=90
        linewid=round((img.shape[0]+img.shape[1])/cont)
        thick=round(linewid/10)
        ran=range(linewid,img.shape[0]+img.shape[1],linewid)
        for i in range(len(ran)):
            cv2.line(img,(0,ran[i]),(ran[i],0),(0,255,255),thick)
            cv2.line(img,(0,img.shape[0]-ran[i]),(ran[i],img.shape[0]),(0,255,255),thick)
        cv2.imwrite(str(path.get()[:-4:]) + ".drawn" + str(path.get()[-4::]),img)
        b_warning.set("The picture is done (in the original folder)")
    else:
        b_warning.set("It's not a jpg or png picture")

def lsb_encode():
    global framemain
    global frame_com
    global frame_describe
    framemain.pack_forget()
    frame_com=tk.Frame(win,bg="#F0F0F0")
    frame_title=tk.Frame(frame_com,bg="#F0F0F0")
    tk.Label(frame_title,text="LSB Encode",bg="#F0F0F0").pack(side="left")
    tk.Button(frame_title,text="Encode",padx=5,pady=3,command=b_encode).pack(side="left")
    tk.Frame(frame_title,width=10,bg="#F0F0F0").pack(side="left")
    tk.Button(frame_title,text="Decode",padx=5,pady=3,command=b_decode).pack(side="left")
    tk.Frame(frame_title,width=10,bg="#F0F0F0").pack(side="left")
    tk.Button(frame_title,text="Back",padx=5,pady=3,command=back).pack(side="left")
    frame_title.pack()
    frame_describe=tk.Frame(frame_com,bg="#F0F0F0")
    tk.Frame(frame_describe,height=20,bg="#F0F0F0").pack()
    tk.Label(frame_describe,text="This function will help you encode your text.",bg="#F0F0F0").pack()
    tk.Label(frame_describe,text="It will use LSB tech to encode your info",bg="#F0F0F0").pack()
    tk.Label(frame_describe,text="and hide it into a picture you provided.",bg="#F0F0F0").pack()
    frame_describe.pack()
    frame_com.pack()

def convert_jp():
    global framemain
    global frame_com
    framemain.pack_forget()
    frame_com=tk.Frame(win,bg="#F0F0F0")
    frame_title=tk.Frame(frame_com,bg="#F0F0F0")
    tk.Label(frame_title,text="Convert jpg&png",bg="#F0F0F0").pack(side="left")
    tk.Button(frame_title,text="jpg to png",padx=5,pady=3,command=j_to_p).pack(side="left")
    tk.Frame(frame_title,width=10,bg="#F0F0F0").pack(side="left")
    tk.Button(frame_title,text="png to jpg",padx=5,pady=3,command=p_to_j).pack(side="left")
    tk.Frame(frame_title,width=10,bg="#F0F0F0").pack(side="left")
    tk.Button(frame_title,text="Back",padx=5,pady=3,command=back).pack(side="left")
    frame_title.pack()
    frame_com.pack()

def anti_identify():
    global framemain
    global frame_com
    global frame_describe
    framemain.pack_forget()
    frame_com=tk.Frame(win,bg="#F0F0F0")
    frame_title=tk.Frame(frame_com,bg="#F0F0F0")
    tk.Label(frame_title,text="Anti-identify",bg="#F0F0F0").pack(side="left")
    tk.Frame(frame_title,width=5,bg="#F0F0F0").pack(side="left")
    tk.Button(frame_title,text="Draw lines",padx=5,pady=3,command=anti_id).pack(side="left")
    tk.Frame(frame_title,width=10,bg="#F0F0F0").pack(side="left")
    tk.Button(frame_title,text="Back",padx=5,pady=3,command=back).pack(side="left")
    frame_title.pack()
    frame_describe=tk.Frame(frame_com,bg="#F0F0F0")
    tk.Frame(frame_describe,height=20,bg="#F0F0F0").pack()
    tk.Label(frame_describe,text="This function will help you anti-identify your picture.",bg="#F0F0F0").pack()
    tk.Label(frame_describe,text="It will draw multiple yellow slanted lines",bg="#F0F0F0").pack()
    tk.Label(frame_describe,text="on your picture to cover your sensitive info.",bg="#F0F0F0").pack()
    frame_describe.pack()
    frame_com.pack()

tk.Frame(win,height=15,bg="#F0F0F0").pack()
framemain=tk.Frame(win,bg="#F0F0F0")
tk.Label(framemain,text="Picpro",bg="#F0F0F0").pack()
tk.Frame(framemain,height=15,bg="#F0F0F0").pack()
frame_start1=tk.Frame(framemain,bg="#F0F0F0")
tk.Button(frame_start1,text="Convert jpg&png",padx=6,pady=4,command=convert_jp).pack(side="left")
tk.Frame(frame_start1,width=20,bg="#F0F0F0").pack(side="left")
tk.Button(frame_start1,text="LSB Encode",padx=6,pady=4,command=lsb_encode).pack(side="left")
frame_start1.pack()
tk.Frame(framemain,height=15,bg="#F0F0F0").pack()
frame_start2=tk.Frame(framemain,bg="#F0F0F0")
tk.Button(frame_start2,text="Anti-identify",padx=6,pady=4,command=anti_identify).pack(side="left")
tk.Frame(frame_start2,width=20,bg="#F0F0F0").pack(side="left")
tk.Button(frame_start2,text="Coming soon",padx=6,pady=4,command="disabled").pack(side="left")
frame_start2.pack()
framemain.pack()






win.mainloop()
