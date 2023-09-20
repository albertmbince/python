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

k=1
for i in range(1,5):
    for j in range(2,i*4,2):
        print(j,end="  ")
    # j=j+2
    print()
    