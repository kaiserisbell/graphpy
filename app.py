import os
from random import randint

for i in range(1, 365):
    d = str(i) + ' days ago '
    with open('file.txt', 'a') as file:
        file.write(d)
        os.system('git add .')
        os.system('git commit --date="' + d + '" -m "Commit"')


os.system('git push -u origin main')