from tkinter import *

root = Tk()

#Create the players & teams
#Card Baseball GUI Impl
import random as r
import names as n
from functools import partial

class Player:
    def __init__(self, AVG, Singles, Doubles, Triples, HRs, Steals, Name=""):
        self.avg = AVG
        self.singles = Singles
        self.doubles = Doubles
        self.triples = Triples
        self.hrs = HRs
        self.steals = Steals
        self.name = Name

    def __str__(self):
        return self.name + ": " + str(self.avg) + " AVG " + \
               str(self.hrs) + " HRs"

    def __repr__(self):
        return self.name + ": " + str(self.avg) + " AVG " + \
               str(self.hrs) + " HRs"

def createPlayer():
    return Player(float(r.randrange(175, 326)/1000),
                  r.randrange(0,161),
                  r.randrange(0,60),
                  r.randrange(0,11),
                  r.randrange(0,54),
                  r.randrange(0,72),
                  r.choice(n.names))


# create the board background
canv = Canvas(root, width=1300, height=1500, bg='grey')
canv.grid(row=2, column=3)
img = PhotoImage(file="C://Users//denni//Pictures//field.png")
canv.create_image(20, 20, anchor=NW, image=img)

#Card Baseball Console-Based Impl
import random as r
import names as n

class Player:
    def __init__(self, AVG, Singles, Doubles, Triples, HRs, Steals, Name=""):
        self.avg = AVG
        self.singles = Singles
        self.doubles = Doubles
        self.triples = Triples
        self.hrs = HRs
        self.steals = Steals
        self.name = Name

    def __str__(self):
        return self.name + ": " + str(self.avg) + " AVG " + \
               str(self.hrs) + " HRs"

    def __repr__(self):
        return self.name + ": " + str(self.avg) + " AVG " + \
               str(self.hrs) + " HRs"

def createPlayer():
    return Player(float(r.randrange(175, 326)/1000),
                  r.randrange(0,161),
                  r.randrange(0,60),
                  r.randrange(0,11),
                  r.randrange(0,54),
                  r.randrange(0,72),
                  r.choice(n.names))

#init dice outcomes
def init_grid():
    global grid
    grid[0] = ['Triple Plus', 'Double Plus', 'Out', 'Hit', 'Out', 'Out', 'Hit', 'Out', 'Strike Out', 'Walk', 'Home Run Plus']
    grid[1] = ['Triple Plus', 'Out', 'Hit', 'Out', 'Out', 'Hit', 'Out', 'Out', 'Hit', 'Strike Out', 'Home Run Plus']
    grid[2] = ['Double Plus', 'Hit', 'Strike Out', 'Out', 'Hit', 'Out', 'Out', 'Hit', 'Out','Double Plus', 'Home Run Plus']
    grid[3] = ['Double Plus', 'Hit', 'Out', 'Hit', 'Out', 'Out', 'Hit', 'Out', 'Out', 'Double Plus', 'Home Run Plus']
    grid[4] = ['Triple Plus', 'Out', 'Hit', 'Out', 'Out', 'Hit', 'Out', 'Out', 'Walk', 'Strike Out', 'Home Run Plus']
    grid[5] = ['Triple Plus', 'Double Plus', 'Out', 'Out', 'Hit', 'Out', 'Out', 'Hit', 'Out', 'Hit', 'Home Run Plus']

#init hit card deck
def init_hitDeck():
    global hitDeck
    i=0
    while i < 4:
        hitDeck.append('Double Plus')
        i += 1
    j = 0
    while j < 3:
        hitDeck.append('Triple Plus')
        hitDeck.append('Home Run Plus')
        j += 1
    avgs = [.2,.205,.210,.215,.22,.225,.230,.230,.235,.235,.240,.240,.245,.245,
            .250,.250,.255,.255,.260,.265,.265,.270,.270,.275,.280,.285,.290,.295,.300]
    for avg in avgs:
        hitDeck.append(str(avg))
    return hitDeck

