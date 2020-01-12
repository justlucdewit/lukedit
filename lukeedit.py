import tkinter as tk

text_area_font = ("Ariel", 18)
menubar_font = ("Ariel", 14)
width = 1200
height = 700

class MenuBar():
    def __init__(self, app):
        menubar = tk.Menu(app.root, font=menubar_font)
        app.root.config(menu=menubar)
           
        #menubuttons
        file_dropdown = tk.Menu(menubar, font=menubar_font, tearoff=0)
        
        file_dropdown.add_command(label="New File")
        file_dropdown.add_command(label="Open File")
        file_dropdown.add_command(label="Save File")
        file_dropdown.add_command(label="Save As")
        
        menubar.add_cascade(label="File", menu=file_dropdown)
        

class LukeEdit:
    def __init__(self, root):
        #make window
        self.root = root
        root.title("LukeEdit v0.0.1")
        root.geometry(f"{width}x{height}")
           
        #make typing areas with scroll bar
        self.typingArea = tk.Text(root, font=text_area_font, width=0)
        self.scrollbar = tk.Scrollbar(root, command=self.typingArea.yview)
        self.typingArea.configure(yscrollcommand=self.scrollbar.set)
        
        #making the menu bar
        self.menubar = MenuBar(self)
        
        #pack modules
        self.typingArea.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
       
root = tk.Tk()
LukeEdit(root)
root.mainloop()