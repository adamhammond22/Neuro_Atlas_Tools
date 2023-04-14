import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image #python img library needed for resizing
#from tkinter import ttk

#placeholder command for unused menu buttons
def donothing():
	print("ok!")

#Class ImageWindow extends tk.Tk, allowing the use of components present in the Tk() class!
class AtlasGUI(tk.Tk):
	#init allows acceptance of arbitrary number of args
	def __init__(self, *args, **kwargs):
		#Init our parent tk class
		tk.Tk.__init__(self, *args, **kwargs)


		#Add Title to Window
		self.title("Align Atlas Window")
		self.geometry("1000x600")
		self.config(bg = "white")


		#menuBar is our bar containing subsequent menus
		menuBar = tk.Menu(self)

		#subsequent menus
		filemenu = tk.Menu(menuBar, tearoff=0)

		#filemenu commands
		filemenu.add_command(label="New", command=donothing)
		filemenu.add_command(label="Open", command=self.add_image)
		filemenu.add_command(label="Save", command=donothing)
		filemenu.add_command(label="Save as...", command=donothing)
		filemenu.add_command(label="Close", command=donothing)

		# Add menuBar to AtlasGUI
		self.config(menu = menuBar)

		#attach subsequent menus to menubar
		menuBar.add_cascade(label="File", menu=filemenu)

	#adds image to screen
	def add_image(self):
		img_path = filedialog.askopenfilename()
		print(img_path)

		img = Image.open(img_path)

	#event function called on each new resize
	#e is the event with the height and width	
	def resizer(self, e):
		print("resizing!!")


#Maybe a seperate toolswindow?
# class ToolsWindow(tk.TK):
# 	pass
# https://www.digitalocean.com/community/tutorials/tkinter-working-with-classes
#working with this guy rn
#making multiple frames controlled by 1 class, toggling visibility
#maybe draw the layout and hierarchy first?