#init out card deck
def init_outDeck():
    global outDeck
    outDeck = []
    outDeck.append("Strike Out")
    i=0
    while i<6:
        outDeck.append("Ground Out. Runners hold.")
        outDeck.append("Fly Out. Runners hold.")
        i+=1
    i=0
    while i<5:
        outDeck.append("Pop Out. Runners hold.")
        i+=1
    i=0
    while i< 3:
        outDeck.append("Fly Out. (Potential lead runner advance)")
        outDeck.append("Ground Out. Runners advance 1 base")
        outDeck.append("Fly Out. Runners advance 1 base")
        i += 1
    outDeck.append("Double Play")
    outDeck.append("Double Play Maybe. 5")
    outDeck.append("Double Play Maybe. 10")
    outDeck.append("Double Play Maybe. 15")
    outDeck.append("Double Play Maybe. 20")
    outDeck.append("Double Play Maybe. 25")
    outDeck.append("Out. Potential Injury")
    outDeck.append("Draw a Plus Card,Hit By Pitch,10")
    outDeck.append("Draw a Plus Card,Infield Hit,20")
    outDeck.append("Draw a Plus Card,Bunt,20")
    outDeck.append("Draw a Plus Card,Safe on Error,15")
    outDeck.append("Draw a Plus Card,Safe on Error,15")
    outDeck.append("Draw a Plus Card,Safe on Error,15")
    return outDeck

#initalize all decks
#init decks
global plus_cards
plus_cards = list(range(41))

global hitDeck
hitDeck = []
hitDeck = init_hitDeck()

global outDeck
outDeck = init_outDeck()

def draw_hitDeck(batter,teamName, outs_this_inning):
    global hitDeck
    if len(hitDeck) == 0:
        init_hitDeck()
    card = r.choice(hitDeck)
    hitDeck.remove(card)
    if card == "Home Run Plus":
        homeRunPlus(batter,teamName)
    elif card == "Triple Plus":
        triplePlus(batter,teamName)
    elif card == "Double Plus":
        doublePlus(batter,teamName)
    else:
        card = float(card)
        if batter.avg  >=  card:
            single(batter,teamName)
        else:
            return draw_outDeck(batter,teamName, outs_this_inning)
    return 0


def draw_outDeck(batter,teamName, outs):
    global game_details
    global outDeck

    if len(outDeck) == 0:
        init_outDeck()
    card = r.choice(outDeck)
    outDeck.remove(card)
    n_outs = 0
    if card == "Ground Out. Runners hold." or card == "Fly Out. Runners hold." or card == "Pop Out. Runners hold.":
        print("Out")
        n_outs = 1
    elif card == "Fly Out. (Potential lead runner advance)":
        if outs < 2:
            print("Fly Out. (Potential lead runner advance)")
            lead_runner_advance_option(teamName)
        else:
            print('Fly Out.')
        n_outs = 1
    elif card == "Ground Out. Runners advance 1 base" or card  ==  "Fly Out. Runners advance 1 base":
        if outs < 2:
            print('Out. Runners advance 1 base')
            all_runners_advance(teamName)
        else:
            print('Out')
        n_outs = 1
    elif card == "Double Play":
        if outs == 0:
            n_outs = double_play(batter, teamName)
        else:
            print("Double Play")  #No reason to call else. bases will clear at end of inning

    elif "Double Play Maybe" in card:
        steals = int(card.split(".")[1])
        n_outs = double_play_maybe(batter,teamName, steals)
    elif card == "Out. Potential Injury":
        print("Out. Potential Injury")
        n_outs = 1
        plus = draw_plus()
        if plus <= 20: #hurt
            substitution(batter, teamName)
        else:
            print('He is ok!')
    elif card == "Strike Out":
        print("Strike Out")
        n_outs = 1
    elif "Draw a Plus Card" in card:
        parts = card.split(',')
        plus = draw_plus()
        play = parts[1]
        if plus <= int(parts[2]):
            print(batter.name, 'reaches first on', play)
            if play == 'Hit By Pitch':
                hit_by_pitch(batter, teamName)
            elif play == 'Infield Hit' or play == 'Bunt':
                single(batter, teamName)
            elif play == 'Safe on Error':
                single(batter, teamName)
            else:
                print(play)
                print("This should not happen!")
        else:
            if play == 'Hit By Pitch':
                print("Strike Out")
            elif play == 'Infield Hit' or play == 'Bunt':
                if outs < 2:
                    print("Out. Runners advance")
                    all_runners_advance(teamName)
                else:
                    print("Out") #todo do you draw an out card?
            elif play == 'Safe on Error':
                print("Out") #todo do you draw an out card?
                pass #runners hold, 1 out
            else:
                print(play)
                print("This should not happen!")
            n_outs = 1
    return n_outs

