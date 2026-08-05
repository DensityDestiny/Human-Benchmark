from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import pyautogui
import mss
import mss.tools
import cv2
import numpy as np
import keyboard


def open_google(website_link, driver):
    driver.get(website_link)
    driver.maximize_window()


def screenshotTest(image):
    mss.tools.to_png(
        image.rgb,
        image.size,
        output="screenshot.png"
    )


def get_pixel(x, y):
    with mss.mss() as sct:
        pic = sct.grab({'mon':1, 'top':y, 'left':x, 'width':1, 'height':1})
        g = pic.pixel(0,0)
    return g


# NOTE: Change monitor variable so that it matches your computer. This is ONLY used for the aim test
# Change x, y to define where you click for the reaction speed test
monitor = {'mon':1, 'top':220, 'left':275, 'width':900, 'height':500}
x, y = 1150, 500


test = input("Enter which test your doing: ")
if test == "testing":
    sct = mss.mss()
    image = sct.grab(monitor)
    screenshotTest(image)
    pyautogui.moveTo(x, y, 0.1)
elif test == "typing":
    driver = webdriver.Chrome()
    open_google("https://humanbenchmark.com/tests/typing", driver)
    while True:
        letters = driver.find_elements(By.CLASS_NAME, 'incomplete')
        text = ""
        for letter in letters:
            text += letter.text
            if letter.text == "":
                text += " "
        time.sleep(0.3)
        pyautogui.hotkey('shift', text[0])
        pyautogui.write(text[1:len(text)], 0.0)
        exit_program = input("Exit? y/n: ")
        if exit_program == "y":
            driver.quit()
            break
elif test == "reaction":
    while True:
        start = input("Start detecting: ")
        time.sleep(2)
        pyautogui.moveTo(x, y)
        color = get_pixel(x, y)
        if color[2] > 150:
            pyautogui.click()
        while True:
            color = get_pixel(x, y)
            if color[1] > 150:
                pyautogui.click()
                break
        exit_program = input("Exit? y/n: ")
        if exit_program == "y":
            break
elif test == "aim":
    template = cv2.imread("target.png", cv2.IMREAD_UNCHANGED)
    template = cv2.cvtColor(template, cv2.COLOR_BGRA2BGR)
    pixel_scale = 2.0
    h, w = template.shape[:-1]
    time.sleep(3.5)
    while True:
        with mss.mss() as sct:
            pic = sct.grab(monitor)
            screenshotTest(pic)
            screen_array = np.array(pic)
            screen_array = cv2.cvtColor(screen_array, cv2.COLOR_BGRA2BGR)
            res = cv2.matchTemplate(screen_array, template, cv2.TM_CCOEFF_NORMED)
            threshold = 0.5
            loc = np.where(res >= threshold)
            if loc[0].size > 0:
                top_left = (loc[1][0], loc[0][0])
                center_x = (top_left[0] + w // 2) / pixel_scale + monitor["left"]
                center_y = (top_left[1] + h // 2) / pixel_scale + monitor["top"]
                pyautogui.click(x=center_x, y=center_y, interval=0.0)
            else:
                break