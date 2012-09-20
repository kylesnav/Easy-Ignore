import os

repo = '/Users/kylesnav/Documents/Easy-Ignore' #the local location of your git repo.
ignore = ['.DS_Store', '', ''] # add more as needed, it's a list.
file = '.gitignore' # do not change this value.

os.chdir(repo)

if os.path.exists(file): 
    file = open(file, 'r+')
    exist = file.readlines()
    for i in ignore:
        if i in exist: continue
        else: file.write(i)
        
else: 
    file = open(file, 'w+')
    for i in ignore:
        file.write(i)
