import sys
in_str = input("Enter words: ")
if len(in_str) ==0:
    print("Empty")
else:
    print("Original: ",in_str)
    in_str = sorted(in_str)
    print("Sorted: ",in_str)