def hit_by_pitch(batter, teamName):
    global game_details
    runner1 = game_details[teamName]['1B']
    runner2 = game_details[teamName]['2B']
    runner3 = game_details[teamName]['3B']
    if runner1 is None:
        game_details[teamName]['1B'] = batter
    else:
        if runner2 is None:
            game_details[teamName]['2B'] = runner1
            game_details[teamName]['1B'] = batter
        else:
            if runner3 is None:
                game_details[teamName]['3B'] = runner2
                game_details[teamName]['2B'] = runner1
                game_details[teamName]['1B'] = batter
            else:
                game_details[teamName]['runs'] = game_details[teamName]['runs'] + 1 #run scores
                print("Runner", runner3.name, "scores on a hit by pitch!")
                print('The score is', game_details['Home']['runs'],'-',game_details['Away']['runs'])
                game_details[teamName]['3B'] = runner2
                game_details[teamName]['2B'] = runner1
                game_details[teamName]['1B'] = batter

def substitution(batter, teamName):
    global game_details
    lineup = game_details[teamName]['lineup']
    bench = game_details[teamName]['bench']
    i = lineup.index(batter)
    lineup[i] = bench[0]
    bench = bench[1:]
    print(batter.name,'has been subbed out for', lineup[i].name)

def double_play_maybe(batter, teamName, steals):
    global game_details
    runner1 = game_details[teamName]['1B']
    if not (runner1 is None):
        game_details[teamName]['1B'] = None #runner on 1st forced out at 2B
        n_outs = 1
        if batter.steals >= steals:
            print("Force out at 2nd. Safe at first!")
            game_details[teamName]['1B'] = batter # safe
        else:
            print("Double play!")
            n_outs+=1 #out
    else:
        print("Out at first")
        n_outs = 1
    return n_outs

def double_play(batter, teamName):
    global game_details
    runner1 = game_details[teamName]['1B']
    runner2 = game_details[teamName]['2B']
    runner3 = game_details[teamName]['3B']
    runners = [runner1, runner2, runner3, batter]
    n_outs = 0 #init
    runners2 = []
    for runner in runners:
        if runner is None:
            pass
        else:
            runners2.append(runner)
    #choose a random 2 runners in this scenario
    if len(runners2) >= 2:
        print('Double Play!')
        n_outs = 2 #double play ensured
        out1 = r.choice(runners2)
        runners2.remove(out1)
        out2 = r.choice(runners2)
        if runner3 != out1 and runner3 != out2 and not (runner3 is None):
            print(runner3.name, 'scores on a double play!')
            print('The score is', game_details['Home']['runs'],'-',game_details['Away']['runs'])
            game_details[teamName]['runs'] = game_details[teamName]['runs'] + 1
            game_details[teamName]['3B'] = None
        else:
            if runner3 == out1 or runner3 == out2:
                print(runner3.name, 'is out heading to home!')
                game_details[teamName]['3B'] = None
        if runner2 != out1 and runner2 != out2 and not (runner2 is None):
            print(runner2.name, "advances to 3B on a double play!")
            game_details[teamName]['3B'] = runner2
            game_details[teamName]['2B'] = None
        else:
            if runner2 == out1 or runner2 == out2:
                print(runner2.name, 'is out heading to 3B!')
                game_details[teamName]['2B'] = None
        if runner1 != out1 and runner1 != out2 and not (runner1 is None):
            game_details[teamName]['2B'] = runner1
            game_details[teamName]['1B'] = None
            print(runner1.name, "advances to 2B on a double play!")
        else:
            if runner1 == out1 or runner1 == out2:
                print(runner1.name, 'is out heading to 2B!')
                game_details[teamName]['1B'] = None
        if batter != out1 and batter != out2 and not (batter is None):
            print(batter.name, 'is out at 1B!')
            game_details[teamName]['1B'] = batter
        else:
            pass
    else:
        print("Out at first")
        n_outs = 1 #only the batter is out
    return n_outs

