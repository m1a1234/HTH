#1
check_age = True
while check_age == True:
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    if age >= 18:
        print(f"{name} can vote.")
    else:
        print(f"{name} can not vote.")
    user_answer = input("Do you want to check another age? (yes/no): ")
    if user_answer  == "yes":
        check_age = True
    elif user_answer  == "no":
        check_age = False

#2
nums = [-2, -1, 0, 1, 2]
for num in nums:
    if num < 0:
        print(f"{num} is negative")
    elif num == 0:
        print(f"{num} is zero")
    else:
        print(f"{num} is positive")

#3
inventory = ["coal", "dirt", "diamond", "gravel", "stone"]

for item in inventory:
    print(f"{item} is in the inventory")

    if item == "diamond":
        print("JACKPOT!!")
       