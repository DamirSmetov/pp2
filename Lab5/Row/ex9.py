import re

s = "BarcelonaIsTheBest"
x = re.sub(r"([a-z])([A-Z])", r"\1 \2", s)
print(x)