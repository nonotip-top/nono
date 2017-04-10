# code renaud


from tkinter import *
import tkinter.font as tkfont
from math import *


def quitter():
    fen.destroy()
    
    
    
def redessinner_queue(event):
    global q,a
    canevas.delete(q)
    a = ((angle.get())*pi)/180
    xq = x0-14*cos(a)
    yq = y0+14*sin(a)
    x_q = x0-350*cos(a)
    y_q = y0+350*sin(a)
    q = canevas.create_line(xq, yq, x_q, y_q, fill='red', width=5)


def placer_blanche():
    global x0,y0,blanche
    x0 = 192
    y0 = 122
    blanche = canevas.create_oval(x0-12,y0-12,x0+12,y0+12, fill='white')


def placer_rouge():
    global x1,y1,rouge
    x1 = 142
    y1 = 162
    rouge = canevas.create_oval(x1-12,y1-12,x1+12,y1+12, fill='red')

    
def collision_boule() :
    if (x1-24)<=x0<=(x1+24) and (y1-24)<=y0<=(y1+24) :
        opp = abs(y0-y1)
        adj = abs(x0-x1)
        if x0<=x1 and y0<=y1:
            angl.set(degrees(atan(opp/adj)))
        if x0<=x1 and y0>y1:
            angl.set(-degrees(atan(opp/adj)))
        if x0>x1 and y0>y1:
            angl.set(-180-degrees(atan(opp/adj)))
        if x0>x1 and y0<=y1:
            angl.set(180-degrees(atan(opp/adj)))
        angle.set((angl.get()+180)%360)
        
    
    
    
    
    
    
    
    
    
        
def collision_murale() :
    a = angle.get()
    if a == 360 :
        angle.set(0)
    
    if x0>=951 or x0<=38 : #collision horizontale
        if a == 0:
            angle.set(180)
        else :
            angle.set((180-a)%360)
        
    if y0<=38 or y0>=482 : #collision verticale
            angle.set(-a%360)
    a = angl.get()
    if a == 360 :
        angl.set(0)
    
    if x1>=951 or x1<=38 : #collision horizontale
        if a == 0:
            angl.set(180)
        else :
            angl.set((180-a)%360)
        
    if y1<=38 or y1>=482 : #collision verticale
            angl.set(-a%360)
        

















def tirer():
    p = puissance_tir.get()
    a = ((angle.get())*pi)/180
    b = ((angl.get())*pi)/180
    global blanche,x0,y0,x1,y1,rouge
    canevas.delete(blanche)
    canevas.delete(rouge)
    x0 = x0 + 1*cos(a)  #Nouvelle pos de la bille en x
    y0 = y0 - 1*sin(a)  #Nouvelle pos de la bille en y
    collision_murale()
    collision_boule()
    blanche = canevas.create_oval(x0-12,y0-12,x0+12,y0+12, fill='white')
    rouge = canevas.create_oval(x1-12,y1-12,x1+12,y1+12, fill='red')
    if p>0:
        canevas.after(9 , tirer)
        puissance_tir.set(p-1)
    faire_tir.bind('<Button-1>', redessinner_queue)


def verif_tir():
    return 1
    




def tir():
    if (verif_tir()==1):
        p = puissance_tir.get()
        puissance_tir.set(p)
        tirer()





fen = Tk()
fen.geometry("%dx%d%+d%+d" % (1260,940,1,1))
fen['bg']="#92afac"
fen.title("Jeu du Billard")

angle = IntVar()
angl = IntVar()

police1 = tkfont.Font(family='Fixedsys', size=50, underline=1)  #définition d'une police de caractères
police2 = tkfont.Font(family='Fixedsys', size=10, slant='italic')


# création d'un widget 'Canvas' contenant une image bitmap :
canevas = Canvas(fen, width =990, height =522, bg ='#92afac', borderwidth=0)
photo = PhotoImage(file="C:/Users/TestAdmin/Downloads/moquette_f.png")                                                                         
canevas.create_image(495,261, image=photo) 
canevas.grid(row=2, column=0, columnspan=4, pady=0, padx=130, sticky='sw')
canevas.bind('<Button-1>', redessinner_queue)

billes_j1 = StringVar()
billes_j2 = StringVar()

panel_j1 = Label(fen, width=28, height=5, textvariable=billes_j1)
panel_j1.grid(row=0, column=0, sticky="nw")

panel_j2 = Label(fen, width=28, height=5, textvariable=billes_j2)
panel_j2.grid(row=0, column=2, sticky='ne',padx=8)

titre = Label(fen, text='Billard', font=police1, bg="#92afac")
titre.grid(row=0, column=1, padx=280, pady=0)

nom_j1 = Label(fen, bg='#92afac', text="Joueur 1", font=police2)
nom_j1.grid(row=1, column=0,) 

nom_j2 = Label(fen, bg='#92afac', text="Joueur 2", font=police2)
nom_j2.grid(row=1, column=2,) 

quitter = Button(fen, text="Quitter la partie ?", command=quitter)
quitter.grid(row=3, rowspan=5,column=2)

position = Scale(fen, orient='horizontal', from_=0, to=360, tickinterval=30, length=560, label='Angle de tir', variable=angle, resolution=1)
position.grid(row=3, column=0, columnspan=2)
position.bind('<ButtonRelease-1>', redessinner_queue)

    

placer_blanche()
q = canevas.create_line(x0-12,y0,x0-350,y0, fill='red', width=7)

placer_rouge()





puissance_tir = IntVar()
puissance_tir.set(100465410)
fenetre_tir = Entry(fen, textvariable=puissance_tir)
fenetre_tir.grid()

faire_tir = Button(fen, text=" Tirer la blanche ! ", command=tir)
faire_tir.grid(row=1, column=1)











fen.mainloop()