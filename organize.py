import os
import shutil

path = input("enter the path of you folder: ")
datainfile = os.listdir(path)

for file in datainfile:
    name,ext = os.path.splitext(file)
    ext = ext[1:]
    if ext == "":
        continue
    if os.path.exists(path+"/"+ext):
        shutil.move(path + "/"+  file , path+"/"+ext+"/"+file)
    else:
        os.makedirs(path+"/"+ext)
        shutil.move(path + "/" + file, path +"/"+ext+"/"+file)