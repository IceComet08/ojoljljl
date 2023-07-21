import os
import shutil
from_dir = "C:/Users/ferfu/Downloads"
to_dir = "C:/Users/ferfu/OneDrive/Documentos/Arquivos_documentos"
list_of_files = os.listdir(from_dir)
print(list_of_files)
for file_name in list_of_files:
    name, extension = os.path.splitext(file_name)

    if not extension:
        continue
    if extension.lower() in[".text", ".doc", ".docx" , ".pdf"]:
        path1 = os.path.join(from_dir, file_name)
        path2 = os.path.join(to_dir, extension[1:])
        path3 = os.path.join(to_dir, file_name)
        if os.path.exists(path2):
            print("movendo" + file_name + ".....")
            shutil.move(path1, path3)

        else :
            os.makedirs(path2)
            print("Movendo" + file_name + "......") 
            shutil.move(path1, path3)   
