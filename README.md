# twitchplays
some twitch plays code


i decied to try to make the code for twitch plays simpler and esier to run, this is a wip so feel free to add to it as you want


### installation

1. install the latest version of conda from here https://docs.conda.io/en/latest/miniconda.html, leave all options as defult

2. download and run the file called twitch plays installer from the git, it may say that its virus, it isnt

3. run Anaconda Powershell Prompt (miniconda3), it should be in your resently installed files

4. run the command `conda init powershell` inside of it

### the program will be installed in C:/twitchplays
5. run the file called FIRST_TIME_SETUP_runtwtichplays.ps1 , you will need to right click then go run with powershell
    this will :
    1. set up a conda enviroment
    2. set the restricted policy to allow the script to run, select y to let the scrpit run
    3. install the packages needed to run, they are pyautogui and pynput
    4. and run the program within it 


6. follow the instuctions in the program
   you should be good to go 

### if it crashes check your auth token and name 

p.s you can use the chat box in stream manager to test if the program is running correctly



## the socrce code is in the code stuff folder of the repo


## profile explinations

defult is a bunch of standed commands

destiny is based of destiny 2 but is more or less a generic fps

minecraft does what its says on the tin

open world is a bunch generic openworld things such as camera movement etc



__use the file called runtwitchplays1.ps1 after set up/first use__


#Errors
there are many errors at the moment, if you get one refer to blelow for fixes / work arounds
    - if you run either of the .ps1 files and it crashes without doing anything, try copy pasting each line of the command into powershell to see what went wrong
    - check that conda is runnning nativly in powershell
    - check file paths of your conda enviroment etc

#disclaimers 

if you install from github you will need to change the .ps1 files so that they fit to your computor

this is a work in progress feel free to modify as needed as well as pull requests etc




## credits
full credit to doug doug for most if not all the code, as well as insperation

i tried to make a launcher thing to make the process a bit more streamlined to the averange user, 
