# Task 1
# start = int(input("Enter start number: "))
# stop = int(input("Enter stop number: "))
# sumParni = 0
# sumNeParni = 0
# sumKratni = 0
# countParni = 0
# countNeParni = 0
# countKratni = 0

# for i in range(start, stop + 1, 1):
#     if i % 2 == 0:
#         sumParni += i
#         countParni += 1
#     if i % 9 == 0:
#         sumKratni += i
#         countKratni += 1
#     if i % 2 != 0:
#         sumNeParni += i
#         countNeParni += 1

# print(f"Suma parni: {sumParni}, seredne arifmetichne: {sumParni/countParni}")
# print(f"Suma neparni: {sumNeParni}, seredne arifmetichne: {sumNeParni/countNeParni}")
# print(f"Suma kratni 9: {sumKratni}, seredne arifmetichne: {sumKratni/countKratni}")

# Task 2
# len = int(input("Enter string len: "))
# symbol = str(input("Enter symbol: "))

# for i in range(0, len, 1):
#     print(symbol)

# Task 3
# while True:
#     number = int(input("Enter your number: "))
#     if number == 7:
#         print("Good bye!")
#         break
#     elif number > 0:
#         print("Number is positive")
#     elif number < 0:
#         print("Number is negative")
#     elif number == 0:
#         print("Number is equal to zero")

# Task 4
# minInt = 10000
# maxInt = 0
# sumInt = 0
# while True:
#     number = int(input("Enter your number: "))
#     if number == 7: 
#         print("Good bye!")
#         break
#     if number < minInt: 
#         minInt = number
#         sumInt += number
#     if number > maxInt: 
#         maxInt = number
#         sumInt += number

# print(f"Maximalne chislo: {maxInt}")
# print(f"Minimalne chislo: {minInt}")
# print(f"Sum chisel: {sumInt}")
