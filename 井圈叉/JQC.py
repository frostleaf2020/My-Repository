#!/usr/bin/python3
# -*- coding: UTF-8 -*-
 
import tkinter as tk
import time
from tkinter import messagebox as mb
from random import randrange as rand

win = tk.Tk()
win.title("井圈叉")
width = 300
height = 300
screenwidth = win.winfo_screenwidth()  
screenheight = win.winfo_screenheight() 
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth-width)/2, (screenheight-height)/2)   
win.geometry(alignstr)
win.resizable(width=False, height=False)

def startgame():
    global turn
    turn = 1
    if gamestarter.get()=="Start game":
        gamestarter.set("Try again")
        ingame[1][1].set("o")
    else:
        for k in range(3):
            for l in range(3):
                ingame[k][l].set("")
        gamestarter.set("Start game")

def checkline(a,b,num,cha):
    numline = 0
    for k in [0,1,2]:
        if ingame[a][k].get()==cha:
            numline+=1
        if ingame[a][k].get()=="":
            numline+=4
    if numline==num:
        return [True,"row"]
    else:
        numline = 0
        for l in [0,1,2]:
            if ingame[l][b].get()==cha:
                numline+=1
            if ingame[l][b].get()=="":
                numline+=4
        if numline==num:
            return [True,"col"]
        else:
            numline = 0
            for m in [0,1,2]:
                if ingame[m][m].get()==cha:
                    numline+=1
                if ingame[m][m].get()=="":
                    numline+=4
            if numline==num:
                return [True,"fsl"]
            else:
                numline = 0
                for n in [0,1,2]:
                    if ingame[n][2-n].get()==cha:
                        numline+=1
                    if ingame[n][2-n].get()=="":
                        numline+=4
                if numline==num:
                    return [True,"sla"]
                else:
                    return [False]

def compeline(a,b,wh,cha):
    if wh=="row":
        for k in [0,1,2]:
            if ingame[a][k].get()!=cha:
                return a,k
    if wh=="col":
        for k in [0,1,2]:
            if ingame[k][b].get()!=cha:
                return k,b
    if wh=="sla":
        for k in [0,1,2]:
            if ingame[k][2-k].get()!=cha:
                return k,2-k
    if wh=="fsl":
        for k in [0,1,2]:
            if ingame[k][k].get()!=cha:
                return k,k

def clickgame(a,b):
    global turn
    k = 1
    l = 1
    if ingame[1][1].get()=="o" and ingame[a][b].get()=="":
        ingame[a][b].set("x")
        if turn==1:
            chlist1 = [[0,2],[2,0]]
            for k in chlist1[rand(2)]:
                for l in chlist1[rand(2)]:
                    if k==2:
                        fk=0
                    else:
                        fk=2
                    if l==2:
                        fl=0
                    else:
                        fl=2
                    if ingame[k][l].get()=="" and ingame[fk][fl].get()=="":
                        ingame[k][l].set("o")
                        turn+=1
                        break
                else:
                    continue
                break
        elif turn==2:
            for fk in [0,2]:
                for fl in [0,2]:
                    if ingame[fk][fl].get()=="o":
                        if fk==2:
                            k=0
                        else:
                            k=2
                        if fl==2:
                            l=0
                        else:
                            l=2
                        if ingame[k][l].get()=="":
                            ingame[k][l].set("o")
                            turn+=1
                            break
                        else:
                            result = checkline(k,l,6,"x")
                            if result[0]:
                                k,l = compeline(k,l,result[1],"x")
                                ingame[k][l].set("o")
                                turn+=1
                                break
                            else:
                                for m in [[fk+1,fl],[fk-1,fl],[fk,fl+1],[fk,fl-1]]:
                                    k,l = m[0],m[1]
                                    if k>-1 and k<3 and l>-1 and l<3:
                                        if ingame[m[0]][m[1]].get()=="":
                                            k,l = m[0],m[1]
                                            ingame[k][l].set("o")
                                            turn+=1
                                            break
                                break
                            
                else:
                    continue
                break
        elif turn==3:
            chlist2 = [[0,1],[1,0],[1,2],[2,1]]
            for m in chlist2:
                result = checkline(m[0],m[1],6,"o")
                if result[0]:
                    k,l = compeline(m[0],m[1],result[1],"o")
                    ingame[k][l].set("o")
                    turn+=1
                    break
                else:
                    if ingame[m[0]][m[1]].get()=="o":
                        if m[1]==1:
                            k = 2-m[0]
                            l = 1
                        if m[0]==1:
                            k = 1
                            l = 2-m[1]
                        if ingame[k][l].get()=="":
                            ingame[k][l].set("o")
                            turn+=1
                            break
                        else:
                            while True:
                                randnum = chlist2[rand(4)]
                                k,l = randnum[0],randnum[1]
                                if ingame[k][l].get()=="":
                                    ingame[k][l].set("o")
                                    turn+=1
                                    break
                            break
        elif turn==4:
            chlist3 = [[0,1],[1,0],[1,2],[2,1],[1,1]]
            for m in chlist3:
                result = checkline(m[0],m[1],6,"o")
                if result[0]:
                    k,l = compeline(m[0],m[1],result[1],"o")
                    ingame[k][l].set("o")
                    turn+=1
                    break
            else:
                mb.showinfo('Winner','Tie!')

    if checkline(a,b,3,"x")[0]:
        mb.showinfo('Winner','You win!')
    if checkline(k,l,3,"o")[0]:
        mb.showinfo('Winner','Computer wins!')

tk.Label(win,text="井圈叉",font=("Helvetica",25)).pack()

framedown = []
ingame = []
for i in range(3):
    framedown.append(tk.Frame(win))
    ingame.append([])
    if i>0:
        tk.Frame(win,bg="black",height=3,width=210).pack()
    for j in range(3):
        ingame[i].append(tk.StringVar())
        ingame[i][j].set("")
        if j>0:
            tk.Frame(framedown[i],bg="black",width=3).pack(fill="y",side="left")
        tk.Button(framedown[i],width=3,textvariable=ingame[i][j],font=("Helvetica",25),command=lambda a=i, b=j: clickgame(a,b)).pack(side="left")
    framedown[i].pack()

tk.Frame(win,height=5).pack()
gamestarter=tk.StringVar()
gamestarter.set("Start game")
tk.Button(win,textvariable=gamestarter,pady=2,command=startgame).pack()

win.mainloop()
