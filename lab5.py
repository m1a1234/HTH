# 1
def cat_greeting():
    print("Cat says meow")
cat_greeting()

#2
def generate_superhero_power():
    user_name = "Mia"
    user_power = "Flying"
    print(f"My name is {user_name} and my power is {user_power}.")
generate_superhero_power()

#3
def generate_superhero_power_return():
    user_name = "Mia"
    user_power = "Flying"
    output =  f"My name is {user_name} and my power is {user_power}."
    return output
print(generate_superhero_power_return())

#4
def generate_superhero_power_return_args(name, power):
    return f"My name is {name} and my power is {power}."
print(generate_superhero_power_return_args("Mia", "Flying"))

#5
def cat_greetings_loop():
    for i in range(5):
        print("Meow!")
cat_greetings_loop()

#6
def generate_multiple_powers():
    powers = ["Flying", "Invisibility", "Super Strength"]
    for power in powers:
        print(power)
generate_multiple_powers()