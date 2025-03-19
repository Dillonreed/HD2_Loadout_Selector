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

# Setting Default Loadout
stratagem1 = Stratagem("500Kg Bomb", "Stratagem List/Eagles/500_Bomb.txt", "Assets/Eagles/500_Bomb.png")
stratagem2 = Stratagem("Anti-Tank Mines", "Stratagem List/Emplacements/Anti-Tank_Mines.txt", "Assets/Emplacements/Anti-Tank_Mines.png")
stratagem3 = Stratagem("Stalwart", "Stratagem List/Support Weapons/Stalwart.txt", "Assets/Support Weapons/Stalwart.png")
stratagem4 = Stratagem("Gas Guard Dog", "Stratagem List/Backpacks/Gas_Guard_Dog.txt", "Assets/Backpacks/Gas_Guard_Dog.png")

# Create tkinter object
app = tk.Tk()

# Global Attributes
backgroundColour = "grey"
textFont = "Arial"
h1Size = 20
h2Size = 15
h3Size = 11

# Tkinter window attributes
app.title("HD2 Loadout Selector")
app.configure(bg=backgroundColour)

# Layout configuration
# Header
headerFrame = tk.Frame(master=app, relief="groove", bd=5, bg=backgroundColour)
headerFrame.pack(fill="both")

# Body
bodyFrame = tk.Frame(master=app, bg=backgroundColour)
bodyFrame.pack()
# Stratagem 1
stratagem1Frame = tk.Frame(master=bodyFrame, relief="groove", bd=5, bg=backgroundColour)
stratagem1Frame.grid(row=0, column=0)
# Stratagem 2
stratagem2Frame = tk.Frame(master=bodyFrame, relief="groove", bd=5, bg=backgroundColour)
stratagem2Frame.grid(row=0, column=1)
# Stratagem 3
stratagem3Frame = tk.Frame(master=bodyFrame, relief="groove", bd=5, bg=backgroundColour)
stratagem3Frame.grid(row=0, column=2)
# Stratagem 4
stratagem4Frame = tk.Frame(master=bodyFrame, relief="groove", bd=5, bg=backgroundColour)
stratagem4Frame.grid(row=0, column=3)

# Footer
footerFrame= tk.Frame(master=app, relief="groove", bd=5, bg=backgroundColour)
# Make the grid fill the whole space available
footerFrame.grid_rowconfigure(0, weight=1)
footerFrame.grid_columnconfigure(0, weight=1)
footerFrame.grid_columnconfigure(1, weight=1)
footerFrame.grid_columnconfigure(2, weight=1)
footerFrame.grid_columnconfigure(3, weight=1)
footerFrame.pack(fill="both")
# Mission Stratagems
missionStratagemFrame = tk.Frame(master=footerFrame, bg=backgroundColour)
missionStratagemFrame.grid(row=0, column=0, sticky="nsew")
# Save Button
saveButtonFrame = tk.Frame(master=footerFrame, bg=backgroundColour)
saveButtonFrame.grid(row=0, column=1, sticky="nsew")
# Run Button
runButtonFrame = tk.Frame(master=footerFrame, bg=backgroundColour)
runButtonFrame.grid(row=0, column=2, sticky="nsew")
# Stop Button
stopButtonFrame = tk.Frame(master=footerFrame, bg=backgroundColour)
stopButtonFrame.grid(row=0, column=3, sticky="nsew")

# Adding Content
# ------------------------------------------------------------------------------------
# Header Section
# ------------------------------------------------------------------------------------
# Title
titleLabel = tk.Label(headerFrame, text="HD2 Loadout Selector", font=(textFont, h1Size), bg=backgroundColour)
titleLabel.grid(row=0, column=0)

# TODO Add instruction label

# HD2 Logo
# Load & configure the image
hd2Logo = Image.open("Assets/HD2LogoSmaller.png")
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

# -------------------------------------------------------------------------------------
# Body
# -------------------------------------------------------------------------------------

