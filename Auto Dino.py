import pyautogui,keyboard      # used to automate the functionality of keyboard
from numpy import asarray      # used to understand the picture captured in the matrix form
from PIL import ImageGrab      # to capture the screen shot of the screen
import time    
import webbrowser                # to use functionality of sleep
# chrome://dino  link for the game
# 230 450     581 680


def hit(key):
    pyautogui.keyDown(key)    # press the key mentioned


def iscollide(data):

# creating a rectangle
    for i in range(232,450):
        for j in range(581,680):  
            if data[150,150] == 255:    # chek for day mode/ white screen                                         
                if data[i,j] != 255:    # check if anything(cactus/bird) come inside the rectangle
                    hit("up")
                    return True
            elif data[150,150] < 255:  #check for night mode/black screen
                if data[i,j] != 0:      #check if anything(cactus/bird) come inside the rectangle
                    hit("up")
                    return True


time.sleep(3)

pyautogui.press('space')  # start the game

while True:              

    img = ImageGrab.grab().convert('L')    # Image.grab() will take the screen shot and .convert('L') will convert it into black and white image which is easy to usee
    data = img.load()                      # .load() will convert image into matrix of pixles

    # for i in range(232,450):
    #     for j in range(581,680):                                             
    #         data[i,j] = 145

    # img.show()
    # break

    iscollide(data)    # check whether any obstacle is coming in path
    
    
    if keyboard.is_pressed('s'):    
        break
   