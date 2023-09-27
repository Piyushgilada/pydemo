####### Array in python #######
# from array import *
# a=array('i',[-5,6,-7,8])
# n=len(a)
# for i in range (n):
#     print(a[i])
# u=a[0:]
# print(u)
# a.append(12)
# print(a)
# print(a.count(-5))
# b=array('i',[90,80,70])
# a.extend(b)
# o=a.tolist()
# print(o)

# str =input("enter marks:").split(' ')
# print(str)
# marks=[int(i) for i in str]
# print(marks)

########     bubble sort in array         #####
# from array import *
# x=array('i',[])
# n=int(input("how many element you want to insert"))
# for i in range (n):
#     print("insert a number",end='')
#     x.append(int(input()))
# print("original array",x)
# flag=False
# for i in range(n-1):
#     for j in range(n-1-i):
#         if x[j]>x[j+1]:
#             t=x[j]
#             x[j]=x[j+1]
#             x[j+1]=t
#             flag=True
# print('sorted array',x)
# s=int(input("enter element to search"))
# flag =False
# for i in range(len(x)):
#     if s==x[i]:
#         print('found at position',i+1)
#         flag=True
# if flag==False:
#     print("not found in array")

print("Welcome to the higher and lower game")
data=[
        {
        'name':'cristano ronaldo',
        'follower_count':'215',
        'description':'346',
        'country':'portugal'
        },
        {
        'name':'instagram',
        'follower_count':'345',
        'description' : 'social media platform',
        'country':'united states'
        },
        {
        'name':'Arina Gomez',
        'follower_count':'183',
        'description':'singer and artist',
        'country':'united states'
         },
    {
        'name':'virat kohli',
        'follower_count':'190',
        'description':'cricketer',
        'country':'india'
    }
]
print(data)