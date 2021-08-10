# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#print(type(year))
#y1 = year % 4
#y2 = year % 100
#y3 = year % 400 
#print(type(y1))

#if y1 ==0 :
 # print ("Leap Year")
#elif y2 !=0 :
 # print ("Leap Year")
#elif y3 ==0 :
 # print ("Leap Year")
if year % 4 == 0 and year % 100 != 0 :
 print ("Leap Year")
elif year % 400 == 0 :
 print ("Leap Year")
else :
 print ("Not Leap Year")





