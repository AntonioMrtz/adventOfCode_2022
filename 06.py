import logging

logging.basicConfig(level=logging.DEBUG,format="%(levelname)s - %(funcName)s: %(message)s")

SIZE_SEGMENT_P1=4
SIZE_SEGMENT_P2=14


def main_v1():
    
    line = open("inputs\input06.txt").readline()

    current_segment = []
    current_segment.append(line[0])
    current_segment.append(line[1])
    current_segment.append(line[2])
    current_segment.append(line[3])

    if len(set(current_segment))==SIZE_SEGMENT_P1:
        logging.debug(current_segment)
        return 0

    for i in range(4,len(line)):

        current_segment.pop(0)
        current_segment.append(line[i])

        if len(set(current_segment))==SIZE_SEGMENT_P1:

            return i+1

def main_v2():
    
    line = open("inputs\input06.txt").readline()

    current_segment = []
   
    for i in range(0,14):

        current_segment.append(line[i])


    if len(set(current_segment))==SIZE_SEGMENT_P2:
        logging.debug(current_segment)
        return 0

    for i in range(14,len(line)):

        current_segment.pop(0)
        current_segment.append(line[i])

        if len(set(current_segment))==SIZE_SEGMENT_P2:

            return i+1



if __name__ == '__main__':
    print(f"part 1 : {main_v1()}", f"part 2 : {main_v2()}")