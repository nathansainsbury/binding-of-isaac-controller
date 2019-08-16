import subprocess 
from pywinauto.application import Application

file_path = 'C:\Program Files (x86)\Steam\steamapps\common\The Binding of Isaac Rebirth\isaac-ng.exe' 
app = Application().start(file_path)
#process = subprocess.Popen([file_path])


#%%