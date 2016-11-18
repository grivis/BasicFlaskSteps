import pickle

f = open('swadesh.dic', 'rb')
newdic = pickle.load(f)

for key, value in newdic.items():
    print(key, '\t', value)