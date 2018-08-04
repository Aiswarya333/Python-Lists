'''SORTED ORDER - SORTED ORDER
Write a program that:
 reads integers from the user and
 stores them in a list.
 Your program should continue reading values until the user enters 0.
 Then it should display all of the values entered by the user (except for the 0)
 in order from smallest to largest, with one value appearing on each line
 Use either the sort method or the sorted function to sort the list'''

l=[]
while 1:
    num=int(input('Enter number  :'))
    if num == 0 :
        break
    else:
        l.append(num)
    l.sort()
print(l)
    
