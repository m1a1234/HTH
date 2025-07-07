#Step 1

cookbook = []

#Step 2

def add_recipe(recipe):
    cookbook.append(recipe)

#Step 3
def find_recipe(index):
    if 0 <= index < len(cookbook):
        return cookbook[index]

#Step 4
def update_recipe(index, new_recipe):
    if 0 <= index < len(cookbook):
        cookbook[index] = new_recipe
        print(f"Recipe at index {index} updated to: {new_recipe}")

#Step 5
def delete_recipe(index):
    if 0 <= index < len(cookbook):
        removed_recipe = cookbook.pop(index)
        print(f"Recipe '{removed_recipe}' was deleted at index {index}.")

#Step 6
def list_all_recipes():
    for recipe in cookbook:
        print(recipe)

# Step 7
def main():
    while True:
        print("\nCookbook Recipes")
        print("1. Add a Recipe")
        print("2. Read a Recipe")
        print("3. Update a Recipe")
        print("4. Delete a Recipe")
        print("5. Display all Recipes")
        print("6. Exit")


        choice = input("Choose an option (1-6): ")


        if choice == "1":
            recipe = input("Enter the name of the recipe: ")
            add_recipe(recipe)
        elif choice == "2":
            index = input("Enter the index of the recipe to read: ")
            index = int(index)
            find_recipe(index)
        elif choice == "3":
            index = input("Enter the index of the recipe to update: ")
            recipe = input("Enter the name of the recipe you want to update it with: ")
            index = int(index)
            update_recipe(index, recipe)
        elif choice == "4":
            index = input("Enter the index of the recipe to delete: ")
            index = int(index)
            delete_recipe(index)
        elif choice == "5":
            list_all_recipes()
        elif choice == "6":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please try again.")


main()
