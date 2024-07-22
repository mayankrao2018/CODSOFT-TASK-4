#import all what is needed
import tkinter as tk
import random
from tkinter import *
import tkinter.ttk as ttk
from functools import partial



main=Tk()
#"main" is main ;)

main.title("Project:|...")

main.geometry('700x450')

main.maxsize(height=450,width=700)

#Some global variables :)
global nmcp
nmcp=StringVar()
nmcp.set("Player")

global pc
pc=StringVar()
pc="Player choose: "

global cc
cc=StringVar()
cc="Computer choose: "

#game func...
def gm():
    global cpyn
    cypn=""
    cpyn=nmcp.get()
    gam=Tk()

    gam.title("Yes Project:|...")

    global psc
    psc=0
    global csc
    csc=0
    scrdis=StringVar()
    scrdis="Player won = "+str(psc)+" "+"Computer won = "+str(csc)
    
    wol=StringVar()
    wol="START"
    gam.attributes('-fullscreen',TRUE)

    cho={"1":"stone","2":"paper","3":"scissor"}

    #For stone as choice...
    def st():
        rslt=""
        global psc
        global csc
        global pc
        global cc
        cv=cho[str(random.randint(1,3))]
        if(cv=="paper"):
            rslt="Lose :("
            xc=int(csc)
            csc=xc+1
        elif(cv=="scissor"):
            rslt="won :)"
            xp=int(psc)
            psc=xp+1
        else:
            rslt="Draw :|"

        tst=pc
        dfpc="Stone"
        tst+=dfpc
        dp3_3.config(text=tst)

        tst2=cc
        dfpc=cv
        tst2+=dfpc
        dp3_4.config(text=tst2)
        
            
        global wol
        wol=str(rslt)
        dp4.config(text=wol)

        scrdis="Player won = "+str(psc)+" "+"Computer won = "+str(csc)
        dp5.config(text=scrdis)

    #For paper as choice...
    def pp():
        rslt=""
        global psc
        global csc
        global pc
        global cc
        cv=cho[str(random.randint(1,3))]
        if(cv=="scissor"):
            rslt="Lose :("
            xc=int(csc)
            csc=xc+1
        elif(cv=="stone"):
            rslt="won :)"
            xp=int(psc)
            psc=xp+1
        else:
            rslt="Draw :|"

        tst=pc
        dfpc="Paper"
        tst+=dfpc
        dp3_3.config(text=tst)

        tst2=cc
        dfpc=cv
        tst2+=dfpc
        dp3_4.config(text=tst2)

            
        global wol
        wol=str(rslt)
        dp4.config(text=wol)

        scrdis="Player won = "+str(psc)+" "+"Computer won = "+str(csc)
        dp5.config(text=scrdis)

    #For scissor as choice...
    def sc():
        rslt=""
        global psc
        global csc
        global pc
        global cc
        cv=cho[str(random.randint(1,3))]
        if(cv=="stone"):
            rslt="Lose :("
            xc=int(csc)
            csc=xc+1
        elif(cv=="paper"):
            rslt="won :)"
            xp=int(psc)
            psc=xp+1
        else:
            rslt="Draw :|"

        tst=pc
        dfpc="Scissor"
        tst+=dfpc
        dp3_3.config(text=tst)

        tst2=cc
        dfpc=cv
        tst2+=dfpc
        dp3_4.config(text=tst2)
            
        global wol
        wol=str(rslt)
        dp4.config(text=wol)

        scrdis="Player won = "+str(psc)+" "+"Computer won = "+str(csc)
        dp5.config(text=scrdis)

    #registering player with score for scoring...
    def rgstr():
        global psc
        global csc
        global cpyn
        un=""
        un=cpyn
        x=open("a.py",'a')
        l=[" ",un]
        x.writelines(l)
        un=""
        cypn=""
        x.close()
        s=open("aa.py",'a')
        if(csc==0):
            csc=1
        l=[" ",str(round(psc/csc,2))]
        s.writelines(l)
        s.close()
        gam.destroy()
        
    

    #GAME Window...
    lab2=LabelFrame(gam,text="Let's Start The Game...",font=("bold",20),fg='red',labelanchor="n",relief='solid',bg='green')
    space=Label(lab2,text="",bg='green').pack(side=TOP,padx=100)
    dp=Label(lab2,text=cpyn,borderwidth=1,relief='solid',bg='orange',font=("broadway",20)).pack(side=TOP,padx=0)
    dp2=Label(lab2,text="VS",bg='green').pack(side=TOP,padx=50)
    dp3=Label(lab2,text="Computer",borderwidth=1,relief='solid',bg='orange',font=("broadway",20)).pack(side=TOP,padx=100)

    Label(lab2,text="",bg='green').pack(side=TOP,padx=100)
    Label(lab2,text="",bg='green').pack(side=TOP,padx=100)
    dp3_3=Label(lab2,text=pc,font=("forte",18),fg='red',bg='green')
    dp3_3.pack(side=LEFT)

    dp3_4=Label(lab2,text=cc,font=("forte",18),fg='red',bg='green')
    dp3_4.pack(side=RIGHT)

    space=Label(lab2,text="",bg='green').pack(side=TOP,padx=100)
    space=Label(lab2,text="",bg='green').pack(side=TOP,padx=100)
    dp4=Label(lab2,text=wol,font=("showcard gothic",30),fg='red',bg='green')
    
    dp4.pack(side=TOP,padx=100)
    space2=Label(lab2,text="",bg='green').pack(side=TOP,padx=100)
    dp5=Label(lab2,text=scrdis,font=("broadway",20),bg='green')

    dp5.pack(side=TOP,padx=100)

    dp6=Label(lab2,text="OPTIONS:",borderwidth=1,relief='solid',bg='orange',font=("jokerman",20)).pack(side=LEFT,padx=0)
    b1=Button(lab2,text="stone",bd='5',command=st,height=1,width=15,bg='orange',font=("jokerman",12))
    b1.pack(side=LEFT)
    b2=Button(lab2,text="paper",bd='5',command=pp,height=1,width=15,bg='orange',font=("jokerman",12))
    b2.pack(side=LEFT)
    b3=Button(lab2,text="scissor",bd='5',command=sc,height=1,width=15,bg='orange',font=("jokerman",12))
    b3.pack(side=LEFT)
    qt=Button(lab2,text="quit",bd='5',command=rgstr,height=1,width=15,bg='orange',font=("jokerman",12)).pack(side=RIGHT)
    lab2.pack(expand=True,fill=BOTH,padx=15,pady=15)
    gam.mainloop()

