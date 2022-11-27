import os
os.chdir('name')
for i in os.listdir():
    try:
        os.chdir(dir)
        os.chdir('..')
    except notADirectoryError:
        continue