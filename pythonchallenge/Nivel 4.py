import requests
import re
nothing = 12345
while True:
    t = requests.get(f"http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={nothing}").text
    nothing = ''.join(re.findall("[0-9]", t))
    print(t)
#RESPOTA: peak.html


