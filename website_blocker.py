import time
from datetime import datetime as dt
hosts_temp='hosts'
hosts_path=r"C:\Windows\System32\drivers\etc\hosts"    


redirect="192.168.0.106" #IP address of your computer
     
web_list=["www.facebook.com","facebook.com","dub119.mail.live.com","www.dub119.mail.live.com"] #list presents the host name which website you want to block
while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8) <dt.now() <dt(dt.now().year,dt.now().month,dt.now().day,16):
        #dt.now().year=return year,dt.now().month=return month,dt.now().day=return current date and 16=current time
        print("Working Hours.....")
        with open(hosts_path,'r+') as file:
            content=file.read() #content has the copy of the host file text
            print(content)
            for web in web_list:
                if web in content:
                    pass
                else:
                    file.write(redirect+" "+ web +'\n')

            
    else:
        with open(hosts_path,'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(web in line for web in web_list):
                    file.write(line)
            file.truncate()
        print("Fun Hours.....")
    time.sleep(5)
    

    