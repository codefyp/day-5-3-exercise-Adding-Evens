#Write your code below this row 👇
total = 0
for number in range (0, 101):
  if number % 2 == 0:
    total += number
print (total)    
#way 2 more efficient
total2 = 0
for number in range (0 , 101, 2):
  total2 += number
print (total2)    
