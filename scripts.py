#problem 1
#Laura Laurenti, ID: 1751854

#INTRODUCTION

#Say "Hello, World!" With Python
print("Hello, World!")


#Python If-Else
#!/bin/python

import math
import os
import random
import re
import sys


n=input()
if n%2 ==1:
    print("Weird")
if n==2 or n==4:
    print("Not Weird")
if (n%2==0) and (n>=6 and n<=20):
    print("Weird")
if n%2==0 and n>20:
    print("Not Weird")



#Arithmetic Operators
a = int(raw_input())
b = int(raw_input())
print(a+b)
print(a-b)
print(a*b)



#Python: Division
from __future__ import division

if __name__ == '__main__':
    a = int(raw_input())
    b = int(raw_input())
    print(a//b)
    print(a/b)


#Loops
if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        print(i*i)



#Write a function
def is_leap(year):
    leap = False

    # Write your logic here
    if year%4==0:
        leap=True
        if year%100==0:
            leap=False
            if year%400==0:
                leap=True
    return leap


#Print Function
from __future__ import print_function

if __name__ == '__main__':
    n = int(raw_input())
    for i in range(n):
        print(i+1, end="")





#DATA TYPES

#List Comprehensions
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    ret = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n]
    print(ret)


#Find the Runner-Up Score!
if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    # I inizialize the two max with a big negative number
    max1=-1000
    max2=-1000
    for n in arr:
        if n>max1:
            max2=max1
            max1=n
        if n<max1 and n>max2:
            max2=n
    print(max2)



#Nested Lists
if __name__ == '__main__':
    d={}
    sc=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        sc.append(score)
        d[name]=score
    min2Vec=[]
    # I inizialize the two min with high value
    min1=100
    min2=100
    for i in sc:
        if i<min1:
            min2=min1
            min1=i
        if i>min1 and i<min2:
            min2=i
    for i in d.keys():
        if d[i]==min2:
            min2Vec.append(i)
    min2Vec.sort()
    for i in min2Vec:
        print(i)



#Finding the percentage
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    S=float(0)
    for i in student_marks[query_name]:
        S=float(S+i)
    S=float(S/len(student_marks[query_name]))
    print("%.2f"%(S))


#Lists
if __name__ == '__main__':
    N = int(input())
    l=[]
    out=[]
    for i in range(N):
        l.append(input().split())
    for i in l:
        if i[0]=='insert':
            out.insert(int(i[1]),int(i[2]))
        elif i[0]=='print':
            print(out)
        elif i[0]=='remove':
            out.remove(int(i[1]))
        elif i[0]=='append':
            out.append(int(i[1]))
        elif i[0]=='sort':
            out.sort()
        elif i[0]=='pop':
            out.pop()
        else:
            out.reverse()



#Tuples
if __name__ == '__main__':
    n = int(raw_input())
    integer_list = map(int, raw_input().split())
    t=tuple(integer_list)
    h=hash(t)
    print(h)



#STRINGS

#sWAP cASE
def swap_case(s):
    # I simply use the appropriate method
    S=s.swapcase()
    return S

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)


#String Split and Join
def split_and_join(line):
    line = line.split(" ")
    line="-".join(line)
    return line



#What's Your Name?
def print_full_name(a, b):
    print "Hello "+a+" "+b+"! You just delved into python."


#Mutations
def mutate_string(string, position, character):
    l=list(string)
    l[position]=character
    string = ''.join(l)
    return string



#Find a string
def count_substring(string, sub_string):
    c=0
    slen=len(string)
    sslen=len(sub_string)
    equal=False
    for i in range (slen-sslen+1):
        if string[i:i+sslen]==sub_string:
            equal=True
        else:
            equal=False
        if equal:
            c=c+1
            equal=False

    return c

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)




#String Validators
if __name__ == '__main__':
    s = input()
    alnum=False
    alpha=False
    digit=False
    lower=False
    upper=False

    for i in range(len(s)):
        if s[i].isalnum():
            alnum=True
        if s[i].isalpha():
            alpha=True
        if s[i].isdigit():
            digit=True
        if s[i].islower():
            lower=True
        if s[i].isupper():
            upper=True

    print("True") if alnum else print("False")
    print("True") if alpha else print("False")
    print("True") if digit else print("False")
    print("True") if lower else print("False")
    print("True") if upper else print("False")




