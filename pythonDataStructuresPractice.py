# Part 1: Lists
# 1. Create a list of 10 numbers.
num_list = [1,2,3,4,5,6,7,8,9,10]

# 2. Print the first, last, and middle number.
print(num_list[0])
print(num_list[-1])
print(num_list[4])

# 3. Add a new number to the end of the list.
num_list.append(11)
print(num_list)

# 4. Replace the third number with 99.
num_list[2] = 99
print(num_list)

# 5. Loop through the list and print only the even numbers.
for num in num_list:
    if num % 2 == 0:
        print(num)



# ---

# Part 2: Dictionaries
# 1. Create a dictionary of 5 countries and their capitals.
country_dict = {"England": "London", "France": "Paris", "Spain": "Madrid", "Russia": "Moscow", "Italy": "Rome"}
print(country_dict)

# 2. Print the capital of 2 countries.
print(country_dict["England"])
print(country_dict["France"])

# 3. Add a new country-capital pair.
country_dict["Philippines"] = "Manila"
country_dict["Germany"] = "Berlin"
print(country_dict)

# 4. Change the capital of one country.
country_dict["England"] = "Birmingham"
print(country_dict)

# 5. Loop through and print all countries and capitals.
for country in country_dict:
    print (country + " " + country_dict[country])



# ---

# Part 3: Sets
# 1. Create a set of your favorite fruits.
fruit_set = {"orange", "grapes", "apple", "kiwi"}
print(fruit_set)

# 2. Add a new fruit, then remove one.
fruit_set.add("lychee")
fruit_set.remove("grapes")
print(fruit_set)

# 3. Create another set of fruits your friend likes.
friend_set = {"orange", "banana", "kiwi"}
print(friend_set)

# 4. Print:
#    - Fruits you both like (intersection).
inter_set = fruit_set & friend_set
print(inter_set)

#    - Fruits only you like (difference).
diff_set = fruit_set - friend_set
print(diff_set)

#    - All fruits either of you like (union).
union_set = fruit_set | friend_set
print(union_set)



# ---

# Part 4: Tuples
# 1. Create a tuple of 5 colors.
colors = ("red", "yellow", "blue", "green", "orange")

# 2. Print the first and last color.
print(colors[0])
print(colors[-1])

# 3. Loop through the tuple and print each color.
for color in colors:
    print (color)

# 4. Try to change one color (note the error).
colors[2] = "purple"