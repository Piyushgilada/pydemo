# class Car:
#     def __init__(self,username,userid):
#         self.username=username
#         self.id=userid
#         self.follower=0
# user1=Car("Piyush","001")
# user2=Car("Mayank","002")
# print(user1.username)
# print(user2.follower)
# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age
#
# p1 = Person("John", 36)
#
# print(p1)


# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age
#
#   def __str__(self):
#     return f"{self.name}({self.age})"
#
# p1 = Person("John", 36)
#
# print(p1)
# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age
#
#   def __str__(self):
#     return f"{self.name} of ({self.age})"
#
# p1 = Person("John", 36)
#
# print(p1)

# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age
#
#   def myfunc(self):
#     print("Hello my name is " + self.name)
#
# p1 = Person("John", 36)
# p1.myfunc()

# class Person:
#   def __init__(mysillyobject, name, age):
#     mysillyobject.name = name
#     mysillyobject.age = age
#
#   def myfunc(abc):
#     print("Hello my name is " + abc.name)
#
# p1 = Person("John", 36)
# p1.myfunc()
# from numpy import *
# b = matrix("1 2 3;4 5 6;7 8 9 ")
# print(b)
# print()
# d=b.prod(1)
# print(d)
# a=[[1,2,3],[4,5,6],[7,8,9]]
# for i in range(len(a)):
#   for j in range (len(a[i])):
#     print(a[i][j],end=' ')
# print()
# a=reshape(a,(3,3))
# print(a)
# c=reshape(arrange(11,36,1),(5,5))
# print(c)

# import sys
# from numpy import *
# r1,c1=[int (a) for a in input("first matrix rows ,column: ").split()]
# r2,c2=[int (a) for a in input("Second matrix rows ,column: ").split()]
#
# if c1!=r2:
#     print("multiplication is not possible")
#     sys.exit()
# str1=input("Enter elements in first matrix\n")
# x=reshape(matrix(str1),(r1,c1))
#
# str2=input("Enter elements in second matrix\n")
# y=reshape(matrix(str2),(r2,c2))
# z=x*y
# print("product of matrix is\n",z)

# def fact(n):
#     prod=1
#     while n>=1:
#         prod*=n
#         n-=1
#     return prod
# n=int(input("enter number"))
# x=fact(n)
# print("factorial of given number is = ",x)


# num=int(input("Enter number to check"))
# def prime_number(n):
#     x=1
#     for i in range (2,n):
#         if n%i==0:
#             x=0
#             break
#         else:
#             x=1
#     return x
# result=prime_number(num)
# if result==1:
#     print(num,"is prime")
# else:
#     print(num,"is not prime")q

# def func(item,price):
#     print('item = %s'%item)
#     print('price =%.2f'%price)
# func(item='sugar',price=50)

# list=["sunday","monday","tuesday","wednesday","thursday","friday","saturday"]
# print(list)
# i=len(list)-1
# print(i)
# while i>=0:
#     print(list[i],end=' ')
#     i-=1

# list

x=[]
n=int(input("how many elements ?"))
for i in range (0,n):
    print("Enter number:-")
    x.append(input())
print(x)
# bubble sort
flag=False
for i in range (n-1):
    for j in range(n-i-1):
        if x[j]>x[j+1]:
            t=x[j]
            x[j]=x[j+1]
            x[j+1]=t
            flag =True
    if flag==False:
       break;
    else:
        flag=False
print("sorted list:-",x)