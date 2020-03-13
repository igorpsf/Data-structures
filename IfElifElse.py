n = 2
if n % 2 == 0:
    print("Number " + str(n) + " is even")
else:
    print("Number " + str(n) + " is odd")

season = "summer"
if season == "spring":
    print("plant the garden!")
elif season == "summer":
    print("water the garden!")
elif season == "fall":
    print("harvest the garden!")
elif season == "winter":
    print("stay indoors!")
else:
    print("unrecognized season")


phone_balance = 3
bank_balance = 100

print(phone_balance, bank_balance)

if phone_balance < 5:
    phone_balance += 10
    bank_balance -= 10

print(phone_balance, bank_balance)


weight = 55
height = 164

if 18.5 <= weight / height**2 < 25:
    print("BMI is considered 'normail'")

# if (non unsubscribe) and (location == "USA" or location == "CAN")
# print("send email")