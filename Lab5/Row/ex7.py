import re

snake_case = "Barcelona_is_the_best"
x = re.split("_", snake_case)
camel_case = ""
for i in x:
    camel_case += i.capitalize()
print(camel_case)