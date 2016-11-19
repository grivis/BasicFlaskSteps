import pickle
import os, glob
os.chdir("./")
count = 0
for file in glob.glob("swdic*.dic"):
        count = count + 1
        f = open(file, 'rb')
        print('---', file, '---' )
        newdic = pickle.load(f)
        for key, value in newdic.items():
            print(key, '\t', value)

print('-------\nИтого найдено', count, 'анкет\n-------')