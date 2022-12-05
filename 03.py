import logging


logging.basicConfig(level=logging.CRITICAL,format="%(levelname)s - %(funcName)s: %(message)s")

def main_v1():

    total_value=0

    for line in open("inputs\input03.txt"):


        repeated_chars=''.join(set(line[:len(line)//2]).intersection(line[len(line)//2:]))

        for char in repeated_chars:

            if char.islower():

                total_value+=ord(char)-96

            elif char.isupper():

                total_value+=ord(char)-65+27
        
        logging.debug(total_value)

    return total_value



def main_v2():
    
    total_value=0
    number_lines = len(open("inputs\input03.txt").readlines())

    archivo=open("inputs\input03.txt")

    for i in range(0,number_lines,3):

        

        repeated_chars=''.join(set(archivo.readline()).intersection(archivo.readline()))
        repeated_chars=''.join(set(archivo.readline()).intersection(repeated_chars))

        for char in repeated_chars:

            if char.islower():

                total_value+=ord(char)-96

            elif char.isupper():

                total_value+=ord(char)-65+27
        
        logging.debug(total_value)

    return total_value



if __name__ == '__main__':
    print(f"part 1 : {main_v1()}", f"part 2 : {main_v2()}")