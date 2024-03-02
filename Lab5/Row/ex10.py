import re

snake_case = "BarcelonaIsTheBest"
x = re.sub("([a-z])([A-Z])",r"\1_\2", snake_case)
print(x)