# Function to open stratagem category selector
def openStratagemCategorySelector(stratagemSlot):
    # Create tkinter object
    categorySelector = tk.Toplevel()

    # Tkinter window attributes
    categorySelector.title("Stratagem Category Selector")
    categorySelector.configure(bg=backgroundColour)

    # cS = category selector

    # Layout configuration
    # Header
    cSHeaderFrame = tk.Frame(master=categorySelector, relief="groove", bd=5, bg=backgroundColour)
    cSHeaderFrame.pack(fill="both")

    # Body
    cSBodyFrame = tk.Frame(master=categorySelector, relief="groove", bd=5, bg=backgroundColour)
    cSBodyFrame.pack(fill="both")

    # Adding content
    # ---------------------------------------------------------------------------------
    # Header
    # ---------------------------------------------------------------------------------

    cSTitleLabel = tk.Label(master=cSHeaderFrame, text="Stratagem Category Selector", font=(textFont, h1Size), bg=backgroundColour)
    cSTitleLabel.grid(row=0, column=0)

    # ---------------------------------------------------------------------------------
    # Body TODO Add functions to buttons
    # ---------------------------------------------------------------------------------
    # Orbitals
    # Load image
    orbitalsImage = Image.open("Assets/Orbitals/Precision_Strike.png")
    # Convert the image to be usable by tkinter
    orbitalsImageTk = ImageTk.PhotoImage(orbitalsImage)
    # Create orbitals Button
    orbitalsButton = tk.Button(master=cSBodyFrame, text="Orbitals", font=(textFont, h2Size), image=orbitalsImageTk, compound="left", bg=backgroundColour)
    orbitalsButton.pack(fill="both")

    # Eagles
    # Load image
    eaglesImage = Image.open("Assets/Eagles/500_Bomb.png")
    # Convert the image to be usable by tkinter
    eaglesImageTk = ImageTk.PhotoImage(eaglesImage)
    # Create eagles Button
    eaglesButton = tk.Button(master=cSBodyFrame, text="Eagles", font=(textFont, h2Size), image=eaglesImageTk,
                               compound="left", bg=backgroundColour)
    eaglesButton.pack(fill="both")

    # Support Weapons
    # Load image
    supportWeaponsImage = Image.open("Assets/Support Weapons/Railgun.png")
    # Convert the image to be usable by tkinter
    supportWeaponsImageTk = ImageTk.PhotoImage(supportWeaponsImage)
    # Create support weapons Button
    supportWeaponsButton = tk.Button(master=cSBodyFrame, text="Support Weapons", font=(textFont, h2Size), image=supportWeaponsImageTk,
                             compound="left", bg=backgroundColour)
    supportWeaponsButton.pack(fill="both")

    # Backpacks
    # Load image
    backpacksImage = Image.open("Assets/Backpacks/Jump_Pack.png")
    # Convert the image to be usable by tkinter
    backpacksImageTk = ImageTk.PhotoImage(backpacksImage)
    # Create backpacks Button
    backpacksButton = tk.Button(master=cSBodyFrame, text="Backpacks", font=(textFont, h2Size), image=backpacksImageTk,
                             compound="left", bg=backgroundColour)
    backpacksButton.pack(fill="both")

    # Emplacements
    # Load image
    emplacementsImage = Image.open("Assets/Emplacements/Gatling_Sentry.png")
    # Convert the image to be usable by tkinter
    emplacementsImageTk = ImageTk.PhotoImage(emplacementsImage)
    # Create Orbitals Button
    emplacementsButton = tk.Button(master=cSBodyFrame, text="Emplacements", font=(textFont, h2Size), image=emplacementsImageTk,
                             compound="left", bg=backgroundColour)
    emplacementsButton.pack(fill="both")

    # Vehicles
    # Load image
    vehiclesImage = Image.open("Assets/Vehicles/Fast_Recon_Vehicles.png")
    # Convert the image to be usable by tkinter
    vehiclesImageTk = ImageTk.PhotoImage(vehiclesImage)
    # Create Orbitals Button
    vehiclesButton = tk.Button(master=cSBodyFrame, text="Vehicles", font=(textFont, h2Size), image=vehiclesImageTk,
                             compound="left", bg=backgroundColour)
    vehiclesButton.pack(fill="both")

    # Run the application
    categorySelector.mainloop()

# -------------------------------------------------------------------------------------
# Stratagem 1
# -------------------------------------------------------------------------------------
# Stratagem 1 title
stratagem1TitleLabel = tk.Label(stratagem1Frame, text="Stratagem 1", font=(textFont, h2Size), bg=backgroundColour)
stratagem1TitleLabel.grid(row=0, column=0)

# Stratagem 1 image (500Kg by default)
# Load image
stratagem1Image = Image.open(stratagem1.getImagePath())
# Convert image to be usable by tkinter
stratagem1ImageTk = ImageTk.PhotoImage(stratagem1Image)

