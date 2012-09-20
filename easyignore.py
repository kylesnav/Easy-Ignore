import os

repo = '/Users/kylesnav/Documents/Easy-Ignore' #the local location of your git repo.
ignore = ['.DS_Store', '', ''] # add more as needed, it's a list.
file = '.gitignore' # do not change this value.

os.chdir(repo)

if os.path.exists(file):
    file = open(file, 'a+')
else:
    file = open(file, 'w+')
    
for i in ignore:
    # add check to see if file is in the .gitignore.
    file.write(i + '\n')
    