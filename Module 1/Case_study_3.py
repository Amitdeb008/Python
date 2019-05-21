import sys
f_num = input("Enter starting number: ")
f_num = int(str(f_num))
l_num = input("Enter last number: ")
l_num = int(str(l_num))
for num in range(f_num,(l_num + 1)):
    if(num % 2) == 0:
        print(str(num) + ",", end="")
    else:
        continue
