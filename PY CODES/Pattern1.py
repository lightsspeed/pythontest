rows=int(input("enter the no. of rows: "))

for row in range(1, rows+1 ):
    for column in range( 1 , row+1 ):
        print(column, end=" ")
    print()

for row in range(rows-1, 0, -1):
    for column in range( 1 , row+1 ):
        print(column, end=" ")
    print()   