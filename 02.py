

POINTS_ROCK=1
POINTS_PAPER=2
POINTS_SCISSORS=3

POINTS_WIN=6
POINTS_DRAW=3
POINTS_LOSE=0

points_per_election={

    "X":POINTS_ROCK,
    "Y":POINTS_PAPER,
    "Z":POINTS_SCISSORS,

}

translate_election={

    "A":"X",
    "B":"Y",
    "C":"Z",

}

translate_outcome={

    "X":POINTS_LOSE,
    "Y":POINTS_DRAW,
    "Z":POINTS_WIN,
}

def check_outcome(enemy,you):


    if you==translate_election[enemy]:
        return POINTS_DRAW

    if (you=="X" and enemy=="B") or (you=="Y" and enemy=="C") or (you=="Z" and enemy=="A"):
        return POINTS_LOSE

    return POINTS_WIN


def main_v1():

    total_points=0
    
    for line in open("inputs/input02.txt"):
        enemy,you = line.split()[0],line.split()[1]

        total_points+=points_per_election[you]+check_outcome(enemy,you)
        #print(total_points)

    return total_points





def check_outcome_p2(enemy,you):

    if you=="Y":
        #print(list(translate_election.keys())[list(translate_election.values()).index(enemy)])
        return points_per_election[translate_election[enemy]]   #return points_per_election[translate_election.keys()[translate_election.values().index(enemy)]]

    
    if you=="X":

        if enemy=="A":
            return points_per_election["Z"]

        elif enemy=="C":
            return points_per_election["Y"]

        elif enemy=="B":
            return points_per_election["X"]
    
    if enemy=="A":
            return points_per_election["Y"]

    elif enemy=="C":
        return points_per_election["X"]

    elif enemy=="B":
        return points_per_election["Z"]





def main_v2():
    
    total_points=0
    
    for line in open("inputs/input02.txt"):
        enemy,you = line.split()[0],line.split()[1]

        total_points+=translate_outcome[you]+check_outcome_p2(enemy,you)
        #print(total_points)

    return total_points



if __name__ == '__main__':
    print(f"part 1 : {main_v1()}", f"part 2 : {main_v2()}")