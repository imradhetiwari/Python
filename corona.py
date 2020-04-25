p = int(input("enter the current death : "))
r = int(input("enter the death rate : "))
n = int(input("enter the time period till which you want to know total death : "))
total_death = (p*(1 + r/100)**n)
print("Total death : ",total_death)


for day in range(n):
    p = p+(p/100)*r

