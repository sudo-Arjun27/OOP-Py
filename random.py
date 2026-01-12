# n=5
# array=[]
# i=0
# j=0
# while i<=n:
#     n=n-1
#     array.append(n)
# x=array[:n]
# print(x)
# for k in range(len(x)):
#         j=j-1
#         print(x[j]*x[j])


#program for leap year

# def is_leap(year):
#     leap = False

#     if year % 400 == 0:
#         leap=True

#     elif year % 4 == 0 and year % 100 != 0:
#         leap=True
        
#     else:
#         leap=False

#     print(leap)
#     return leap

# year = int(input("enter the year number: \n"))

# is_leap(year)



#program for printing nos
n=int(input("enter the number: \n"))
i=0
j=0
arr=[]
while n>i:
    arr.append(n)

    n=n-1
for k in range(len(arr)):
    j=j-1
    print(arr[j],end="")