# Create button with image on it
stratagem1Button = tk.Button(master=stratagem1Frame, image=stratagem1ImageTk, command= lambda: openStratagemCategorySelector("1"), bg=backgroundColour)
stratagem1Button.grid(row=1, column=0)

# Create label with stratagem name
stratagem1Label = tk.Label(master=stratagem1Frame, text=stratagem1.getName(), font=(textFont, h3Size), bg=backgroundColour)
stratagem1Label.grid(row=2, column=0)

# Create label with which key this stratagem is bound to
stratagem1KeybindLabel = tk.Label(master=stratagem1Frame, text="Bound to : Numpad 4", font=(textFont, h3Size), bg=backgroundColour)
stratagem1KeybindLabel.grid(row=3, column=0)

# -------------------------------------------------------------------------------------
# Stratagem 2
# -------------------------------------------------------------------------------------
# Stratagem 2 title
stratagem2TitleLabel = tk.Label(stratagem2Frame, text="Stratagem 2", font=(textFont, h2Size), bg=backgroundColour)
stratagem2TitleLabel.grid(row=0, column=0)

# Stratagem 2 image (Anti-Tank mines by default)
# Load image
stratagem2Image = Image.open(stratagem2.getImagePath())
# Convert image to be usable by tkinter
stratagem2ImageTk = ImageTk.PhotoImage(stratagem2Image)

# Create button with image on it
stratagem2Button = tk.Button(master=stratagem2Frame, image=stratagem2ImageTk, command= lambda: openStratagemCategorySelector("2"), bg=backgroundColour)
stratagem2Button.grid(row=1, column=0)

# Create label with stratagem name
stratagem2Label = tk.Label(master=stratagem2Frame, text=stratagem2.getName(), font=(textFont, h3Size), bg=backgroundColour)
stratagem2Label.grid(row=2, column=0)

# Create label with which key this stratagem is bound to
stratagem2KeybindLabel = tk.Label(master=stratagem2Frame, text="Bound to : Numpad 6", font=(textFont, h3Size), bg=backgroundColour)
stratagem2KeybindLabel.grid(row=3, column=0)

# -------------------------------------------------------------------------------------
# Stratagem 3
# -------------------------------------------------------------------------------------
# Stratagem 3 title
stratagem3TitleLabel = tk.Label(stratagem3Frame, text="Stratagem 3", font=(textFont, h2Size), bg=backgroundColour)
stratagem3TitleLabel.grid(row=0, column=0)

# Stratagem 3 image (Stalwart by default)
# Load image
stratagem3Image = Image.open(stratagem3.getImagePath())
# Convert image to be usable by tkinter
stratagem3ImageTk = ImageTk.PhotoImage(stratagem3Image)

# Create button with image on it
stratagem3Button = tk.Button(master=stratagem3Frame, image=stratagem3ImageTk, command= lambda: openStratagemCategorySelector("3"), bg=backgroundColour)
stratagem3Button.grid(row=1, column=0)

# Create label with stratagem name
stratagem3Label = tk.Label(master=stratagem3Frame, text=stratagem3.getName(), font=(textFont, h3Size), bg=backgroundColour)
stratagem3Label.grid(row=2, column=0)

# Create label with which key this stratagem is bound to
stratagem3KeybindLabel = tk.Label(master=stratagem3Frame, text="Bound to : Numpad 7", font=(textFont, h3Size), bg=backgroundColour)
stratagem3KeybindLabel.grid(row=3, column=0)

# -------------------------------------------------------------------------------------
# Stratagem 4
# -------------------------------------------------------------------------------------
# Stratagem 4 title
stratagem4TitleLabel = tk.Label(stratagem4Frame, text="Stratagem 4", font=(textFont, h2Size), bg=backgroundColour)
stratagem4TitleLabel.grid(row=0, column=0)

# Stratagem 4 image (Gas Guard Dog by default)
# Load image
stratagem4Image = Image.open(stratagem4.getImagePath())
# Convert image to be usable by tkinter
stratagem4ImageTk = ImageTk.PhotoImage(stratagem4Image)

# Create button with image on it
stratagem4Button = tk.Button(master=stratagem4Frame, image=stratagem4ImageTk, command= lambda: openStratagemCategorySelector("4"), bg=backgroundColour)
stratagem4Button.grid(row=1, column=0)

# Create label with stratagem name
stratagem4Label = tk.Label(master=stratagem4Frame, text=stratagem4.getName(), font=(textFont, h3Size), bg=backgroundColour)
stratagem4Label.grid(row=2, column=0)

