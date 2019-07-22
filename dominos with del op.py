#Dominos Billing System
#Code For Selecting Different Items From Different Categories And Finally Printing
#The Names Of Selected Items With Price And Total Bill Amount.
global a
a=True
#------------------------------------------------------------------------------
#Creates The Pizza Main Menu
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
#Create Pizza Size Sub Menu
#------------------------------------------------------------------------------
def pizza_size():
    print("------------------------------------------") 
    print("1:Small          2:Medium          3:Large")
    print("------------------------------------------")
    print("Select Size:")
#------------------------------------------------------------------------------
#Create The Drinks Main Menu
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
#Creates The Drinks Main Menu
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
#Creates The Deserts Main Menu
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
#Declaring Some Variable As Global For Later Use In Program
#------------------------------------------------------------------------------
global itemlist
itemlist=[] 
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
#Pizza Code For Entering Name Of Selected Pizza Into A List "pizzalist" 
#Also Adding Corresponging Price Of Selected Pizza To Another List Named "pricelist"  
#------------------------------------------------------------------------------ 
def choosepizza():
    print("Select The Desired Pizza: ",end='') 
    d=input()
    if d=='1':       
        pizza_size()
        s=input()
        if s=='1':
            itemlist.extend([l1[0][1]])
            pricelist.extend([l1[0][2]])  
        elif s=='2':
            itemlist.extend([l1[0][1]])
            pricelist.extend([l1[0][2]])    
        elif s=='3':
            itemlist.extend([l1[0][1]])
            pricelist.extend([l1[0][2]])
        
    elif d=='2':
        pizza_size()
        s=input()
        if s=='1':
            itemlist.extend([l1[1][1]])
            pricelist.extend([l1[1][2]])
        elif s=='2':
            itemlist.extend([l1[1][1]])
            pricelist.extend([l1[1][2]])
        elif s=='3':
            itemlist.extend([l1[1][1]])
            pricelist.extend([l1[1][2]])
        
    elif d=='3':
        pizza_size()
        s=input()
        if s=='1':
            itemlist.extend([l1[2][1]])
            pricelist.extend([l1[2][2]])
        elif s=='2':
            itemlist.extend([l1[2][1]])
            pricelist.extend([l1[2][2]])
        elif s=='3':
            itemlist.extend([l1[2][1]])
            pricelist.extend([l1[2][2]])
        
    elif d=='4':
        pizza_size()
        s=input()
        if s=='1':
            itemlist.extend([l1[3][1]])
            pricelist.extend([l1[3][2]])
        elif s=='2':
            itemlist.extend([l1[3][1]])
            pricelist.extend([l1[3][2]])
        elif s=='3':
            itemlist.extend([l1[3][1]])
            pricelist.extend([l1[3][2]])
        
    elif d=='5':
        pizza_size()
        s=input()
        if s=='1':
            itemlist.extend([l1[4][1]])
            pricelist.extend([l1[4][2]])
        elif s=='2':
            itemlist.extend([l1[4][1]])
            pricelist.extend([l1[4][2]])
        elif s=='3':
            itemlist.extend([l1[4][1]])
            pricelist.extend([l1[4][2]])
        
    elif d=='6':
        pizza_size()
        s=input()
        if s=='1':
            itemlist.extend([l1[5][1]])
            pricelist.extend([l1[5][2]])
        elif s=='2':
            itemlist.extend([l1[5][1]])
            pricelist.extend([l1[5][2]])
        elif s=='3':
            itemlist.extend([l1[5][1]])
            pricelist.extend([l1[5][2]])
        
    else:
        print("------------------------------------------")
        print("Sorry,Invalid Option! Select Correct Option.")
        print("------------------------------------------")
        print()
        pizza_menu()
        choosepizza()
    pizzacontrol()
#------------------------------------------------------------------------------
#Pizza Menu Controls
#------------------------------------------------------------------------------ 
def pizzacontrol():
    print("------------------------------------------")
    print(">>Press 1 To Go Back To Pizza Menu")
    print(">>Press 2 To Go Back To Main Menu")
    print(">>Press 3 To Check The Final Bill")
    print(">>Press 4 To Edit Bill")
    print(">>Press 5 To Exit")
    print("------------------------------------------")
    e=input()
    if e=='1':
        pizza_menu()
        choosepizza()
    elif e=='2':
        choose()
    elif e=='3':
        bill()
    elif e=='4':
        print("Which Item Do You Want To Remove.Please Specify The SI.No:")
        
    elif e=='5':
        print()
        print("------------------------------------------")
        print("Thank You For Visiting Us!")
        print("------------------------------------------")
