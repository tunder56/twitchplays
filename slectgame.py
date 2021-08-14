import time
import subprocess
import ctypes
import random
import string

# Twitch imports
import TwitchPlays_Connection


twitchname = 'defult'
twitchtoken = 'oauth:defult'

gamerunning=0

# Controller imports
import pyautogui
import pynput
from pynput.mouse import Button, Controller

SendInput = ctypes.windll.user32.SendInput

# KEY PRESS NOTES
# The standard "Twitch Plays" tutorial key commands do NOT work in DirectX games (they only work in general windows applications)
# Instead, we use DirectX key codes and input functions below.
# This DirectX code is partially sourced from: https://stackoverflow.com/questions/53643273/how-to-keep-pynput-and-ctypes-from-clashing

# Presses and permanently holds down a keyboard key
def PressKeyPynput(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = pynput._util.win32.INPUT_union()
    ii_.ki = pynput._util.win32.KEYBDINPUT(0, hexKeyCode, 0x0008, 0, ctypes.cast(ctypes.pointer(extra), ctypes.c_void_p))
    x = pynput._util.win32.INPUT(ctypes.c_ulong(1), ii_)
    SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

# Releases a keyboard key if it is currently pressed down
def ReleaseKeyPynput(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = pynput._util.win32.INPUT_union()
    ii_.ki = pynput._util.win32.KEYBDINPUT(0, hexKeyCode, 0x0008 | 0x0002, 0, ctypes.cast(ctypes.pointer(extra), ctypes.c_void_p))
    x = pynput._util.win32.INPUT(ctypes.c_ulong(1), ii_)
    SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

# Helper function. Holds down a key for the specified number of seconds, then releases it.
def PressAndHoldKey(hexKeyCode, seconds):
    PressKeyPynput(hexKeyCode)
    time.sleep(seconds)
    ReleaseKeyPynput(hexKeyCode)

def defultgame():
    print ("running defult profile")
    # An optional countdown before the code actually starts running, so you have time to load up the game before messages are processed.
    # TODO: Set the "countdown" variable to whatever countdown length you want.
    countdown = 5 #The number of seconds before the code starts running
    while countdown > 0:
        print(countdown)
        countdown -= 1
        time.sleep(1)

    # Connects to your twitch chat, using your username and OAuth token.
    # TODO: make sure that your Twitch username and OAuth token are added to the "TwitchPlays_AccountInfo.py" file
    t = TwitchPlays_Connection.Twitch()
    t.twitch_connect(twitchname, twitchtoken)

    ##########################################################

    while True:
        # Check for new chat messages
        new_messages = t.twitch_recieve_messages()
        if not new_messages:
            #No new messages. 
            continue
        else:
            try:  
                for message in new_messages:
                    # We got a new message! Get the message and the username.
                    msg = message['message'].lower()
                    username = message['username'].lower()
                    
                    # TODO:
                    # Now that you have a chat message, this is where you add your game logic.
                    # Use the "PressKeyPynput(KEYCODE)" function to press and hold down a keyboard key.
                    # Use the "ReleaseKeyPynput(KEYCODE)" function to release a specific keyboard key.
                    # Use the "PressAndHoldKey(KEYCODE, SECONDS)" function press down a key for X seconds, then release it.
                    # Use "mouse.press(Button.left)" or "mouse.release(Button.left)" to press/release the mouse. Can use Button.right for right click.

                    # I've added some example videogame logic code below:

                    #minecraft

                    # If the chat message is "left", then hold down the A key for 2 seconds
                    if msg == "left": 
                        PressAndHoldKey(A, 1)

                    # If the chat message is "right", then hold down the D key for 2 seconds
                    if msg == "right": 
                        PressAndHoldKey(D, 1)

                    if msg == "inventory" or msg == "menu": 
                        PressAndHoldKey(E, 1)

                    if msg == "1": 
                        PressAndHoldKey(ONE, 1)

                    if msg == "2": 
                        PressAndHoldKey(TWO, 1)

                    if msg == "3": 
                        PressAndHoldKey(THREE, 1)

                    if msg == "4": 
                        PressAndHoldKey(FOUR, 1)

                    if msg == "5": 
                        PressAndHoldKey(FIVE, 1)

                    if msg == "6": 
                        PressAndHoldKey(SIX, 1)

                    if msg == "7": 
                        PressAndHoldKey(SEVEN, 1)

                    if msg == "8": 
                        PressAndHoldKey(EIGHT, 1)

                    if msg == "9": 
                        PressAndHoldKey(NINE, 1)


                    # If message is "run", then permanently hold down the W key
                    if msg == "run": 
                        ReleaseKeyPynput(S) #release brake key first
                        PressKeyPynput(W) #start permanently driving

                    if msg == "sprint": 
                        ReleaseKeyPynput(S) #release brake key first
                        PressKeyPynput(LEFT_SHIFT)
                        PressKeyPynput(W) #start permanently driving

                    # If message is "back", then permanently hold down the S key
                    if msg == "back": 
                        ReleaseKeyPynput(W) #release drive key first
                        ReleaseKeyPynput(LEFT_SHIFT)
                        PressKeyPynput(S) #start permanently reversing

                    # Release both the "run" and "back" keys
                    if msg == "stop": 
                        ReleaseKeyPynput(W)
                        ReleaseKeyPynput(LEFT_SHIFT)
                        ReleaseKeyPynput(S)

                    # Press the spacebar for 0.7 seconds
                    if msg == "jump": 
                        PressAndHoldKey(SPACE, 0.7)

                    # Presses the left mouse button down for 1 second, then releases it
                    if msg == "hit": 
                        mouse.press(Button.left)
                        time.sleep(1)
                        mouse.release(Button.left)

                    if msg == "right click": 
                        mouse.press(Button.right)
                        time.sleep(1)
                        mouse.release(Button.right)

                    



                

            except:
                # There was some error trying to process this chat message. Simply move on to the next message.
                print('Encountered an exception while reading chat.')

def destinygame():
    print ("running destiny profile")
    # An optional countdown before the code actually starts running, so you have time to load up the game before messages are processed.
    # TODO: Set the "countdown" variable to whatever countdown length you want.
    countdown = 5 #The number of seconds before the code starts running
    while countdown > 0:
        print(countdown)
        countdown -= 1
        time.sleep(1)

    # Connects to your twitch chat, using your username and OAuth token.
    # TODO: make sure that your Twitch username and OAuth token are added to the "TwitchPlays_AccountInfo.py" file
    t = TwitchPlays_Connection.Twitch()
    t.twitch_connect(twitchname, twitchtoken)

    ##########################################################

    while True:
        # Check for new chat messages
        new_messages = t.twitch_recieve_messages()
        if not new_messages:
            #No new messages. 
            continue
        else:
            try:  
                for message in new_messages:
                    # We got a new message! Get the message and the username.
                    msg = message['message'].lower()
                    username = message['username'].lower()
                    
                    # TODO:
                    # Now that you have a chat message, this is where you add your game logic.
                    # Use the "PressKeyPynput(KEYCODE)" function to press and hold down a keyboard key.
                    # Use the "ReleaseKeyPynput(KEYCODE)" function to release a specific keyboard key.
                    # Use the "PressAndHoldKey(KEYCODE, SECONDS)" function press down a key for X seconds, then release it.
                    # Use "mouse.press(Button.left)" or "mouse.release(Button.left)" to press/release the mouse. Can use Button.right for right click.

                    # I've added some example videogame logic code below:

                    #minecraft

                    # If the chat message is "left", then hold down the A key for 2 seconds
                    if msg == "left": 
                        PressAndHoldKey(A, 1)

                    # If the chat message is "right", then hold down the D key for 2 seconds
                    if msg == "right": 
                        PressAndHoldKey(D, 1)

                    if msg == "class ablity" or msg == "classablity": 
                        PressAndHoldKey(V, 1)

                    if msg == "interact" or msg == "talk": 
                        PressAndHoldKey(E, 1)

                    if msg == "grenade" or msg == "nade": 
                        PressAndHoldKey(Q, 1)

                    if msg == "melee" or msg == "punch": 
                        PressAndHoldKey(C, 1)

                    if msg == "super" or msg == "crutch": 
                        PressAndHoldKey(F, 1)

                    if msg == "1": 
                        PressAndHoldKey(ONE, 1)

                    if msg == "2": 
                        PressAndHoldKey(TWO, 1)

                    if msg == "3": 
                        PressAndHoldKey(THREE, 1)

                    if msg == "crouch" or msg =="stealth mode activate": 
                        PressKeyPynput(LEFT_CONTROL)

                    if msg == "un crouch" or msg =="stealth mode deactivate" or msg == "uncrouch": 
                        ReleaseKeyPynput(LEFT_CONTROL)


                    # If message is "drive", then permanently hold down the W key
                    if msg == "run": 
                        ReleaseKeyPynput(S) #release brake key first
                        PressKeyPynput(W) #start permanently driving

                    if msg == "sprint": 
                        ReleaseKeyPynput(S) #release brake key first
                        PressKeyPynput(LEFT_SHIFT)
                        PressKeyPynput(W) #start permanently driving

                    # If message is "reverse", then permanently hold down the S key
                    if msg == "back": 
                        ReleaseKeyPynput(W) #release drive key first
                        ReleaseKeyPynput(LEFT_SHIFT)
                        PressKeyPynput(S) #start permanently reversing

                    # Release both the "drive" and "reverse" keys
                    if msg == "stop": 
                        ReleaseKeyPynput(W)
                        ReleaseKeyPynput(LEFT_SHIFT)
                        ReleaseKeyPynput(S)

                    # Press the spacebar for 0.7 seconds
                    if msg == "jump": 
                        PressAndHoldKey(SPACE, 0.7)

                    # Presses the left mouse button down for 1 second, then releases it
                    if msg == "shoot": 
                        mouse.press(Button.left)
                        time.sleep(1)
                        mouse.release(Button.left)

                    if msg == "scope in": 
                        mouse.press(Button.right)
                        time.sleep(1)
                        mouse.release(Button.right)

                    if msg == "aim up" or msg =="aimup": 
                        pyautogui.move(0, -200, 1)

                    if msg == "aim down" or msg =="aimdown": 
                        pyautogui.move(0, 200, 1)

                    if msg == "aim left" or msg =="aimleft": 
                        pyautogui.move(-200, 0, 1)

                    if msg == "aim right" or msg =="aimright": 
                        pyautogui.move(200, 0, 1)



            except:
                # There was some error trying to process this chat message. Simply move on to the next message.
                print('Encountered an exception while reading chat.')

def openworldgame ():
    print ("running open world profile")
    # An optional countdown before the code actually starts running, so you have time to load up the game before messages are processed.
    # TODO: Set the "countdown" variable to whatever countdown length you want.
    countdown = 5 #The number of seconds before the code starts running
    while countdown > 0:
        print(countdown)
        countdown -= 1
        time.sleep(1)

    # Connects to your twitch chat, using your username and OAuth token.
    # TODO: make sure that your Twitch username and OAuth token are added to the "TwitchPlays_AccountInfo.py" file
    t = TwitchPlays_Connection.Twitch()
    t.twitch_connect(twitchname, twitchtoken)

    ##########################################################

    while True:
        # Check for new chat messages
        new_messages = t.twitch_recieve_messages()
        if not new_messages:
            #No new messages. 
            continue
        else:
            try:  
                for message in new_messages:
                    # We got a new message! Get the message and the username.
                    msg = message['message'].lower()
                    username = message['username'].lower()
                    
                    # TODO:
                    # Now that you have a chat message, this is where you add your game logic.
                    # Use the "PressKeyPynput(KEYCODE)" function to press and hold down a keyboard key.
                    # Use the "ReleaseKeyPynput(KEYCODE)" function to release a specific keyboard key.
                    # Use the "PressAndHoldKey(KEYCODE, SECONDS)" function press down a key for X seconds, then release it.
                    # Use "mouse.press(Button.left)" or "mouse.release(Button.left)" to press/release the mouse. Can use Button.right for right click.

                    # I've added some example videogame logic code below:

                    #minecraft

                    # If the chat message is "left", then hold down the A key for 2 seconds
                    if msg == "left": 
                        PressAndHoldKey(A, 1)

                    # If the chat message is "right", then hold down the D key for 2 seconds
                    if msg == "right": 
                        PressAndHoldKey(D, 1)

                    if msg == "inventory" or msg == "menu": 
                        PressAndHoldKey(E, 1)

                    if msg == "1": 
                        PressAndHoldKey(ONE, 1)

                    if msg == "2": 
                        PressAndHoldKey(TWO, 1)

                    if msg == "3": 
                        PressAndHoldKey(THREE, 1)

                    if msg == "4": 
                        PressAndHoldKey(FOUR, 1)

                    if msg == "5": 
                        PressAndHoldKey(FIVE, 1)

                    if msg == "6": 
                        PressAndHoldKey(SIX, 1)

                    if msg == "7": 
                        PressAndHoldKey(SEVEN, 1)

                    if msg == "8": 
                        PressAndHoldKey(EIGHT, 1)

                    if msg == "9": 
                        PressAndHoldKey(NINE, 1)


                    # If message is "drive", then permanently hold down the W key
                    if msg == "run": 
                        ReleaseKeyPynput(S) #release brake key first
                        PressKeyPynput(W) #start permanently driving

                    if msg == "sprint": 
                        ReleaseKeyPynput(S) #release brake key first
                        PressKeyPynput(LEFT_SHIFT)
                        PressKeyPynput(W) #start permanently driving

                    # If message is "reverse", then permanently hold down the S key
                    if msg == "back": 
                        ReleaseKeyPynput(W) #release drive key first
                        ReleaseKeyPynput(LEFT_SHIFT)
                        PressKeyPynput(S) #start permanently reversing

                    # Release both the "drive" and "reverse" keys
                    if msg == "stop": 
                        ReleaseKeyPynput(W)
                        ReleaseKeyPynput(LEFT_SHIFT)
                        ReleaseKeyPynput(S)

                    # Press the spacebar for 0.7 seconds
                    if msg == "jump": 
                        PressAndHoldKey(SPACE, 0.7)

                    # Presses the left mouse button down for 1 second, then releases it
                    if msg == "hit": 
                        mouse.press(Button.left)
                        time.sleep(1)
                        mouse.release(Button.left)

                    if msg == "place": 
                        mouse.press(Button.right)
                        time.sleep(1)
                        mouse.release(Button.right)

                    if msg == "aim up" or msg =="aimup": 
                        pyautogui.move(0, -200, 1)

                    if msg == "aim down" or msg =="aimdown": 
                        pyautogui.move(0, 200, 1)

                    if msg == "aim left" or msg =="aimleft": 
                        pyautogui.move(-200, 0, 1)

                    if msg == "aim right" or msg =="aimright": 
                        pyautogui.move(200, 0, 1)



                    

            except:
                # There was some error trying to process this chat message. Simply move on to the next message.
                print('Encountered an exception while reading chat.')

def minecraft():
    print ("running minecraft profile")
    # An optional countdown before the code actually starts running, so you have time to load up the game before messages are processed.
    # TODO: Set the "countdown" variable to whatever countdown length you want.
    countdown = 5 #The number of seconds before the code starts running
    while countdown > 0:
        print(countdown)
        countdown -= 1
        time.sleep(1)

    # Connects to your twitch chat, using your username and OAuth token.
    # TODO: make sure that your Twitch username and OAuth token are added to the "TwitchPlays_AccountInfo.py" file
    t = TwitchPlays_Connection.Twitch()
    t.twitch_connect(twitchname, twitchtoken)

    ##########################################################

    while True:
        # Check for new chat messages
        new_messages = t.twitch_recieve_messages()
        if not new_messages:
            #No new messages. 
            continue
        else:
            try:  
                for message in new_messages:
                    # We got a new message! Get the message and the username.
                    msg = message['message'].lower()
                    username = message['username'].lower()
                    
                    # TODO:
                    # Now that you have a chat message, this is where you add your game logic.
                    # Use the "PressKeyPynput(KEYCODE)" function to press and hold down a keyboard key.
                    # Use the "ReleaseKeyPynput(KEYCODE)" function to release a specific keyboard key.
                    # Use the "PressAndHoldKey(KEYCODE, SECONDS)" function press down a key for X seconds, then release it.
                    # Use "mouse.press(Button.left)" or "mouse.release(Button.left)" to press/release the mouse. Can use Button.right for right click.

                    # I've added some example videogame logic code below:

                    #minecraft

                    # If the chat message is "left", then hold down the A key for 2 seconds
                    if msg == "left": 
                        PressAndHoldKey(A, 1)

                    # If the chat message is "right", then hold down the D key for 2 seconds
                    if msg == "right": 
                        PressAndHoldKey(D, 1)

                    if msg == "inventory" or msg == "menu": 
                        PressAndHoldKey(E, 1)

                    if msg == "1": 
                        PressAndHoldKey(ONE, 1)

                    if msg == "2": 
                        PressAndHoldKey(TWO, 1)

                    if msg == "3": 
                        PressAndHoldKey(THREE, 1)

                    if msg == "4": 
                        PressAndHoldKey(FOUR, 1)

                    if msg == "5": 
                        PressAndHoldKey(FIVE, 1)

                    if msg == "6": 
                        PressAndHoldKey(SIX, 1)

                    if msg == "7": 
                        PressAndHoldKey(SEVEN, 1)

                    if msg == "8": 
                        PressAndHoldKey(EIGHT, 1)

                    if msg == "9": 
                        PressAndHoldKey(NINE, 1)


                    # If message is "drive", then permanently hold down the W key
                    if msg == "run": 
                        ReleaseKeyPynput(S) #release brake key first
                        PressKeyPynput(W) #start permanently driving

                    if msg == "sprint": 
                        ReleaseKeyPynput(S) #release brake key first
                        PressKeyPynput(LEFT_CONTROL)
                        PressKeyPynput(W) #start permanently driving

                    # If message is "reverse", then permanently hold down the S key
                    if msg == "back": 
                        ReleaseKeyPynput(W) #release drive key first
                        ReleaseKeyPynput(LEFT_CONTROL)
                        PressKeyPynput(S) #start permanently reversing

                    # Release both the "drive" and "reverse" keys
                    if msg == "stop": 
                        ReleaseKeyPynput(W)
                        ReleaseKeyPynput(LEFT_CONTROL)
                        ReleaseKeyPynput(S)

                    # Press the spacebar for 0.7 seconds
                    if msg == "jump": 
                        PressAndHoldKey(SPACE, 0.7)

                    # Presses the left mouse button down for 1 second, then releases it
                    if msg == "hit": 
                        mouse.press(Button.left)
                        time.sleep(1)
                        mouse.release(Button.left)

                    if msg == "place": 
                        mouse.press(Button.right)
                        time.sleep(1)
                        mouse.release(Button.right)

                    if msg == "aim up" or msg =="aimup": 
                        pyautogui.move(0, -200, 1)

                    if msg == "aim down" or msg =="aimdown": 
                        pyautogui.move(0, 200, 1)

                    if msg == "aim left" or msg =="aimleft": 
                        pyautogui.move(-200, 0, 1)

                    if msg == "aim right" or msg =="aimright": 
                        pyautogui.move(200, 0, 1)

                    if msg == "turn around" or msg =="turnaround": 
                        pyautogui.move(1600, 0, 1)



                
            except:
                # There was some error trying to process this chat message. Simply move on to the next message.
                print('Encountered an exception while reading chat.')

def newvegas(): 
    print ("running new vegas profile")
    # An optional countdown before the code actually starts running, so you have time to load up the game before messages are processed.
    # TODO: Set the "countdown" variable to whatever countdown length you want.
    countdown = 5 #The number of seconds before the code starts running
    while countdown > 0:
        print(countdown)
        countdown -= 1
        time.sleep(1)

    # Connects to your twitch chat, using your username and OAuth token.
    # TODO: make sure that your Twitch username and OAuth token are added to the "TwitchPlays_AccountInfo.py" file
    t = TwitchPlays_Connection.Twitch()
    t.twitch_connect(twitchname, twitchtoken)

    ##########################################################

    while True:
        # Check for new chat messages
        new_messages = t.twitch_recieve_messages()
        if not new_messages:
            #No new messages. 
            continue
        else:
            try:  
                for message in new_messages:
                    # We got a new message! Get the message and the username.
                    msg = message['message'].lower()
                    username = message['username'].lower()
                    print(username + ": " + msg);
                    
                    # TODO:
                    # Now that you have a chat message, this is where you add your game logic.
                    # Use the "PressKeyPynput(KEYCODE)" function to press and hold down a keyboard key.
                    # Use the "ReleaseKeyPynput(KEYCODE)" function to release a specific keyboard key.
                    # Use the "PressAndHoldKey(KEYCODE, SECONDS)" function press down a key for X seconds, then release it.
                    # Use "mouse.press(Button.left)" or "mouse.release(Button.left)" to press/release the mouse. Can use Button.right for right click.

                    # I've added some example videogame logic code below:

                    #minecraft

                    # If the chat message is "left", then hold down the A key for 2 seconds
                    if msg == "left": 
                        PressAndHoldKey(A, 1)

                    # If the chat message is "right", then hold down the D key for 2 seconds
                    if msg == "right": 
                        PressAndHoldKey(D, 1)

                    if msg == "1": 
                        PressAndHoldKey(ONE, 1)

                    if msg == "2": 
                        PressAndHoldKey(TWO, 1)

                    if msg == "3": 
                        PressAndHoldKey(THREE, 1)

                    if msg == "4": 
                        PressAndHoldKey(FOUR, 1)

                    if msg == "5": 
                        PressAndHoldKey(FIVE, 1)

                    if msg == "6": 
                        PressAndHoldKey(SIX, 1)

                    if msg == "7": 
                        PressAndHoldKey(SEVEN, 1)

                    if msg == "8": 
                        PressAndHoldKey(EIGHT, 1)

                    if msg == "9": 
                        PressAndHoldKey(NINE, 1)

                    if msg == "e" or msg =="interact": 
                        PressAndHoldKey(E, 1)

                    if msg == "r" or msg =="reload" or msg =="repair": 
                        PressAndHoldKey(R, 1)

                    if msg == "crouch" or msg =="stealth mode activate": 
                        PressKeyPynput(LEFT_CONTROL)

                    if msg == "un crouch" or msg =="stealth mode deactivate" or msg == "uncrouch": 
                        ReleaseKeyPynput(LEFT_CONTROL)

                    if msg == "z" or msg =="pickup" or msg =="pick up" or msg =="drop": 
                        PressAndHoldKey(Z, 1)

                    if msg == "z" or msg =="pickup" or msg =="pick up" or msg =="drop": 
                        PressAndHoldKey(Z, 1)

                    if msg == "a" or msg =="take all": 
                        PressAndHoldKey(A, 1)

                    if msg == "x" or msg =="cancel": 
                        PressAndHoldKey(X, 1)

                    if msg == "tab" or msg =="pip boy" or msg =="pipboy": 
                        PressAndHoldKey(TAB, 1)

                    # If message is "drive", then permanently hold down the W key
                    if msg == "run": 
                        ReleaseKeyPynput(S) #release brake key first
                        PressKeyPynput(W) #start permanently driving

                    if msg == "sprint": 
                        ReleaseKeyPynput(S) #release brake key first
                        PressKeyPynput(LEFT_SHIFT)
                        PressKeyPynput(W) #start permanently driving

                    # If message is "reverse", then permanently hold down the S key
                    if msg == "back": 
                        ReleaseKeyPynput(W) #release drive key first
                        ReleaseKeyPynput(LEFT_SHIFT)
                        PressKeyPynput(S) #start permanently reversing

                    # Release both the "drive" and "reverse" keys
                    if msg == "stop": 
                        ReleaseKeyPynput(W)
                        ReleaseKeyPynput(LEFT_SHIFT)
                        ReleaseKeyPynput(S)

                    # Press the spacebar for 0.7 seconds
                    if msg == "jump": 
                        PressAndHoldKey(SPACE, 0.7)

                    # Presses the left mouse button down for 1 second, then releases it
                    if msg == "shoot": 
                        mouse.press(Button.left)
                        time.sleep(1)
                        mouse.release(Button.left)

                    if msg == "drop item": 
                        mouse.press(Button.right)
                        time.sleep(1)
                        mouse.release(Button.right)

                    if msg == "aim up" or msg =="aimup": 
                        pyautogui.move(0, -200, 1)

                    if msg == "aim down" or msg =="aimdown": 
                        pyautogui.move(0, 200, 1)

                    if msg == "aim left" or msg =="aimleft": 
                        pyautogui.move(-200, 0, 1)

                    if msg == "aim right" or msg =="aimright": 
                        pyautogui.move(200, 0, 1)



                

            except:
                # There was some error trying to process this chat message. Simply move on to the next message.
                print('Encountered an exception while reading chat.')

# Mouse Controller, using pynput
    # pynput.mouse functions are found at: https://pypi.org/project/pynput/
    # NOTE: pyautogui's click() function permanently holds down in DirectX, so I used pynput instead for mouse instead.
mouse = Controller()

###############################################
# DIRECTX KEY CODES
# These codes identify each key on the keyboard.
# Note that DirectX's key codes (or "scan codes") are NOT the same as Windows virtual hex key codes. 
#   DirectX codes are found at: https://docs.microsoft.com/en-us/previous-versions/visualstudio/visual-studio-6.0/aa299374(v=vs.60)
Q = 0x10
W = 0x11
E = 0x12
R = 0x13
T = 0x14
Y = 0x15
U = 0x16
I = 0x17
O = 0x18
P = 0x19
A = 0x1E
S = 0x1F
D = 0x20
F = 0x21
G = 0x22
H = 0x23
J = 0x24
K = 0x25
L = 0x26
Z = 0x2C
X = 0x2D
C = 0x2E
V = 0x2F
B = 0x30
N = 0x31
M = 0x32
ESC = 0x01
ONE = 0x02
TWO = 0x03
THREE = 0x04
FOUR = 0x05
FIVE = 0x06
SIX = 0x07
SEVEN = 0x08
EIGHT = 0x09
NINE = 0x0A
ZERO = 0x0B
MINUS = 0x0C
EQUALS = 0x0D
BACKSPACE = 0x0E
SEMICOLON = 0x27
TAB = 0x0F
CAPS = 0x3A
ENTER = 0x1C
LEFT_CONTROL = 0x1D
LEFT_ALT = 0x38
LEFT_SHIFT = 0x2A
SPACE = 0x39
DELETE = 0x53
COMMA = 0x33
PERIOD = 0x34
BACKSLASH = 0x35
NUMPAD_0 = 0x52
NUMPAD_1 = 0x4F
NUMPAD_2 = 0x50
NUMPAD_3 = 0x51
NUMPAD_4 = 0x4B
NUMPAD_5 = 0x4C
NUMPAD_6 = 0x4D
NUMPAD_7 = 0x47
NUMPAD_8 = 0x48
NUMPAD_9 = 0x49
NUMPAD_PLUS = 0x4E
NUMPAD_MINUS = 0x4A
LEFT_ARROW = 0xCB
RIGHT_ARROW = 0xCD
UP_ARROW = 0xC8
DOWN_ARROW = 0xD0
LEFT_MOUSE = 0x100
RIGHT_MOUSE = 0x101
MIDDLE_MOUSE = 0x102
MOUSE3 = 0x103
MOUSE4 = 0x104
MOUSE5 = 0x105
MOUSE6 = 0x106
MOUSE7 = 0x107
MOUSE_WHEEL_UP = 0x108
MOUSE_WHEEL_DOWN = 0x109
########################################################


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
        defultgame()
        print("running defult twitch plays profile")
        gamerunning = 1
        

if gameselect == 2 and gamerunning == 0:
        newvegas()
        print("running fallout new vegas twitch plays profile")
        gamerunning = 1

if gameselect == 3 and gamerunning == 0:
        minecraft()
        print("running minecraft twitch plays profile")
        gamerunning = 1

if gameselect == 4 and gamerunning == 0:
        openworldgame()
        print("running open world twitch plays profile")
        gamerunning = 1

if gameselect == 5 and gamerunning == 0:
        destinygame()
        print("running destiny twitch plays profile")
        gamerunning = 1;   



