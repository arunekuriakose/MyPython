#
with open('sample_email.csv', 'rb') as csvfile:

    # get number of columns
    for line in csvfile.readlines():
        array = line.split(',')
        first_item = array[0]

    num_columns = len(array)
    csvfile.seek(0)

    reader = csv.reader('sample_email.csv', delimiter=' ')
    included_cols = [1, 2, 6, 7]

    for row in reader:
            content = list(row[i] for i in included_cols)
            print(content)