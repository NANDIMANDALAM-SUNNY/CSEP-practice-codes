a = input("Enter first input : ")
b = input("Enter second input : ")
a = a.lower()
b = b.lower()
if(len(a) == len(b)):
    sorted_a = sorted(a)
    sorted_b = sorted(b)
    if(sorted_a == sorted_b):
        print(a + " and " + b + " are anagram.")
    else:
        print(a + " and " + b + " are not anagram.")

else:
    print(a + " and " + b + " are not anagram.")