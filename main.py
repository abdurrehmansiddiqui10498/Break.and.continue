# # printing a for loop (continue) from 1 to 10 except 3 & 7
# for a in range(11):
#  if a == 3 or a == 7:
#     continue
#  print(a)
# # print a for loop (break) from 1 to 10 and stops at 4
# for a in range(11):
#   if a == 4:
#     break
#   print(a)

# print a while loop (continue) that print even numbers from 1 to 10

a = 1
while a in range(11):
  a += 1
  if a == 1 or a == 3 or a == 5 or a == 7 or a == 9:
    continue
  elif a % 2 == 0:
   print(a)

# print a while loop (break) that prints from 1 to 10 and stops at 8

a = 1
while a != 11:
  if a == 8:
    break
  print(a)
  a += 1
  