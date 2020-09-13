import os
import re

# 1. 获取一个要重命名的文件夹的名字
folder_name = r'E:\笑傲江湖'

# 2. 获取那个文件夹中所有的文件名字
file_names = os.listdir(folder_name)


for name in file_names:
    print(name)
    matchObj = re.match( r'(.*)\.mp3', name, re.M|re.I)
    newName = matchObj.group(1)
  
    old_file_name = folder_name + "/" + name
    new_file_name = folder_name + "/"  + newName
    os.rename(old_file_name, new_file_name)
   