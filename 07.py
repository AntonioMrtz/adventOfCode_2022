import logging
import sys


logging.basicConfig(level=logging.DEBUG,format="%(levelname)s - %(funcName)s: %(message)s")

folder_structure={}

class Folder:

    def __init__(self, name):
        self.name = name
        self.folders=[]
        self.files=[]
    
    def addFile(self,file):
        self.files.append(file)

    def addFolder(self,folder):
        self.folders.append(folder)


    def __repr__(self):
        return f"{self.name} \n  {str(self.files)} \n {str(self.folders)}\n\n"  

class File:

    def __init__(self, name, size):
        self.name = name
        self.size = size

    def __repr__(self):
        return f"{self.name}, {self.size} \n"  


def search_parent_folder(folder):
    
    global folder_structure

    #logging.debug(folder_structure.keys())

    for key in folder_structure:

        if folder in folder_structure[key].folders:

            current_folder=key


    return current_folder


def build_path():

    global folder_structure

    archivo = open("inputs/input07.txt")
    #archivo = open("inputs/prueba.txt")

    

    current_folder=""


    while True:
    
        line=archivo.readline()

        if not line:
            break


        line=line.replace("\n","")
        if line.startswith("dir"):

            folder_structure[current_folder].addFolder(line.split(" ")[1])
            continue


        line=line.replace("$","").strip()

        
        
        if line.startswith("cd"):

            if(line.split(" ")[1]==".."):

                current_folder=search_parent_folder(current_folder)

            else:

                
                current_folder=line.split(" ")[1]

                if not current_folder in folder_structure:

                    folder_structure[current_folder]=Folder(current_folder)
            



        elif line!="ls":
            folder_structure[current_folder].addFile(File(line.split(" ")[1],line.split(" ")[0])) 



    return folder_structure




def total_size_folders(folder):

    file_size=0
    folder_size=0

    for f in folder_structure[folder].files:
        file_size+=int(f.size)

    for f in folder_structure[folder].folders:
        folder_size+=total_size_folders(f)


    if file_size+folder_size<=100000:
        return file_size+folder_size

    return 0


def main_v1():

    

    build_path()
    total_size=0
    #logging.debug(folder_structure)
    #logging.debug(len(folder_structure.keys()))
    return sum([total_size_folders(key) for key in folder_structure.keys()])




def main_v2():
    pass



if __name__ == '__main__':
    print(f"part 1 : {main_v1()}", f"part 2 : {main_v2()}")