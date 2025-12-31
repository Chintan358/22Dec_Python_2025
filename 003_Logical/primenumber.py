# number = 13
# flag = 0
# for i in range(2,number):
#    if number%i==0:
#         flag =1
#         break
   
# if flag==0:
#     print("prime")
# else:
#     print("Not prime")


# for i in range(3,101):
#     number = i
#     flag = 0
#     for i in range(2,number):
#         if number%i==0:
#                 flag =1
#                 break
    
#     if flag==0:
#         print(f"{number} is prime")
#     else:
#         pass
#         # print(f"{number} is Not prime")  




sum =0
for i in range(3,101):
    number = i
    flag = 0
    for i in range(2,number):
        if number%i==0:
                flag =1
                break
    
    if flag==0:
        sum+=number
        print(f"{number} is prime")
    else:
        pass
        # print(f"{number} is Not prime")  

print("sum is ",sum)