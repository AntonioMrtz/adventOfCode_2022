import logging


logging.basicConfig(level=logging.DEBUG,format="%(levelname)s - %(funcName)s: %(message)s")


def build_path():

    archivo = open("inputs/input07.txt")

    folder_structure=[]


    while True:
    
        line=archivo.readline()

        if not line:
            break

        #logging.debug(line)

        line=line.replace("$","").strip()

        
        
        if line.startswith("cd"):

            # cd puede volver atras o entrar a directorio
            folder_structure.append(line)


    return folder_structure



def main_v1():
    
    return build_path()





def main_v2():
    pass



if __name__ == '__main__':
    print(f"part 1 : {main_v1()}", f"part 2 : {main_v2()}")