def all_runners_advance(teamName):
    runner3 = game_details[teamName]['3B']
    runner2 = game_details[teamName]['2B']
    runner1 = game_details[teamName]['1B']
    if not (runner3 is None):
        print(runner3.name,'scored from 3B!')
        print('The score is', game_details['Home']['runs'],'-',game_details['Away']['runs'])
        game_details[teamName]['runs'] = game_details[teamName]['runs'] + 1
        game_details[teamName]['3B'] = None
    if not (runner2 is None):
        print(runner2.name,'advanced from 2B to 3B!')
        game_details[teamName]['3B'] = runner2
        game_details[teamName]['2B'] = None
    if not (runner1 is None):
        print(runner1.name,'advanced from 1B to 2B!')
        game_details[teamName]['2B'] = runner1
        game_details[teamName]['1B'] = None

def lead_runner_advance_option(teamName):
    global game_details
    runner3 = game_details[teamName]['3B']
    runner2 = game_details[teamName]['2B']
    runner1 = game_details[teamName]['1B']
    if runner3 is None:
        if runner2 is None:
            if runner1 is None:
                pass #no advancing, no one on base
            else:
                if runner1.steals  >=  15:
                    print(runner1.name,'advanced from 1B to 2B!')
                    game_details[teamName]['2B'] = runner1
                    game_details[teamName]['1B'] = None
                else:
                    print(runner1.name,'stayed')
        else:
            if runner2.steals  >=  15:
                print(runner2.name,'advanced from 2B to 3B!')
                game_details[teamName]['3B'] = runner2
                game_details[teamName]['2B'] = None
            else:
                print(runner2.name,'stayed')
    else:
        if runner3.steals >= 15:
            print(runner3.name, 'scored from 3B!')
            print('The score is', game_details['Home']['runs'],'-',game_details['Away']['runs'])
            game_details[teamName]['runs'] = game_details[teamName]['runs'] + 1
            game_details[teamName]['3B'] = None
        else:
            print(runner1.name, 'stayed')


#this function takes in the dice rolls & returns how many outs happened as a result of the AB
def at_bat(batter, teamName, outs_this_inning):
    global game_details
    global outs
    walkoff = False
    dye1 = r.randrange(1,7)
    dye2 = r.randrange(1,7)
    dye3 = r.randrange(1,7)
    row = dye1 + dye2
    column = dye3
    result = grid[column - 1][row - 2]
    batter_i = game_details[teamName]["batter"]
    batter = game_details[teamName]['lineup'][batter_i]
    if result == "Hit":
        outs += draw_hitDeck(batter, teamName, outs_this_inning)
        print("In play!")
    elif result == "Out":
        outs += draw_outDeck(batter, teamName, outs_this_inning)
        print("In play!")
    elif result == "Walk":
        walk(batter, teamName)
        print("Walk!")
    elif result == "Strike Out":
        print(batter.name, 'strikes out!')
        outs += 1
    elif result == "Double Plus":
        doublePlus(batter, teamName)
    elif result == "Triple Plus":
        triplePlus(batter, teamName)
    elif result == "Home Run Plus":
        homeRunPlus(batter,teamName)
    else:
        print("This should not happen!")
    if game_details[teamName]['batter'] == 8:
        game_details[teamName]['batter'] = 0
    else:
        game_details[teamName]['batter'] = game_details[teamName]['batter'] + 1
    if game_details['Home']['runs']>game_details['Away']['runs'] and inning >= 9.5 and teamName == 'Home':
        walkoff = True #home team walkoff condition
    if not walkoff:
        clear_bases(teamName)
        game_details[teamName]['outs'] = game_details[teamName]['outs'] + 3

#todo activate/inactivate sprites at set location based on whether value is None or not
#todo find coordinates
#todo call after every roll & start of every inning
def on_base(teamName):
    global game_details
    runner1 = game_details[teamName]['1B']
    runner2 = game_details[teamName]['2B']
    runner3 = game_details[teamName]['3B']
    if runner1 is None:
        print('1B:')
    else:
        print('1B:',runner1.name)
    if runner2 is None:
        print('2B:')
    else:
        print('2B:',runner2.name)
    if runner3 is None:
        print('3B:')
    else:
        print('3B:',runner3.name)

