MyTest.txt
DETAILS
ACTIVITY
MyTest.txt
Sharing Info
Not shared
General Info
Type
Text
Size
4 KB (4,165 bytes)
Storage used
4 KB (4,165 bytes)
Location
PyDev
Owner
me
Modified
Jan 7, 2017 by me
Opened
3:26 AM by me
Created
Jan 7, 2017 with Google Drive Web
Description
Add a description
Download permissions
Viewers can download

#testing map() and lamda
list = ['a', 'c', 'd', 'e']
strfromlist = ''.join(map(lambda s: s+'!', list))
print strfromlist


#testing function definition evaluation with default args.
def foo(para = []):
    para.append("test")
    return para

print foo()
print foo()

def foo2(para = None):
    if para is None:
        para = []
    para.append("test")
    return para

print foo2()
print foo2()

#randomly select an item from the given list
import random

list = ['x', 'y', 'z']

print random.choice(list)

#pseudo random number generator (good for generating camera shakes without changing the values each time)
import random

random.seed(3) #if you comment the seed the random nos. will differ with each execution.
for x in range(3):
    print random.randint(1,6)

#print gives you random nos. in range for specified limit in this case 2	
print random.sample(range(1,5),2) 

#uniquely randomized a list and assign the values (dict values) to the first list (dict keys)
import random
list = ['a', 'c', 'd']
codes = ['2a','2c', '2d']
randCodes = random.sample(codes,len(codes))
test = dict(zip(list,randCodes))
print test.keys(), test.values()

#maps random codes (non unique) to the given list.
import random
list = ['a', 'c', 'd']
codes = ['2a','2c', '2d']

test = map(lambda s : random.choice(codes),list)
print test

#shuffle a list
import random
list = ['a', 'c', 'd']
codes = ['2a','2c', '2d']

random.shuffle(codes)
print codes

#to iterate over list with indices
a = [3,4,5,6]
for i, val in enumerate(a): #enumerate gives [(0,3), (1,7), (2,19)]
	print i, val
	
#binary gap problem (CODILITY)
def binaryGap(n):
    gap = 0
    binary_gap = 0
    x = str(bin(n)).strip("0b")
#     print int('1001000100000001',2)
    list = map(int,str(x))
    for i,b in enumerate(list):
        if b == 0:
            gap = gap+1
        if b == 1:
            if list[i-gap-1] and i-gap-1 != -1 and binary_gap < gap:
                binary_gap = gap
            gap = 0

    return binary_gap
                

print binaryGap(37121)

#example of filter, it filters a list according to the given condition.
list = ['2a', '3c', '2x']
newlist = filter(lambda x: '2' in x , list)
print newlist #prints ['2a', '2x']

#example of reduce
list = ['2a', '3c', '2x']
str = reduce((lambda x, y: x + y), list)
print str #prints 2a3c2x

#another problem showing functions handling default list at definition
def extendList(val, list = []):
    list.append(val)
    return list

l1 = extendList(10)
l2 = extendList(123, [])
l3 = extendList('a')

print id(l1)
print id(l2)
print id(l3)

print l1
print l2
print l3

#slicing and indexing issue
list = [1,2,3,4,5]
print list[10:] #gives empty list []
#print list[10] #gives Index Error

#reverse string without slicing and with list comprehension
str = "PYTHON"
str1 = ''.join([str[i] for i in xrange(len(str)-1,-1,-1)])
print str,"&", str1

#reverse string with slicing
str = "PYTHON"
str1 = ''.join(str[::-1])
print str,"&", str1

#reverse words without slicing and with list comprehension
str = "PYTHON IS AWESOME"
strList = str.split(' ')
reverseWords = ''.join([strList[x]+' ' for x in xrange(len(strList)-1,-1,-1)])
print str, "&", reverseWords

#reverse words with slicing
str = "PYTHON IS AWESOME"
reverseWords = ' '.join(str.split(' ')[::-1])
print str, "&", reverseWords

"""Shallow and Deep copy test"""
import copy
list1=[1,2,3,4]

#regular assignment copy
list2 = list1
list2[0]=6
print list1, list2
print id(list1) == id(list2)
print "\n"

#shallow copy using slicing
list1=[1,2,3,4]
list3=list1[:] #even using list3 = copy.copy(list1) will produce the same result
list3[1]=9
print list1, list3
print id(list1) == id(list3)
print "\n"

#shallow copy using slicing fails with a sublist
list1=[1,2,[3,4]]
list3=list1[:]
list3[1]=9
list3[2][0]=55
print list1, list3
print id(list1) == id(list3)
print "\n"

#deep copy
list1=[1,2,[3,4]]
list4=copy.deepcopy(list1)
list4[1]=9
list4[2][0]=55
print list1, list4
print id(list1) == id(list4)
print "\n"
