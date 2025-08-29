import requests
import tkinter as tk
import pyautogui
# from tkinterweb import HtmlFrame - were replaced by pyQt6 at v0.3.1 (ROCKZER VANTA --prealpha)
# from tkhtmlview import HTMLLabel - were replaced by HtmlFrame at 0.3 (ROCKZER)
import webview
import threading




window = tk.Tk()
window.title("Rockzer")
window.geometry("1920x1080")
window.configure(bg="#292600") 
window.resizable(height=False,width=False)
window.attributes("-fullscreen",True)
# htmlScreenLader = HtmlFrame(window)


url = tk.Entry(window, width=250)
url.configure(bg="#FFFFFF",fg="#292600",relief="flat",highlightbackground="#292600",highlightcolor="#FFFFFF")
url.pack()





def searching():
    
    
    try:
        finalUrl = url.get()
        if not finalUrl.startswith("https://"):
            finalUrl = "https://" + finalUrl
        response = requests.get(finalUrl)
        def GetEmbeededCode():
            EmbeededCodeWindow = tk.Tk()
            EmbeededCodeText = tk.Label(EmbeededCodeWindow,text=response.text)
            EmbeededCodeText.pack()
            EmbeededCodeWindow.title(f"Embeedeed code of {finalUrl}")
            EmbeededCodeWindow.mainloop()
        embedeedCodeButton = tk.Button(window,text="Embeeded code",command=GetEmbeededCode)
        embedeedCodeButton.configure(fg="#FFFFFF",bg="#292600",highlightbackground="#FAC723",highlightcolor="#212022")
        embedeedCodeButton.pack()  
        text = tk.Label(text=f"url{response.status_code}")
        text.pack()
        browser = webview.create_window("browser",finalUrl,height=1024,width=1940,x=0,y=100,frameless=True,resizable=False,easy_drag=False)
        webview.start(gui="edgechromium")

        # htmlScreenLader.set_content("")
        # htmlScreenLader.load_website(finalUrl)
        # htmlScreenLader.pack(fill="both")

        
        


        if(response.status_code == 200):
            responseText = requests.get(response.text)
        else:
            print("Site doesn't existe")
    except Exception as e:
        print(e)

search = tk.Button(window, text="Search", command=searching)
search.configure(fg="#FFFFFF",bg="#292600",highlightbackground="#FAC723",highlightcolor="#212022")


def utilitsFUNC():
    utilitsWindow = tk.Tk()
    utilitsWindow.title("Утилиты")

    def settings():
        settingsWindow = tk.Tk()
        settingsWindow.title("Settings")
        settingsWindow.geometry("800x600")
        # settingsText = tk.Label(settingsWindow,text="Задний фон")
        # settingsText.configure(fg="#292600")
        # settingsButtonRed = tk.Button(settingsWindow,text="RED",command=turningToRed)
        # settingsButtonRed.configure(fg="#FFFFFF",bg="#292600",highlightbackground="#FAC723",highlightcolor="#212022")
        # def ChanigngColor():
        #     window.configure(bg=colorchoserEntryVALUE)
        customBkText =tk.Label(settingsWindow,text="Задний фон")
        customBkText.pack()
        colorchoserEntry =tk.Entry(settingsWindow)
        colorchoserEntry.pack()
        customBkBTN = tk.Entry(settingsWindow)
        def chaingingColor():
            colorchoserEntryVALUE = colorchoserEntry.get()
            colorchoserEntryBGVALUE = customBkBTN.get()
            window.configure(bg=colorchoserEntryVALUE)
            url.configure(bg=colorchoserEntryBGVALUE)
            screenshotBt.configure(bg=colorchoserEntryBGVALUE)
            search.configure(bg=colorchoserEntryBGVALUE)
            print(colorchoserEntryVALUE)
        customBkBTNText =tk.Label(settingsWindow,text="Задний фон кнопок")
        customBkBTNText.pack()
        customBkBTN.pack()
        settingsButtonBlack = tk.Button(settingsWindow,text="Применить",command=chaingingColor)
        settingsButtonBlack.configure(fg="#FFFFFF",bg="#292600",highlightbackground="#FAC723",highlightcolor="#212022")
        settingsButtonBlack.pack()

        
        # settingsText.pack()
        # settingsButtonRed.pack()
        settingsWindow.mainloop()

    screenshotBt = tk.Button(utilitsWindow,text="Took a screenshot",command=screenshotFunc)
    settings = tk.Button(utilitsWindow,text="Настройки",command=settings)
    screenshotBt.pack()
    settings.pack()
    utilitsWindow.mainloop()



utilits = tk.Button(window,text="Утилиты",command=utilitsFUNC)
utilits.pack()


def screenshotFunc():
    nice = pyautogui.screenshot()
    nice.save("photo.png")  

search.pack()

if(pyautogui.position() > (0,100)):
    window.mainloop()
if(pyautogui.position() < (0,100)):
    webview.start()




window.mainloop()