#Text Alignment
#Replace all ______ with rjust, ljust or center.

thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))






#Text Wrap
import textwrap

def wrap(string, max_width):
    res= textwrap.fill(string,max_width)
    return res

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)



#Designer Door Mat
n, m = map(int,input().split())
a=int((m-2)/2)
b=int((n-1)/2)
c=int((m-1)/2)
for i in range(0,b):
    print(('.|.'*i).rjust(a,'-')+'.|.'+('.|.'*i).ljust(a,'-'))
print(('WEL').rjust(c,'-')+'C'+('OME').ljust(c,'-'))
for i in reversed(range(0,b)):
    print(('.|.'*i).rjust(a,'-')+'.|.'+('.|.'*i).ljust(a,'-'))



#String Formatting
def print_formatted(number):
    form=len(bin(number)[2:])
    for i in range(1,number+1):
        s=''
        d=str(i)
        for j in range(0,form-len(d)):
            s+=' '
        s+=d
        o=oct(i)[2:]
        for j in range(0,form-len(o)+1):
            s+=' '
        s+=o
        h=hex(i)[2:].upper()
        for j in range(0,form-len(h)+1):
            s+=' '
        s+=h
        b=bin(i)[2:]
        for j in range(0,form-len(b)+1):
            s+=' '
        s+=b
        print(s)



#Alphabet Rangoli
import string
from collections import defaultdict
def print_rangoli(num):

    d = defaultdict(list)
    alph = list(string.ascii_lowercase)
    for i in range(1,(2*num-1)+1):
        for j in range(1,(2*(2*num-1)-1)+1):
            d[i].append('-')

    k = (len(d)*2)//2
    temp = (len(d)//2 )
    for i in range(1,len(d)+1):
        if i <= (len(d)+1)//2:
            index = num
            middle  = (len(d[i])+1)//2
            for j in range(k,k+4*i-3,2):
                d[i][j-1] = alph[index-1]
                if j >= middle:
                    index = index +1
                else:
                    index = index -1
            k = k-2
        else:
            d[i] = d[temp]
            temp = temp -1
    for i in range(1,len(d)+1):
        p=''.join(d[i])
        print(p)



#Capitalize!
import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    s1=''
    nextUpp=True

    for i in s:
        if nextUpp:
            s1+=i.upper()
            nextUpp=False
        else:
            s1+=i
        if i==' ':
            nextUpp=True

    return s1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()






#SETS

#Introduction to Sets
def average(array):
    s=set(array)
    av=0
    l=len(s)
    for i in s:
        av+=i
    av=av/l
    return av

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)


#No Idea!
# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    n, m = map(int, input().split())
    arr = map(int, input().split())
    A= set(map(int, input().split()))
    B= set(map(int, input().split()))
    happy=0
    for i in arr:
        if i in A:
            happy+=1
        if i in B:
            happy-=1
    print(happy)



#Symmetric Difference
if __name__ == '__main__':
    n = int(input())
    N = set(map(int, input().split()))
    m = int(input())
    M = set(map(int, input().split()))
    c=[]
    for i in N:
        if i not in M:
            c.append(i)
    for i in M:
        if i not in N:
            c.append(i)
    c.sort()
    for i in c:
        print(i)



#Set .add()
if __name__ == '__main__':
    n = int(input())
    city = set()
    for i in range(0,n):
        c = str(input())
        if c not in city:
            city.add(c)
    a=len(city)
    print(a)



#Set .discard(), .remove() & .pop()
if __name__ == '__main__':
    n = int(input())
    s = set(map(int, input().split()))
    operations = int(input())
    for i in range(operations):
        command = input().split(' ')

        if command[0]=='pop':
            s.pop()

        elif command[0]=='remove':
            s.remove(int(command[1]))

        elif command[0]=='discard':
            s.discard(int(command[1]))

    Sum=0
    for i in s:
        Sum+=i
    print(Sum)



#Set .union() Operation
if __name__ == '__main__':
    n = int(input())
    sN = set(map(int, input().split()))
    b = int(input())
    sB = set(map(int, input().split()))
    c=len(sN.union(sB))

    print(c)



#Set .intersection() Operation
if __name__ == '__main__':
    n = int(input())
    sN = set(map(int, input().split()))
    b = int(input())
    sB = set(map(int, input().split()))
    c=len(sN.intersection(sB))

    print(c)