#------------------------------------------------------------------------------
#Drinks Code For Entering Name Of Selected Drinks Into A List "drinkslist" 
#Also Adding Corresponging Price Of Selected Drinks To Another List Named "pricelist1"  
#------------------------------------------------------------------------------ 
def choosedrinks():
    print("Select The Desired Drink: ")   
    d=input()
    if d=='1':
        itemlist.extend([l2[0][1]])
        pricelist.extend([l2[0][2]])
    elif d=='2':
        itemlist.extend([l2[1][1]])
        pricelist.extend([l2[1][2]])
    elif d=='3':
        itemlist.extend([l2[2][1]])
        pricelist.extend([l2[1][2]])
    elif d=='4':
        itemlist.extend([l2[3][1]])
        pricelist.extend([l2[1][2]])
    elif d=='5':
        itemlist.extend([l2[4][1]])
        pricelist.extend([l2[1][2]])
    else:
        print("------------------------------------------")
        print("Sorry,Invalid Option! Select Correct Option.")
        print("------------------------------------------")
        print()
        drinks_menu()
        choosedrinks()
    drinkscontrol()
#------------------------------------------------------------------------------ 
#Drinks Menu Controls
#------------------------------------------------------------------------------      
def drinkscontrol():
    print("------------------------------------------")
    print(">>Press 1 To Go Back To Drinks Menu")
    print(">>Press 2 To Go Back To Main Menu")
    print(">>Press 3 To Check The Bill")
    print(">>Press 4 To Edit Bill")
    print(">>Press 5 To Exit")
    print("------------------------------------------")
    e=input()
    if e=='1':
        drinks_menu()
        choosedrinks()
    elif e=='2':
        choose()
    elif e=='3':
        bill()
    elif e=='4':
        print("Which Item Do You Want To Remove.Please Specify The SI.No:")
        
    elif e=='5':
        print()
        print("------------------------------------------")
        print("Thank You For Visiting Us!")
        print("------------------------------------------")
#------------------------------------------------------------------------------
#Sides Code For Entering Name Of Selected Sides Into A List "sideslist" 
#Also Adding Corresponging Price Of Selected Sides To Another List Named "pricelist2"  
#------------------------------------------------------------------------------ 
def choosesides():
    print("Select The Sides: ")
    
    d=input()
    if d=='1':
        itemlist.extend([l3[0][1]])
        pricelist.extend([l3[0][2]])
    elif d=='2':
        itemlist.extend([l3[1][1]])
        pricelist.extend([l3[1][2]])
    elif d=='3':
        itemlist.extend([l3[2][1]])
        pricelist.extend([l3[2][2]])
    elif d=='4':
        itemlist.extend([l3[3][1]])
        pricelist.extend([l3[3][2]])
    elif d=='5':
        itemlist.extend([l3[4][1]])
        pricelist.extend([l3[4][2]])
    elif d=='6':
        itemlist.extend([l3[5][1]])
        pricelist.extend([l3[5][2]])
    else:
        print("------------------------------------------")
        print("Sorry,Invalid Option! Select Correct Option.")
        print("------------------------------------------")
        print()
        sides_menu()
        choosesides()
    sidescontrol()
#------------------------------------------------------------------------------
#Sides Menu Controls
#------------------------------------------------------------------------------       
def sidescontrol():
    print("------------------------------------------")
    print(">>Press 1 To Go Back To Sides Menu")
    print(">>Press 2 To Go Back To Main Menu")
    print(">>Press 3 To Check The Bill")
    print(">>Press 4 To Edit Bill")
    print(">>Press 5 To Exit")
    print("------------------------------------------")
    e=input()
    if e=='1':
        sides_menu()
        choosesides()     
    elif e=='2':
        choose()
    elif e=='3':
        bill()
    elif e=='4':
        print("Which Item Do You Want To Remove.Please Specify The SI.No:")
        
    elif e=='5':
        print()
        print("------------------------------------------")
        print("Thank You For Visiting Us!")
        print("------------------------------------------")
