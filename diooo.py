sel=[]
tp=[]
def p_menu():
    l=[[1,"PA",230,330,430],[2,"PB",240,340,440,],[3,"PC",250,350,450]]
    
    print()
    print("*************************************")
    print("** S.no            Pizza           **")
    print("*************************************")
    for i in l:
        print("**                                 **")
        print("**",i[0],"              ",i[1],"            **")
        print("**          Small Medium Large     **")
        print("**          ",i[2]," ",i[3],"  ",i[4],"     **")
        print("**                                 **")
        print("*************************************")
    print("**                                 **")
    print("** 4               GoBack          **")
    print("**                                 **")
    print("*************************************")
    e=1
    print("Please select the Pizza you want from above menu:")
    while e:
        k=int(input())
        d=k-1
        if d<3:
            print("You have selected: ",l[d][1])
            print("Please select the size(S for Small, M for Medium, L for Large): ")
            print("          Small Medium Large     ")
            print("          ",l[d][2]," ",l[d][3],"  ",l[d][4],"     ")
            c=1
            while c:
                s=input()
                if s=="s" or s=="S":
                    print("You have selected",l[d][1],"pizza of size Small costing",l[d][2])
                    
                elif s=="m" or s=="M":
                    print("You have selected",l[d][1],"pizza of size Medium costing",l[d][3])
                elif s=="l" or s=="L":
                    print("You have selected",l[d][1],"pizza of size Large costing",l[d][4])
                else:
                    print("Please enter only the mentioned sizes")
                    continue
                c=0
                sel.append([l[d][1],l[d][2]])
                tp.append(l[d][2])
                break
        elif d==3:
            menu()
        else:
            print("please select from given menu only")
            continue
        e=0
def s_menu():
    l=[[1,"SA",130],[2,"SB",230],[3,"SC",330]]
    
    print()
    print("*************************************")
    print("** S.no            Sides           **")
    print("*************************************")
    for i in l:
        print("**                                 **")
        print("**",i[0],"               ",i[1],"           **")
        
        print("**                  ",i[2],"          **")
        print("**                                 **")
        print("*************************************")
    print("**                                 **")
    print("** 4               GoBack          **")
    print("**                                 **")
    print("*************************************")
    e=1
    print("Please select the Sides you want from above menu:")
    while e:
        k=int(input())
        d=k-1
        if d<3:
            print("You have selected Sides",l[d][1],"costing",l[d][2])
            sel.append([l[d][1],l[d][2]])
            tp.append(l[d][2])
        elif d==3:
            menu()
        else:
            print("please select from given menu only")
            continue
        e=0
def dr_menu():
    l=[[1,"DrA",10],[2,"DrB",20],[3,"DrC",30]]
    
    print()
    print("*************************************")
    print("** S.no            Drinks          **")
    print("*************************************")
    for i in l:
        print("**                                 **")
        print("**",i[0],"               ",i[1],"          **")
        
        print("**                  ",i[2],"           **")
        print("**                                 **")
        print("*************************************")
    print("**                                 **")
    print("** 4               GoBack          **")
    print("**                                 **")
    print("*************************************")
    e=1
    print("Please select the Drinks you want from above menu:")
    while e:
        k=int(input())
        d=k-1
        if d<3:
            print("You have selected Drink",l[d][1],"costing",l[d][2])
            sel.append([l[d][1],l[d][2]])
            tp.append(l[d][2])
        elif d==3:
            menu()
        else:
            print("please select from given menu only")
            continue
        e=0
def des_menu():
    l=[[1,"DsA",55],[2,"DsB",65],[3,"DsC",75]]
    
    print()
    print("*************************************")
    print("** S.no            Desserts        **")
    print("*************************************")
    for i in l:
        print("**                                 **")
        print("**",i[0],"              ",i[1],"           **")
        
        print("**                 ",i[2],"            **")
        print("**                                 **")
        print("*************************************")
    print("**                                 **")
    print("** 4               GoBack          **")
    print("**                                 **")
    print("*************************************")
    e=1
    print("Please select the Desserts you want from above menu:")
    while e:
        k=int(input())
        d=k-1
        if d<3:
            print("You have selected Dessert",l[d][1],"costing",l[d][2])
            sel.append([l[d][1],l[d][2]])
            tp.append(l[d][2])
        elif d==3:
            menu()
        else:
            print("please select from given menu only")
            continue
        e=0
def menu():
    print()
    print("*************************************")
    print()
    print("Please choose from the below menu:")
    l=[[1,"Pizza"],[2,"Sides"],[3,"Drinks"],[4,"Desserts"],[5,"Exit"]]

    for i in l:
        print(i[0],i[1])
    print()
    print("(Enter the number)")
    print()

    f=1
    while f:
        j=input()
        if j=="1":
            p_menu()    
        elif j=='2':
            s_menu()    
        elif j=='3':
            dr_menu()            
        elif j=='4':
            des_menu()
        elif j=='5':
            print("Thank you for visiting")
        else:
            print("Please choose the right option")
            continue
        f=0
b=1
while b:
    n=input("Enter your name: ")
    if n=="":
        print("Invalid Input")
        print("Do you wish to continue? (Y or N)")
        y=input()
        if y=="y" or y=="Y":
            continue
        elif y=="n" or y=="N":
            print("Thank you for visiting us")
            break
        else:
            print("Please enter the valid input")
            
    else:
        
        print("Dominos".center(100,"*"))
        print("Welcome Mr/Ms",n)
        print()

        menu()
        c=True
        while c:
            print()
    
            print()
            print("Your selected items are:")
            print("*******************************************")
            print(" S.No Selected Item      Cost")
            print("*******************************************")
            q=0
            for i in sel:
                print(" ",q+1,"       ",i[0],"          ",i[1])
                print()
                q+=1
            print("*******************************************")
            print("        Total cost:      ",sum(tp))
            print("*******************************************")
            print()
            print("Do you need anything more? (Y or N)")
            y=input()
            if y=="y" or y=="Y":
                menu()
                continue
            elif y=="n" or y=="N":
                print()
                
            else:
                print("Please enter the valid input")
                continue
            print("Do you want to remove anything? (Y or N)")
            z=input()
            if z=="y" or z=="Y":
                print("which one to remove?")
                t=int(input())
                del sel[t-1]
                del tp[t-1]
            elif z=="n" or z=="N":
                print("Please pay the bill of",sum(tp)," and GTFO")
                print("Thank you for visiting us, Please visit again")
                c=False
                b=0
            else:
                print("Please enter valid input")
                continue
        b=0