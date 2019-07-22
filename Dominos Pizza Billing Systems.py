#Dominos Billing System

global a
a=True
#------------------------------------------------------------------------------
def pizza_menu():
    global l1
    l1=[[1,'Veg Extravaganza       ',175,215,245],
       [2,'Pepper Barbecue Chicken',245,265,295],
       [3,'Margherita             ',175,190,230],
       [4,'Pepper Paneer          ',270,280,290],
       [5,'Mexican Green Wave     ',185,235,280],
       [6,'Veggie Paradise        ',165,205,245]]
    print("******************************************")
    print("S.no              Pizza                  *")
    print("******************************************")
    
    for i in l1:
        print(i[0],"        ",i[1],"      *")
        print("       Small       Medium       Large    *")
        print("       ₹",i[2],"      ₹",i[3],"       ₹",i[4],"   *")
        
    print("******************************************")
#------------------------------------------------------------------------------
def pizza_size():
    print("------------------------------------------")
    print("Select size:")
    print("------------------------------------------")
    print("1:Small          2:Medium          3:Large")
    print("------------------------------------------")
#------------------------------------------------------------------------------    
def drinks_menu():
    global l2
    l2=[[1,'Pepsi         ',60],
       [2,'Bailley Water ',20],
       [3,'Mountain Dew  ',42],
       [4,'Mirinda       ',60],
       [5,'Lipton Ice Tea',37]]
    print("******************************************")
    print("S.no      Drinks               Price     *")
    print("******************************************")
    
    for i in l2:
        print(i[0],"       ",i[1],"      ₹",i[2],"     *")
    print("******************************************")
#------------------------------------------------------------------------------
def sides_menu():
    global l3
    l3=[[1,'Garlic Bread Sticks ',105],
       [2,'Stuffed Garlic Bread',139],
       [3,'Taco Mexicana       ',135],
       [4,'Pasta Italiano White',145],
       [5,'Burger Pizza        ',110],
       [6,'Zingy Parcel        ',125]]
    print("******************************************")
    print("S.no   Sides                      Price  *")
    print("******************************************")
    
    for i in l3:
        print(i[0],"    ",i[1],"      ₹",i[2]," *")
   
    print("******************************************")
#------------------------------------------------------------------------------
def deserts_menu():
    global l4
    l4=[[1,'Choco Lava Cake         ',185],
       [2,'Butterscotch Mousse Cake',125],
       [3,'Blackberry Cobler       ',195],
       [4,'New York Cheesecake     ',145],
       [5,'Key Lime Pie            ',160],
       [6,'Chocolate Cake          ',175]]
    print("******************************************")
    print("S.no   Deserts                    Price  *")
    print("******************************************")   
    for i in l4:
        print(i[0],"    ",i[1],"  ₹",i[2]," *")  
    print("******************************************")
#------------------------------------------------------------------------------   
global pizzalist
pizzalist=[] 
global drinkslist
drinkslist=[]
global sideslist
sideslist=[]
global desertslist
desertslist=[]
global pricelist
pricelist=[]
global pricelist1
pricelist1=[]
global pricelist2
pricelist2=[]
global pricelist3
pricelist3=[]
global pizzatotal
global drinkstotal
global sidestotal
global desertstotal
global totalprice
#------------------------------------------------------------------------------ 
def choosepizza():
    print("Select the pizza: ",end='') 
    d=input()
    if d=='1':       
        pizza_size()
        s=input()
        if s=='1':
            pizzalist.extend([l1[0][1]])
            pricelist.extend([l1[0][2]])  
        elif s=='2':
            pizzalist.extend([l1[0][1]])
            pricelist.extend([l1[0][2]])    
        elif s=='3':
            pizzalist.extend([l1[0][1]])
            pricelist.extend([l1[0][2]])
        
    elif d=='2':
        pizza_size()
        s=input()
        if s=='1':
            pizzalist.extend([l1[1][1]])
            pricelist.extend([l1[1][2]])
        elif s=='2':
            pizzalist.extend([l1[1][1]])
            pricelist.extend([l1[1][2]])
        elif s=='3':
            pizzalist.extend([l1[1][1]])
            pricelist.extend([l1[1][2]])
        
    elif d=='3':
        pizza_size()
        s=input()
        if s=='1':
            pizzalist.extend([l1[2][1]])
            pricelist.extend([l1[2][2]])
        elif s=='2':
            pizzalist.extend([l1[2][1]])
            pricelist.extend([l1[2][2]])
        elif s=='3':
            pizzalist.extend([l1[2][1]])
            pricelist.extend([l1[2][2]])
        
    elif d=='4':
        pizza_size()
        s=input()
        if s=='1':
            pizzalist.extend([l1[3][1]])
            pricelist.extend([l1[3][2]])
        elif s=='2':
            pizzalist.extend([l1[3][1]])
            pricelist.extend([l1[3][2]])
        elif s=='3':
            pizzalist.extend([l1[3][1]])
            pricelist.extend([l1[3][2]])
        
    elif d=='5':
        pizza_size()
        s=input()
        if s=='1':
            pizzalist.extend([l1[4][1]])
            pricelist.extend([l1[4][2]])
        elif s=='2':
            pizzalist.extend([l1[4][1]])
            pricelist.extend([l1[4][2]])
        elif s=='3':
            pizzalist.extend([l1[4][1]])
            pricelist.extend([l1[4][2]])
        
    elif d=='6':
        pizza_size()
        s=input()
        if s=='1':
            pizzalist.extend([l1[5][1]])
            pricelist.extend([l1[5][2]])
        elif s=='2':
            pizzalist.extend([l1[5][1]])
            pricelist.extend([l1[5][2]])
        elif s=='3':
            pizzalist.extend([l1[5][1]])
            pricelist.extend([l1[5][2]])
        
    else:
        print("------------------------------------------")
        print("Sorry,invalid Option! Select correct one.")
        print("------------------------------------------")
        print()
        pizza_menu()
        choosepizza()
    pizzacontrol()
