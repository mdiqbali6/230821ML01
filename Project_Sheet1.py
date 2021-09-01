## 3 ##

s1= "Nice to have it "
s2= "here"
print(s1 + s2)

## 4 ##

a= [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
print(a[3][1][2])

## 5 ##

a.append(s1+s2)
a.insert(0,s1+s2)
print(a)

## 6 ##

numbers=  [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978,328,615,953,345,399,162,758,219,918,237,412,566,826,248,866,950,626,949,687,217,815,67,104,58,512,24,892,894,767,553,81,379,843,831,445,742,717,958,743,527] 
for i in range(len(numbers)):
    if(i<=21):
        if(numbers[i]%2==0):
            print(numbers[i])

## 7 ##

color_list_1= { "white", "black", "red"}
color_list_2= { "red", "green"}
print(color_list_1 - color_list_2)

## 8 ##

c= input("enter a string")
d= c[::-1]
if c==d:
    print(c, " is pangram.")
else:
        print(c, " is not pangam.")

## 9 ##

e= input("Enter a integer")
print(int(e)+int(e*2)+int(e*3))

## 10 ##

f= input(" enter something in the form of ____#_____.  ")
print(f.split( '#'))

## 11 ##
g= input(" Enter words:  " )

g_list = g.split(",")
g_list.sort()
print(', '.join(g_list))

## 12 ##




## h= { 'student': ['rahul','kishore','vidhya','raakhi'], 'marks': [57,87,67,79]}





## 13 ##

j= input(" Enter a sentence ")
k=l=0
for m in j:
    if m.isdigit():
        k+=1
    elif m.isalpha():
        l+=1
    else:
        pass
print("Letters: ",l)
print("Digit: ",k)

## 14 ##







## 15 ##

def divisible():
    n= int(input("input a number: "))
    print("Given numbers are divisible by 7: ")
    for i in range(0,n):
        if(i%7==0):
            print(i)
divisible()

## 16  ##

import math

x, y = 0, 0

while (1):
    step = input("Type in UP/DOWN/LEFT/RIGHT and step number: ")

    if step == "":
        break

    else:
        step = step.split(" ")

        if step[0] == "UP":
            y = y + int(step[1])
        elif step[0] == "DOWN":
            y = y - int(step[1])
        elif step[0] == "LEFT":
            x = x - int(step[1])
        elif step[0] == "RIGHT":
            x = x + int(step[1])

c = math.sqrt(x*2 + y*2)

print("Distance:", c)





            


