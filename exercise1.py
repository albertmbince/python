# #inpubstring and print heir length
# a=10
# while a<=10:
#     a=str(input("enter the input="))
#     print(a)
#     print(len(a))



# #number of times
# a=str(input("enter the word="))
# y=len(a)
# while y!=0:
#    print(a)
#    y=y-1
         
#3
# list1=[]
# i=0
# j=0
# listcommon=[]
# a=int(input("enter the no of elements:"))
# while a!=0:
#     b=str(input("enter the word:"))
#     list1.append(b)
#     a=a-1
# print("the first list is",list1)
# list2=[]
# a=int(input("enter the no of elements:"))
# while a!=0:
#     b=str(input("enter the word:"))
#     list2.append(b)
#     a=a-1
# print("the second list is",list2)


# while i<len(list1) and j<len(list2):
#     if list1[i]==list2[j]:
#         listcommon.append(list1[i])
#         i=i+1
#         j=j+1
#     elif list1[i]<list2[j]:
#         i=i+1
#     else:
#         j=j+1
# print("the common list is",listcommon)
 
 
# #string reversal
# a=str(input("enter the word:"))
# b=len(a)
# i=0
# while i!=b:
#     i=a[-1]
#     print(i)
#     i=a[-i]-1
    
#largest integer  question 6

# a=int(input("enter the number:"))
# list=[]

# while a>0:
#     b=int(input("enter the number:"))
#     a=a-1
#     list.append(b)
#     list.sort()
# print("the largest number is",list[-1])

#question 7

# a=int(input("enter the number:"))
# list=[]
# while a>0:
#     b=str(input("enter the string:"))
#     a=a-1
#     list.append(b)
# print(list)
# print("the number of words in list is",len(list))

#question 8 not completed

a=int(input("enter the number:"))
list=[]
new=[]
i=0
while a>0:
    b=str(input("enter the str:"))
    a=a-1
    list.append(b)
    if len(b)>5:
        new.append(b)
    else:
        continue
print(new)
      
# # print("the largest string is",)
    
    
#question 9 even number list    
# a=int(input("enter the number:"))
# list=[]
# while a>0:
#     b=int(input("enter the integer:"))
#     c=b%2
#     a=a-1
#     if c==0:
#         list.append(b)
        
#     else:
#         continue
# print("the list containing even numbers is ",list)

#question 10 first letter capital
# a=int(input("enter the number:"))
# list=[]
# i=0
# new=[]
# while a>0:
#     b=str(input("enter the integer:"))
#     a=a-1
#     c=b.capitalize()
#     list.append(c)
    
# print(list)
