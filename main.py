import requests

def respond():
    print("Name?")
    x=input()
    data=requests.get("https://api.mojang.com/users/profiles/minecraft/{}".format(x)).json()
    print(data['id'])

respond()