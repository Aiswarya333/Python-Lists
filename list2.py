'''REVERSE ORDER - Write a program that
 reads integers from the user and
 stores them in a list.
 Use 0 as a sentinel value to mark the end of the input.
 Once all of the values have been read your program should display them (except for the 0)
 in reverse order, with one value appearing on each line.'''


l=[]
while 1:
    num=int(input('Enter numbers  :'))
    if num ==0:
        break
    else:
        l.append(num)
l.reverse()
print(l)
