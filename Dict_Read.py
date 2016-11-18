import pickle

f = open('questions.dic', 'rb')
newdic = pickle.load(f)

for key, value in newdic.items():
    print(key, '\t', value)