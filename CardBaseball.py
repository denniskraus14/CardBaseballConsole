#Card Baseball Console-Based Impl
import random as r


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
        return self.name + ": " + str(self.avg) + " AVG " +\
               str(self.hrs) + " HRs"

    def __repr__(self):
        return self.name + ": " + str(self.avg) + " AVG " +\
               str(self.hrs) + " HRs"

def createPlayer():
    #todo pick a random name for the player
    l = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t']
    return Player(float(r.randrange(175,326)/1000),
           r.randrange(0,161),
           r.randrange(0,60),
           r.randrange(0,11),
           r.randrange(0,54),
           r.randrange(0,72),
           r.choice(l))

def half_inning(teamName):
    team = game_details[teamName]
    outs_this_inning = 0
    while outs_this_inning < 3:
        batter_i = team["batter"]
        batter = game_details[teamName]['lineup'][batter_i]
        print(batter.name + " is up!")
        dye1=r.randrange(1,7)
        dye2=r.randrange(1,7)
        dye3=r.randrange(1,7)
        #todo: impl grid logic
        print(dye1)
        print(dye2)
        print(dye3)
        outs_this_inning += 1 # for now
        if team['batter'] == 8:
            team['batter']=0
        else:
            team['batter']=team['batter']+1
    game_details[teamName] = team
    
home = []
away = []
i=0
while i<12:
    home.append(createPlayer())
    away.append(createPlayer())
    i+=1

print(home)
print(away)

game_details = dict()
game_details["Home"]=dict()
game_details["Away"]=dict()
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

gameIsWon = False
inning = 1.0
while  not gameIsWon:
    home_runs = game_details["Home"]["runs"]
    away_runs = game_details["Away"]["runs"]
    home_outs = game_details['Home']['outs']
    away_outs = game_details['Away']['outs']
    if inning >=9.5 and home_runs > away_runs:
        gameIsWon = true
    elif home_outs==away_outs and away_runs>home_runs:
        gameIsWon = true
    else: #play ball!
        if home_outs==away_outs:
            half_inning("Away")
            inning += .5
        else:
            half_inning("Home")
            inning += .5
            
        

if home_runs>away_runs:
    print('Home Team Wins ' + game_details["Home"]['runs']+ "-" +\
          game_details["Away"]['runs']+ "!")
else:
    print('Away Team Wins ' + game_details["Home"]['runs']+ "-" +\
          game_details["Away"]['runs']+ "!")
          
