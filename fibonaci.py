a = int(input("Enter Your Number : "))

t1 = 0
t2 = 1
temp = 0
print(t1,t2)

i = 1
while i<=a:
    
    temp = t1 + t2
    print(temp)
    t1 = t2 
    t2 = temp
    
    i = i + 1


# 0 1 1 2 3 5 8 13
# frequency of number (587) 3  (47889) 5
# reverse of number  587  785
# palindrome number 121 545 
#fibonaci series 0 1 1 2 3 5 8
# check given number is prime number or not prime number