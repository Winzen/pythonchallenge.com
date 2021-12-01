from urllib.request import urlopen
import pickle

f = ''
link = pickle.load(urlopen("http://www.pythonchallenge.com/pc/def/banner.p"))
for t in link:
    for x, y in t:
        f += x*y
    f += '\n'
print(f)

#Respota: channel