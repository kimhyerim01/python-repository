def display_multiplication_table( ) :
    i = 1
    n = 2
    while n <= 5 :
        while i <= 9 :
            print(f'{n} x {i} = {n * i:2d}\n')
            i += 1
        n += 1

    while 6<= n <=9 :
        while i<= 9:
            print(f'{n} x {i} = {n*i:2d}\n')
            i += 1
        n+= 1
        
        

print(display_multiplication_table)



