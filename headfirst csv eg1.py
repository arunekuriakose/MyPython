with open('sample_email.csv') as paces:     
    
    row_data={}
    column_headings=paces.readline().strip().split(',')
    for each_line in paces:                        
        num_cols = len(column_headings) 
        print(num_cols, end=' -> ') 
        print(column_headings)
        num_2mi = len(row_data[]) 
        print(num_2mi, end=' -> ') 
        
        print(row_data['2mi'])
        num_Marathon = len(row_data['Marathon']) 
        print(num_Marathon, end=' -> ') 
        print(row_data['Marathon'])