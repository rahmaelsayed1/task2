#R code
print_r=[[" " for i in range(6)]for j in range(6)]
print_o=[[" " for i in range(6)]for j in range(6)]
print_rr=[[" " for i in range(6)]for j in range(6)]
print_oo=[[" " for i in range(6)]for j in range(6)]
for col in range(6):
    for row in range(6):
        if (col==0 or (col==4 and row!=0 and row!=3) or((row==0 or row==3) and(col>0 and col<4))): #or ((row==0 or row==5 )and (col!=7 and col!=12) or (col==7 or col==12) and (row!=0 and row!=5)):
            print_r[row][col]= "*"
            print_rr[row][col] = "*"

#o code
for row in range(6):
    for col in range(6):
        if (row==0 or row==5 )and (col!=0 and col!=5) or (col==0 or col==5) and (row!=0 and row!=5):
            print_o[row][col]="*"
            print_oo[row][col] = "*"

for i in range(6):
    for j in range(6):
        print(print_r[i][j],end="")
    print(end="  ")
    for j in range(6):
        print(print_o[i][j],end="")
    print(end="  ")
    for j in range(6):
        print(print_rr[i][j],end="")
    print(end="  ")
    for j in range(6):
        print(print_oo[i][j],end="")
    print(end="  ")

    print()