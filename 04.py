import logging


logging.basicConfig(level=logging.CRITICAL,format=" %(levelname)s - %(funcName)s: %(message)s")

def main_v1():

    fully_included_ranges=0
    
    for line in open("inputs\input04.txt"):

        first_start=int(line.split(",")[0].split("-")[0])
        first_end=int(line.split(",")[0].split("-")[1])

        second_start=int(line.split(",")[1].split("-")[0])
        second_end=int(line.split(",")[1].split("-")[1])

        if (second_start>=first_start and second_end<= first_end) or (first_start>=second_start and first_end<= second_end):
            logging.debug(line)
            fully_included_ranges+=1

    return fully_included_ranges

def main_v2():

    fully_included_ranges=0
    
    for line in open("inputs\input04.txt"):

        first_start=int(line.split(",")[0].split("-")[0])
        first_end=int(line.split(",")[0].split("-")[1])

        second_start=int(line.split(",")[1].split("-")[0])
        second_end=int(line.split(",")[1].split("-")[1])

        if (second_start>=first_start and second_start<=first_end) or (second_end>=first_start and second_end<=first_end) or (first_start>=second_start and first_start<=second_end) or  (first_end>=second_start and first_end<=second_end):
            logging.debug(line)
            fully_included_ranges+=1

    return fully_included_ranges



if __name__ == '__main__':
    print(f"part 1 : {main_v1()}", f"part 2 : {main_v2()}")