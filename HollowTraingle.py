n=5
for i in range(1,n+1):
    for j in range(i):
        if j==0 or j==i-1:
            print('*',end='')
        else:
            if 1!=n:
                print('',end='')
            else:
                print('*',end='')
    print()