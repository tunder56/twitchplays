
twitchname = 'defult'
twitchtoken = 'oauth:defult'

gamerunning=0




while twitchname == 'defult':
    twitchname = (raw_input("enter your twitch name please "))
    if twitchname != 'defult':
        break
    else:
        print ("enter your twitch name");

print ('im goign to assume thats valid idk till later tho')
print ('________________________________________________________________________________________________')
print ('                                                                                                ')

print ('For this next step youll need an oauth token, they can be generated from here http://twitchapps.com/tmi/')

while twitchtoken == 'oauth:defult':
    twitchtoken = (raw_input("enter your twitch oauth token please "))
    if twitchtoken != 'oauth:defult':
        break
    else:
        print ("enter your twitch token");


print (' your twitch name is',twitchname,"and your token is",twitchtoken)  

print ('________________________________________________________________________________________________')
print ('                                                                                                ')
print(" game id list, ")
print("1  defult game profile")
print("2  fallout newvegas")
print("3  minecraft")
print("4  open world game")
print("5  destiny")

while gamerunning == 0:
    gameselect = int(raw_input("enter id of game twitch chat will play "))
    if gameselect == 1 or gameselect == 2 or gameselect == 3 or gameselect == 4 or gameselect == 5: 
        break
    else:
        print ("select a valid game")

 
if gameselect == 1 and gamerunning == 0:
        execfile('C:/twitchplays/TwitchPlaysdefult.py')
        print("running defult twitch plays profile")
        gamerunning = 1
        

if gameselect == 2 and gamerunning == 0:
        execfile('C:/twitchplays/TwitchPlaysfalloutnewvegas.py')
        print("running fallout new vegas twitch plays profile")
        gamerunning = 1

if gameselect == 3 and gamerunning == 0:
        execfile('C:/twitchplays/TwitchPlaysminecraft.py')
        print("running minecraft twitch plays profile")
        gamerunning = 1

if gameselect == 4 and gamerunning == 0:
        execfile('C:/twitchplaysTwitchPlaysopenworldgames.py')
        print("running open world twitch plays profile")
        gamerunning = 1

if gameselect == 5 and gamerunning == 0:
        execfile('C:/twitchplays/TwitchPlaysdestiny.py')
        print("running destiny twitch plays profile")
        gamerunning = 1;   

