import requests
import tkinter as tk
import keyboard
import pyautogui
from tkhtmlview import HTMLLabel

window = tk.Tk()
window.title("Rockzer")
window.geometry("1920x1080")

url = tk.Entry(window, width=250)
url.pack()

def searching():
    try:
        finalUrl = url.get()
        if not finalUrl.startswith("https://"):
            finalUrl = "https://" + finalUrl
        response = requests.get(finalUrl)
        text = tk.Label(text=f"url{response.status_code}")
        text.pack()
        pageText = HTMLLabel(window, html=response.text, width=60, height=60)
        pageText.pack(fill="both")
        if(response.status_code == 200):
            responseText = requests.get(response.text)
        else:
            print("Site doesn't existe")
    except Exception as e:
        print(e)

search = tk.Button(window, text="Search", command=searching)
search.pack()
if(keyboard.is_pressed("Enter")):
    screenshotI = pyautogui.screenshot()
    screenshotI.save("screenshot.png")
    ScreenshotWarning = tk.Label(window,text="Вы сделали скриншот")
    ScreenshotWarning.pack()
    

window.mainloop()
