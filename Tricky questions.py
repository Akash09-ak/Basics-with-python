'''Q.1'''
print(0.1+0.2==0.3) # o/p=False,as 0.1+0.2=0.30000000000000004 in python

'''Q.2'''
s=[1,2,2,3,2,9,6,5]
t=set(s)         # when we converted list into set it doesn't take repeated nos, and set are in curly braces
#print(t)
st=[3,4,5,4]
print(len(t)+sum(st))            # output is 22 sum is function of list where it add all nos.
#print(type(st),type(t),type(s))


'''Q.3'''
t=[0]
s1=s2=t      # here s1 and s2 sharing same name for t
s1=s1+[1]
s2+=[1]         # as we append [1] to s2 then t will also be changed 
print(t)         # o/p is [0,1]
''' Explanation 
t=[0]
s1=s2=t      # here  i thought s1 and s2 sharing same name for t
s1=s1+[1]   # here change in s1 does not effect s2 or t they both remain same
print(s1)
print(s2)
print(t)
print("lets change it")
s2+=[2]         # as we append [2] to s2 then t also get changed 
print(s2)
print(t)        # t wont get affected by changing in s1
print(s1)
'''

'''Q.4'''

s=[100,84,63,97]
st=s.sort()
#print(type(st))
#print (s)       here we get the sortest list
print(s[::-1][0]) # here we get reverse list in s[::-1] and [0] represent ist first element

'''Q.5'''

s='apple'
x=s.find('p')       # it return first p postion from left
#print(x)
y=s.find('n')
#print(y)                # as there is no n it will return -1
z=s.find('')
#print(z)               # it return position of null string i.e. 0
print(x+y+z)

'''Q.6'''

n=0
for i in range(5,0,-1):
    #print(i)
    
    n+=i>n       # in rhs i>n is a boolean value that will give true or false while in lhs there is integer therefore boolean value gets converted into int like true to 1 and fase to 0
    #print(i,n)
print(n)      # o.p =3

'''Q.7'''

b=50           # here b is assigned 50 
def f(a,b=b):          # two parameters are passed in f function a and b where b is assigned value of above b i.e 50
    return a+b
b=20            # here b is assigned value 20
print(f(1))          # here we only passed 1 as value of a not b so the output will be 51
#print(f(1,b))  # but if we pass both 1, b as parameters to function f then the outpute is 21

'''Q.8

s=(1,2,4,5,6)
s[3]=90
print(s)
What will be the output?
Answer is error as s here is tuple and they are immutables'''

'''Q.9'''

m="ITACHI"
i="s"
while i in m:
    print(i,end=" ")
'''output is None i.e. nothing will print as condition is false
for i in m:
    print(i,end=" ")
If it was for in place of while the output would be "I T A C H I " '''

'''Q.10'''

n=[1,34,55,6,7,89]
x=n[-3::-1]                # here -3 indicate third element from right side  and it goes on with increase of -1 in its position towards left
print(x)