#------------------------------------------------------------------------------
def pizzacontrol():
    print("------------------------------------------")
    print(">>Press 1 to go back to pizza menu")
    print(">>Press 2 to go back to main menu")
    print(">>Press 3 to check the bill")
    print(">>Press 4 to edit bill")
    print(">>Press 5 to exit")
    print("------------------------------------------")
    e=input()
    if e=='1':
        pizza_menu()
        choosepizza()
    elif e=='2':
        choose()
    elif e=='3':
        bill()
    elif e=='5':
        print()
        print("------------------------------------------")
        print("Thank You For Visiting Us")
        print("------------------------------------------")
#------------------------------------------------------------------------------    
def choosedrinks():
    print("Select the Drink")   
    d=input()
    if d=='1':
        drinkslist.extend([l2[0][1]])
        pricelist1.extend([l2[0][2]])
    elif d=='2':
        drinkslist.extend([l2[1][1]])
        pricelist1.extend([l2[1][2]])
    elif d=='3':
        drinkslist.extend([l2[2][1]])
        pricelist1.extend([l2[1][2]])
    elif d=='4':
        drinkslist.extend([l2[3][1]])
        pricelist1.extend([l2[1][2]])
    elif d=='5':
        drinkslist.extend([l2[4][1]])
        pricelist1.extend([l2[1][2]])
    else:
        print("------------------------------------------")
        print("Sorry,invalid Option! Select correct one.")
        print("------------------------------------------")
        print()
        drinks_menu()
        choosedrinks()
    drinkscontrol()
#------------------------------------------------------------------------------       
def drinkscontrol():
    print("------------------------------------------")
    print(">>Press 1 to go back to drinks menu")
    print(">>Press 2 to go back to main menu")
    print(">>Press 3 to check the bill")
    print(">>Press 4 to edit bill")
    print(">>Press 5 to exit")
    print("------------------------------------------")
    e=input()
    if e=='1':
        drinks_menu()
        choosedrinks()
    elif e=='2':
        choose()
    elif e=='3':
        bill()
    elif e=='5':
        print()
        print("------------------------------------------")
        print("Thank You For Visiting Us")
        print("------------------------------------------")
#------------------------------------------------------------------------------
def choosesides():
    print("Select the sides:")
    
    d=input()
    if d=='1':
        sideslist.extend([l3[0][1]])
        pricelist2.extend([l3[0][2]])
    elif d=='2':
        sideslist.extend([l3[1][1]])
        pricelist2.extend([l3[1][2]])
    elif d=='3':
        sideslist.extend([l3[2][1]])
        pricelist2.extend([l3[2][2]])
    elif d=='4':
        sideslist.extend([l3[3][1]])
        pricelist2.extend([l3[3][2]])
    elif d=='5':
        sideslist.extend([l3[4][1]])
        pricelist2.extend([l3[4][2]])
    elif d=='6':
        sideslist.extend([l3[5][1]])
        pricelist2.extend([l3[5][2]])
    else:
        print("------------------------------------------")
        print("Sorry,invalid Option! Select correct one.")
        print("------------------------------------------")
        print()
        sides_menu()
        choosesides()
    sidescontrol()
#------------------------------------------------------------------------------       
def sidescontrol():
    print("------------------------------------------")
    print(">>Press 1 to go back to sides menu")
    print(">>Press 2 to go back to main menu")
    print(">>Press 3 to check the bill")
    print(">>Press 4 to edit bill")
    print(">>Press 5 to exit")
    print("------------------------------------------")
    e=input()
    if e=='1':
        sides_menu()
        choosesides()
        
    elif e=='2':
        choose()
    elif e=='3':
        bill()
    elif e=='5':
        print()
        print("------------------------------------------")
        print("Thank You For Visiting Us")
        print("------------------------------------------")
