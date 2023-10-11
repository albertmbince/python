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
#     l1=l.copy()
#     for i in range(len(l)):
#         for j in range(len(l1)):
#             for char in l[i]:
#                 if char in l1[j]:
#                     print(l[i],l1[j])
#                     break
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

# def A():
#     s=str(input("enter string:"))
#     b=2
#     a=0
#     d=0
#     l=[]
#     e=0
#     for i in range(0,3):
#         c=s[a:b]
#         l.append(c)
#         b=b+4+d
#         a=a+2+e
#         d=d+2
#         e=e+2
#     print(l)
# A()

# def python():
#     l=[]
#     n=str(input('enter string='))
#     for i in n:
#            l.append(i)
#     l.insert(1,".")
#     l.insert(6,".")
#     l[3:5]=["."]
    
#     print("".join(l))
          
# python()

# def sentence():
#     n=str(input('enter sentence:'))
#     print(len(n.split()))
# sentence()


# def sen():
#     n=str(input('enter sentence:'))
#     n.split()
#     l=[]
#     l1=[]
#     d=1
#     e=0
#     c=len(l[e])
#     b=len(l[d])
#     # b=len(i)
#     for i in n.split():
#         l.append(i)
#     s=max(n,key:len)
    
#     print(l1)

    
      
    
        
        
# sen()

# print("1.create list\n2.add elements\n3.Replace element\n4.remove elements\n5.exit")

# list=[3,2,5,4]
# def create():
#     l=[]
#     for i in range(0,4):
#         n=int(input("enter number="))
#         l.append(n)
#     print('the created list is ',l)
# def add():
#     a=int(input("enter the elemnt:"))
#     list.append(a)
#     print("the new list is",list)
# def replace():
#     replace=int(input("enter position to be replaced="))
#     v=int(input("enter elemnt to be replaced="))
#     list.remove(replace)
#     list.insert(replace,v)
#     print("the new list after replacement =",list)
      
# def remove():
#     Remove=int(input('enter the elment to be removed='))
#     list.remove(Remove)
#     print("the new list after removal is",list)
# while True:
#     choice=int(input("enter your choice:"))
#     if choice==1:
#         create()
        
#     elif choice==2:
#         add()
#     elif choice==3:
#         replace()
#     elif choice==4:
#         remove()
#     elif choice==5:
#         print('exit out of operation')
#         break
#     else:
#         print("enter the correct choice")
    
# l=[]  

# for k in range(0,4):
#     n=int(input("enter number="))
#     l.append(n)
# print("the entered list is",l)
# target=int(input("enter the target="))
# for i in l:
#     for j in l:
#         if i+j==target:
#             a=l.index(i)
#             b=l.index(j)
#             print("the position of numbers are",a,"and",b)
        

# l1=[]
# l2=[]
# l3=[]
# for k in range(0,4):
#     n=int(input("enter number="))
#     l1.append(n)
# print("the first list is",l1)
# for k in range(0,4):
#     n=int(input("enter number="))
#     l2.append(n)
# c=1
# print('the second list is',l2)

# for k in range(0,4):
#     n=int(input("enter number="))
#     l3.append(n)
# print('the second list is',l3)


# print("the first list is",l1)
# print('the second list is',l2)
# print('the second list is',l3)
# target=int(input("enter the target="))

# print("the position of numbers are;")
# for i in l1:
#     for j in l2:
#         for m in l3:
#           if i+j+m==target:
#             a=l1.index(i)
#             b=l2.index(j)
#             c=l3.index(m)
#             print("\nin list1=",a,"\nand in list2=",b,"\n and in list3=",c)
#             c=c+1
        
    
    
# import random
# l=[1,2,3,5,7,8]
# n=random.choice(l)
# print(n)


# l=["s","p","r"]
# n=random.choice(l)
# c=0
# u=0
# while True:
#     user=str(input("enter your choice="))
#     print("computer choosed:",n)
#     if user==n:
#         print("tie")
#     elif user=="r" and n=="s":
#         print("yimport randomou won")
#         u=u+1
#     elif user=="r" and n=="p":
#         print("computer wons")
#         c=c+1
#     elif user=="s" and n=="p":
        
#         print("you won")
#         u=u+1print("")
        
#     elif user=='s' and n=="r":
#         print("computer wons")
#         c=c+1
#     elif user=="p" and n=="s":
#         print("computer won")
#         c=c+1
#     elif user=="p" and n=="r":
        
#         print("you won")
#         u=u+1
#     elif user=="quit":
#         print("game over")
#         print("computer scored;",c)
#         print("your score:",u)
#         if u>c:
#             print("you won the game")
#         elif u==c:
#             print("the result is tie")
#         else:
#             print("computer won the game")
        
#         break
#     else:
#         print('invalid input')

import random
l=["lemon","crows","mango"]
n=random.choice(l)
chance=7
g=["_","_","_","_","_"]
while True:
    guess=str(input("enter the letter:"))
    if guess in n:
        print("your guess was right")
        k=n.index(guess)
        print(k)
        chance=chance-1
        g[k]=guess
        print(g)
        j="".join(g)
        if j in l:
            print("you guessed the correct word",j)
            print("you won the game \n remaining chances are",chance)
            print("game over")
            break
        
        
        
    elif chance==0:
        print('your chances are done')
        
        m="".join(g)
        print("what u entered is:",m)
        print("the correct answer was",n)
        print("game over")
        break
    elif guess=="quit":
        print("game over,better luck next time")
        print("the correct answer was",n)
        
        break
    else:
        if guess not in n:
            print("that letter is wrong")
            chance=chance-1
        