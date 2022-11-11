from pathlib import Path

# Absolute path
#    starts from the root of the hard disk
#   eg c:/programs/users/...

# relative path:
#   starts from current directory
#   helloworld/working with directories.py

path = Path('ecommerce')
print(path.exists())
path = Path('ecommerce1')
print(path.exists())

# pathh = Path('emails')  # creates directory 'emails' in the relative dir i.e under helloworld
# print(pathh.mkdir())

# pathh = Path('emails')    # deletes the 'emails' dir
# print(pathh.rmdir())


# we can also find all the files in a given path. This is udeful in a praogram to automate something and search a file,
# open them and process them.

curpath = Path()   # Path() with no arguments passed is current path
for file in curpath.glob('*.py'):   # this gives all py files
    print(file)
print("\n")
 # with glob method we can searchand fine files in current path. we need to pass a string to
# define the search pattern and optionally the extension like py or json or xls ,etc ... * means everything

for file in curpath.glob('*'):    # this gives all the directories and files , as no particular file is mentioined.
    print(file)