#------------------------------------------------------------------------------
def choosedeserts():
    print("Choose the deserts")
    
    d=input()
    if d=='1':
        desertslist.extend([l4[0][1]])
        pricelist3.extend([l4[0][2]])
    elif d=='2':
        desertslist.extend([l4[1][1]])
        pricelist3.extend([l4[1][2]])
    elif d=='3':
        desertslist.extend([l4[2][1]])
        pricelist3.extend([l4[2][2]])
    elif d=='4':
        desertslist.extend([l4[3][1]])
        pricelist3.extend([l4[3][2]])
    elif d=='5':
        desertslist.extend([l4[4][1]])
        pricelist3.extend([l4[4][2]])
    elif d=='6':
        desertslist.extend([l4[5][1]])
        pricelist3.extend([l4[5][2]])
    else:
        print("------------------------------------------")
        print("Sorry,invalid Option! Select correct one.")
        print("------------------------------------------")
        print()
        deserts_menu()
        choosedeserts()
    desertscontrol()
#------------------------------------------------------------------------------       
def desertscontrol():
    print("------------------------------------------")
    print(">>Press 1 to go back to deserts menu")
    print(">>Press 2 to go back to main menu")
    print(">>Press 3 to check the bill")
    print(">>Press 4 to edit bill")
    print(">>Press 5 to exit")
    print("------------------------------------------")
    e=input()
    if e=='1':
        deserts_menu()
        choosedeserts()
    elif e=='2':
        choose()
    elif e=='3':
        bill()
    elif e=='5':
        print()
        print("Thank You For Visiting Us")
    else:
        print("Invalid Option.Choose correct one.")
#------------------------------------------------------------------------------
#def editbill       
#------------------------------------------------------------------------------
def choose(): 
    print("------------------------------------------")       
    print("Choose the category")
    print("------------------------------------------")
    first_view=[[1,"Pizza"],[2,"Drinks"],[3,"Sides"],[4,"Deserts"],[5,"Exit"]]
    for i in first_view:
        print(i[0],"  ",i[1])
    print("------------------------------------------")
    c=input()
    if c=='1':
        pizza_menu()
        choosepizza()
    elif c=='2':
        drinks_menu()
        choosedrinks()
    elif c=='3':
        sides_menu()
        choosesides()
    elif c=='4':
        deserts_menu()
        choosedeserts()
    elif c=='5':
        print()
        print("------------------------------------------")
        print("Thank You For Visiting Us!")
        print("------------------------------------------")
    else:
        print("Invalid Option.Select correct option")
        choose()
#------------------------------------------------------------------------------
def bill():
    print("******************************************")
    print("             Bill Amount                 *")
    print("******************************************")
    print("SI No:         Item               Price  *")
    print("******************************************")
    
    for i in range(len(pizzalist)):
        print(i+1,"    ",end='')
        print(pizzalist[i],"     ₹",end='')
        print(pricelist[i]," *")
    for i in range(len(drinkslist)):
        print(len(pizzalist)+i+1,"    ",end='')
        print(drinkslist[i],"               ₹",end='')
        print(pricelist1[i]," *")
    for i in range(len(sideslist)):
        print(len(pizzalist)+len(drinkslist)+i+1,"    ",end='')
        print(sideslist[i],"        ₹",end='')
        print(pricelist2[i]," *")
    for i in range(len(desertslist)):
        print(len(pizzalist)+len(drinkslist)+len(sideslist)+i+1,"    ",end='')
        print(desertslist[i],"    ₹",end='')
        print(pricelist3[i]," *")    
    print("******************************************")
    t=q=r=s=0
    for i in pricelist:
        t=sum(pricelist)
    for i in pricelist1: 
        q=sum(pricelist1)
    for i in pricelist2:
        r=sum(pricelist2)
    for i in pricelist3:
        s=sum(pricelist3)   
    totalprice=t+q+r+s
    print("Total Amount:                      ₹",end='')
    print(totalprice," *",end='')
    print()
    print("******************************************")
#------------------------------------------------------------------------------
while a:
    print("------------------------------------------")
    name=input("Enter the name:")
    if name=='':
        print("Invalid Input.")
        c=input("Do You Wish To Continue.Press y or n ")
        if c!='y':
            a=False
            print()
            print("------------------------------------------")
            print("Thanks For Visiting Us!")
            print("------------------------------------------")
    else:
        a=False
        print("Dominos".center(42,"-"))
        print("Welcome Mr/Mrs.",name,"to Dominos")
        choose()
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------        




    