# Create label with which key this stratagem is bound to
stratagem4KeybindLabel = tk.Label(master=stratagem4Frame, text="Bound to : Numpad 9", font=(textFont, h3Size), bg=backgroundColour)
stratagem4KeybindLabel.grid(row=3, column=0)

# -------------------------------------------------------------------------------------
# Footer
# -------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------
# Mission Stratagems
# -------------------------------------------------------------------------------------
# Reinforce
# Load the image
reinforceImage = Image.open("Assets/Mission Stratagems/Smaller Versions/Reinforce.png")
# Convert image to be usable by tkinter
reinforceImageTk = ImageTk.PhotoImage(reinforceImage)
# Create reinforce image label
reinforceImageLabel = tk.Label(master=missionStratagemFrame, image=reinforceImageTk, bg=backgroundColour)
reinforceImageLabel.grid(row=0, column=0)
# Create reinforce text label to show which key this stratagem is bound to
reinforceLabel = tk.Label(master=missionStratagemFrame, text="Reinforce : Numpad 1", font=(textFont, h3Size), bg=backgroundColour)
reinforceLabel.grid(row=0, column=1)

# Resupply
# Load the image
resupplyImage = Image.open("Assets/Mission Stratagems/Smaller Versions/Resupply.png")
# Convert image to be usable by tkinter
resupplyImageTk = ImageTk.PhotoImage(resupplyImage)
# Create resupply reinforce image label
resupplyImageLabel = tk.Label(master=missionStratagemFrame, image=resupplyImageTk, bg=backgroundColour)
resupplyImageLabel.grid(row=1, column=0)
# Create resupply text label to show which key this stratagem is bound to
resupplyLabel = tk.Label(master=missionStratagemFrame, text="Resupply : Numpad 2", font=(textFont, h3Size), bg=backgroundColour)
resupplyLabel.grid(row=1, column=1)

# Eagle Resupply
# Load the image
eagleResupplyImage = Image.open("Assets/Mission Stratagems/Smaller Versions/Eagle_Resupply.png")
# Convert image to be usable by tkinter
eagleResupplyImageTk = ImageTk.PhotoImage(eagleResupplyImage)
# Create eagle resupply image label
eagleResupplyImageLabel = tk.Label(master=missionStratagemFrame, image=eagleResupplyImageTk, bg=backgroundColour)
eagleResupplyImageLabel.grid(row=2, column=0)
# Create eagle resupply text label to show which key this stratagem is bound to
eagleResupplyLabel = tk.Label(master=missionStratagemFrame, text="Eagle Resupply : Numpad 3", font=(textFont, h3Size), bg=backgroundColour)
eagleResupplyLabel.grid(row=2, column=1)

# Hellbomb
# Load the image
hellbombImage = Image.open("Assets/Mission Stratagems/Smaller Versions/Hellbomb.png")
# Convert image to be usable by tkinter
hellbombImageTk = ImageTk.PhotoImage(hellbombImage)
# Create hellbomb image label
hellbombImageLabel = tk.Label(master=missionStratagemFrame, image=hellbombImageTk, bg=backgroundColour)
hellbombImageLabel.grid(row=3, column=0)
# Create hellbomb text label to show which key this stratagem is bound to
hellbombLabel = tk.Label(master=missionStratagemFrame, text="Hellbomb : Numpad 8", font=(textFont, h3Size), bg=backgroundColour)
hellbombLabel.grid(row=3, column=1)

# -------------------------------------------------------------------------------------
# Save Button
# -------------------------------------------------------------------------------------
# Create save button TODO Add functions to buttons
saveButton = tk.Button(master=saveButtonFrame, text="Save", font=(textFont, h2Size))
saveButton.pack(fill="both", expand=True)

# -------------------------------------------------------------------------------------
# Run Button
# -------------------------------------------------------------------------------------
# Create run button TODO Add functions to buttons
runButton = tk.Button(master=runButtonFrame, text="Run", font=(textFont, h2Size))
runButton.pack(fill="both", expand=True)

# -------------------------------------------------------------------------------------
# Stop Button
# -------------------------------------------------------------------------------------
# Create run button TODO Add functions to buttons
stopButton = tk.Button(master=stopButtonFrame, text="Stop", font=(textFont, h2Size))
stopButton.pack(fill="both", expand=True)

# Run the application
app.mainloop()