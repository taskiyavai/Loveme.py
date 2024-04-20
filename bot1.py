

import base64 
h=open("shellbot.py","r").read().encode("utf-8")
b=base64.b64encode(h)
print(b)