#Set .difference() Operation
if __name__ == '__main__':
    n = int(input())
    sN = set(map(int, input().split()))
    b = int(input())
    sB = set(map(int, input().split()))
    c=len(sN.difference(sB))

    print(c)




#Set .symmetric_difference() Operation
if __name__ == '__main__':
    n = int(input())
    sN = set(map(int, input().split()))
    b = int(input())
    sB = set(map(int, input().split()))
    c=len(sN.symmetric_difference(sB))

    print(c)




#Set Mutations
if __name__ == '__main__':
    a = int(input())
    sA= set(map(int, input().split()))
    n = int(input())
    com=''
    num=0
    for i in range(n*2):
        if i%2==0:
            command = input().split(' ')
            if command[0]=='intersection_update':
                com='i_u'
            if command[0]=='update':
                com='u'
            if command[0]=='symmetric_difference_update':
                com='s_d_u'
            if command[0]=='difference_update':
                com='d_u'
            num=int(command[1])
        else:
            s = set(map(int, input().split()))
            if com=='i_u':
                sA.intersection_update(s)
            if com=='u':
                sA.update(s)
            if com=='s_d_u':
                sA.symmetric_difference_update(s)
            if com=='d_u':
                sA.difference_update(s)

    summ=0
    for i in sA:
        summ+=i
    print(summ)




#The Captain's Room
if __name__ == '__main__':
    k = int(input())
    room= list(map(int, input().split()))
    nRoom=(len(room)-1)/k
    existing={}
    captain=0
    for i in room:
        if i in existing:
            existing[i]+=1
        else:
            existing[i]=1
    for i in existing:
        if existing[i]==1:
            captain=i
    print(captain)



#Check Subset
if __name__ == '__main__':
    n = int(input())
    for i in range(0,n):
        check=False
        a = int(input())
        sA= set(map(int, input().split()))
        b = int(input())
        sB= set(map(int, input().split()))
        if a>b:
            check=False
        else:
            if(sA == sA.intersection(sB)):
                check=True
        print(check)



#Check Strict Superset
if __name__ == '__main__':
    A= set(map(int, input().split()))
    n = int(input())
    sets=[]
    check=[]
    for i in range(0,n):
        S= set(map(int, input().split()))
        sets.append(S)
    for i in sets:
        if (i == i.intersection(A)):
                check.append(1)
        else:
            check.append(0)
    x=True
    for i in check:
        if i==0:
            x=False
    print(x)







#COLLECTIONS

#collections.Counter()
from collections import Counter
if __name__ == '__main__':

    X = int(input())
    shoes = list(map(int, input().split()))
    N = int(input())
    shoeCount = Counter(shoes)
    tot = 0
    for i in range(N):
        size, money = map(int, input().split())
        if shoeCount.get(size):
            tot += money
            shoeCount[size] -= 1

print(tot)


#DefaultDict Tutorial
from collections import defaultdict

if __name__ == '__main__':
    d = defaultdict(list)
    n, m= map(int, input().split())

    for i in range(0,n):
        c = input()
        d[c].append(i)
    for i in range(0,m):
        c = input()
        pr=[]
        if c in d:
            pr=d[c]
            for j in pr:
                print(j+1, end = ' ')
            print('')
        else:
            print('-1')



#Collections.namedtuple()
from collections import namedtuple
if __name__ == '__main__':
    n = int(input())
    stud=namedtuple('stud', input().split())
    students=[]
    for i in range(0,n):
        stlist=input().split()
        st1=stud._make(stlist)
        students.append(st1)
    c=0
    for i in students:
        mark=int(i.MARKS)
        c+=mark
    print(c/n)




#Collections.OrderedDict()
from collections import OrderedDict
if __name__ == '__main__':
    d = OrderedDict()
    n=int(input())

    for i in range(0,n):
        l=input().split()
        item_name=' '.join(l[:-1])
        net_price=int(l[-1])
        a=d.get(item_name,0)
        a+=net_price
        d[item_name]=a
    for i in d:
        print(i,end=' ')
        print(d[i])



#Word Order
from collections import OrderedDict

