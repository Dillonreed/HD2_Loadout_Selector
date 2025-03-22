import subprocess
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import csv

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

    def setImagePath(self, imagePath):
        self.imagePath = imagePath

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

stratagemsList = [stratagem1, stratagem2, stratagem3, stratagem4]

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
    # Function to open stratagem selector
    def openStratagemSelector(category):
        # Create tkinter object
        stratagemSelector = tk.Toplevel()

        # Tkinter window attributes
        stratagemSelector.title("Stratagem Selector")
        stratagemSelector.configure(bg=backgroundColour)
        stratagemSelector.minsize(400, 400)

        # sS = Stratagem Selector

        # Layout configuration
        # Header
        sSHeaderFrame = tk.Frame(master=stratagemSelector, relief="groove", bd=5, bg=backgroundColour)
        sSHeaderFrame.pack(fill="both")

        # Making body frame scrollable
        # Making outer frame to hold the canvas, body frame and scrollbar
        outerFrame = tk.Frame(master=stratagemSelector)
        outerFrame.pack(fill="both", expand=True)
        # Creating the canvas
        canvas = tk.Canvas(master=outerFrame)
        canvas.pack(side="left", fill="both", expand=True)
        # Creating the scrollbar
        scrollbar = tk.Scrollbar(master=outerFrame, orient="vertical", command=canvas.yview, width=70)
        scrollbar.pack(side="right", fill="y")
        # Configuring the canvas
        canvas.configure(yscrollcommand=scrollbar.set)

        # Body
        sSBodyFrame = tk.Frame(master=canvas, width=10, height=10, bg=backgroundColour)
        sSBodyFrame.pack(fill="both", expand=True)

        # Create the canvas
        def update_canvas(event):
            # Update the scroll region
            canvas.configure(scrollregion=canvas.bbox("all"))
            # Resize the embedded frame
            canvas.itemconfig(canvas_window, width=event.width)

        def _on_mouse_wheel(event):
            canvas.yview_scroll(-1 * (event.delta // 120), "units")

        canvas_window = canvas.create_window((0, 0), window=sSBodyFrame, anchor="nw")

        # When the canvas is scrolled/resized, update it
        canvas.bind("<Configure>", update_canvas)
        # Bind the mouse wheel to scrolling
        stratagemSelector.bind_all("<MouseWheel>", _on_mouse_wheel)

        # Adding content

        # Function to update the main window
        def updateSelectedStratagem(name, keyCombinationPath, imagePath):
            # Update stratagem object with new selected stratagem information
            stratagemsList[stratagemSlot-1].setName(name)
            stratagemsList[stratagemSlot-1].setKeyCombinationPath(keyCombinationPath)
            stratagemsList[stratagemSlot-1].setImagePath(imagePath)

            # Update main window
            # Load image
            newStratagemImage = Image.open(imagePath)
            # Convert image to be usable by tkinter
            newStratagemImageTk = ImageTk.PhotoImage(newStratagemImage)

            # Create lists of tkinter widgets to use to update the specific slot that was selected
            stratagemSlotButtonsList = [stratagem1Button, stratagem2Button, stratagem3Button, stratagem4Button]
            stratagemSlotLabelsList = [stratagem1Label, stratagem2Label, stratagem3Label, stratagem4Label]

            # Update image for stratagem slot button
            stratagemSlotButtonsList[stratagemSlot-1].configure(image=newStratagemImageTk)
            # Added a variable to ensure that each iteration's image is not garbage collected
            stratagemSlotButtonsList[stratagemSlot-1].photo = newStratagemImageTk

            # Update label for stratagem slot
            stratagemSlotLabelsList[stratagemSlot-1].configure(text=name)

            # Destroy category selector and stratagem selector windows
            categorySelector.destroy()

            def onClose():
                # Unbinds the mousewheel watcher to ensure erroneous errors are not thrown once the window has been destroyed
                stratagemSelector.unbind_all("<MouseWheel>")
                stratagemSelector.destroy()
            onClose()

        # -----------------------------------------------------------------------------
        # Header
        # -----------------------------------------------------------------------------
        # Add a title to the page
        sSTitleLabel = tk.Label(master=sSHeaderFrame, text="Stratagem Selector", font=(textFont, h1Size), bg=backgroundColour)
        sSTitleLabel.grid(row=0, column=0)

        # -----------------------------------------------------------------------------
        # Body
        # -----------------------------------------------------------------------------
        # Create stratagem list
        with open(f"Stratagems/{category}StratagemList.csv", mode="r") as stratagemList:
            stratagemListCSV = csv.reader(stratagemList)
            for stratagem in stratagemListCSV:
                # Ignore the top line of the csv
                if stratagem[0] == "name":
                    pass
                else:
                    # stratagem[0] = name
                    # stratagem[2] = imagePath

                    # Load image
                    stratagemImage = Image.open(stratagem[2])
                    # Convert image to be usable by tkinter
                    stratagemImageTk = ImageTk.PhotoImage(stratagemImage)
                    # Create button
                    stratagemButton = tk.Button(master=sSBodyFrame, text=stratagem[0], font=(textFont, h2Size), image=stratagemImageTk, compound="left", anchor="w", command=lambda chosenStratagem=stratagem: updateSelectedStratagem(chosenStratagem[0], chosenStratagem[1], chosenStratagem[2]), bg=backgroundColour)
                    # Added a variable to ensure that each iteration's image is not garbage collected
                    stratagemButton.photo = stratagemImageTk
                    stratagemButton.pack(fill="x", expand=True)

        # Run the application
        stratagemSelector.mainloop()

    # ---------------------------------------------------------------------------------
    # Header
    # ---------------------------------------------------------------------------------
    # Add a title to the page
    cSTitleLabel = tk.Label(master=cSHeaderFrame, text="Stratagem Category Selector", font=(textFont, h1Size), bg=backgroundColour)
    cSTitleLabel.grid(row=0, column=0)

    # ---------------------------------------------------------------------------------
    # Body
    # ---------------------------------------------------------------------------------
    # Orbitals
    # Load image
    orbitalsImage = Image.open("Assets/Orbitals/Precision_Strike.png")
    # Convert the image to be usable by tkinter
    orbitalsImageTk = ImageTk.PhotoImage(orbitalsImage)
    # Create orbitals Button
    orbitalsButton = tk.Button(master=cSBodyFrame, text="Orbitals", font=(textFont, h2Size), image=orbitalsImageTk, compound="left", anchor="w", command=lambda: openStratagemSelector("Orbitals"), bg=backgroundColour)
    orbitalsButton.pack(fill="both")

    # Eagles
    # Load image
    eaglesImage = Image.open("Assets/Eagles/500_Bomb.png")
    # Convert the image to be usable by tkinter
    eaglesImageTk = ImageTk.PhotoImage(eaglesImage)
    # Create eagles Button
    eaglesButton = tk.Button(master=cSBodyFrame, text="Eagles", font=(textFont, h2Size), image=eaglesImageTk, compound="left", anchor="w", command=lambda: openStratagemSelector("Eagles"), bg=backgroundColour)
    eaglesButton.pack(fill="both")

    # Support Weapons
    # Load image
    supportWeaponsImage = Image.open("Assets/Support Weapons/Railgun.png")
    # Convert the image to be usable by tkinter
    supportWeaponsImageTk = ImageTk.PhotoImage(supportWeaponsImage)
    # Create support weapons Button
    supportWeaponsButton = tk.Button(master=cSBodyFrame, text="Support Weapons", font=(textFont, h2Size), image=supportWeaponsImageTk, anchor="w", compound="left", command=lambda: openStratagemSelector("SupportWeapons"), bg=backgroundColour)
    supportWeaponsButton.pack(fill="both")

    # Backpacks
    # Load image
    backpacksImage = Image.open("Assets/Backpacks/Jump_Pack.png")
    # Convert the image to be usable by tkinter
    backpacksImageTk = ImageTk.PhotoImage(backpacksImage)
    # Create backpacks Button
    backpacksButton = tk.Button(master=cSBodyFrame, text="Backpacks", font=(textFont, h2Size), image=backpacksImageTk, compound="left", anchor="w", command=lambda: openStratagemSelector("Backpacks"), bg=backgroundColour)
    backpacksButton.pack(fill="both")

    # Emplacements
    # Load image
    emplacementsImage = Image.open("Assets/Emplacements/Gatling_Sentry.png")
    # Convert the image to be usable by tkinter
    emplacementsImageTk = ImageTk.PhotoImage(emplacementsImage)
    # Create Orbitals Button
    emplacementsButton = tk.Button(master=cSBodyFrame, text="Emplacements", font=(textFont, h2Size), image=emplacementsImageTk, compound="left", anchor="w", command=lambda: openStratagemSelector("Emplacements"), bg=backgroundColour)
    emplacementsButton.pack(fill="both")

    # Vehicles
    # Load image
    vehiclesImage = Image.open("Assets/Vehicles/Fast_Recon_Vehicles.png")
    # Convert the image to be usable by tkinter
    vehiclesImageTk = ImageTk.PhotoImage(vehiclesImage)
    # Create Orbitals Button
    vehiclesButton = tk.Button(master=cSBodyFrame, text="Vehicles", font=(textFont, h2Size), image=vehiclesImageTk, compound="left", anchor="w", command=lambda: openStratagemSelector("Vehicles"), bg=backgroundColour)
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
stratagem1Button = tk.Button(master=stratagem1Frame, image=stratagem1ImageTk, command= lambda: openStratagemCategorySelector(1), bg=backgroundColour)
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
stratagem2Button = tk.Button(master=stratagem2Frame, image=stratagem2ImageTk, command= lambda: openStratagemCategorySelector(2), bg=backgroundColour)
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
stratagem3Button = tk.Button(master=stratagem3Frame, image=stratagem3ImageTk, command= lambda: openStratagemCategorySelector(3), bg=backgroundColour)
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
stratagem4Button = tk.Button(master=stratagem4Frame, image=stratagem4ImageTk, command= lambda: openStratagemCategorySelector(4), bg=backgroundColour)
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
# Information box
# -------------------------------------------------------------------------------------
def showImageBox(message):
    # Message box to advise the user
    informationBox = tk.Toplevel()

    # Tkinter window attributes
    informationBox.title("Information")
    informationBox.configure(bg=backgroundColour)

    # Create label to show information
    informationBoxLabel = tk.Label(master=informationBox, text=message, font=(textFont, h3Size))
    informationBoxLabel.pack(fill="both")

    # Automatically destroy the window after a time period
    informationBox.after(1000, lambda: informationBox.destroy())

    # Run the application
    informationBox.mainloop()

# -------------------------------------------------------------------------------------
# Save Button
# -------------------------------------------------------------------------------------
# Create function to save the macro
def saveMacro():
    # Get the key combinations for the stratagems
    stratagem1KeyCombination = ""
    stratagem2KeyCombination = ""
    stratagem3KeyCombination = ""
    stratagem4KeyCombination = ""

    with open(stratagem1.getKeyCombinationPath(), mode="r") as keyCombinationFile:
        for line in keyCombinationFile:
            stratagem1KeyCombination += line

    with open(stratagem2.getKeyCombinationPath(), mode="r") as keyCombinationFile:
        for line in keyCombinationFile:
            stratagem2KeyCombination += line

    with open(stratagem3.getKeyCombinationPath(), mode="r") as keyCombinationFile:
        for line in keyCombinationFile:
            stratagem3KeyCombination += line

    with open(stratagem4.getKeyCombinationPath(), mode="r") as keyCombinationFile:
        for line in keyCombinationFile:
            stratagem4KeyCombination += line

    # Write file
    # Read in template
    with open("TemplateMacro.ahk", "r") as templateFile:
        template = templateFile.read()

    # Replace placeholder strings
    template = template.replace("; %1StratagemName", f"; {stratagem1.getName()}")
    template = template.replace("; %2StratagemName", f"; {stratagem2.getName()}")
    template = template.replace("; %3StratagemName", f"; {stratagem3.getName()}")
    template = template.replace("; %4StratagemName", f"; {stratagem4.getName()}")

    template = template.replace("%1KeyCombination", f"{stratagem1KeyCombination}")
    template = template.replace("%2KeyCombination", f"{stratagem2KeyCombination}")
    template = template.replace("%3KeyCombination", f"{stratagem3KeyCombination}")
    template = template.replace("%4KeyCombination", f"{stratagem4KeyCombination}")

    # Write new macro file
    with open("MacroFile.ahk", "w") as macroFile:
        macroFile.write(template)

    # Show message box to advise the user that the file was saved
    showImageBox("File Saved")

# Create save button
saveButton = tk.Button(master=saveButtonFrame, text="Save", font=(textFont, h2Size), command=saveMacro)
saveButton.pack(fill="both", expand=True)

# -------------------------------------------------------------------------------------
# Run Button
# -------------------------------------------------------------------------------------
# Create function to run the macro
def runMacro():
    # Save the current selected stratagems
    saveMacro()
    # Show message box to advise the user that the macro was run
    showImageBox("File ran")
    # Run the macro file
    subprocess.run([".\MacroFile.ahk"])
# Create run button
runButton = tk.Button(master=runButtonFrame, text="Run", font=(textFont, h2Size), command=runMacro)
runButton.pack(fill="both", expand=True)

# -------------------------------------------------------------------------------------
# Stop Button
# -------------------------------------------------------------------------------------
# Create run button TODO Add functions to buttons
stopButton = tk.Button(master=stopButtonFrame, text="Stop", font=(textFont, h2Size))
stopButton.pack(fill="both", expand=True)

# Run the application
app.mainloop()