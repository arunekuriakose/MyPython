#Dominos Billing System
a=True

def pizza_menu():
    l1=[[1,'  Veg Extravaganza     ',175,215,245],
       [2,'Pepper Barbecue Chicken',245,265,295],
       [3,'      Margherita       ',175,190,230],
       [4,'    Pepper Paneer      ',270,280,290],
       [5,'  Mexican Green Wave   ',185,235,280],
       [6,'   Veggie Paradise     ',165,205,245]]
    print("******************************************")
    print("S.no              Pizza                  *")
    print("******************************************")
    
    for i in l1:
        print(i[0],"        ",i[1],"      *")
        print("       Small       Medium       Large    *")
        print("       ₹",i[2],"      ₹",i[3],"       ₹",i[4],"   *")
        print("                                         *")
    print("******************************************")

def drinks_menu():
    l2=[[1,'Pepsi         ',60],
       [2,'Bailley Water ',20],
       [3,'Mountain Dew  ',42],
       [4,'Mirinda       ',60],
       [5,'Lipton Ice Tea',37]]
    print("******************************************")
    print("S.no      Drinks               Price     *")
    print("******************************************")
    #
    for i in l2:
        print(i[0],"       ",i[1],"      ₹",i[2],"     *")
        print("                                         *")
    print("******************************************")

def sides_menu():
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
        print("                                         *")
   
    print("******************************************")

def deserts_menu():
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
        print("                                         *")
   
    print("******************************************")
 

while a:
    name=input("Enter the name:")
    if name=='':
        print("Invalid Input.")
        c=input("Do You Wish To Continue.Press Y or N ")
        if c!='y':
            a=False
            print("Thanks For Visiting Us!")
    else:
        a=False
        print("Dominos".center(41,"-"))
        print("Welcome Mr/Mrs.",name,"to Dominos")

def choose():        
    print("Choose the category")
    first_view=[[1,"Pizza"],[2,"Drinks"],[3,"Sides"],[4,"Deserts"],[5,"Exit"]]
    for i in first_view:
        print(i[0],"  ",i[1])
    c=input()
    if c=='1':
        pizza_menu()
    elif c=='2':
        drinks_menu()
    elif c=='3':
        sides_menu()
    elif c=='4':
        deserts_menu()
    elif c=='5':
        print("Thank You For Visiting Us!")
        
choose()
#print("choose)

    