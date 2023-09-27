# def add():
#     a=10
#     b=20
#     c=a+b
#     print(c)
    
# add()
# def add(a,b):
#     m=b*a
#     return m
# p=int(input("enter p="))
# k=int(input("enter k="))
# print(add(p,k))


#1

# def name(a):
#     c=print(a.title())
#     return c
# b=str(input("enter the name:"))
# name(b)

#2
# def special():
#     st=""
#     k=set("abcdefghijklmnopqrstuvwxyz")
#     for i in strg:
#         if i in k:
#             st=st+i
#     return st
# strg=input("enter string")
# print(special())   


def square():
    list=[]
    list1=[]
    for i in range(0,4):
        a=int(input("enter number="))
        list.append(a)
    for i in list:
        i=i**2
        list1.append(i)
    d=print("the squred list is ",list1)
square()