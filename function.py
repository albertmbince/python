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


# def square():
#     list=[]
#     list1=[]
#     for i in range(0,4):
#         a=int(input("enter number="))
#         list.append(a)
#     for i in list:
#         i=i**2
#         list1.append(i)
#     d=print("the squared list is ",list1)
# square()


# def list():
#   l=[]
#   c=0
#   for i in range(0,3):
#       n=int(input("enter number="))
#       l.append(n)
#   for i in l:
#       b=i**2
#       c=c+b
#   print("the sum of squares=",c)

      
list()    


# def list():
#   l=[]
#   l2=[]
#   l3=[]
# #   c=0
#   for i in range(0,4):
#       n=int(input("enter number="))
#       l.append(n)
#   print("the list one is inserted")
#   for i in range(0,5):
#       n=int(input("enter number="))
#       l2.append(n)
#   print("the list two is inserted")
#   for i in l:
#       if i indef prime():
#     n=int((input("enter limit")))
#     for i in range(0,n+1):
#         if i%2!=0 or i==2:
#             print(i)
# prime() l2:
#           l3.append(i)
  
#   print("The common numbers in both lists are=",l3)        
      
# list()

# def factorial():
#     c=1
#     n=int(input("enter the number="))
#     for i in range(1,n+1):
#        c=c*i
#     print(c)
# factorial()

# def prime():
#     n=int((input("enter limit")))
#     for i in range(0,n+1):
#         if i%2!=0 or i==2:
#             if i%3!=0:
#               print(i)
# prime()

# def fibonacci():
#  c=0
#  d=0
#  a=1
#  n=int((input("enter the value=")))
#  for i in range(1,n):
#        print(d)
#        c=d+a
#        d=a
#        a=c
       
# fibonacci()      


# def pri():
#       for i in range(65,68):
#         for j in range(i,64,-1):
#             print(chr(i),end=" ")
#         print()
# pri()    
    
    
# def pri():
#  n=70 
#  k=65
#  for i in range(65,n):
#     for j in range(65,i+1,1):
#         print(chr(k),end="  ")
#         k=k+1
#     print()
# pri()    
    
# def pri():
#  n=70 
#  k=65
#  for i in range(65,n):
#     for j in range(65,i+1):
#         print(chr(j),end="  ")
#         k=k+1
#     print()
# pri()    



# def pri():
#  n=70 
#  k=65
#  for i in range(65,n):
#     for j in range(65,i+1):
#         print(chr(i),end="  ")
#         i=i-1
#     print()
# pri()    

# def star():
#     for i in range(5,0,-1):
#         for j in range(0,i):
#             print("",end=" ")
#             # i=i+1
#         print("*")
#     for i in range(0,5):
#               for j in range(0,i):
#                  print("",end=" ")
#             # i=i+1
#               print("*")
# star()


# 
# def A():
#  n = 5
#  for i in range(1, n+1):
#     for j in range(n - i):
#         print(' ', end='')

#     for k in range(2 * i - 1):
#         if k == 0 or k == 2 * i - 2:
#             print('*', end='')
#         else:
#             if i == 3:
#                 print('*', end='')
#             else:
#                 print(' ', end='')
#     print()
# A()
# def pattern():
#     k=1
#     for i in range(1,8):
                  
#                  for j in range(0,i):
#                       print("*",end="" )    
#                  print()
                        
#                  if i%2==0 :  
#                       for j in range(1,i+1):
#                          print(j,end="")
#                         
#                       print()
                 
#                  else:
#                     for j in range(i,0,-1):
#                        print(j,end="")
#                     print()    
                     
                     
            
                     
# pattern()


# def decimal():
#  l=[]
#  n=float(input("enter decimal number:"))
#  a=n/2
#  b=a%10
#  l.append(b)
#  print(l)
 
   
   

# decimal()


# def ascending():
#    l=[]
#    for i in range(0,6):
#       n=int(input("enter number="))
#       l.append(n)
#    l.sort()
#    print("ascending order is =",l)
#    l.sort(reverse= True)
#    print('descending order is=',l)
# ascending()


# def fibo():
#     a=int(input("enter number:"))
#     b=0
#     c=1
#     for i in range(0,a):
#        if b<=a:
#         print(b)
#         d=b+c
#         b=c
#         c=d
# fibo()

# def sum():
#     l=[3,8,12,7,6,10,21,15]
#     total=18
#     for i in l:
#         for j in l:
#             if i+j==total:
#              print("the numbers that give sum 18 are",i,j)
            
           
      
# sum()
# def words():
    
    
#     l=["apple","banana","cherry","date"]
#     for x in l :
#         for y in l:
#             for j in x:
#                 for q in y:
                    
#                   if j==q:
#                    print(x,y)   
                         
# words()


# def number():
#     l=[2,3,4,5,6]
#     print("the numbers which give product even are")
#     for i in l:
#         for j in l:
#             a=i*j
            
#             if a%2==0:
#                 print(i,j)
#     print("the numbers which give sum odd are")
#     for i in l:
#      for j in l:
#         b=i+j
#         if b%2!=0:
#                 print(i,j)
# number()