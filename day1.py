# # print("hello world\n")
# # print("day 1 "+"string concatenation")
# # print("new line\npython \tprograming")
# # # comments in python
# # print(len(input("what is your name")))
# # # length of the string
# # name=input("what is your cat name?")
# # print(name)
# # a=input("a:")
# # b=input("b:")
# # print("a: "+a)
# # print("b: "+b)
# # c=a
# # a=b
# # b=c
# # print("a: "+a)
# # print("b: "+b)
# # print("c: "+c)
# #
# # # final project
#
#
# # d={10:'aman',20:'piyush'}
# # print(d)
# # e={}
# # e[10]="vikas"
# # e[11]="mayank"
# # print(e)
# # s= """This is first indian author book " core's python by Piyush Gilada" which is very useful """
# # print(type(s))
# # print(type(e))
# # ch='a'
# # print(type(ch))
#
# # ch1= "shubham"
# # print(len(ch1))
# # # for i in ch1:print(i)
# # print(ch1[6])
#
#
# # a=13
# # b=5
# # print(a/b)
# # print(a//b)
# # print(a%b)
# # print(a**b)
# # print((1+2)*3**2//2+3)
#
# import math
# # x=10
# # y=11
# # print(id(x))
# # if(x == y):
# #     print("equal")
# # else:
# #     print("not equal")
#
#
# a=math.sqrt(4)
# b=math.factorial(3)
# print(a)
# print(b)
# pi1=math.pi
# # print(math.degrees(3.14),end=' ')
# print(math.radians(180))
# print(math.sin(0))
# str,str1,str2 =[int(x) for x in input("enter three numbers: ").split()]
# print(str,str1,str2)
# result=eval("str+str1+20")
# print(result)
#
# num=1
# # for i in range(1,11):
# #     for j in range(1,11):
# #         print('{:5}'.format(num),end="")
# #         num+=1
#     print()
#
# max=int(input("Enter number upto :- "))
# for num in range(2,max+1):
#     for i in range(2,num):
#         if (num %i)==0:
#             break
#         else:
#             print(num)
#             break


# def is_prime(num):
#     if num < 2:
#         return False
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             return False
#     return True
#
# def print_prime_numbers(n):
#     print("Prime numbers up to", n, ":")
#     for num in range(2, n + 1):
#         if is_prime(num):
#             print(num, end=" ")
#
# # Get user input
# user_input = int(input("Enter a number: "))
#
# # Print prime numbers
# print_prime_numbers(user_input)

# user=int(input("Enter the no of element want in fibonacci series...."))
# f1=0
# print(f1,end=' ')
# f2=1
# print(f2,end=' ')
# for i in range(1,user-1):
#     f = f1 + f2
#     print(f,end=' ')
#     f1=f2
#     f2=f

# arr=array('i',[1,2,3,4,5,6])
# print("original array =",arr)
# arr.append(10)
# print("array after append =",arr)
# arr.insert(1,99)
# print("array after insert at 1st index=",arr)
# print(arr.index(4))
# print(arr.itemsize);       # 4 in bytes
# lst=arr.tolist()
# print(lst)
# arr.tostring()

from array import *
# str=input("enter marks :- ").split(' ')
# marks=[int(num)for num in str]
# print(marks)
# sum=0
# for x in marks:
#     print(x)
#     sum+=x;
# print("total marks :-",sum)

#  // sorting of array..
# from array import *
# x=array('i',[])
# print('how many elements?',end='')
# n=int(input())
# for i in range(n):
#     print("Enter element :",end='')
#     x.append(int(input()))
# print('original array :',x)
# flag=False
# for i in range(n-1):
#     for j in range (n-1-i):
#         if x[j]>x[j+1]:
#             t=x[j]
#             x[j]=x[j+1]
#             x[j+1]=t
#             flag=True
#     if flag ==False:
#         break;
#     else:
#         flag=False
# print('sorted array=',x)

# searching an array for an element
from array import *
x=array('i',[])
print("how many elements?")
n=int(input())
for i in range(n):
    print("Enter elements :",end='')
    x.append(int(input()))
print('original array :',x)

print("enter element to search")
s=int(input())
flag=False
for i in range(len(x)):
    if s==x[i]:
        print("element found at location of index",i)
        flag=True
if flag==False:
    print("element not found")


