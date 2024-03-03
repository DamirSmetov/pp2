import os


path = '/Users/dilya/OneDrive/Документы/Мама'

if os.path.exists(path):
    files = os.path.basename(path)
    directories = os.path.dirname(path)
    
    print("Files: ", files)
    print("Directories: ", directories)