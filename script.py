import telepot,time,subprocess,os
from telepot.loop import MessageLoop
from cfg import *
bot = telepot.Bot(bot_id)
def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    name = msg["from"]["first_name"]
    if chat_id == admin:
        if (content_type == 'text'):
            command = msg['text']       
            print ('Got command: %s' % command)
            if  '/clean' in command:
                p = subprocess.Popen(cmd1, shell=True)
                bot.sendMessage(chat_id, os.getenv("computername")+"is executing Security Protocol!")
            if  '/erase' in command:
                p = subprocess.Popen(cmd2, shell=True)
                bot.sendMessage(chat_id, os.getenv("computername")+" is executing CCleaner.")
            if  '/restore' in command:
                p = subprocess.Popen(cmd3, shell=True)
                bot.sendMessage(chat_id, os.getenv("computername")+" is restoring.")       
            if  '/shutdown' in command:
                p = subprocess.Popen(cmd4, shell=True)
                bot.sendMessage(chat_id, os.getenv("computername")+" is shutting down in 5 seconds.")
            if  '/reboot' in command:
                p = subprocess.Popen(cmd5, shell=True)
                bot.sendMessage(chat_id, os.getenv("computername")+" is going to reboot in 5 seconds.")
            if  '/status' in command:
                p = subprocess.Popen(cmd6, shell=True)
                bot.sendMessage(chat_id,cmd6)    
            if  '/version' in command:
                p = subprocess.Popen(cmd7, shell=True)
                bot.sendMessage(chat_id,cmd7)                               
    else:   
        bot.sendMessage(chat_id,"Sorry, {}, I can't help you :(".format(name))            
bot.sendMessage(admin,os.getenv("computername")+" are online.")
cmd1 = ('rmdir "%Public%\\Desktop\\" /s /q &\
        rmdir "%APPDATA%\\Microsoft\\Windows\\Recent\\" /s /q &\
        rmdir "%APPDATA%\\Microsoft\\Windows\\Recent\\AutomaticDestinations\\" /s /q &\
        rmdir "%APPDATA%\\Microsoft\\Windows\\Recent\\CustomDestinations\\" /s /q &\
        rmdir "%TMP%" /s /q &\
        rmdir "%TEMP%" /s /q &\
        rmdir "%APPDATA%\\Mozilla\\" /s /q &\
        mkdir "%Public%\\Desktop\\" &\
        mkdir "%TMP%" &\
        mkdir "%TEMP%" &\
        reg delete HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\TypedPaths /f &\
        reg delete HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Office\ /f &\
        reg add HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\TypedPaths /f &\
        taskkill -im explorer.exe -f')
cmd2 = '"c:\Program Files\CCleaner\CCleaner.exe" /AUTO'
cmd3 = ('net use Z: \\\\192.168.1.5\\_shared_folder /user:_username_ PASSWORD /P:Yes')
cmd4 = "shutdown -s -f -t 5"
cmd5 = "shutdown -r -f -t 5"
cmd6 = os.getenv("computername") + " waiting for the instructions."
cmd7 = version
MessageLoop(bot, handle).run_as_thread()
while 1:
    time.sleep(10)
