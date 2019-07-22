




def Ref():
    x=random.randint(10908,500876)
    randomRef=str(x)
    rand.set(randomRef)

    if (Fries.get()==""):
        CoFries=0
    else:
        CoFries=float(Fries.get())


    
    if (Noodles.get()==""):
        CoNoodles=0
    else:
        CoNoodles=float(Noodles.get())



    if (Soup.get()==""):
        CoSoup=0
    else:
        CoSoup=float(Soup.get())



    if (Burger.get()==""):
        CoBurger=0
    else:
        CoBurger=float(Burger.get())

        
    if (Sandwich.get()==""):
        CoSandwich=0
    else:
        CoSandwich=float(Sandwich.get())

     
    if (Drinks.get()==""):
        CoD=0
    else:
        CoD=float(Drinks.get())

                   
    CostofFries =CoFries * 140
    CostofDrinks=CoD * 65
    CostofNoodles = CoNoodles* 90
    CostofSoup = CoSoup * 140
    CostBurger = CoBurger* 260
    CostSandwich=CoSandwich * 300

    CostofMeal= "Rs", str('%.2f' % (CostofFries+CostofDrinks+CostofNoodles+CostofSoup+CostBurger+CostSandwich))

    PayTax=((CostofFries+CostofDrinks+CostofNoodles+CostofSoup+CostBurger+CostSandwich) * 0.2)

    TotalCost=(CostofFries+CostofDrinks+CostofNoodles+CostofSoup+CostBurger+CostSandwich)
 
    Ser_Charge= ((CostofFries+CostofDrinks+CostofNoodles+CostofSoup+CostBurger+CostSandwich)/99)

    Service = "Rs", str ('%.2f' % Ser_Charge)

    OverAllCost ="Rs", str ('%.2f' % (PayTax+TotalCost+Ser_Charge))

    PaidTax= "Rs", str ('%.2f' % PayTax)

    Service_Charge.set(Service)
    Cost.set(CostofMeal)
    Tax.set(PaidTax)
    SubTotal.set(CostofMeal)
    Total.set(OverAllCost)
    
def qExit():
    root.destroy()

def Reset():
    rand.set("") 
    Fries.set("")
    Noodles.set("")
    Soup.set("")
    SubTotal.set("")
    Total.set("")
    Service_Charge.set("")
    Drinks.set("")
    Tax.set("")
    Cost.set("")
    Burger.set("")
    Sandwich.set("")
"""    
#====================================Restaraunt Info 1===========================================================
rand = StringVar()
Fries=StringVar()
Noodles=StringVar()
Soup=StringVar()
SubTotal=StringVar()
Total=StringVar()
Service_Charge=StringVar()
Drinks=StringVar()
Tax=StringVar()
Cost=StringVar()
Burger=StringVar()
Sandwich=StringVar()





root.mainloop()
"""