def single(batter, teamName):
    global game_details
    runner1 = game_details[teamName]['1B']
    runner2 = game_details[teamName]['2B']
    runner3 = game_details[teamName]['3B']
    runs = 0
    if not(runner3 is None):
        runs += 1
    if not (runner2 is None):
        game_details[teamName]['3B'] = runner2
        game_details[teamName]['2B'] = None
    if not (runner1  is None):
        game_details[teamName]['2B'] = runner1
    game_details[teamName]['1B'] = batter
    print(batter.name, 'hits a single!')
    if runs > 0:
        game_details[teamName]['runs'] = game_details[teamName]['runs'] + runs
        print('The score is', game_details['Home']['runs'], '-', game_details['Away']['runs'])


def double(batter, teamName):
    global game_details
    runner1 = game_details[teamName]['1B']
    runner2 = game_details[teamName]['2B']
    runner3 = game_details[teamName]['3B']
    runs = 0
    if not (runner3 is None):
        runs += 1
        game_details[teamName]['3B'] = None
    if not (runner2 is None):
        runs += 1
    if not (runner1 is None):
        game_details[teamName]['3B'] = game_details[teamName]['1B']
        game_details[teamName]['1B']  = None
    game_details[teamName]['2B'] = batter
    print(batter.name, 'hits a double!')
    if runs > 0:
        game_details[teamName]['runs'] = game_details[teamName]['runs'] + runs
        print('The score is', game_details['Home']['runs'], '-', game_details['Away']['runs'])

def triple(batter, teamName):
    global game_details
    runner1 = game_details[teamName]['1B']
    runner2 = game_details[teamName]['2B']
    runner3 = game_details[teamName]['3B']
    runners = [runner1, runner2,runner3]
    runners = list(filter(lambda a: a is not None, runners))
    runs = len(runners)
    clear_bases(teamName)
    print(batter.name, 'hits a triple!')
    if runs > 0:
        game_details[teamName]['runs'] = game_details[teamName]['runs'] + runs
        print('The score is', game_details['Home']['runs'], '-' ,game_details['Away']['runs'])

def homeRun(batter, teamName):
    global game_details
    runner1 = game_details[teamName]['1B']
    runner2 = game_details[teamName]['2B']
    runner3 = game_details[teamName]['3B']
    runners = [runner1, runner2,runner3]
    runners = list(filter(lambda a: a is not None, runners))
    runs = len(runners) + 1
    game_details[teamName]['runs'] = game_details[teamName]['runs'] + runs
    print(batter.name, 'hits a home run with', runs-1, 'runners on!')
    print('The score is', game_details['Home']['runs'], '-', game_details['Away']['runs'])
    clear_bases(teamName)

def doublePlus(batter, teamName):
    print('DoublePlus')
    global game_details
    plus = draw_plus()
    if batter.doubles  >=  plus:
        double(batter, teamName)
    else:
        single(batter, teamName)

def triplePlus(batter, teamName):
    print('TriplePlus')
    global game_details
    plus = draw_plus()
    if batter.triples >= plus:
        triple(batter, teamName)
    else:
        single(batter, teamName)

def homeRunPlus(batter, teamName):
    print('HomeRunPlus')
    global game_details
    plus = draw_plus()
    if batter.hrs >= plus: #home run!
        homeRun(batter, teamName)
    else:
        single(batter, teamName)

def walk(batter,teamName):
    global game_details
    print(batter.name, "walks!")
    runner1 = game_details[teamName]['1B']
    runner2 = game_details[teamName]['2B']
    runner3 = game_details[teamName]['3B']
    if runner1 is None:
        game_details[teamName]['1B'] = batter
    else:
        if runner2 is None:
            game_details[teamName]['2B'] = runner1
            game_details[teamName]['1B'] = batter
        else:
            if runner3 is None:
                game_details[teamName]['3B'] = runner2
                game_details[teamName]['2B'] = runner1
                game_details[teamName]['1B'] = batter
            else:
                game_details[teamName]['runs'] = game_details[teamName]['runs'] + 1 #run scores
                print("Runner", runner3.name, "scores on a walk!")
                print('The score is', game_details['Home']['runs'], '-', game_details['Away']['runs'])
                game_details[teamName]['3B'] = runner2
                game_details[teamName]['2B'] = runner1
                game_details[teamName]['1B'] = batter

