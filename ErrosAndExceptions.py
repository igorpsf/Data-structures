# while True:
#     try:
#         x = int(input("Enter a number: "))
#         break
#     except ValueError:
#         print("That's not a valid number!")
#     except:
#         print("\nNo input taken")
#         break
#     finally:
#         print("\nAttempted Input\n")
#
#



try:
    x = int(input("Enter a number: "))
    # break - will keep loop until number
except:
    print("Thats not a valid number!")

print("Attempted Input")

while True:
    try:
        x = int(input("Enter a number: "))
        break #- will keep loop until number
    except:
        print("Thats not a valid number!")

    print("Attempted Input")