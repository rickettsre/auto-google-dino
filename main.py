import pyautogui
from PIL import ImageGrab
from PIL import ImageOps
import numpy as np
from time import sleep
import webbrowser

url = "https://elgoog.im/t-rex/"
chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe"
# chrome_path = "/opt/google/chrome/chrome"
# Use a free app to get the current position of the dino will be dependent on screen size
dino_position = (120, 551)


def start_browser(url):
    webbrowser.register("chrome", None, webbrowser.BackgroundBrowser(chrome_path))
    webbrowser.get("chrome").open_new(url)
    sleep(5)


def jump():
    pyautogui.press("up")


def image_grab():
    hit_box = ImageGrab.grab(
        bbox=(
            dino_position[0] + 50,  # left x
            dino_position[1],  # left y
            dino_position[0] + 145,  # width
            dino_position[1] + 5,  # height
        )
    )
    im = ImageOps.grayscale(hit_box)
    colours = np.array(im.getcolors())
    return np.sum(colours)


def main():
    start_browser(url)
    jump()
    while True:
        if image_grab() > 730:
            jump()


if __name__ == "__main__":
    main()
