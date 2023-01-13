for i in range(0,7):
    for j in range(0,7):

        if (i+j==3)or(j-i==3)or(i+j==9)or(i-j==3):
            print("*",end=" ")

        else:
            print("",end="")
    print()
