#capitalizing
# firstname=str(input("enter the name:"))
# middlename=str(input("enter the name:"))
# lastname=str(input("enter the name:"))

# firstname.capitalize()
# lastname.capitalize()
# middlename.capitalize()
# print(firstname.capitalize(),middlename.capitalize(),lastname.capitalize())

#3
# list=[]
# limit=int(input("enter the limit:"))
# i=0
# for b in range(limit):
#     b=int(input("enter the elememt:"))
#     list.append(b)
# print("the list is",list)
# for b in list:
#     b=b**2
#     print("the square is",b)

#4
# list=[]
# i=0
# sum=0
# for b in range(3):
#     b=int(input("enter the element:"))
#     list.append(b)
# print("The list is=",list)
# for i in range(list[i]):
#     c=list[i]
#     d=c**2
#     sum=sum+d
# print("the sum is=",sum)
    
#5

# list1=[]
# list2=[]
# newlist=[]

# limit1=int(input("enter the limit:"))
# limit2=int(input("enter the limit:"))
# for i in range(limit1):
#     b=int(input("enter element:"))
#     list1.append(b)
# for i in range(limit2):
#     c=int(input("enter element:"))
#     list2.append(c)
# print("firstlist:",list1)
# print("secondlist",list2)
# q=set(list1)
# l=set(list2)
# if(q & l):
#     # print("common elements are",q & l)
#     newlist.append(q & l)
#     print(newlist)
# else:
#     print("no common elemnts")

# b="not:-First letter of the month should be capital"
# print(b)
# a=str(input("enter the month:"))
# D={31:["January","March","May","July","August","October","December"],30:["April","June","September","November"],28:["february"]}

# if a in D[31]:
#     print("31 days")
        
# elif a in D[30]:
#     print("30 days")
# elif a in D[28]:
#     print("28 days")
# else:
#     print("enter the correct Month")

# a=int(input("enter the limit"))
# list1=[]
# i=0
# while i<a:
#     n=int(input("enter the number:"))
#     list1.append(n)
#     i=i+1
# print(list1)
# j=1
# large=list1[0]
# while j<a:
#     if list1[j]>large:
#         large=list1[j]
#     j=j+1
# print("largest number is:",large)
# p=5
# for i in range(0,5):
#     for j in range(0,p):
#         print(end="  ")
#     p=p-1
#     for k in range(0,i+1):
#         print("*",end=" ")
#     print()
# n = 5
# for i in range(n, 0, -1):
#     for j in range(1, i + 1):
#         print("*", end=" ")
#     print("")

# for i in range(1,5):
#     for j in range(1,i+1):
#         print(j,end=" ")   
#     print()
    
# for i in range(2,5):
#     for j in range(2,i*2,2):
#         print(j,end=" ")   
#     print()
# k=1
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(k,end=" ")
#         k=k+1 
#     print()

# k=1
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(k+1,end=" ")
#         k=k+2
#     print()
    
# k=1
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(k,end=" ")
#         k=k+2
#     print()
    
# k=1
# for i in range(1,5):
#     for j in range(1,i*2,2):
#         print(j,end=" ")
#     print()

# k=1
# for i in range(1,5):
#     for j in range(1,i*2):
#         print(k,end="  ")
#         k=k+2
#     print()
    
# k=1
# for i in range(1,5):
#     for j in range(1,i*2):
#         print(k,end="  ")
#         k=k+1
#     print()

# k=1
# for i in range(1,5):
#     for j in range(2,i*4,2):
#         print(j,end="  ")
#     print()
# n=68  
# k=65
# for i in range(65,n):
#     for j in range(65,i+1):
#         print(chr(k),end="  ")
#         k=k+1
#     print()

# n=68  
# k=65
# for i in range(65,n):
#     for j in range(65,i+1):
#         print(chr(j),end="  ")
#     print()

# n=68  
# k=65
# for i in range(65,n):
#     for j in range(65,i+1):
#         print(chr(k),end="  ")
#     k=k+1
#     print()

# n=5
# k=1
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         if j%2==0:
#             print(2,end=" ")
#         else:
#             print(1,end=" ")
#     print()

# n=5
# k=1
# for i in range(1,n):
#     for s in range(0,n):
#         print(end="  ")
#     n=n-1
#     for j in range(1,i+1):
#         print(j, end=' ')
#     for k in range(i-1,0,-1):
#         print(k,end=" ")
#     print("")
# n=5
# k=1
# for i in range(1,n):
#     for s in range(0,n):
#         print(end="  ")
#     n=n-1
#     for j in range(1,i+1):
#         if j %2==0:
#           print("A", end=' ')
#         else:
#           print("*", end=' ') 
#     for k in range(i-1,0,-1):
#         if k %2==0:
#           print("A", end=' ')
#         else:
#           print("*", end=' ') 
#     print("")

# l1=[1,2,3,4,5,6]
# l2=[6,7,8,9,10,11]
# l3=[]
# l4=[]
# for i in l1:
#     if i%2!=0:
#         l3.append(i)
    
# # print(l3)
# for j in l2:
#      if j%2==0:
#          l4.append(j)
     
# print(l3)
# print(l4)


#3
# l1=[]
# a=int(input("enter limit:"))
# for i in range(a):
#     b=str(input("enter ="))
#     l1.append(b)
# print(l1)
# for i in range(0,len(l1)):
#     if i%2==0:
#         print(l1[i])

#4
# a=int(input('enter number'))
# b=int(input('enter number'))
# for i in range(a,b+1):
#     if i%2==0:
#         print(i)

#2
# l1=[]
# l2=[]
# a=int(input("enter limit:"))
# for i in range(a):
#     b=str(input("enter ="))
#     l1.append(b)
# print(l1)
# for  i in l1:
#     if i not in l2:
#         l2.append(i)
# print("the unique elemnts are:",l2)
 
 
 #pattern printing
 # l1=[5,2,3,4,1,3,4,2,3]
# for i in range(0,len(l1)):
#     print("*"*l1[i])

# l=[1,2,3,4,5]
# b=int(input("enter choice:"))
# for i in range(len(l)):
    
# print(c)



#vowels

# b=str(input("enter the string="))
# v=0
# for i in b:
#     if (i=="a"or i=="e" or i=="i" or i=="o" or i=="u" or i=="A" or i=="E" or i=="I" or i=="O" or i=="U"):
#         v=v+1

# print("the number of vowels are=",v)    

#3 Palindrome
# b=str(input("enter the string="))
# if(b==b[::-1]):
#     print("palindrome")
# else:
#     print("not palindrome")

#4
b=str(input("enter the string:"))
for i in b:
      if (i==i[::-1]):
        b.replace(i,"@")
print(b.replace(i,"@"))       
    
    

