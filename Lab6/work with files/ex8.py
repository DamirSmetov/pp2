import os


path = '/Users/dilya/OneDrive/Документы/Мама'

for i in os.listdir(path):
    if os.path.isfile(os.path.join(path, i)):
        k = os.path.join(path, i)
if os.path.exists(k) and os.access(k, os.F_OK) and os.access(k, os.R_OK) and os.access(k, os.W_OK) and os.access(k, os.X_OK):
    os.remove(k)
else:
    print("No")
    