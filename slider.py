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
    imagePaths = ["./images/n1.jpg", "./images/n12.jpg", "./images/n9.jpg", "./images/n4.jpg", "./images/n10.jpg", "./images/n7.jpg", "./images/n8.jpg", "./images/n11.jpg", "./images/n2.jpg"]
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
        basewidth = 700
        width, height = image.size
        if(width > height):
            basewidth = 1200

        wpercent = (basewidth / float(width))
        hsize = int((float(height) * float(wpercent)))
        newImg = image.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
        return newImg
        
    def next_image(self):
        img = self.resize(Image.open(imagePaths[self.counter]))
        imgtk = ImageTk.PhotoImage(img)
        
        #change panel image
        self.panel.configure(image=imgtk)
        self.panel.image = imgtk

        self.counter += 1
        if self.counter >= numImages:
            self.counter = 0

        self.root.after(5000, self.next_image)

def exit(event):
    import sys; sys.exit()

app = Slider(root, panel)
app.next_image()
root.bind('<Return>', exit)
root.mainloop()

