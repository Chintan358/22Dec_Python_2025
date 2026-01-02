number = 10010011
p =0
total = 0
while number!=0:
    rem = number%10
    total+=(rem*(2**p))
    number=number//10
    p+=1

print(total)