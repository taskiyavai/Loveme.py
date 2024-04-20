import base64
file=open("virus.py","r").read().encode("utf-8")

heron=base64.b64encode(file)

print(heron)
