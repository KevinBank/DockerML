#import libraries
import requests

#request name and return UUID by contacting mojang API
def respond():
    print("Name?")
    x=input()
    data=requests.get("https://api.mojang.com/users/profiles/minecraft/{}".format(x)).json()
    print(data['id'])

#call respond
respond()