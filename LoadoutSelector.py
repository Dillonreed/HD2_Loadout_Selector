import tkinter as tk
from PIL import Image, ImageTk

# Used to create a AutoHotKey script for selected stratagems for Helldivers 2

# Class for representing a stratagem
class Stratagem:
    def __init__(self, name=None, keyCombinationPath=None, imagePath=None):
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
    def __init__(self, stratagem1=None, stratagem2=None, stratagem3=None, stratagem4=None):
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

# Setting Default Loadout TODO Add images
stratagem1 = Stratagem("500Kg Bomb", "Stratagem List/Eagles/500_Bomb.txt")
stratagem2 = Stratagem("Anti-Tank Mines", "Stratagem List/Emplacements/Anti-Tank_Mines.txt")
stratagem3 = Stratagem("Stalwart", "Stratagem List/Support Weapons/Stalwart.txt")
stratagem4 = Stratagem("Gas Guard Dog", "Stratagem List/Backpacks/Gas_Guard_Dog.txt")

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
# Stratagem 1
stratagem1Frame = tk.Frame(master=bodyFrame, bg=backgroundColour)
stratagem1Frame.grid(row=0, column=0)
# Stratagem 2
stratagem2Frame = tk.Frame(master=bodyFrame, bg=backgroundColour)
stratagem2Frame.grid(row=0, column=1)
# Stratagem 3
stratagem3Frame = tk.Frame(master=bodyFrame, bg=backgroundColour)
stratagem3Frame.grid(row=0, column=2)
# Stratagem 4
stratagem4Frame = tk.Frame(master=bodyFrame, bg=backgroundColour)
stratagem4Frame.grid(row=0, column=3)

# Footer
footerFrame= tk.Frame(master=app, bg=backgroundColour)
footerFrame.pack()

# Adding Content
# ------------------------------------------------------------------------------------
# Header Section
# ------------------------------------------------------------------------------------
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

# Github link TODO Add hyperlink functionality
githubLink = "https://github.com/Dillonreed/HD2_Loadout_Selector"
githubLinkLabel = tk.Label(headerFrame, text=githubLink, bg=backgroundColour)
githubLinkLabel.grid(row=0, column=3)

# Run the application
app.mainloop()