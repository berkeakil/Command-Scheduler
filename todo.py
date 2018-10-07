import os
import sys
from datetime import datetime

print("""
 /$$      /$$                       /$$         /$$             /$$                                                
| $$  /$ | $$                      |__/        | $$            | $$                                                
| $$ /$$$| $$        /$$$$$$        /$$       /$$$$$$         /$$$$$$          /$$$$$$        /$$$$$$$             
| $$/$$ $$ $$       /$$__  $$      | $$      |_  $$_/        |_  $$_/         /$$__  $$      | $$__  $$            
| $$$$_  $$$$      | $$  \__/      | $$        | $$            | $$          | $$$$$$$$      | $$  \ $$            
| $$$/ \  $$$      | $$            | $$        | $$ /$$        | $$ /$$      | $$_____/      | $$  | $$            
| $$/   \  $$      | $$            | $$        |  $$$$/        |  $$$$/      |  $$$$$$$      | $$  | $$            
|/       \__/      |__/            |__/         \___/           \___/         \_______/      |__/  |__/            

|/$$$$$$$
| $$__  $$                                                                                                         
| $$  \ $$       /$$   /$$                                                                                         
| $$$$$$$       | $$  | $$                                                                                         
| $$__  $$      | $$  | $$                                                                                         
| $$  \ $$      | $$  | $$                                                                                         
| $$$$$$$/      |  $$$$$$$                                                                                         
|_______/        \____  $$                                                                                         
                 /$$  | $$                                                                                         
                |___$$$$$/                                                                                         
                 
                 
 /$$   /$$       /$$$$$$$        /$$   /$$        /$$$$$$        /$$   /$$                                         
| $$  /$$/      | $$__  $$      | $$  | $$       /$$__  $$      | $$  /$$/                                         
| $$ /$$/       | $$  \ $$      | $$  | $$      | $$  \__/      | $$ /$$/                                          
| $$$$$/        | $$$$$$$/      | $$$$$$$$      | $$            | $$$$$/                                           
| $$  $$        | $$__  $$      |_____  $$      | $$            | $$  $$                                           
| $$\  $$       | $$  \ $$            | $$      | $$    $$      | $$\  $$                                          
| $$ \  $$      | $$  | $$            | $$      |  $$$$$$/      | $$ \  $$                                         
|__/  \__/      |__/  |__/            |__/       \______/       |__/  \__/                                         
                                                                                                                                                          
""")

#This script executes the command right on the time that you desire.
#To begin enter the desired time.

##################################################################
time=datetime.now().strftime('%H:%M')
##################################################################
if len(sys.argv) <= 2:
    print ("""  
Usage   ---> python todo.py ['time'] ['command']
Example ---> python todo.py '02:00' 'cat //etc/passwd'
Be Caution To The Single Quotes!!!
    """)
    exit()
##################################################################
desired_time =sys.argv[1]
cmd=sys.argv[2]
str(desired_time)
str(cmd)
time=time.replace(':','')
hour=time[0]+time[1]
minute=time[2]+time[3]
desired_time=desired_time.replace(':','')
h=desired_time[0]+desired_time[1]
m=desired_time[2]+desired_time[3]
##################################################################
if(desired_time<=time<="2400"):

    hour=24-int(hour)
    m=int(m)+(int(h)*60)
    minute=(int(hour)*60)-int(minute)+m

elif("0000"<=time<=desired_time):
    
    m=int(m)+(int(h)*60)
    minute=(int(hour)*60)+int(minute)
    minute=m-minute
##################################################################
print("Todo List Will be executed after "+ str(minute)+" minute")
os.system('sleep '+str(minute*60))
os.system(cmd)

