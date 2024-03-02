import time
import math

def find_square_root(n, t):
    time.sleep(t/1000)
    x = math.sqrt(n)
    print(f"Square root of {n}, after {t} is {x}")
    
find_square_root(25100, 2123)
    

