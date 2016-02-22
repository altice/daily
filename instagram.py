import os
from os import path


path = "/"
dirs = os.listdir( path )

for file in dirs:
   print file





def rename_files(file_name):
    index = file_name.find('?')  
    return file_name[0:index]



file_name = '12555897_767448723359314_1048860564_n.jpg?ig_cache_key=MTE1OTcyNDk5OTUyMDM1MDM3MQ%3D%3D.2.c'