#------------------------------------------------------------------------------
#Deserts Code For Entering Name Of Selected Deserts Into A List "desertslist" 
#Also Adding Corresponging Price Of Selected Deserts To Another List Named "pricelist3"  
#------------------------------------------------------------------------------ 
def choosedeserts():
    print("Choose The Deserts: ")
    
    d=input()
    if d=='1':
        itemlist.extend([l4[0][1]])
        pricelist.extend([l4[0][2]])
    elif d=='2':
        itemlist.extend([l4[1][1]])
        pricelist.extend([l4[1][2]])
    elif d=='3':
        itemlist.extend([l4[2][1]])
        pricelist.extend([l4[2][2]])
    elif d=='4':
        itemlist.extend([l4[3][1]])
        pricelist.extend([l4[3][2]])
    elif d=='5':
        itemlist.extend([l4[4][1]])
        pricelist.extend([l4[4][2]])
    elif d=='6':
        itemlist.extend([l4[5][1]])
        pricelist.extend([l4[5][2]])
    else:
        print("------------------------------------------")
        print("Sorry,Invalid Option! Select Correct Option.")
        print("------------------------------------------")
        print()
        deserts_menu()
        choosedeserts()
    desertscontrol()
#------------------------------------------------------------------------------ 
#Deserts Menu Controls
#------------------------------------------------------------------------------      
def desertscontrol():
    print("------------------------------------------")
    print(">>Press 1 To Go Back To Deserts Menu")
    print(">>Press 2 To Go Back To Main Menu")
    print(">>Press 3 To Check The Bill")
    print(">>Press 4 To Edit Bill")
    print(">>Press 5 To Exit")
    print("------------------------------------------")
    e=input()
    if e=='1':
        deserts_menu()
        choosedeserts()
    elif e=='2':
        choose()
    elif e=='3':
        bill()
    elif e=='4':
        print("Which Item Do You Want To Remove.Please Specify The SI.No:")
        
    elif e=='5':
        print()
        print("Thank You For Visiting Us!")
    else:
        print("Invalid Option.Choose Correct Option.")
#------------------------------------------------------------------------------
#Main Category Code
#------------------------------------------------------------------------------
def choose(): 
    print("------------------------------------------")       
    print("Choose The Category: ")
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
        print("Invalid Option.Select Correct Option.")
        choose()
#------------------------------------------------------------------------------
#Billing Menu Code
#Fetch Selected Items From List and corresponding Price From The Other LIst
#And Dislay The Bill
#Also Calculates Total Cost Of All The Items
#------------------------------------------------------------------------------
def bill():
    print("******************************************")
    print("             Bill Amount                 *")
    print("******************************************")
    print("SI.no:         Item               Price  *")
    print("******************************************")
    si=1
    for i in range(len(itemlist)):
        print(si+i,"    ",itemlist[i],"     ₹",pricelist[i]," *")
    """for i in range(len(itemlist)):
        print(si+1,"    ",end='')
        print(itemlist[i],"               ₹",end='')
        print(pricelist[i]," *")
    for i in range(len(itemlist)):
        print(len(itemlist)+i+1,"    ",end='')
        print(itemlist[i],"        ₹",end='')
        print(pricelist[i]," *")
    for i in range(len(itemlist)):
        print(len(itemlist)+i+1,"    ",end='')
        print(itemlist[i],"    ₹",end='')
        print(pricelist[i]," *") """   
    print("******************************************")
    t=0
    for i in itemlist:
        t=sum(pricelist)
    """for i in pricelist1: 
        q=sum(pricelist1)
    for i in pricelist2:
        r=sum(pricelist2)
    for i in pricelist3:
        s=sum(pricelist3)"""   
    totalprice=t
    print("Total Amount:                      ₹",end='')
    print(totalprice," *",end='')
    print()
    print("******************************************")
#------------------------------------------------------------------------------    
"""def deletefrombill():
    for i in range(len(pizzalist)+len(drinkslist)+len(sideslist)+i+1):
        x=input()
        if x==i:
            del """
        
    
    
#------------------------------------------------------------------------------
#First Code
#------------------------------------------------------------------------------
while a:
    print("------------------------------------------")
    name=input("Please Enter Your Name: ")
    print()
    print()
    if name=='':
        print("Invalid Input.")
        c=input("Do You Wish To Continue.Press y Or n:")
        if c!='y':
            a=False
            print()
            print("------------------------------------------")
            print("Thanks For Visiting Us!")
            print("------------------------------------------")
    else:
        a=False
        print("Dominos".center(42,"-"))
        print("Welcome Mr/Mrs.",name,"To Dominos")
        choose()
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------        




    