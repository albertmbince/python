# print("hello")
# x=complex(input('enter the number:'))
# y=str(input('enter the number:'))
# print(x)
# print(type(x))
# print(y)
# print(type(y))
# a=int(input('enter the number:'))
# b=int(input('enter the number:'))
# print("a=",a)
# print("b=",b)
# print("a=",b)
# print("b=",a)
# x=a
# a=b
# b=x
# a,b=b,a
# print(a,b)
# list=[1,2,"hlo"]
# list[2]=8
# print(list)
# print(list[2])
# tuple1=(1,2,3,"python")
# tuple2=list(tuple1)
# tuple2[3]="hello"
# tuple1=tuple(tuple2)
# print(tuple1)
# list1=[2,3,4]
# list1.append(5)
# list1.clear()
# list1.count()
# list1.reverse()
# list1.insert(1)
# list1.remove(2)
# list1.pop(0)
# list1=[2,3,4]
# list1.extend(7)
# print(list1)
# thislist = ["apple", "banana", "cherry"]
# thistuple = ("kiwi", "orange")
# thislist.extend(thistuple)
# print(list1)
# print(len(list1))
# for x in list1:
#     print(x)-
# 
# find the greatest among 3 digits using condition?
# check whether the emtered number is even or odd?

#1
# a=int(input('enter a:'))
# b=int(input('enter b:'))
# c=int(input('enter c:'))
# if a>b:
    
#     if a>c:
#         print("a is greater")
#     else:
#         print("c is the greatest")
    
# elif b>a:
#     if b>c:
#         print("bis greater")
#     else:
#         print("c is greatest")
# else:
#     print("all are equal") 

#    #2 
# a=int(input('enter a:'))
# if a%2==0:
#     print("a is even")
# else:
#     print("a is odd")
    #leap year or not
# a=int(input("enter the year:"))
# if a%4==0:
#     print("leap year")
# else:
#     print("not leap year")
#dtermine the given the number is positive negative or zero
#define the grade of mark

#1
# a=int(input("enter the number:"))
# if a<0:
#     print("a is negative")
# elif a>0:
#     print("a is positive")
# else:
#     print("zero")
    
#2
# a=int(input("enter the number:"))
# if a>90 and a<100:
#     print('A grade')
# elif a>80 and a<90:
#     print("B grade") 
# elif a>70 and a<80:
#     print("C grade") 
# elif a>60 and a<70:
#     print("D grade") 
# elif a>50 and a<60:
#     print("E grade")    
# else:
#     print("fail")



# a=int(input("enter the number:"))
# if a%7==0 and a%5==0:
#     print('the number is divisible by both 5 and 7')
# else:
#     print("not divisible")
    
# a=int(input("enter the number:"))
# if a%5==0:
#     print('the number is multiple of 5')
# else:
#     print('not a multiple of 5')
# #last digit finder

# a=int(input("enter the number:"))
# a=a%10
# print(a)


# a=int(input("enter the number:"))
# x=a%10
# if x%3==0:
#     print("the last digit is divisible by 3")
# else:
#     print("the last digit is  not divisible by 3")



# a=int(input("enter the unit:"))
# b=0
# if a<=100:
#     print("no charge")
# elif 100<a<=200:
#     b=(a-100)*5
#     print("the amount is",b)
# else:
#     b=500+(a-200)*10
#     print("the amount is",b)
    
    
# a=int(input("enter the unit:"))
# dictionary={1:"sunday",2:"Monday",3:"Tuesday",4:"wednesday",5:"Thursday",6:"Friday",7:"Saturday"}
# print(dictionary[a])

# days=int(input("enter the number of days"))
# d={31:["January", "March", "May", "July", "August", "October", "December"],28:"februvary",30:["April","june","september","november"]}
# if days==31:
#     print(d[31])
# elif days==28:
#     print(d[28])
# elif days==30:
#     print(d[30])
# else:
#     print("Enter the valid number of days")


# days=int(input("enter the number of days"))
# d={31:["January", "March", "May", "July", "August", "October", "December"],28:"februvary",30:["April","june","september","november"]}
# # print(d[days])
# m=input("enter the month")
# if(m in d[31]):
#     print("31 days")
# elif(m in d[30]):
#     print("30 days")
# elif(m in d[28]):
#     print("28 days")
# else:
#     print("enter the month correctly")

# a

# i=0
# while i<=10:
#     print("hello")
# i=i+1

# a=int(input("enter the numbers:"))
# sum=0
# for i in range(a+1):
#     sum=sum+i
#     i=i+1
# print("sum=",sum)
    
# a=int(input("enter the numbers:"))
# sum=0
# while a>0:
#    x=a%10

# a=0
# i=0
# while i<10:
#     d=int(input("enter the numbers:"))
#     a=d+a
#     i=i+1
# print("total sumis=",+a)

1    #print even numbers
# a=int(input("enter the number"))
# for i in range(0,20):
#     if i%2==0:
#         print(i)
#     i=i+1


#2 integer and their square root
# a=0
# for i in range(10):
#     print(i)
#     a=(i**2)
#     i=i+1
#     print("the square root is",a)
    
#prime or not
# a=int(input("enter the number="))
# i=2
# p=0
# while(i<=a/2):
#    if a%2==0:
#        p=1
#        break
# if a==1:
#     print("neither prime nor composite")
# elif p==1:
#     print("the number is not prime")
# elif p==0:
#     print("it is prime")



# for i in range(200,2700):
#     if i%7==0 and i%5==0:
#         print(i)

