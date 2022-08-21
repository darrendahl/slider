import Tkinter as tk
import PIL
from PIL import Image, ImageTk
import os
import time
import fnmatch
import sys

#initialize tkinter
root = tk.Tk()
root.overrideredirect(True)
root.overrideredirect(False)
root.attributes('-fullscreen',True)

#define images
imagePaths = []
folders = []


for (path, dirnames, filenames) in os.walk('/media/usb0'):
    folders.extend(os.path.join(path, name) for name in dirnames)
    imagePaths.extend(os.path.join(path, name) for name in fnmatch.filter(filenames, "[!.]*.jpg"))

numImages = len(imagePaths)
print(imagePaths)

#for testing purposes
if(numImages <= 0):
    imagePaths = ["./images/start.jpg"]
    numImages = len(imagePaths)


if(numImages <= 0):
    print("No Images, Aborting...")
    sys.exit()    

#build first panel
img = ImageTk.PhotoImage(Image.open(imagePaths[0]).resize((700,1000)))
panel = tk.Label(root, image=img)
panel.pack(side = "bottom", fill = "both", expand = "yes")

class Slider:
    def __init__(self, root, panel):
        self.root = root
        self.panel = panel
        self.counter = 0
    
    def resize(self, image):
        basewidth = 800
        width, height = image.size
        if(width > height):
            basewidth = 1200

        wpercent = (basewidth / float(width))
        hsize = int((float(height) * float(wpercent)))
        newImg = image.resize((basewidth, hsize))
        return newImg
        
    def next_image(self):
        img = self.resize(Image.open(imagePaths[self.counter]))
        #imgtk = ImageTk.PhotoImage(Image.open(imagePaths[self.counter]).resize((700, 1000)))
        imgtk = ImageTk.PhotoImage(img)
        
        #change panel image
        self.panel.configure(background='black')
        self.panel.configure(image=imgtk)
        self.panel.image = imgtk

        self.counter += 1
        if self.counter >= numImages:
            self.counter = 0

        self.root.after(5000, self.next_image)

app = Slider(root, panel)
app.next_image()
root.bind('<Escape>', lambda e: (e.widget.withdraw(), e.widget.quit()))
root.mainloop()

