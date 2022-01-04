from typing import Text
import json, requests, pprint
from termcolor import colored
from time import sleep
WelcomeMessage = colored("Welcome to Netease Account Creator V1.0","green")
print(WelcomeMessage)
with open("config.json") as json_file:
    config = json.load(json_file)
FivesimAPIKey = config.get('FiveSimAPIToken')


FivesimAmounthead = {
    'Authorization': 'Bearer ' + FivesimAPIKey,
    'Accept': 'application/json',
}
FivesimAmountResponse = requests.get('https://5sim.net/v1/user/profile', headers=FivesimAmounthead)
output = json.loads(FivesimAmountResponse.content)

print("You have : " + format(output["balance"], 'f') + "₽")
Amount = input("How many Accounts do you want to create ? : ")

country = 'canada' #can change to usa after virtual8 is in stock
operator = 'virtual8'
product = 'other'

headersfivesim = {
    'Authorization': 'Bearer ' + FivesimAPIKey,
    'Accept': 'application/json',
}

fivesimnumber = requests.get('https://5sim.net/v1/user/buy/activation/' + country + '/' + operator + '/' + product, headers=headersfivesim)
fivesimnumberout = json.loads(fivesimnumber.content)





url1 = "https://n.cg.163.com/api/v1/phones-registered/1-6039880154"

payload1 = ""
headers1 = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62'
}



url2 = "https://n.cg.163.com/api/v1/phone-captchas/1-8022090889"

payload2 = "{\"etc\":{\"validate\":\"CN31_I0i9294K1clfEWwMF0kJ5TtvrGq75g5wqGWq4trwP8qhdztex-9xBO6T.okOWDuUIsQxeOdGANrVpjEQTQN490Ka02faPnFrCNMGJGPMa.PdVjN2ps_6Xtv8XH5dz8R2nBD02RabENvzrrodWQDbb_-Udy0VUaihYxJW8CrTatRJXe4Ny4LnISBC5-qmxVq4fm-QGvy9kc5FYA-lz_26OYZJkBgfuU-C2J2eduh4mPqKVB8R8VE9ifmx4EheyCL1odq5a1LXECXt2UudJtfFiWVreTN0XQd5mLliAfQy0C4.UqTQbiwE5erEMqQjPPSxBOqf6j0IXCPcSsbb0X2rGh.L9iIg2kGHxj4KJ097Ch8pa4la0.RWdAAUhZp-SFBoWN4A9uQ_g.M-7DbxXnXjjg5YkC08u_riuOEWGP1e5EzRMGaLGXAbNwHgck666qvuzwnEkdlsYjr5A_i6md25hXtWsjFypln15x_0xPRYTztccvMl_rVv6WAGArN3\"}}"
headers2 = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62',
  'Content-Type': 'text/plain'
}


headers3 = {
    'Authorization': 'Bearer ' + FivesimAPIKey,
    'Accept': 'application/json',
}

payload4 = "{\"auth_method\":\"phone-captcha\",\"ctcode\":\"1\",\"phone\":\"8022090889\",\"captcha\":\"072699\",\"device_info\":{\"userAgent\":\"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/536.36 Edg/96.0.1054.62\",\"appVersion\":\"5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/536.36 Edg/96.0.1054.62\",\"codecs\":[\"vp8\",\"rtx\",\"vp9\",\"vp9\",\"vp9\",\"h264\",\"h264\",\"h264\",\"h264\",\"h264\",\"h264\",\"red\",\"ulpfec\",\"flexfec-03\"]}}"
headers4 = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62',
  'Content-Type': 'text/plain'
}

def acccreate():
  fivesimnumber = requests.get('https://5sim.net/v1/user/buy/activation/' + country + '/' + operator + '/' + product, headers=headersfivesim)
  fivesimnumberout = json.loads(fivesimnumber.content)
  if(len(fivesimnumberout["phone"]) == 0):
      print("5sim not giving numbers :(")
      return
  phonenumber = fivesimnumberout["phone"]  
  purchaseid = fivesimnumberout["id"]
  phonenumber = phonenumber[2:]
  url1 = "https://n.cg.163.com/api/v1/phones-registered/1-" + phonenumber
  response1 = requests.request("GET", url1, headers=headers1, data=payload1)
  sleep(2)   
  url2 = "https://n.cg.163.com/api/v1/phone-captchas/1-" + phonenumber
  response2 = requests.request("POST", url2, headers=headers2, data=payload2)
  print("[-] Waiting sms...")
  for _ in range(15):
    try:
       sleep(10) 
       response3 = requests.get('https://5sim.net/v1/user/check/' + str(purchaseid), headers=headers3)
       response3out = json.loads(response3.content)
       
        
       if response3out["sms"][0]["code"] != type(None):
        smscode = response3out["sms"][0]["code"]
        break
       else:
        sleep(10)    
        response3 = requests.get('https://5sim.net/v1/user/check/' + str(purchaseid), headers=headers3)
        response3out = json.loads(response3.content)
        if response3out["sms"][0]["code"] != type(None):
         smscode = response3out["sms"][0]["code"]
         
         break
        else:
         print("[x] no sms Quiting") 
    except IndexError:
        pass        
  print("[+] Received Sms")     
  x = payload4.replace("8022090889", phonenumber)
  x = x.replace("072699", str(smscode))
  response4 = requests.request("POST", "https://n.cg.163.com/api/v1/tokens", headers=headers4, data=x)
  response4out = json.loads(response4.content)
  if response4out["channel"] != type(None):
   succes =colored("[+] Account Created ["+ phonenumber +"] Code : ["+ smscode+"]","green")
   print(succes)
   with open('Accs.txt', 'a') as the_file:
     the_file.write("[+] Account Created ["+ phonenumber +"] Code : ["+ smscode+"]\n")

for x in range(int(Amount)):
   acccreate()
   sleep(2)

       




un = input("Done All Succesfull Account are saved in Accs.txt\n Press enter to Quit")
exit()






