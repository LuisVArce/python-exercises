
# Exercise 1
fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']
for fruit in fruits:
    output.append(fruit.upper())
    
uppercased_fruits = [fruit.upper() for fruit in fruits]
print(uppercased_fruits)
# Exercise 2

capitalized_fruits = [fruit.capitalize() for fruit in fruits]
print(capitalized_fruits)
# Exercise 3
fruits_with_more_than_two_vowels = [fruit for fruit in fruits if (fruit.count('a') + fruit.count('e') + fruit.count('i') + fruit.count('o') + fruit.count('u')) > 2]
print(fruits_with_more_than_two_vowels)

# Exercise 4
fruits_with_only_two_vowels = [fruit for fruit in fruits if (fruit.count('a') + fruit.count('e') + fruit.count('i') + fruit.count('o') + fruit.count('u')) == 2]
print(fruits_with_only_two_vowels)

#Exercise 5
fruits_with_more_than_five_characters = [fruit for fruit in fruits if len(fruit) > 5]
print(fruits_with_more_than_five_characters)

#Exercise 6




