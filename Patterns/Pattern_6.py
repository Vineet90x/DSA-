# 1
# 22
# 333
# 4444
# 55555


def pattern(num):
    for i in range(num):
        for j in range(num-i):
            print(j+1,end="")
        print()
 
pattern(5)