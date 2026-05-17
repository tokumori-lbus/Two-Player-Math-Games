#Two Player Games
import random
cont = True
class Player:
    def __init__(self, name, points, status, objects):
        self.name = name
        self.points = points
        self.status = status
        self.objects = objects
    def turns(self):
        self.status = not self.status
    def winner(self):
        self.points += 1
        print(self.name, "wins")
    def update(self):
        print(self.name, ":", self.points,"points")
    def compile(self, value):
        self.objects += value
    def judgement(self):
        print(f"{self.name}'s collected objects:", self.objects)
       
def random_num(play1, play2, mini, maxi):
    formula = 67 * (len(play1.name) * len(play2.name) + play1.points + play2.points) + play1.objects - play2.objects
    random.seed(formula)
    return random.randint(mini, maxi)

# Game 1
def basic_takeaway(play1,play2):
    print("Select number from 1-4 to reach a sum of 17, last one to input wins")
    total = 0
    while total < 17:
        if play1.status == True:
            total = takeaway_algo(play1,total)
        elif play2.status == True:
            total = takeaway_algo(play2,total)
        play1.turns()
        play2.turns()
    if play1.status == False:
        play1.winner()
    else:
        play2.winner()
    ultraupdate(play1,play2)
    
def takeaway_algo(player,tot):
    accepted_inputs = {1,2,3,4}
    nummy = None
    while nummy == None:
        try:
            print("Current Number:", tot)
            nummy = input_taker(player.name, accepted_inputs)
        except ValueError:
            print ("Number must be 1 to 4")
        except TypeError:
            print("Invalid input. Try again.")
    tot += nummy
    return tot

# Game 2
def penny_lane(play1, play2):
    print("Start will 100 pennies. Each player can remove a divisor of the number of pennies remaining as long as the divisor is strictly less than the number of pennies remaining.")
    remaining = 100
    while remaining > 1:
        if play1.status == True:
            remaining = pennyl_algo(play1,remaining)
        elif play2.status == True:
            remaining = pennyl_algo(play2,remaining)
        play1.turns()
        play2.turns()
    if play1.status == False:
        play1.winner()
    else:
        play2.winner()
    ultraupdate(play1,play2)

