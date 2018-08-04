'''AVOIDING DUPLICATES - AVOIDING DUPLICATES
 In this exercise, you will create a program that reads words from the user until the user enters a blank line.
 After the user enters a blank line your program should display each word entered by the user exactly once. The words should be displayed in the same order that they were entered.
 For example, if the user enters:
first
second
first
third
second
then your program should display:
first
second
third'''


l=[]
while 1:
    w=input('Enter a word')
    if w=='':
        break
    else:
        l.append(w)
a=len(l)
x=[]
for i in l:
    if i not in x:
         x.append(i)
for e in x:
    print(e)
        
  
