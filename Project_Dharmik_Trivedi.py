# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 12:19:34 2021

@author: ADMIN
"""
# IMPORTING NEEDED LIBRARIES
from tkinter import*
import random
import time
import datetime
from tkinter import Image    
from tkinter import Tk,StringVar,ttk

root =Tk()
root.title("\t\t Famous Restaurant")


# WE WILL BE HAVING 7 FRAMES : TOPS, BOTTOMMAINFRAME, F1, F2, F2TOP, F2BOTTOM, F3

#1
tops = Frame(root,width=1800,height=100,bd=12,relief="raise")
tops.pack(side=TOP)
lblTitle = Label(tops,font=('arial',35,'bold'),text="\tFamous Restaurant\t")
lblTitle.grid(row=0,column=0)

#2
bottomMainFrame = Frame(root,width=1600,height=650,bd=12,relief="raise")
bottomMainFrame.pack(side=BOTTOM)

#3
f1 = Frame(bottomMainFrame,width=200,height=650,bd=12,relief="raise")
f1.pack(side=LEFT)

#4
f2 = Frame(bottomMainFrame,width=450,height=650,bd=12,relief="raise")
f2.pack(side=LEFT)

#5
f2TOP = Frame(f2,width=450,height=350,bd=4,relief="raise")
f2TOP.pack(side=TOP)

#6
f2BOTTOM = Frame(f2,width=450,height=300,bd=4,relief="raise")
f2BOTTOM.pack(side=BOTTOM)

#7
f3 = Frame(bottomMainFrame,width=500,height=350,bd=12,relief="raise")
f3.pack(side=RIGHT)



# DEFINING VARIABLES
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()
var10 = IntVar()
var11 = IntVar()
var12 = IntVar()
var13 = IntVar()
var14 = IntVar()
var15 = IntVar()
var16 = IntVar()
var17 = IntVar()
var18 = IntVar()
var19 = IntVar()
var20 = IntVar()
var21 = IntVar()
var22 = IntVar()
var23 = IntVar()

# ASSIGNING VALUE = 0 TO EACH VARIABLE
var1.set(0)
var2.set(0)
var3.set(0)
var4.set(0)
var5.set(0)
var6.set(0)
var7.set(0)
var8.set(0)
var9.set(0)
var10.set(0)
var11.set(0)
var12.set(0)
var13.set(0)
var14.set(0)
var15.set(0)
var16.set(0)
var17.set(0)
var18.set(0)
var19.set(0)
var20.set(0)
var21.set(0)
var22.set(0)
var23.set(0)

# DEFINING FOOD ITEM AS A STRING VARIABLE
varFries = StringVar()
varSalad = StringVar()
varHamburger = StringVar()
varOnionRings = StringVar()
varChickenSalad = StringVar()
varFishSandwich = StringVar()
varCheeseSandwich = StringVar()
varChickenSandwich = StringVar()

varHashBrown = StringVar()
varTostedBagel = StringVar()
varPanCakesSyrup = StringVar()
varPinappleStick = StringVar()
varChocolateMuffin = StringVar()

varTea = StringVar()
varCola = StringVar()
varCoffee = StringVar()
varOrange = StringVar()
varWaterBottle = StringVar()

varVAT = StringVar()
varTax = StringVar()
varChange = StringVar()
varSubTotal = StringVar()
varTotal = StringVar()

varVanillaCone = StringVar()
varVanillaShake = StringVar()
varStrawberryShake = StringVar()


# ASSIGNING THE INITIAL VALUES AS 0 FOR EACH ITEAMS
varFries.set("0")
varSalad.set("0")
varHamburger.set("0")
varOnionRings.set("0")
varFishSandwich.set("0")
varCheeseSandwich.set("0")
varChickenSandwich.set("0")
varChickenSalad.set("0")

varHashBrown.set("0")
varTostedBagel.set("0")
varPanCakesSyrup.set("0") 
varPinappleStick.set("0") 
varChocolateMuffin.set("0") 

varTea.set("0")
varCola.set("0")
varCoffee.set("0")
varOrange.set("0")
varWaterBottle.set("0")

varVAT.set("")
varTax.set("0")
varChange.set("0")
varSubTotal.set("0")
varTotal.set("0")

varVanillaCone.set("0")
varVanillaShake.set("0")
varStrawberryShake.set("0")

# DIFINING EXIT BUTTON TO QUIT THE PROGRAM
def iExit():
    qExit = messagebox.askyesno("Fast Food","Do you want to quit?")
    if qExit > 0:
        root.destroy()
        

# DIFINING RESET BUTTON TO REASSIGN THE ORDERING
def reset():
    
    varFries.set("0")
    varSalad.set("0")
    varHamburger.set("0")
    varOnionRings.set("0")
    varFishSandwich.set("0")
    varCheeseSandwich.set("0")
    varChickenSandwich.set("0")
    varChickenSalad.set("0")

    varHashBrown.set("0")
    varTostedBagel.set("0")
    varPanCakesSyrup.set("0") 
    varPinappleStick.set("0") 
    varChocolateMuffin.set("0") 

    varTea.set("0")
    varCola.set("0")
    varCoffee.set("0")
    varOrange.set("0")
    varWaterBottle.set("0")

    varVAT.set("")
    varTax.set("0")
    varChange.set("0")
    varSubTotal.set("0")
    varTotal.set("0")

    varVanillaCone.set("0")
    varVanillaShake.set("0")
    varStrawberryShake.set("0")

    txtFries.configure(state=DISABLED)
    txtSalad.configure(state=DISABLED)
    txtHamburger.configure(state=DISABLED)
    txtOnionRings.configure(state=DISABLED)
    txtChickenSalad.configure(state=DISABLED)
    txtFishSandwich.configure(state=DISABLED)
    txtCheeseSandwich.configure(state=DISABLED)
    txtChickenSandwich.configure(state=DISABLED)
    
    txtHashBrown.configure(state=DISABLED)
    txtTostedBagel.configure(state=DISABLED)
    txtPanCakesSyrup.configure(state=DISABLED)
    txtPinappleStick.configure(state=DISABLED)
    txtChocolateMuffin.configure(state=DISABLED)
   
    txtTea.configure(state=DISABLED)
    txtCola.configure(state=DISABLED)
    txtCoffee.configure(state=DISABLED)
    txtOrange.configure(state=DISABLED)
    txtWaterBottle.configure(state=DISABLED)
    
    txtVanillaCone.configure(state=DISABLED)
    txtVanillaShake.configure(state=DISABLED)
    txtStrawberryShake.configure(state=DISABLED)
    
    txtPayment.configure(state=DISABLED)
    txtChange.configure(state=DISABLED)
    txtTax.configure(state=DISABLED)
    txtSubTotal.configure(state=DISABLED)
    txtTotal.configure(state=DISABLED)



# NOW, WE WILL DEFINE THE FUNCTION FOR EACH ITEMS TO ENABLE AND DISABLE THEIR SELECTION
def chkFries():
    if var1.get() == 1:
        txtFries.configure(state=NORMAL)
        varFries.set("")
    elif (var1.get()==0):
        txtFries.configure(state=DISABLED)
        varFries.set("0")

def chkSalad():
    if var2.get() == 1:
        txtSalad.configure(state=NORMAL)
        varSalad.set("")
    elif (var2.get()==0):
        txtSalad.configure(state=DISABLED)
        varSalad.set("0")

def txtHamburger():
    if var3.get() == 1:
        txtHamburger.configure(state=NORMAL)
        varHamburger.set("")
    elif (var3.get()==0):
        txtHamburger.configure(state=DISABLED)
        varHamburger.set("0")

def txtOnionRings():
    if var4.get() == 1:
        txtOnionRings.configure(state=NORMAL)
        varOnionRings.set("")
    elif (var4.get()==0):
        txtOnionRings.configure(state=DISABLED)
        varOnionRings.set("0")
        
def txtChickenSalad():
    if var5.get() == 1:
        txtChickenSalad.configure(state=NORMAL)
        varChickenSalad.set("")
    elif (var5.get()==0):
        txtChickenSalad.configure(state=DISABLED)
        varChickenSalad.set("0")
        
def txtFishSandwich():
    if var6.get() == 1:
        txtFishSandwich.configure(state=NORMAL)
        varFishSandwich.set("")
    elif (var6.get()==0):
        txtFishSandwich.configure(state=DISABLED)
        varFishSandwich.set("0")

def txtCheeseSandwich():
    if var7.get() == 1:
        txtCheeseSandwich.configure(state=NORMAL)
        varCheeseSandwich.set("")
    elif (var7.get()==0):
        txtCheeseSandwich.configure(state=DISABLED)
        varCheeseSandwich.set("0")

def txtChickenSandwich():
    if var8.get() == 1:
        txtChickenSandwich.configure(state=NORMAL)
        varChickenSandwich.set("")
    elif (var8.get()==0):
        txtChickenSandwich.configure(state=DISABLED)
        varChickenSandwich.set("0")
        
        

def txtTostedBagel():
    if var10.get() == 1:
        txtTostedBagel.configure(state=NORMAL)
        varTostedBagel.set("")
    elif (var10.get()==0):
        txtTostedBagel.configure(state=DISABLED)
        varTostedBagel.set("0")

def txtPanCakesSyrup():
    if var11.get() == 1:
        txtPanCakesSyrup.configure(state=NORMAL)
        varPanCakesSyrup.set("")
    elif (var11.get()==0):
        txtPanCakesSyrup.configure(state=DISABLED)
        varPanCakesSyrup.set("0")

def txtPinappleStick():
    if var12.get() == 1:
        txtPinappleStick.configure(state=NORMAL)
        varPinappleStick.set("")
    elif (var12.get()==0):
        txtPinappleStick.configure(state=DISABLED)
        varPinappleStick.set("0")

def txtChocolateMuffin():
    if var13.get() == 1:
        txtChocolateMuffin.configure(state=NORMAL)
        varChocolateMuffin.set("")
    elif (var13.get()==0):
        txtChocolateMuffin.configure(state=DISABLED)
        varChocolateMuffin.set("0")


def txtVanillaCone():
    if var19.get() == 1:
        txtVanillaCone.configure(state=NORMAL)
        varVanillaCone.set("")
    elif (var19.get()==0):
        txtVanillaCone.configure(state=DISABLED)
        varVanillaCone.set("0")

def txtVanillaShake():
    if var20.get() == 1:
        txtVanillaShake.configure(state=NORMAL)
        varVanillaShake.set("")
    elif (var20.get()==0):
        txtVanillaShake.configure(state=DISABLED)
        varVanillaShake.set("0")
        
def txtStrawberryShake():
    if var21.get() == 1:
        txtStrawberryShake.configure(state=NORMAL)
        varStrawberryShake.set("")
    elif (var21.get()==0):
        txtStrawberryShake.configure(state=DISABLED)
        varStrawberryShake.set("0")
        
# DEFINING THE TOTAL COST OF ITEMS WITH THEIR QUANTITES 
def costOfMeal():
    meal1 = float(varFries.get())
    meal2 = float(varSalad.get())
    meal3 = float(varHamburger.get())
    meal4 = float(varOnionRings.get())
    meal5 = float(varFishSandwich.get())
    meal6 = float(varCheeseSandwich.get())
    meal7 = float(varChickenSandwich.get())
    meal8 = float(varChickenSalad.get())
    
    meal9 = float(varHashBrown.get())
    meal10 = float(varTostedBagel.get())
    meal11 = float(varPanCakesSyrup.get())
    meal12 = float(varPinappleStick.get())
    meal13 = float(varChocolateMuffin.get())
    
    meal14 = float(varTea.get())
    meal15 = float(varCola.get())
    meal16 = float(varCoffee.get())
    meal17 = float(varOrange.get())
    meal18 = float(varWaterBottle.get())
    
    
    meal19 = float(varVanillaCone.get())
    meal20 = float(varVanillaShake.get())
    meal21 = float(varStrawberryShake.get())
    
 
    iTotal1 = ((meal1*1.20) +(meal2*1.30) + (meal3*1.40) + (meal4*1.50))
    
    iTotal2 = ((meal5*1.60) +(meal6*1.70) + (meal7*1.80) + (meal8*1.90))

    iTotal3 = ((meal9*1.40) +(meal10*1.50) + (meal11*1.40) + (meal12*1.60))

    iTotal4 = ((meal13*1.40) +(meal14*1.50) + (meal15*1.70) + (meal16*1.80))
    
    iTotal5 = ((meal17*1.90) +(meal18*1.00) + (meal19*1.50) + (meal20*1.60) + (meal21*1.70))
 
    txtVanillaShake.configure(state=NORMAL)

    iCost = (iTotal1 + iTotal2 + iTotal3 + iTotal4 + iTotal5)
    iTax = (iCost*3.4)/100
    varTax.set(iTax)
    varSubTotal.set(iCost)
    varTotal.set(iCost+iTax)
    
    
# -------------------Frame: Fast Food Meal and Vegitarian------------------------------------------------------


lblMeal = Label(f1,font=('arial',18,'bold'),text='Fast Food Meal and Vegetarian')
lblMeal.grid(row=0,column=0)

Fries = Checkbutton(f1,text="Fries\t\t\t1.20$",variable=var1,onvalue=1,offvalue=0,font=('arial',14,'bold'),command=chkFries).grid(row=1,column=0,sticky=W)
txtFries = Entry(f1,font=('arial',14,'bold'),textvariable=varFries,width=6,justify='left',state=DISABLED)
txtFries.grid(row=1,column=1)

Salad = Checkbutton(f1,text="Salad\t\t\t1.30$",variable=var2,onvalue=1,offvalue=0,font=('arial',14,'bold'),command=chkSalad).grid(row=2,column=0,sticky=W)
txtSalad = Entry(f1,font=('arial',14,'bold'),textvariable=varSalad,width=6,justify='left',state=DISABLED)
txtSalad.grid(row=2,column=1)

Hamburger = Checkbutton(f1,text="Hamburger\t\t1.40$",variable=var3,onvalue=1,offvalue=0,font=('arial',14,'bold'),command=txtHamburger).grid(row=3,column=0,sticky=W)
txtHamburger = Entry(f1,font=('arial',14,'bold'),textvariable=varHamburger,width=6,justify='left',state=DISABLED)
txtHamburger.grid(row=3,column=1)

OnionRings = Checkbutton(f1,text="Onion Rings\t\t1.50$",variable=var4,onvalue=1,offvalue=0,font=('arial',14,'bold'),command = txtOnionRings).grid(row=4,column=0,sticky=W)
txtOnionRings = Entry(f1,font=('arial',14,'bold'),textvariable=varOnionRings,width=6,justify='left',state=DISABLED)
txtOnionRings.grid(row=4,column=1)

ChickenSalad = Checkbutton(f1,text="Chicken Salad\t\t1.60$",variable=var5,onvalue=1,offvalue=0,font=('arial',14,'bold'),command=txtChickenSalad).grid(row=5,column=0,sticky=W)
txtChickenSalad = Entry(f1,font=('arial',14,'bold'),textvariable=varChickenSalad,width=6,justify='left',state=DISABLED)
txtChickenSalad.grid(row=5,column=1)

FishSandwich = Checkbutton(f1,text="Fish Sandwich\t\t1.70$",variable=var6,onvalue=1,offvalue=0,font=('arial',14,'bold'),command=txtFishSandwich).grid(row=6,column=0,sticky=W)
txtFishSandwich = Entry(f1,font=('arial',14,'bold'),textvariable=varFishSandwich,width=6,justify='left',state=DISABLED)
txtFishSandwich.grid(row=6,column=1)

CheeseSandwich = Checkbutton(f1,text="Cheese Sandwich\t\t1.80$",variable=var7,onvalue=1,offvalue=0,font=('arial',14,'bold'),command=txtCheeseSandwich).grid(row=7,column=0,sticky=W)
txtCheeseSandwich = Entry(f1,font=('arial',14,'bold'),textvariable=varCheeseSandwich,width=6,justify='left',state=DISABLED)
txtCheeseSandwich.grid(row=7,column=1)

ChickenSandwich = Checkbutton(f1,text="Chicken Sandwich\t\t1.90$",variable=var8,onvalue=1,offvalue=0,font=('arial',14,'bold'),command=txtChickenSandwich).grid(row=8,column=0,sticky=W)
txtChickenSandwich = Entry(f1,font=('arial',14,'bold'),textvariable=varChickenSandwich,width=6,justify='left',state=DISABLED)
txtChickenSandwich.grid(row=8,column=1)

lblSpace = Label(f1,text="\n\n\n")
lblSpace.grid(row=9,column=0)




# ----------------------------------------------Frame -2 Desserts----------------------
 
lblMeal = Label(f2TOP,font=('arial',18,'bold'),text="\tDesserts")
lblMeal.grid(row=0,column=0)

TostedBagel = Checkbutton(f2TOP,text="Tosted Bagel\t1.50$",variable=var10,onvalue=1,offvalue=0,font=('arial',14,'bold'),command=txtTostedBagel).grid(row=2,column=0,sticky=W)
txtTostedBagel = Entry(f2TOP,font=('arial',14,'bold'),textvariable=varTostedBagel,width=6,justify='left',state=DISABLED)
txtTostedBagel.grid(row=2,column=1)

PanCakesSyrup = Checkbutton(f2TOP,text="Pancakes Syrup\t1.40$",variable=var11,onvalue=1,offvalue=0,font=('arial',14,'bold'),command=txtPanCakesSyrup).grid(row=3,column=0,sticky=W)
txtPanCakesSyrup = Entry(f2TOP,font=('arial',14,'bold'),textvariable=varPanCakesSyrup,width=6,justify='left',state=DISABLED)
txtPanCakesSyrup.grid(row=3,column=1)

PinappleStick = Checkbutton(f2TOP,text="Pinapple Stick\t1.60$",variable=var12,onvalue=1,offvalue=0,font=('arial',14,'bold'),command=txtPinappleStick).grid(row=4,column=0,sticky=W)
txtPinappleStick = Entry(f2TOP,font=('arial',14,'bold'),textvariable=varPinappleStick,width=6,justify='left',state=DISABLED)
txtPinappleStick.grid(row=4,column=1)


ChocolateMuffin = Checkbutton(f2TOP,text="Chocolate Muffin\t1.40$",variable=var13,onvalue=1,offvalue=0,font=('arial',14,'bold'),command=txtChocolateMuffin).grid(row=5,column=0,sticky=W)
txtChocolateMuffin = Entry(f2TOP,font=('arial',14,'bold'),textvariable=varChocolateMuffin,width=6,justify='left',state=DISABLED)
txtChocolateMuffin.grid(row=5,column=1)




# ----------------------FRAME:3 SHAKES---------------------------------------------------


lblShakes = Label(f3,font=('arial',18,'bold'),text='\tShakes')
lblShakes.grid(row=6,column=0)

VanillaCone = Checkbutton(f3,text="Vanilla Cone\t1.50$",variable=var19,onvalue=1,offvalue=0,font=('arial',14,'bold'),command=txtVanillaCone).grid(row=7,column=0,sticky=W)
txtVanillaCone = Entry(f3,font=('arial',14,'bold'),textvariable=varVanillaCone,width=6,justify='left',state=DISABLED)
txtVanillaCone.grid(row=7,column=1)

VanillaShake = Checkbutton(f3,text="Vanilla Shake\t1.60$",variable=var20,onvalue=1,offvalue=0,font=('arial',14,'bold'),command=txtVanillaShake).grid(row=8,column=0,sticky=W)
txtVanillaShake = Entry(f3,font=('arial',14,'bold'),textvariable=varVanillaShake,width=6,justify='left',state=DISABLED)
txtVanillaShake.grid(row=8,column=1)

StrawberryShake = Checkbutton(f3,text="Strawberry Shake\t1.70$",variable=var21,onvalue=1,offvalue=0,font=('arial',14,'bold'),command=txtStrawberryShake).grid(row=9,column=0,sticky=W)
txtStrawberryShake = Entry(f3,font=('arial',14,'bold'),textvariable=varStrawberryShake,width=6,justify='left',state=DISABLED)
txtStrawberryShake.grid(row=9,column=1)

lblSSpace = Label(f3,text='\n\n\n\n')
lblSSpace.grid(row=10,column=0)


#--------------------------------------------------------Payment frame-------------------------------------
lblPayment = Label(f2BOTTOM,font=('arial',14,'bold'),text='Payment Method',bd=10,anchor='w')
lblPayment.grid(row=0,column=0)

cmbPaymentMethod = ttk.Combobox(f2BOTTOM,textvariable=var22,state='readonly',font=('arial',10,'bold'),width=20)
cmbPaymentMethod['value'] = ('Cash','Master Card','Visa Card','Debit Card')
cmbPaymentMethod.current(0)
cmbPaymentMethod.grid(row=1,column=0)

lblTax = Label(f2BOTTOM,font=('arial',14,'bold'),text='Tax  ',bd=10,anchor='w')
lblTax.grid(row=1,column=1)
txtTax = Entry(f2BOTTOM,font=('arial',14,'bold'),textvariable=varTax,width=6,justify='left',state=DISABLED)
txtTax.grid(row=1,column=2)


lblSubTotal = Label(f2BOTTOM,font=('arial',14,'bold'),text='Sub Total',bd=10,width=8,anchor='w')
lblSubTotal.grid(row=2,column=1)
txtSubTotal = Entry(f2BOTTOM,font=('arial',14,'bold'),textvariable=varSubTotal,width=6,justify='left',state=DISABLED)
txtSubTotal.grid(row=2,column=2)

lblTotal = Label(f2BOTTOM,font=('arial',14,'bold'),text='Total',bd=10,width=6,anchor='w')
lblTotal.grid(row=3,column=1)
txtTotal = Entry(f2BOTTOM,font=('arial',14,'bold'),textvariable=varTotal,width=6,justify='left',state=DISABLED)
txtTotal.grid(row=3,column=2)






# ------------------------------DEFINING ButtonS: 1)TOTAL 2)RESET 3)EXIT--------------------------------------------
btnTotal = Button(f2BOTTOM,padx=16,pady=1,bd=4,fg='black',font=('arial',16,'bold'),width=5,text='Total: ',command=costOfMeal).grid(row=4,column=0)

btnReset = Button(f2BOTTOM,padx=16,pady=1,bd=4,fg='black',font=('arial',16,'bold'),width=5,text='Reset: ',command=reset).grid(row=4,column=1)

btnExit = Button(f2BOTTOM,padx=16,pady=1,bd=4,fg='black',font=('arial',16,'bold'),width=5,text='Exit:',command=iExit).grid(row=4,column=2)

lblSpace = Label(f2BOTTOM,text='\n\n\n\n\n\n')
lblSpace.grid(row=5,column=10)


 


root.mainloop()