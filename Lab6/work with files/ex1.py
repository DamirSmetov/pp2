import os


path = '/Users/dilya/OneDrive/Документы/Мама'

files = []
directories = []

f_d = []

for i in os.listdir(path):
    if os.path.isfile(os.path.join(path, i)):
        files.append(i)
    else:
        directories.append(i)
    f_d.append(i)
print("files: ", files)
print("directories: ", directories)
print("files and directories: ", f_d)


