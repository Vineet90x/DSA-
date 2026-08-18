#     *
#    ***
#   *****
#  *******
# *********

def pattern(num):
    for i in range(num//2+1):
        for j in range (num):
            if j >= num//2 - i and j <= num //2 + i:
                print("*",end='')
            else:
                print(" ",end='')
        print()
        

pattern(9)