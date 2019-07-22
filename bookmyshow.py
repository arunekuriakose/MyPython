row_name=list(map(chr,range(65,79)))
m=list("☐"*20)
row=[]
ticket_price=150

class Error(Exception):
    pass

for i in row_name:
    m.insert(0, i)
    row.append(m)
    m = list("☐"*20)
def seat_layout():
    print("SEAT LAYOUT".center(102,'-'))
    print("\n\n")
    print("     ",end='')
    for i in range(20):
        print(str(i+1).ljust(4),end='')
    print("\n")
    for i in row:
        for j in i:
            print(j.ljust(4),end='')
        print("\n")
    print("\n\n")
    print(" SCREEN THIS WAY".center(102),"\n","=======================================".center(102),"\n\n")


def seat_selection():
    global num,row_preference,seat
    global l

    z1 = True
    while z1:
        try:
            num = int(input("Enter number of seats required (1-6): "))
            if num > 0 and num <= 6:
                z2 = True
                while z2:
                    try:
                        row_preference = input('Enter your preferred Row(A-N): ').upper()
                        if row_preference in row_name:
                            z3 = True
                            while z3:
                                try:
                                    seat = int(input('Enter your preferred Seat number (Start or End seat number): '))
                                    if seat>0 and seat<=20:
                                        z4 = True
                                        while z4:
                                            try:
                                                print("select from list:")
                                                if seat + num <= 21 and seat - num >= 0:
                                                    print("1. (", seat, "-", seat + num - 1, ") 2. (", seat - num + 1,"-", seat, ")")
                                                elif seat - num < 0:
                                                    print("1. (", seat, "-", seat+num-1, ")")
                                                elif seat + num > 21:
                                                    print("2. (",seat - num + 1, "-",seat, ")")
                                                prefer = input("which order? ")
                                                for i in row:
                                                    if row_preference == i[0]:
                                                        if prefer == '1':
                                                            i[seat:seat + num] = '☒' * num
                                                            l=range(seat,seat+num)
                                                            print("\n\n")
                                                            seat_layout()
                                                        elif prefer == '2':
                                                            i[seat:seat - num:-1] = '☒' * num
                                                            l=range(seat,seat-num,-1)
                                                            print("\n\n")
                                                            seat_layout()
                                                        else:
                                                            raise Error("Please select from given lists only")
                                                z4 = False
                                            except Error as v:
                                                print(v)
                                                continue
                                    else:
                                        raise ValueError
                                    z3 = False
                                except ValueError:
                                    print("Please select from the seats present")
                                    continue
                        else:
                            raise Error("Please select from the given rows only")
                            continue
                        z2 = False
                    except Error as m:
                        print(m)
                        continue
            else:
                raise Error("Please Select 1-6 seats only")
                continue
            z1 = False
        except ValueError:
            print("Please enter only numbers")
            continue
        except Error as l:
            print(l)
            continue

def movies():
    global movie_list,show_time,selected_time,selected_movie
    movie_list=[[1,'Lucifer (Malayalam)'],[2,'Avengers: ENDGAME (English)'],[3,'Bharath (Hindi)'],[4,'Athiran (Malayalam)']]
    show_time=[[1,'1.30 PM'],[2,'4.30 PM'],[3,'7.30 PM'],[4,'10.30 PM']]
    for i in movie_list:
        print(i[0],i[1])
    print("\n\nCost of each ticket is:",ticket_price,"\n\n")

    t1=True
    while t1:
        try:
            selected_movie = int(input("Select the Movie: "))
            print("\n")
            if selected_movie<=4 and selected_movie>=1:

                print("You have selected ",movie_list[selected_movie-1][1],"Movie\n")
            else:
                raise Error("Please select from the given list only\n")
            t1=False
        except Error as xyz:
            print(xyz)
            continue
        except ValueError:
            print("Please enter only numbers\n")
            continue


    for i in show_time:
        print(i[0],i[1])
    print("\n\n")
    t2=True
    while t2:
        try:
            selected_time = int(input("Select the show timing: "))
            print("\n")
            if selected_time>=1 and selected_time<=4:
                print("You have selected ", movie_list[selected_movie - 1][1], "Movie for the show at",show_time[selected_time - 1][1])
                print("\n\n")
            else:
                raise Error("Please select from the given list only\n")
            t2=False
        except Error as zyx:
            print(zyx)
            continue
        except ValueError:
            print("Please enter only numbers\n")
            continue

def total():
    print("Your selected movie is:", movie_list[selected_movie - 1][1], "and your show timings are: ",show_time[selected_time - 1][1])
    print("You have selected",num," seats for this movie")
    print("\n")
    print("Your selected seats are: ",end=' ')
    for i in l:
        print(row_preference+str(i),end=' ')
    print('\n\n')
    print("Your total movie cost is",ticket_price*num)
    print("\nPlease pay the amount and collect the tickets")
    print("\nThank you for visiting.")
tr=True
while tr:
    name = input("Enter your name: ")
    if name!='':
        print("\nWelcome Mr/Ms.",name)
        print("\n\n")
        movies()
        seat_layout()
        seat_selection()
        total()
        tr=False
    else:
        print("Please try again!!!")
        continue

