#Lab 3

food = "Seafood Pho"
print(food[0:3])
print(food[-3:])

newFood = food[0] + food[-1]
print(newFood)

foodList = food.split()
print(foodList)

joinedFood = " ".join(foodList)
print(joinedFood)


numbs = [1,2,3,4,5]
numbs.append(6)
numbs.insert(3, 7)
numbs.pop(-1)
numbs.remove(2)
print(numbs)
print(numbs[0:3])
print(numbs[-3:])


books = { "Happer Lee": "To Kill a Mockingbrid",
         "George Orwell": "1984",
         "F. Scott Fitzgerald": "The Great Gatsby",
         "Jane Austen": "Pride and Prejudice"}

keys = books.keys()
values = books.values()
gett = books.get("Jane Austen")
print(keys)
print(values)
print(gett)

books.pop("F. Scott Fitzgerald")
print(books)

del books["Happer Lee"]
print(books)
