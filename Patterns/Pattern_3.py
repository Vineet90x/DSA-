# 1
# 12
# 123
# 1234
# 12345


def pattern(num):
    for i in range(num):
        for j in range(i+1):
            print(j+1,end="")
        print()

pattern(5)