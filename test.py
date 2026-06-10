import pyautogui
import random
import time

import pygame


# pyautogui.write("Hello",interval=0.1)


# pyautogui.press("enter")


# # pyautogui.hotkey("ctrl","a")

# pyautogui.moveTo(300,500)

# text=input("Enter text :")

text="Himanshu kumar"

pygame.init()

sound=pygame.mixer.Sound(r"C:\Users\SAJLE\Downloads\dragon-studio-keyboard-typing-sound-effect-335503.mp3")

for ch in text:
    pyautogui.write(ch)
    sound.play()
    time.sleep(random.uniform(0.3,0.5))




