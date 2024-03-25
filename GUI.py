import tkinter as tk
import os

# Root class for GUI
class RootGUI():
    def __init__(self, master):
        # Sets the tkinter root window and title
        self.master = master
        master.title('GUI')
        #

        # Frame for the buttons
        ButtonFrame = tk.Frame(master)
        ButtonFrame.pack(side = 'left', anchor = 'nw', padx = 20, pady = 20)
        #

        # Buttons
        Button1 = tk.Button(ButtonFrame, text = 'Button-1', command = self.Button1Click, height = 3, width = 14)
        Button1.pack()

        Button2 = tk.Button(ButtonFrame, text = 'Button-2', command = self.Button2Click, height = 3, width = 14)
        Button2.pack(pady = 12)

        CloseButton = tk.Button(ButtonFrame, text = 'Close', command = master.destroy)
        CloseButton.pack(side = 'left')
        #

        # Defines the textbox which will be changed by the buttons
        self.Text = tk.Text(master)
        self.Text.pack(pady = 20)
        #

        # Loads the logo
        Logo = tk.Canvas(master, height = 250, width = 250)
        self.LogoDir = tk.PhotoImage(file = os.path.join("Assets", "Midtjysk.png"))
        Logo.create_image(0, 0, anchor = tk.NW, image = self.LogoDir)
        Logo.pack(before = self.Text, side = 'right', anchor = tk.NE, padx = 10, pady = 10)
        #


    # Functions being defined and what the buttons shall do
    def Button1Click(self):
        self.Text.delete(1.0, tk.END) # Clears all text
        self.Text.insert(tk.END, '"Liber Primus" The book of all books') # Sets text as 'defined text'
        self.Text.update() # Updates the text widget
    
    def Button2Click(self):
        self.Text.delete(1.0, tk.END)
        self.Text.insert(tk.END, '"Do or do not, there is no try" - Yoda')
        self.Text.update()
    #



# Initialising the GUI
root = tk.Tk()
GUI = RootGUI(root)
root.mainloop()
