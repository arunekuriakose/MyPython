import datetime

bike='Bikes'
car='Cars'
dash='-'.center(45,'-')
double_dash='*'.center(45,'*')
sn='S.No'.center(5)
pc='Price/hr'.center(5)
back='Go Back'

max_days = 10

max_booking_days=30

numbers_only='\nPlease enter numbers only\n'
list_only='Please select from the given list only\n'
z1=z2=z3=z4=z5=tr=True
class Drivezy:
    cars_list=[['Honda City',65],['Swift Dzire',45],['Tata Nexon',50],['Toyota Yaris',80],['Mercedes GLA',150],['DC Avanti',105]]
    bikes_list=[['TVS Ntorq',15],['Royal Enfield Classic 350',25],['Bajaj Dominar 400',30],['TVS Apache RR 310',33],['Yamaha MT15',25],['KTM Duke 390',35]]
    def cars(self):
        print(double_dash)
        print(sn,car.center(30),pc)
        print(double_dash)
        for i in self.cars_list:
            print(str(self.cars_list.index(i)+1).center(5),i[0].center(30),str(i[1]).center(5))
            print(dash)
        return self.cars_list
    def bikes(self):
        print(double_dash)
        print(sn,bike.center(30),pc)
        print(double_dash)
        for i in self.bikes_list:
            print(str(self.bikes_list.index(i)+1).center(5),i[0].center(30),str(i[1]).center(5))
            print(dash)
        return self.bikes_list
def select():
    global z1,z5,selected_list,selected_vehicle
    d=Drivezy()
    print('1.',car,'2.',bike,'\n')
    while z1:
        try:
            vehicle_choice = int(input('Please Select the type of vehicle you want to book: '))
            print()
            if vehicle_choice == 1:
                selected_list=d.cars()
                z1=False
            elif vehicle_choice == 2:
                selected_list=d.bikes()
                z1=False
            else:
                print(list_only)
                continue
        except ValueError:
            print(numbers_only)
    while z5:
        try:
            selected_vehicle=int(input("\nPlease select vehicle model you would like to book: "))
            if selected_vehicle>0 and selected_vehicle<len(selected_list)+1:
                print("\nYou've selected",selected_list[selected_vehicle-1][0],"and it costs Rs.",selected_list[selected_vehicle-1][1],"per hour\n")
                z5=False
            else:
                print(list_only)
                continue
        except ValueError:
            print(numbers_only)
def date():
    global z3,y,z4,dys,hors,pickup_time,drop_time
    def date_selection():
        global pickup_time
        present_time = datetime.datetime.now()
        # no of days allowed to book
        #max_days = 10
        preferred_date = []
        for i in range(max_days):
            preferred_date.append([])

        for i in range(max_days):
            for j in range(24):
                present_time = present_time + datetime.timedelta(hours=1)
                preferred_date[i].append(present_time.time())
                if present_time.hour == 23:
                    break
            preferred_date[i].insert(0, present_time.date())
        preferred_date[max_days - 1] = preferred_date[max_days - 1][:24 - len(preferred_date[0]) + 2]
        for i in range(max_days):
            print(str(i + 1) + '.', preferred_date[i][0], end=' ')
        print('\n')
        print("You're allowed to book for only",max_days,"days in advance\nYou're allowed to book only from the subsequent hour, if your booking date is todady\n")
        tr = True
        while tr:
            try:
                date_prefer = int(input('Enter the date you want to select: ')) - 1
                print()  # preferred_date[date_prefer][0])
                print("You've selected for pickup on ", preferred_date[date_prefer][0],
                      '\n\nPlease select the time you want to pickup from below timings \n')
                zx = preferred_date[date_prefer][1:]
                for i in preferred_date[date_prefer][1:]:
                    print('(' + str(zx.index(i) + 1) + ')', i.strftime("%I %p"), end=' ')
                tr = False
            except ValueError:
                print(numbers_only)
            except IndexError:
                print(list_only)
        print()
        tr = True

        while tr:
            try:
                time_prefer = int(input('\nEnter your preferred time for pickup: '))
                print()
                text = str(preferred_date[int(date_prefer)][0]) + ' ' + str(preferred_date[int(date_prefer)][time_prefer])[:3] + '00:00.000000'
                pickup_time = datetime.datetime.strptime(text, '%Y-%m-%d %H:%M:%S.%f')
                tr = False
            except ValueError:
                print(numbers_only)
            except IndexError:
                print(list_only)

        print("You've selected",selected_list[selected_vehicle-1][0],"for pickup on ", preferred_date[date_prefer][0], "at", pickup_time.strftime("%I:%M %p"),'\n')
    date_selection()
    def hrs(ti):
        global z2,y,hors
        while z2:
            try:
                hors = int(input("\nNumber of hours:(1-23)"))
                if hors>=ti and hors<24:
                    return hors
                    z2=False
                else:
                    print('Please enter the number of hours between',ti,'and 23 only\n')
                    continue
            except ValueError:
                print(numbers_only)
    while z4:
        dys=0
        print("(You're allowed to book for a maximum of",max_booking_days,"days)")
        hour_days = input("How long do you like to book? \n\n1. Less than 1 day 2. More than 1 day ")
        if hour_days == '1':
            hr = hrs(1)
            drop_time = pickup_time + datetime.timedelta(hours=hr)
            z4 = False
        elif hour_days == '2':
            while z3:
                try:
                    dys = int(input('\nNumber of days: '))
                    if dys > 0 and dys <= max_booking_days:
                        hr = hrs(0)
                        drop_time = pickup_time + datetime.timedelta(days=dys, hours=hr)
                        z3 = False
                    else:
                        print("Please enter a number of days between 1 and",max_booking_days,"only")
                        continue
                except ValueError:
                    print(numbers_only)
            z4 = False
        else:
            print(list_only)
            continue
while tr:
    print("\n\n")
    print("Drivezy".center(90,'*'))
    name = input("\n\nEnter your name: ")
    if name!='' and name[0] not in '0123456789':
        print("\nWelcome Mr/Ms.",name)
        print()
        select()
        date()
        print()
        print(double_dash*2)
        print("Your total bill for",selected_list[selected_vehicle-1][0],"is:",selected_list[selected_vehicle-1][1]*(24*dys+hors))
        print(double_dash*2)
        print("\nYour pickup date is on",pickup_time.date(),"at",pickup_time.strftime("%I:%M %p"),"and Your return date is",drop_time.date(),"at",drop_time.strftime("%I:%M %p"))
        print("\nPlease pay the bill.\nThank you for visiting us. Visit Again")
        tr=False
    else:
        print("Please try again!!!")
        continue
