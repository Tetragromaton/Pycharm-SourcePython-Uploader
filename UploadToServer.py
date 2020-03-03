import os
import ftplib
from valve.rcon import RCON#If you use pycharm, install package by File->Settings->Project Interpeter->Add package->Search Valve rcon

plugin_name_x = "NoDisarmMod"#Your plugin name here

Path_To_Mod = os.path.abspath(os.getcwd())
Path_To_Mod = Path_To_Mod + os.sep + plugin_name_x + ".py"
print(Path_To_Mod)
#Path_ToMod это путь до файла со скриптом который надо залить.

Upload_To_Folder = "/csgo/addons/source-python/plugins/"
ftp_host = "127.0.0.1"
ftp_port = "21"
ftp_login = "server1234"
ftp_password = "1234"

AutoRestart = 1#Плагин сначала загрузит, а потом перезагрузит на всякий случай чтобы тебе лакшери было сразу в игре затестить
#Данные ниже не нужно указываеть если авторестарт плагина вам не нужен.

SERVER_ADDRESS = ("127.0.0.1", 27615)#Укажите IP сервера, затем порт, необязательно если не хотите автоматической перезагрузки
PASSWORD = "1234"


NotFound = 0
print(Upload_To_Folder)

session = ftplib.FTP(ftp_host,ftp_login,ftp_password)
session.cwd(Upload_To_Folder)
session.retrlines('LIST')
if plugin_name_x in session.nlst() :
    print('Plugin already exist in python plugins, queuing future reload of plugin')
else :
    print("Plugin directory not found, plugin will be started ")
    session.mkd(plugin_name_x)
    NotFound = 1


file = open(Path_To_Mod,'rb')
print('STOR '+Upload_To_Folder + plugin_name_x + os.sep + plugin_name_x + '.py')
session.storbinary('STOR '+Upload_To_Folder + plugin_name_x + '/' + plugin_name_x + '.py', file)
file.close()
session.quit()


if AutoRestart > 0:
    print("Sending RCON reload command.")
    with RCON(SERVER_ADDRESS, PASSWORD) as rcon:
        if NotFound == 1:
            rcon("sp plugin load " + plugin_name_x)
        else:
            rcon("sp plugin reload " + plugin_name_x)
    print("Plugin successfully loaded to plugin and restarted.")
