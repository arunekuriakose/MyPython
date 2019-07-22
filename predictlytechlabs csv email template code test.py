import csv

with open('sample_email.csv') as csv_file:
    csv_reader=csv.reader(csv_file, delimiter=',')
#    line_count=0
    for row in csv_reader:
#        if line_count==0:
#            #print(f'Column names are {", ".join(row)}')
#            line_count += 1
#        elif line_count==1:           
        with open("demo.txt",'w',encoding='utf-8')as f:
            f.write(f'Name:{row[0]} Last Name:{row[1]}  Company:{row[2]} Address:{row[3]} City:{row[4]} Country:{row[5]} State:{row[6]} Zip:{row[7]} Phone1:{row[8]} email:{row[10]} subject:{row[11]} email_body:{row[12]}.\n\n')
            #print(f'Name:{row[0]} Last Name:{row[1]}  Company:{row[2]}
            #Address:{row[3]} City:{row[4]} Country:{row[5]} State:{row[6]}
            #Zip:{row[7]}
            #Phone1:{row[8]} email:{row[10]} subject:{row[11]}
            #email_body:{row[12]}.')
            #f.write()
            #print("Email To Be Made")
            f.write(f'Email To:{row[10]}\n')
            f.write(f'Subject Line:{row[11]}\n')
            f.write(f'Hi {row[0]} {row[1]},\n')
            f.write(f'{row[12]}\n')
            f.write('Thanks,\nRob Willison.\n')
#           line_count += 1
           
f=open("demo.txt")
print(f.read())
#    print(f'Processed {line_count} lines.')