#scor func...
def score():
    scor=Tk()
    scor.title("WHAT???")
    scor.geometry('500x500')
    scor.configure(bg='green')
    scor.minsize(height=500,width=500)
    scor.maxsize(height=500,width=500)
    lb=Label(scor,text="SCORES...",font=("showcard gothic",30),bg='green').pack()
    fr=Frame(scor,width=30,height=10,bg='green')
    fr.pack(expand=TRUE,fill=BOTH)
    scrl=Scrollbar(fr)
    scrl.pack(side=RIGHT,fill=Y)
    myst=Listbox(fr,yscrollcommand=scrl.set,height=20)
    x=open("a.py",'r')
    tx=x.read()
    l=list(map(str,tx.split()))
    x.close()
    xx=open("aa.py",'r')
    tt=xx.read()
    l2=list(map(str,tt.split()))
    xx.close()
    temps=0
    tempn=""
    pl=""
    for i in range(len(l2)-1):
        for j in range(0,len(l2)-i-1):
            if(float(l2[j])<float(l2[j+1])):
                temps=l2[j]
                tempn=l[j]
                l2[j]=l2[j+1]
                l[j]=l[j+1]
                l2[j+1]=temps
                l[j+1]=tempn
    
    for i in range(len(l2)):
        pl="Player: "+l[i]
        tempn="scored: "+str(l2[i])
        myst.insert(END,"Player: "+l[i])
        myst.insert(END, "Score: "+l2[i])
        #Label(scor,text=pl,font=("system",15)).pack()
        #Label(scor,text=tempn,font=("system",15)).pack()
    myst.pack(side=TOP,fill=BOTH)
    scrl.config(command=myst.yview)
    bb=Button(scor,text="Close",bd='5',command=scor.destroy,height=1,width=15,bg='orange',font=("jokerman",12)).pack()
    scor.mainloop()


