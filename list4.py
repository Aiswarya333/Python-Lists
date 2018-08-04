'''BELOW AND ABOVE AVERAGE - Write a program that
 reads numbers from the user until a zero is entered.
 Your program should display the average of all of the values entered by the user.
 Then the program should display all of the below average values & label.
 followed by all of the average values (if any) & label,
 followed by all of the above average values & label.'''



sum=0
c=0
num=1
x=[]
s=[]
g=[]
while num!=0:
    num=int(input('Enter numbers   :'))
    sum=sum+num
    c+=1
    x.append(num)
avg=sum/(c-1)
for i in x:
    if i<avg:
        s.append(i)
    else:
        g.append(i)
str1=' '.join(str(e) for e in s)
str2=' '.join(str(p) for p in g)
print('Below average values:',str1,'Average:',avg,'Above average values:',str2)

