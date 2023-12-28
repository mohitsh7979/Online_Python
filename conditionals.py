# find a max no between in 4 values 

# a = 4
# b = 800
# c = 30
# d = 20


# if(a>b):
#     if(a>c):
#         if(a>d):
#             print(a)
#         else:
#             print(d)
#     else:
#         if(c>d):
#             print(c)
#         else:
#             print(d)

# else:
#     if(b>c):
#         if(b>d):
#             print(b)
#         else:
#             print(d)
#     else:
#         if(c>d):
#             print(c)
#         else:
#             print(d)

# Write a python to input any alphabet and check whether it is alphabet , digit or special character
# "10"+"20" "1020"




a = (input("Enter :"))

if(a>='a' and a<='z') or (a>='A' and a<='Z'):
    print("its alphabate")

elif(a>='0' and a<'9'):
    print("it is number")

else:
    print("it is a special char....")