if __name__ == '__main__':
    n = int(input())
    d = OrderedDict()
    for i in range(0,n):
        c = input()
        if c not in d:
            d[c]=1
        else:
            a=d.get(c,0)
            a+=1
            d[c]=a

    print(int(len(d)))
    for i in d:
        print(d[i], end=' ')



#Collections.deque()
from collections import deque
if __name__ == '__main__':
    N = int(input())
    l=[]
    d = deque()
    for i in range(N):
        l.append(input().split())

    for i in l:
        if i[0]=='append':
            d.append(int(i[1]))
        elif i[0]=='appendleft':
            d.appendleft(int(i[1]))
        elif i[0]=='pop':
            d.pop()
        else:
            d.popleft()
    for i in d:
        print(i,end=' ')



#Company Logo
#!/bin/python3

import math
import os
import random
import re
import sys
from collections import OrderedDict



if __name__ == '__main__':
    s = input()

    d = OrderedDict()
    for i in s:
        if i not in d:
            d[i]=1
        else:
            a=d.get(i,0)
            a+=1
            d[i]=a
    D1 = OrderedDict()
    D1 = sorted(d.items(), key = lambda x:(-x[1],x[0]))
    c=0
    for i in D1:
        if c<3:
            for j in i:
                print(j, end=' ')
            c+=1
        print('')









#DATE AND TIME
#Calendar Module
import calendar
k = list(map(int, input().split()))
m = calendar.weekday(k[2],k[0],k[1])
w = ['MONDAY','TUESDAY','WEDNESDAY','THURSDAY','FRIDAY','SATURDAY','SUNDAY']

print(w[m])




#EXCEPTIONS
#Exceptions
if __name__ == '__main__':
    T = int(input())
    for i in range(0,T):
        a , b = input().split()
        try:
            print(int(a)//int(b))
        except ZeroDivisionError as e:
            print("Error Code:",e)
        except ValueError as f:
            print("Error Code:",f)






#BUILT-INS

#Zipped!
if __name__ == '__main__':
    n ,x = input().split()
    res=0
    b=[]
    for i in range(0,int(x)):
        a = (map(float, input().split()))
        b.append(a)
    X=zip(*b)
    for j in X:
        summ=0
        for k in j:
            summ+=float(k)
        res=float(summ/int(x))
        print(res)


#Athlete Sort
#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())
    sArr=sorted(arr, key=lambda arr: arr[k])
    for i in sArr:
        for j in i:
            print(j,end=' ')
        print('')



#ginortS
if __name__ == '__main__':
    S = input()
    numE=[]
    numO=[]
    chLow=[]
    chUpp=[]
    for i in range(len(S)):

        if S[i].isdigit():
            if int(S[i])%2==0:
                numE.append(S[i])
            else:
                numO.append(S[i])
        if S[i].isalpha():
            if S[i].islower():
                chLow.append(S[i])
            if S[i].isupper():
                chUpp.append(S[i])
    sNumE=sorted(numE)
    sNumO=sorted(numO)
    sChLow=sorted(chLow)
    sChUpp=sorted(chUpp)
    for i in sChLow:
        print(i,end='')
    for i in sChUpp:
        print(i,end='')
    for i in sNumO:
        print(i,end='')
    for i in sNumE:
        print(i,end='')





#PYTHON FUNCTIONALS
#Map and Lambda Function
cube = lambda x: x*x*x # complete the lambda function

def fibonacci(n):
    a = []
    for i in range(0,n):
        if i<=1:
            a.append(i)
        else:
            a1=int(a[i-2])
            a2=int(a[i-1])
            a.append(a1+a2)
    return a




#CLOSURES AND DECORATIONS
#Standardize Mobile Number Using Decorators
def wrapper(f):
    def fun(l):
        # complete the function
        #return sorted([f(i) for i in l])
        f(["+91 "+c[-10:-5]+" "+c[-5:] for c in l])
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l)









#NUMPY
#Arrays
import numpy

def arrays(arr):
    narr = numpy.array(arr,float)
    return narr[::-1]

arr = input().strip().split(' ')
result = arrays(arr)
print(result)



#Shape and Reshape
import numpy
if __name__ == '__main__':
    my_array = list(map(int, input().split()))
    print(numpy.reshape(my_array,(3,3)))




#Transpose and Flatten
import numpy
if __name__ == '__main__':

    n,m=(map(int, input().split()))
    arr=[]
    for i in range(n):
        l=list(map(int, input().split()))
        arr.append(l)
    narr = numpy.array(arr)
    print(numpy.transpose(narr))
    print(narr.flatten())



