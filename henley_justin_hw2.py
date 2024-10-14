# 4-1
favorite_pizzas = 'Cheese', 'Pepperoni', 'BBQ Chicken'
for pizza in favorite_pizzas:
    print(f"I like {pizza} pizza")
print("I really love pizza")

# 4-2
animals = ['dog', 'cat', 'rabbit']
for animal in animals:
    print(f"A {animal} would make a good pet.")
print("Any of these animals would make a great pet")

# 4-3
for number in range(1,21):
    print(number)

# 8-1
def display_message():
    print("In this chapter, I will be learning about defining and using specific functions in Python.") 
display_message()

# 8-2
def favorite_book(title):
    print(f"One of my favorite books is {title}")
favorite_book("Alice in Wonderland")

# 8-3
def make_shirt(size,message):
    print(f"Making a {size} shirt with the message: '{message}'.")
make_shirt('Medium', 'Code Like A Pro')
make_shirt(size = 'Large', message = 'Python Rocks!')

# 8-4
def make_shirt(size,message):
    print(f"Making a {size} shirt with the message: '{message}'.")
make_shirt('Medium', 'Code Like A Pro')
make_shirt(size = 'Large', message = 'I love python')
make_shirt(size = 'Small', message = 'Coding Rocks')

# 8-5
def describe_city(city, country='USA'):
    print(f"{city} is in {country}")
describe_city('New York')
describe_city('Paris', 'France')
describe_city('Milan', 'Italy')


# 8-6
def city_country(city, country):
    return f"{city}, {country}"
print(city_country('Toronto', 'Canada'))
print(city_country('Tokyo', 'Japan'))
print(city_country('Rome', 'Italy'))