
# num = int(input("please enter ur num: "))
# while num != 12:
#     num = int(input("please enter ur num: "))
#     print('done!!!')

# for i in range(1,100 + 1):
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#      print("Buzz")
#     else:
#        print(i)

midtern  = float(input("input first score(0-100): "))
final  = float(input("input second score(0-100): "))
project = float(input("input third score(0-100): "))

averange_score = (midtern * 0.20) + (final * 0.40) + (project * 0.40)

if averange_score >= 70:
    print("congrats u scored better than averange u won,")
else:
    print("sorry u failed")