#Concatenate

import numpy
if __name__ == '__main__':

    n,m,p=(map(int, input().split()))
    arrN=[]
    arrM=[]
    for i in range(n):
        l=list(map(int, input().split()))
        arrN.append(l)

    for i in range(m):
        l=list(map(int, input().split()))
        arrM.append(l)

    arrayN = numpy.array(arrN)
    arrayM = numpy.array(arrM)
    print(numpy.concatenate((arrayN, arrayM), axis = 0))




#Eye and Identity
import numpy
if __name__ == '__main__':

    n,m=(map(int, input().split()))
    s=str(numpy.eye(n, m, k = 0))
    s=s.replace('1',' 1').replace('0',' 0')
    print(s)



#Array Mathematics
import numpy

if __name__ == '__main__':

    n,m=(map(int, input().split()))
    a=[]
    b=[]

    for i in range(n):
        l=list(map(int, input().split()))
        a.append(l)

    for i in range(n):
        l=list(map(int, input().split()))
        b.append(l)

    na = numpy.array(a)
    nb = numpy.array(b)

    print(na+nb)
    print(na-nb)
    print(na*nb)
    print(na//nb)
    print(na%nb)
    print(na**nb)



#Floor, Ceil and Rint
import numpy
if __name__ == '__main__':
    a=list(map(float, input().split()))
    my_array = numpy.array(a)

    s=str(numpy.floor(my_array))
    s=s.replace('1.',' 1.').replace('2.',' 2.').replace('3.',' 3.').replace('4.',' 4.').replace('5.',' 5.').replace('6.',' 6.').replace('7.',' 7.').replace('8.',' 8.').replace('9.',' 9.').replace('10.',' 10.')
    print(s)

    s=str(numpy.ceil(my_array))
    s=s.replace('1.',' 1.').replace('2.',' 2.').replace('3.',' 3.').replace('4.',' 4.').replace('5.',' 5.').replace('6.',' 6.').replace('7.',' 7.').replace('8.',' 8.').replace('9.',' 9.').replace('10.',' 10.')
    print(s)

    s=str(numpy.rint(my_array))
    s=s.replace('1.',' 1.').replace('2.',' 2.').replace('3.',' 3.').replace('4.',' 4.').replace('5.',' 5.').replace('6.',' 6.').replace('7.',' 7.').replace('8.',' 8.').replace('9.',' 9.').replace('10.',' 10.')
    print(s)



#Sum and Prod
import numpy
if __name__ == '__main__':

    a=[]
    n,m=(map(int, input().split()))
    for i in range(n):
        l=list(map(int, input().split()))
        a.append(l)
    my_array = numpy.array(a)
    s=numpy.sum(my_array, axis = 0)
    print(numpy.prod(s,axis=0))



#Min and Max
import numpy

if __name__ == '__main__':

    a=[]
    n,m=(map(int, input().split()))
    for i in range(n):
        l=list(map(int, input().split()))
        a.append(l)
    my_array = numpy.array(a)
    m=numpy.min(my_array, axis = 1)
    print(numpy.max(m))



#Mean, Var, and Std
import numpy
if __name__ == '__main__':

    a=[]
    n,m=(map(int, input().split()))
    for i in range(n):
        l=list(map(int, input().split()))
        a.append(l)
    my_array = numpy.array(a)
    s=str(numpy.mean(my_array, axis = 1))
    s=s.replace('1.',' 1.').replace('2.',' 2.').replace('3.',' 3.').replace('4.',' 4.').replace('6.',' 6.').replace('7.',' 7.').replace('8.',' 8.').replace('9.',' 9.').replace('10.',' 10.')
    print(s)
    s=str(numpy.var(my_array, axis = 0))
    s=s.replace('1.',' 1.').replace('2.',' 2.').replace('3.',' 3.').replace('4.',' 4.').replace('6.',' 6.').replace('7.',' 7.').replace('8.',' 8.').replace('9.',' 9.').replace('10.',' 10.')

    print(s)
    s=numpy.std(my_array, axis = None)
    print("%.11f"%(s))



#Dot and Cross
import numpy
if __name__ == '__main__':
    n=int(input())
    a=[]
    b=[]

    for i in range(n):
        l=list(map(int, input().split()))
        a.append(l)

    for i in range(n):
        l=list(map(int, input().split()))
        b.append(l)

    A = numpy.array(a)
    B = numpy.array(b)
    mult = [[sum(a*b for a,b in zip(A_row,B_col)) for B_col in zip(*B)] for A_row in A]
    s=str(mult)
    s=s.replace('],',']\n')
    s=s.replace(',','')
    # I don't know how to fix the indentation problem
    s=s.replace('7',' 7')
    print(s)




#Inner and Outer
import numpy
if __name__ == '__main__':

    A = numpy.array(input().split(), int)
    B = numpy.array(input().split(), int)

    print (numpy.inner(A, B))
    print (numpy.outer(A, B))



#Polynomials
import numpy
if __name__ == '__main__':

    p = numpy.array(input().split(), float)
    x = int(input())
    v=numpy.polyval(p,x)
    print(v)




#Linear Algebra
import numpy
if __name__ == '__main__':

    a=[]
    n=int(input())
    for i in range(n):
        l=list(map(float, input().split()))
        a.append(l)
    my_array = numpy.array(a)
    s=numpy.linalg.det(my_array)
    #print("%.1f"%(s))
    print(s)







#problem 2
#Laura Laurenti, ID: 1751854

#As you can see I commented in a more detailed way the challenges of problem
#2 than the ones of problem 1.

#Birthday Cake Candles
def birthdayCakeCandles(ar):
    ar.sort(reverse=True)
    #the array is reversed sorted, so the first element is the bigger
    tall=int(ar[0])
    res=0
    #increment the variable res by one every time that a tall candle is in ar
    for i in range(0,len(ar)):
        if int(ar[i])==tall:
            res+=1
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(ar)

    fptr.write(str(result) + '\n')

    fptr.close()


#Kangaroo
import os

# Complete the kangaroo function below.
# At the begin I check for the starting location and speed. Than I consider that
# the two kangaroo meet if x1 + i*v1 == x2 + i*v2 so the condition is
# x1-x2=i(v2-v1) for an integer i: I check for (x1-x2)%(v2-v1)==0
def kangaroo(x1, v1, x2, v2):
    res="NO"
    if ((x2>x1 and v2>v1) or (x1>x2 and v1>v2)):
        res="NO"
    else:
        if (x1-x2)%(v2-v1)==0:
            res="YES"
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()


#Viral Advertising

import math
import os

# Complete the viralAdvertising function below.
# I simply apply n times the process described above
def viralAdvertising(n):
    shared=5
    liked=0
    cumulative=0
    for i in range(0,n):
        liked=math.floor(shared/2)
        cumulative+=liked
        shared=liked*3


    return cumulative

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()


#Recursive Digit Sum
# Complete the superDigit function below.
def superDigit(n, k):

    nk=0
    #creation of the first number n*k
    for i in str(n):
        nk+=int(i)
    nk=nk*k
    #recursively call the function while the result is >9
    if nk>9:
        superDigit(str(nk), 1)
    else:
        print(nk)


if __name__ == '__main__':
    nk = input().split()

    n = nk[0]

    k = int(nk[1])

    superDigit(n, k)



#Insertion Sort - Part 1
# Complete the insertionSort1 function below.
def insertionSort1(n, arr):
    # val is the value to be sorted
    val = arr[n-1]
    # I use a for in range 3 2 1 0 to compare the value of all the index of the
    # arr, but not the last index (that is stored in val)
    for i in reversed(range(-2,n-1)):
        # comparisons between val and the value of the arr
        if i == -1:
            arr[i+1] = val
            break
        elif int(arr[i])>int(val):
            arr[i+1]=arr[i]
        else:
            arr[i+1] = val
            break
        for i in arr:
            print(i,end=' ')
        print('')
    for i in arr:
        print(i,end=' ')
    print('')

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)


#Insertion Sort - Part 2

# Complete the insertionSort2 function below.
def insertionSort2(n, arr):
    val=0
    for i in range(1,n):
        # save the value of arr[i]...
        val = arr[i];
        j = i-1
        # ...and check if the previous indices are bigger...
        while j>=0 and arr[j]>val:
            # ...if yes: sort!
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = val
        for i in arr:
            print(i,end=' ')
        print('')


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)
