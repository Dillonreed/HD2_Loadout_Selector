import tkinter as tk
from PIL import Image, ImageTk

# Used to create a AutoHotKey script for selected stratagems for Helldivers 2

# Class for representing a stratagem
class Stratagem:
    def __init__(self, name, keyCombinationPath, imagePath):
        self.name = name
        self.keyCombinationPath = keyCombinationPath
        self.imagePath = imagePath

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getKeyCombinationPath(self):
        return self.keyCombinationPath

    def setKeyCombinationPath(self, keyCombinationPath):
        self.keyCombinationPath = keyCombinationPath

    def getImagePath(self):
        return self.imagePath

    def __str__(self):
        return f"""
        Name : {self.name}
        Key Combination Path : {self.keyCombinationPath}
        Image Path : {self.imagePath}
        """


# Class for representing a loadout
class Loadout:
    def __init__(self, stratagem1 = None, stratagem2 = None, stratagem3 = None, stratagem4 = None):
        self.stratagem1 = stratagem1
        self.stratagem2 = stratagem2
        self.stratagem3 = stratagem3
        self.stratagem4 = stratagem4

    def getStratagem1(self):
        return self.stratagem1

    def setStratagem1(self, stratagem):
        self.stratagem1 = stratagem

    def getStratagem2(self):
        return self.stratagem2

    def setStratagem2(self, stratagem):
        self.stratagem2 = stratagem

    def getStratagem3(self):
        return self.stratagem3

    def setStratagem3(self, stratagem):
        self.stratagem3 = stratagem

    def getStratagem4(self):
        return self.stratagem4

    def setStratagem4(self, stratagem):
        self.stratagem4 = stratagem

    def __str__(self):
        return f"""
        Stratagem 1 : {self.stratagem1}
        Stratagem 2 : {self.stratagem2}
        Stratagem 3 : {self.stratagem3}
        Stratagem 4 : {self.stratagem4}
        """

# Create Loadout Object
loadout = Loadout()

# Create tkinter object
app = tk.Tk()

# Global Attributes
backgroundColour = "grey"

# Tkinter window attributes
app.title("HD2 Loadout Selector")
app.configure(bg="grey")

# Layout configuration
# Header
headerFrame = tk.Frame(master=app, bg=backgroundColour)
headerFrame.pack()

# Body
bodyFrame = tk.Frame(master=app, bg=backgroundColour)
bodyFrame.pack()

# Footer
footerFrame= tk.Frame(master=app, bg=backgroundColour)
footerFrame.pack()

# Adding Content
# Title
titleLabel = tk.Label(headerFrame, text="HD2 Loadout Selector", font=("Arial", 20), bg=backgroundColour)
titleLabel.grid(row=0, column=0)

# HD2 Logo
# Load & configure the image
hd2Logo = Image.open("Assets/HD2Logo.png")
hd2Logo.resize((5, 5))
# Convert image to be usable by tkinter
hd2LogoTk = ImageTk.PhotoImage(hd2Logo)

# Place the logo in the window
logoLabel = tk.Label(headerFrame, image=hd2LogoTk, bg=backgroundColour)
logoLabel.grid(row=0, column=1)

# 

# Run the application
app.mainloop()