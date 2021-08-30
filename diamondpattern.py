'''
Created on Aug 25, 2021

@author: Nasir Khurshid
'''

n=input('Enter number of rows (half of diamond): ')
rows=int(n)

#first half diamond
for i in range(1, rows+1):
    for j in range(i, rows):
        print(" ", end='')
    for k in range(0, 2*i-1):
        print('*', end='')
    print()

#second half diamond
for i in range(rows-1, 0, -1):
    for j in range(rows, i, -1):
        print(" ", end='')
    for k in range(i*2-1, 0, -1):
        print("*", end='')
    print()