#versus mode, but remember scores will not be placed on score board...
def vs():
    
    fvs=Tk()

    fvs.title("Hm! Project:|...")

    global fr1
    fr1=StringVar(fvs)
    fr1.set("Friend 1")

    global fr2
    fr2=StringVar(fvs)
    fr2.set("Friend 2")
    
    global pc1
    pc1=StringVar(fvs)
    pc1.set("")
    
    global pc2
    pc2=StringVar(fvs)
    pc2.set("")
            
    def h1():
        p1ch['show']=' '

    def h2():
        p2ch['show']=' '

    def star():
        global pc1
        global pc2
        global fr1
        global fr2
        
        pch1=pc1.get().lower()
        pch2=pc2.get().lower()
        fnd1=str(fr1.get())
        fnd2=str(fr2.get())
    
        if((pch1=="scissor")and(pch2=="paper"))or((pch1=="paper")and(pch2=="stone"))or((pch1=="stone")and(pch2=="scissor")):
            ch1.config(text="wwooww!! "+fnd1+" is The Winner...")
            
        elif((pch1=="scissor")and(pch2=="stone"))or((pch1=="paper")and(pch2=="scissor"))or((pch1=="stone")and(pch2=="paper")):
            ch1.config(text="wwooww!! "+fnd2+" is The Winner...")
            
        elif((pch1=="scissor")and(pch2=="scissor"))or((pch1=="paper")and(pch2=="paper"))or((pch1=="stone")and(pch2=="stone")):
            ch1.config(text="HaHa!! DRAWW is The Winner...")

        else:
            ch1.config(text="INVALID Input By Players...")

        bn1["state"]='disable'
        bn2["state"]='active'
            
    def rset():
        p1ch['show']=''
        p2ch['show']=''
        bn1["state"]='active'
        bn2["state"]='disable'
        ch1.config(text=" ")
    
    fvs.geometry('400x680')
    fvs.minsize(height=680,width=400)
    fvs.maxsize(height=680,width=400)
    frame=LabelFrame(fvs,text="Friend VS Friend...",font=("showcard gothic",20),fg='red',labelanchor="n",relief='solid',bg='green')
    Label(frame,text="",bg='green').pack()
    f1=Label(frame,text="Player1 Name:",bg='orange',borderwidth=2,relief='solid',font=("jokerman",8)).pack()
    p1inf=Entry(frame,textvariable=fr1,borderwidth=2,relief='solid').pack()
    Label(frame,text="",bg='green').pack()
    f2=Label(frame,text="Player2 Name: ",bg='orange',borderwidth=2,relief='solid',font=("jokerman",8)).pack()
    p2inf=Entry(frame,textvariable=fr2,borderwidth=2,relief='solid').pack()
    Label(frame,text="",bg='green').pack()
    Label(frame,text="",bg='green').pack()
    Label(frame,text="Player 1 Choice:",bg='orange',borderwidth=2,relief='solid',font=("jokerman",8)).pack(side=TOP)
    p1ch=Entry(frame,textvariable=pc1,borderwidth=2,relief='solid')
    p1ch.pack()
    hd1=Button(frame,text="Hide",command=h1,bg='orange',activebackground="grey",bd='5',height=1,width=10,font=("jokerman")).pack()
    Label(frame,text="",bg='green').pack()
    Label(frame,text="Player 2 Choice:",bg='orange',borderwidth=2,relief='solid',font=("jokerman",8)).pack(side=TOP)
    p2ch=Entry(frame,textvariable=pc2,borderwidth=2,relief='solid')
    p2ch.pack()
    hd2=Button(frame,text="Hide",command=h2,bg='orange',activebackground="grey",bd='5',height=1,width=10,font=("jokerman")).pack()
    
    Label(frame,text="",bg='green').pack()
    ch1=Label(frame,text="",font=("times new roman",20),bg='green')
    ch1.pack()
    Label(frame,text="Results After Match...",font=("times new roman",20),bg='green').pack()

    bn2=Button(frame,text="Again",command=rset,activebackground="grey",bd='5',height=1,width=15,state='disable',bg='orange',font=("jokerman"))
    bn2.pack()
    
    bn1=Button(frame,text="START",command=star,activebackground="grey",bd='5',height=1,width=15,bg='orange',font=("jokerman"))
    bn1.pack()
    
    bn=Button(frame,text="Quit",activebackground="grey",command=fvs.destroy,bd='5',height=1,width=15,bg='orange',font=("jokerman")).pack()
    
    frame.pack(expand=True,fill=BOTH,padx=15,pady=15)
    fvs.mainloop()
    

#Main Window and "main" Window :)...
lab=LabelFrame(main,text="Welcome to our Stone Paper Scissor Game...",font=("showcard gothic",20),bg='green',labelanchor="n",relief='solid')
space=Label(lab,text="",bg='green').pack(side=TOP,padx=100)
space=Label(lab,text="",bg='green').pack(side=TOP,padx=100)
ntr=Label(lab,text="Name: ",bg='orange',borderwidth=2,relief='solid',font=("jokerman")).pack()
info=Entry(lab,textvariable=nmcp,borderwidth=2,relief='solid').pack()
space=Label(lab,text=" ",bg='green').pack(side=TOP,padx=100)
btn=Button(lab,text="Play",activebackground="grey",bd='5',command=gm,height=1,width=15,bg='orange',font=("jokerman")).pack()
space=Label(lab,text=" ",bg='green').pack(side=TOP,padx=100)
btn4=Button(lab,text="VS Friend",activebackground="grey",bd='5',command=vs,height=1,width=15,bg='orange',font=("jokerman")).pack()
space=Label(lab,text=" ",bg='green').pack(side=TOP,padx=100)
btn2=Button(lab,text="Score",activebackground="grey",bd='5',command=score,height=1,width=15,bg='orange',font=("jokerman")).pack()
space=Label(lab,text=" ",bg='green').pack(side=TOP,padx=100)
btn3=Button(lab,text="Quit",activebackground="grey",command=main.destroy,bd='5',height=1,width=15,bg='orange',font=("jokerman")).pack()
space=Label(lab,text="\n",bg='green').pack(side=TOP,padx=100)
lab.pack(expand=True,fill=BOTH,padx=15,pady=15)
main.mainloop()
