import Tkinter as tk
from PIL import Image, ImageTk
import os
import time
import fnmatch

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
#build first panel
img = ImageTk.PhotoImage(Image.open(imagePaths[0]).resize((700,1000)))
panel = tk.Label(root, image=img)
panel.pack(side = "bottom", fill = "both", expand = "yes")

class Slider:
    def __init__(self, root, panel):
        self.root = root
        self.panel = panel
        self.counter = 0

    def next_image(self):
        img = ImageTk.PhotoImage(Image.open(imagePaths[self.counter]).resize((700, 1000)))
        
        #change panel image
        self.panel.configure(image=img)
        self.panel.image = img

        self.counter += 1
        if self.counter >= numImages:
            self.counter = 0

        self.root.after(5000, self.next_image)

app = Slider(root, panel)
app.next_image()
root.mainloop()

