import tkinter as tk
from tkinter import filedialog

text_area_font = ("Ariel", 18)
menubar_font = ("Ariel", 14)
width = 1200
height = 700
textcolor = "#00FF00"
cursorcolor = "#00FF00"
backgroundcolor = "#000000"

class MenuBar():
    def __init__(self, app):
        menubar = tk.Menu(app.root, font=menubar_font)
        app.root.config(menu=menubar)
           
        #menubuttons
        file_dropdown = tk.Menu(menubar, font=menubar_font, tearoff=0)
        file_dropdown.add_command(label="New File", command=app.new_file)
        file_dropdown.add_command(label="Open File", command=app.open_file)
        file_dropdown.add_command(label="Save File", command=app.save_file)
        file_dropdown.add_command(label="Save As", command=app.save_file_as)
        file_dropdown.add_separator()
        file_dropdown.add_command(label="Exit", command=app.root.destroy)
        
        edit_dropdown = tk.Menu(menubar, font=menubar_font, tearoff=0)
        view_dropdown = tk.Menu(menubar, font=menubar_font, tearoff=0)
        help_dropdown = tk.Menu(menubar, font=menubar_font, tearoff=0)
        settings_dropdown = tk.Menu(menubar, font=menubar_font, tearoff=0)
        
        menubar.add_cascade(label="File", menu=file_dropdown)
        menubar.add_cascade(label="Edit", menu=edit_dropdown)
        menubar.add_cascade(label="View", menu=view_dropdown)
        menubar.add_cascade(label="Settings", menu=settings_dropdown)
        menubar.add_cascade(label="Help", menu=help_dropdown)
        
class LukeEdit:
    def __init__(self, root):
        #make window
        self.root = root
        self.filename = None

        
        root.title("LukeEdit v0.0.1")
        root.geometry(f"{width}x{height}")
           
        #make typing areas with scroll bar
        self.typingArea = tk.Text(root, font=text_area_font, width=0)
        self.scrollbar = tk.Scrollbar(root, command=self.typingArea.yview)
        self.typingArea.configure(yscrollcommand=self.scrollbar.set)
        self.typingArea.configure(bg=backgroundcolor, fg=textcolor, insertbackground=cursorcolor)
        
        #making the menu bar
        self.menubar = MenuBar(self)
        
        #pack modules
        self.typingArea.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    def set_window_title(self):
        pass

    def new_file(self):
        pass

    def open_file(self):
        self.filename = filedialog.askopenfilename(
            defaultextension=".txt",
            filetypes=[
                ("All Files", "*.*"),
                ("Python", "*.py")
            ]
        )
        if self.filename:
            self.typingArea.delete(1.0, tk.END)
            with open(self.filename, "r") as File:
                self.typingArea.insert(1.0, File.read())

    def save_file(self):
        pass

    def save_file_as(self):
        pass
       
root = tk.Tk()
LukeEdit(root)
root.mainloop()