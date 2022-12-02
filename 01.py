


def main_v1():
    
    archivo = open("inputs/input01.txt")

    top_calories=[]
    
    calories=0
    max_calories=0

    while True:
    
        line=archivo.readline()

        if not line:
            break

        if line=="\n":
            if calories > max_calories:
                max_calories=calories
            calories=0

        else:
            calories+=int(line)


    return max_calories


def main_v2():
    
    archivo = open("inputs/input01.txt")

    top_calories=[]
    
    calories=0

    while True:
    
        line=archivo.readline()

        if not line:
            break

        if line=="\n":

            if len(top_calories)==3 and (calories > top_calories[0] or calories > top_calories[1] or calories > top_calories[2]):
                    top_calories.sort(reverse=True)
                    top_calories.remove(top_calories[-1])
                    top_calories.append(calories)

            elif len(top_calories)<3:
                top_calories.append(calories)
            

            
            calories=0

        else:
            calories+=int(line)

    #print(top_calories)
    return sum(top_calories)


if __name__ == '__main__':
    print(f"part 1 : {main_v1()}", f"part 2 : {main_v2()}")