# # # n=5
# # # array=[]
# # # i=0
# # # j=0
# # # while i<=n:
# # #     n=n-1
# # #     array.append(n)
# # # x=array[:n]
# # # print(x)
# # # for k in range(len(x)):
# # #         j=j-1
# # #         print(x[j]*x[j])


# # #program for leap year

# # # def is_leap(year):
# # #     leap = False

# # #     if year % 400 == 0:
# # #         leap=True

# # #     elif year % 4 == 0 and year % 100 != 0:
# # #         leap=True
        
# # #     else:
# # #         leap=False

# # #     print(leap)
# # #     return leap

# # # year = int(input("enter the year number: \n"))

# # # is_leap(year)



# # #program for printing nos
# # n=int(input("enter the number: \n"))
# # i=0
# # j=0
# # arr=[]
# # while n>i:
# #     arr.append(n)

# #     n=n-1
# # for k in range(len(arr)):
# #     j=j-1
# #     print(arr[j],end="")


# arr=[1,6,7,2,4,6,2,8,0,6,4,1,7,9,4,2,67,9,97]
# arr.sort()
# new_list=[]
# for i in arr:
#     if i not in new_list:
#         new_list.append(i)
# print(new_list)
# print("Runner up is", new_list[-2])


# # if __name__ == '__main__':
# #     n = int(input("Enter number: \n"))
# #     integer_list = map(int, input().split())
# #     arr=[]
# #     arr.append(integer_list)
# #     print(arr)
        

# #working Logiccccc

# # arr = []
# # nums = input("Enter the number: \n") 
# # nums_list = nums.split()
# # for i in nums_list:
# #     arr.append(int(i))
# # print(arr)
# if __name__ == '__main__':
#     n = int(input("enter the val \n"))
#     integer_list = map(int, input().split())
#     arr=[]
#     for i in integer_list:
#         arr.append(int(i))
#     x=tuple(arr)
#     h=hash(x)
#     print(h)
        
def swap_case(s):
    return s.swapcase()

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)