import logging
from collections import defaultdict

logging.basicConfig(level=logging.CRITICAL,format="%(levelname)s - %(funcName)s: %(message)s")


moves=[]

def read_input() -> defaultdict:

    global moves

    stack_map=defaultdict(lambda:[])
    stack_map.clear()

    moves=[]
    stacks=[]
    num_stacks=0
    moves_flag=0

    for line in open("inputs\input05.txt"):

        if moves_flag==0:

            if line.startswith(" 1"):
                num_stacks=int(line[-3])
                moves_flag=1
                continue

            stacks.append(line.replace("\n",""))

        elif line!="\n" and moves_flag==1:

            moves.append(line.replace("\n",""))

    
    for line in reversed(stacks):

        stack=1
        for i in range(1,num_stacks*4-2,4):
            
            if line[i]!=" ":
                stack_map[stack].append(line[i])
            
            stack+=1

    #logging.critical(stack_map)

    return stack_map



def make_move(amount,src,dst,flag,stack_map) -> None:
    
    if flag==0:

        stack_map[dst].extend(reversed(stack_map[src][-amount:]))
    else:
        stack_map[dst].extend(stack_map[src][-amount:])

    stack_map[src]=stack_map[src][0:len(stack_map[src])-amount]

    


def main_v1() -> defaultdict:
    
    stack_map=read_input()

    for move in moves:
        make_move(int(move.split("from")[0].replace("move ","")),int(move.split("from")[1].split("to")[0]),int(move.split("to")[1]),0,stack_map)

    return stack_map

def main_v2():


    stack_map=read_input()

    for move in moves:
        make_move(int(move.split("from")[0].replace("move ","")),int(move.split("from")[1].split("to")[0]),int(move.split("to")[1]),1,stack_map)

    return stack_map



if __name__ == '__main__':
    print(f"part 1 : {main_v1()}", f"part 2 : {main_v2()}")