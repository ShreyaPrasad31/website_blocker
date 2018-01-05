import time 
from datetime import datetime as dt 
#Host files can only be edited by the admin ->
#Either run cmd as admin or copy host file and change path 
hosts_path = "hosts"
hosts_path = "C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.0.1" #IP to which it should redirect
website_list = ["https://www.facebook.com/","facebook.com","youtube.com"]

while True:
        
        if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,19):
                print("Wroking hours")
                with open(hosts_path, 'r+') as file:#open to read and write both 
                        content = file.read()
                        for website in website_list:
                                if website in content:
                                        pass
                                else: 
                                        file.write(redirect + " "+ website + "\n")
        else:
                print("RElaxx")
                with open(hosts_path,'r+') as file:
                        content = file.readlines()
                        file.seek(0)
                        for line in content:
                                if not any(website in line for website in website_list):
                                        file.write(line)
                        file.truncate()
                         
                                        
                        
                
        time.sleep(5)        
        

   
           