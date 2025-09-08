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

# 4. Change the capital of one country.
# 5. Loop through and print all countries and capitals.

# # ---

# # Part 3: Sets
# # 1. Create a set of your favorite fruits.
# # 2. Add a new fruit, then remove one.
# # 3. Create another set of fruits your friend likes.
# # 4. Print:
# #    - Fruits you both like (intersection).
# #    - Fruits only you like (difference).
# #    - All fruits either of you like (union).

# # ---

# # Part 4: Tuples
# # 1. Create a tuple of 5 colors.
# colors = ("red", "yellow", "blue", "green", "orange")

# # 2. Print the first and last color.
# print(colors[0])
# print(colors[-1])

# # 3. Loop through the tuple and print each color.
# for i in colors:
#     print (colors[i])

# 4. Try to change one color (note the error).
