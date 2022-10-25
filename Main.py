#imports
#What shows up When you first Launch the code...
label .startscreen

print(r'''
   _.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._
 ,'_.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._`.
( (                                                         ) )
 ) )                 The Fortnite Drop!!                    ( (
( (               ~~~~~~~~~~~~~~~~~~~~~~~~~~~               ) )
 ) )                                                       ( (
( (_.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._) )
 `._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._,'
''')


goto .start

#End of start screen then go to start of the game...

label .start

#Game Starts...

print('The Battle Bus Starts Where Do you want to Drop?')
print('Salty [1]')
print('Tilted Towers [2]')
print('Risky Reels [3]')
drop = input(": ")


if drop == "1":
    #if input = to 1 goto lable salty
    goto .salty



if drop == "2":
    #if input = to 2 goto lable tilted
    goto .tilted

if drop == "3":
    #if input = to 3 goto lable salty
    goto .risky

#Else Statment so if they inputed a invalid drop it shows a error then then Go to the start of the scene
else:
    print("Not A valid Drop!")
    input("press enter to go to start of scene.")
    goto .start


label .tilted
input("You Get Beemed From The sky By mongral!")
goto .death


label .salty

print("You land and pickup a Blue Pump and a Green Suppresed SMG.")
print("But you start to hear footsteps...")
print("A Person Pops out and starts spraying do you,")
print("shoot back [1]")
print("place a box up then piece him up [2]")
print("or try and escape [3]")
inputa = input(": ")
if inputa == "1":
    goto .push

if inputa == "2":
    print("you box him and mongral clasic him and get the kill!")
if inputa == "3":
    print("while your running away you get sprayed by a ar!")
    goto .death

#Else Statment so if they inputed a invalid drop it shows a error then then Go to the start of the scene
else:
    print("Not A valid Drop!")
    input("press enter to go to start of scene.")
    goto .salty

label .risky

print("You Hear gun fire what do you do?")
print("[1] - Third Party")
print("[2] - wait till late game")
aa = input(": ")

if aa == "1":
    goto .push

if aa == "2":
    print("You survive to late game ")
    goto .endgame

#Else Statment so if they inputed a invalid drop it shows a error then then Go to the start of the scene
else:
    print("Not A valid Drop!")
    input("press enter to go to start of scene.")
    goto .risky


label .endgame
print("wow good job u made it to end game!")
print("Your in the Endgame now! You have 2 options,")
print("Hide in a Bush Till its a 1v1 [1]")
print("RUSH EVERY KID CAUSE YOUR THE BEST IN THIS LOBBY [2]")
num = input(": ")
if num == "1":
    input("a kid sees your head peeking and you get headshot snipped")
    goto .death

if num == "2":
    print("YOU ARE THE BEST BATTLE ROYALER AND YOU GET THE VICTORY!!")
    goto .vic



label .push
print("you spray and get him down to 15 HP but your only 30 HP")
print("Do you escape and wait until endgane or go for the kill")
print("Escape [1]")
print("push [2]")
aaw = input(": ")

if aaw == "1":
    print("To Late to escape you get killed while trying to run away!")
    goto .death
if aaw == "2":
    print("You Get the The finish by hitting him 150 with your shotgun!")
    goto .endgame





label .death
print('''.......................................... .........................................................
.......................................      .......................................................
......................................  7?5!. .......    ...........................................
................................. ..   :Y&@@Y  .....  ..   .........................................
...............................     .?P5J!^!Y!  ..  :JG#P~  ........................................
.............................  :?PJYG@Y.    :JY.  .JP#@@@@Y. .......................................
...........................  :J#@@&B5J7^. ..  ~Y^:G&#&@@@@@! .......................................
.........................  :Y&&BY!:.     ....  :YP@&#&@@@@@P  ......................................
.......................  :J#BJ~.     ......   ^!Y#&@&&&@@@@@5: .....................................
...................... .?G5~.    .........  ~5#&&&##@@&@@@@@@~ .....................................
..................... :Y?:   ............ .J#&&&&&&##@@@@&&&@5. ....................................
...................  :!:   ............  :5&&&@&&&&@BPGB#&@@@@5. ...................................
................... ..  .............  .!G&&&&&&&&&&G5JJP@@&@@@P. ..................................
....................   ............. .7B@&&&&&&&&&&&#B###@&&@&&@J  .................................
.................................... ?@@&&&&@&&&&&&&&@@@BG&@@@@@Y ..................................
.................................... ~&@@@&@@&&@&&&&&&@@@&GB&&&#?. .................................
..................................... ~BBJ~Y#@&@&&&&&&@@@@YJ5PG##! .................................
...................................... ..   JG&@&&&&@@@@@@PPPP#&&~ .................................
.......................................   . !5B@@@@@@@@@@@@@@&GB&^ .................................
........................................... :JB&&@@@@@@@@@@@@@@BP:  ................................
........................................... .J&&&@@@@@@@@@@@@@@@#P~  ...............................
........................................... .5&&&@@@@@@@@@@@@@@&!7G?. ..............................
........................................... .G@&&@@@@@@@&@@@@@G~  ^PG^  ............................
........................................... ^#&&&@@@@@@@&@@@B^. .. .J#J.  ..........................
........................................... !&&&&@@@@@@@&@@@G  ....  :YG!  .........................
........................................... J@&&&@@@@@@@&@@@B. ......  ~G5:  .......................
.......................................... .G&&&&@@@@@@@&@@@#. .......  .?G?.  .....................
.......................................... ~&&&&@@@@@@@@@@@@&: .........  :5B!  ....................
.........................................  JBBBBBBBBBBBBBBB#B: ...........  7BJ. ...................
......................................... .................... ............  ... ...................
...........................................                   ...............   ....................''')

input("""
_____.___.________   ____ ___  ________  .______________._.
\__  |   |\_____  \ |    |   \ \______ \ |   \_   _____/| |
 /   |   | /   |   \|    |   /  |    |  \|   ||    __)_ | |
 \____   |/    |    \    |  /   |    `   \   ||        \ \|
 / ______|\_______  /______/   /_______  /___/_______  / __
 \/               \/                   \/            \/  \/
 
 """)
input("Press Enter To play Again!")
goto .startscreen

lable .vic 

print('''   _.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._
 ,'_.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._`.
( (                                                         ) )
 ) )                    VICRORY ROYAL!                      ( (
( (               ~~~~~~~~~~~~~~~~~~~~~~~~~~~               ) )
 ) )                                                       ( (
( (_.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._) )
 `._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._,''')
 
input("Press Enter To play Again!")
goto .startscreen