def pennyl_algo(player, rem):
    miao = [num for num in range(1, int(round(rem**0.5)+1)) if rem % num == 0]
    miao = miao + sorted([rem//num for num in miao if num != 1])
    miao = list(dict.fromkeys(miao))
    print("Possible numbers:", miao)
    nummy = None
    while nummy == None:
        try:
            print("Current Number:",rem)
            nummy = input_taker(player.name, miao)
        except ValueError:
            print ("Number must be a divisor of the remainder")
        except TypeError:
            print("Invalid input. Try again.")
    player.compile(nummy)
    rem = rem - nummy
    return rem

# Game 3
def greedy_penny(play1, play2, remaining):
    numby = remaining
    print("Start with some pennies. The first player can take any positive number away as long as he or she doesn't take away all the pennies. However the next person can only take what is less of what you took")
    while remaining > 1:
        if play1.status == True:
            sysnums = gpenny_algo(play1, remaining, numby)
            remaining = sysnums.get("rema")
            numby = sysnums.get("num")
        elif play2.status == True:
            sysnums = gpenny_algo(play2, remaining, numby)
            remaining = sysnums.get("rema")
            numby = sysnums.get("num")
        play1.turns()
        play2.turns()
    if play1.status == True:
        play1.winner()
    else:
        play2.winner()
    ultraupdate(play1,play2)

def gpenny_algo(player, rem, num):
   miao = [x for x in range(1, num)]
   nummy = None
   while nummy == None:
        try:
            print("Current Number:",rem)
            nummy = input_taker(player.name, miao)
        except ValueError:
            print ("Number must be within range")
        except TypeError:
            print("Invalid input. Try again.")
   player.compile(nummy)
   rem = rem - nummy
   dobol = {"rema":rem, "num":nummy}
   return dobol

# Game 4 (nimskull)

def nim_game(play1, play2, array):
    stacks = array
    while stacks != [0 for k in range(len(stacks))]:
        if play1.status == True:
            stacks = nim_algo(play1, stacks)
        elif play2.status == True:
            stacks = nim_algo(play2, stacks)
        play1.turns()
        play2.turns()
    if play1.status == False:
        play1.winner()
    else:
        play2.winner()
    ultraupdate(play1,play2)

def nim_algo(player, stack):
    nummy_index = None
    nummy_take = None
    while nummy_index == None:
        try:
            print("Current Stack: ", stack)
            nummy_index = input_taker(f"{player.name}'s index",[x + 1 for x in range(len(stack)) if stack[x] != 0])
        except ValueError:
            print ("Number must be within range")
        except TypeError:
            print("Invalid input. Try again.")
    while nummy_take == None:
        try:
            nummy_take = input_taker(f"{player.name}'s number",[x + 1 for x in range(stack[nummy_index - 1])])
        except ValueError:
            print ("Number must be within range")
        except TypeError:
            print("Invalid input. Try again.")
    player.compile(nummy_take)
    stack[nummy_index - 1] -= nummy_take
    return stack

def array_generator (biggy, partition):
    mathy = sorted(random.sample(range(1,biggy-1),partition-1) + [0, biggy])
    return [mathy[j+1]-mathy[j] for j in range(len(mathy)-1) if [mathy[j+1]-mathy[j]] != 0]

def final_judgement(p1,p2):
    p1.judgement()
    p2.judgement()
    if p1.objects > p2.objects:
        print(p1.name,"is a greedy conqueror")
    elif p1.objects == p2.objects:
        print("You're both equally greedy :P")
    else:
        print(p2.name,"is a greedy conqueror")


def ultraupdate(p1,p2):
    p1.update()
    p2.update()
    
def input_taker(name, acceptable):
    number = int(input(f"{name}: "))
    if number in acceptable:
        return number
    elif type(number) != int:
        raise TypeError
    else:
        raise ValueError

p1 = Player(input("What is player 1's name? "), 0, True, 0)
p2 = Player(input("What is player 2's name? "), 0, False, 0)

while cont == True:
    state = None
    while state == None:
        try:
            state = int(input("What game do you wanna play? (0, 1, 2, 3, 4, 5, 6, 7; where 0 means cancel): "))
            match state:
                case 0:
                    print("Final Score:")
                    ultraupdate(p1,p2)
                    print("Judgement Day:")
                    final_judgement(p1,p2)
                    cont = False
                case 1:
                    basic_takeaway(p1,p2)
                case 2:
                    penny_lane(p1,p2)
                case 3:
                    numper = input_taker("Selected Number", [x for x in range(15, 501)])
                    greedy_penny(p1,p2,numper)
                case 4:
                    greedy_penny(p1,p2,random_num(p1,p2,15,500))
                case 5:
                    big_num = input_taker("What number are we going to split? ", [x for x in range(15, 501)])
                    divide_num = input_taker("How many stacks are we going to divide it into? ", [x for x in range(big_num)])
                    nim_game(p1, p2, array_generator(big_num, divide_num))
                case 6:
                    big_num = random_num(p1,p2,15,500)
                    divide_num = input_taker("How many stacks are we going to divide it into? ", [x for x in range(big_num)])
                    nim_game(p1, p2, array_generator(big_num, divide_num))
                case 7:
                    big_num = random_num(p1,p2,15,500)
                    divide_num = random_num(p1,p2,2,27)
                    nim_game(p1, p2, array_generator(big_num, divide_num))
                case _:
                    if state not in range(8):
                        raise ValueError
                    else:
                        raise TypeError
        except TypeError:
            print("Invalid input. Try again.")
        except ValueError:
            print("Not in range")