def clear_bases(teamName):
    global game_details
    game_details[teamName]['1B'] = None
    game_details[teamName]['2B'] = None
    game_details[teamName]['3B'] = None

def draw_plus():
    global plus_cards
    if len(plus_cards) == 0:
        plus_cards = list(range(41)) #repopulate
    card = r.choice(plus_cards)
    plus_cards.remove(card)
    return card

def update_display():
    global game_details
    update_first_base()
    update_second_base()
    update_third_base()
    update_batter()

#todo first display the names of the batters on the bases
#todo - enhancement - create animations of the batters moving/running around the bases
def update_first_base():
    pass

def update_second_base():
    pass

def update_third_base():
    pass

def update_batter():
    pass

"""
def half_inning(teamName):
    global team_details
    outs_this_inning = 0
    walkoff=False
    while outs_this_inning < 3:
        batter_i = game_details[teamName]["batter"]
        batter = game_details[teamName]['lineup'][batter_i]
        print(batter.name + " is up!")
        dye1=r.randrange(1,7)
        dye2=r.randrange(1,7)
        dye3=r.randrange(1,7)
        n_outs = at_bat(batter, int(dye1), int(dye2 + dye3), teamName, outs_this_inning)
        outs_this_inning += n_outs
        if game_details[teamName]['batter'] == 8:
            game_details[teamName]['batter'] = 0
        else:
            game_details[teamName]['batter'] = game_details[teamName]['batter']+1
        #home team walkoff condition
        if game_details['Home']['runs']>game_details['Away']['runs'] and inning >= 9.5 and teamName == 'Home':
            walkoff = True
            break
    if not walkoff:
        clear_bases(teamName)
        game_details[teamName]['outs'] = game_details[teamName]['outs'] + 3
"""

global grid
grid = [[], [], [], [], [], [], [], [], [], [], []]

home = []
away = []
i = 0
init_grid()
while i < 12:
    home.append(createPlayer())
    away.append(createPlayer())
    i += 1
print("Home team:", home)
print("Away team:", away)

#todo what are the events?
#at bat - after each one you need to check for end of half inning & end of game
#todo pinch hit
#todo pinch run

#todo init batter/runner sprites at set coordinates & figure out how to toggle them on/off


global currentBatter
global teamName
global outs
#todo don't hardcode these
currentBatter = Player(.0,0,0,0,0,0)
teamName = 'Away'
outs = 0

# Creating a button with specified options
atBat = Button(root,
               text="Roll",
               command=partial(at_bat, currentBatter, teamName, outs),
               activebackground="blue",
               activeforeground="white",
               anchor="center",
               bd=3,
               bg="lightgray",
               cursor="hand2",
               disabledforeground="gray",
               fg="black",
               font=("Arial", 12),
               height=2,
               highlightbackground="black",
               highlightcolor="green",
               highlightthickness=2,
               justify="center",
               overrelief="raised",
               padx=10,
               pady=5,
               width=15,
               wraplength=100)

atBat.grid(row=2, column=3)

#init the game details
global game_details
game_details = dict()
game_details["Home"] = dict()
game_details["Away"] = dict()
game_details["Home"]["runs"] = 0
game_details["Away"]["runs"] = 0
game_details["Home"]["outs"] = 0
game_details["Away"]["outs"] = 0
game_details["Home"]["batter"] = 0
game_details["Away"]["batter"] = 0
game_details["Home"]["lineup"] = home[:9]
game_details["Away"]["lineup"] = away[:9]
game_details["Home"]["bench"] = home[9:]
game_details["Away"]["bench"] = away[9:]
clear_bases('Home')
clear_bases('Away')

# Todo make a function that shows who is on base & call it at start of every inning & after every button click
mainloop()
