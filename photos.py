import os , shutil
os.chdir('name')
counter= 0
for dir in os.listdir():
    print(counter, dir)
    try:
        os.chdir(dir)
        for file in os.listdir():
            if file.endswith('_1.jpg'):
                collection =  file[3:5]
                collection_dir = '../../new photos'+'/'+collection

                if not os.path.exists(collection_dir):
                    os.mkdir(collection_dir)

                shutil.copy2(file , 'collection_dir')
        os.chdir('..')
        counter += 1
    except notADirectoryError:
        continue