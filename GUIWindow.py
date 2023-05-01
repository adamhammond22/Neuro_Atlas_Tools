import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image #python img library needed for resizing
import PIL
#from tkinter import ttk
import math # for floor
from GUIToolbars import *


#placeholder command for unused menu buttons
def donothing():
	print("ok!")

# Class AtlasGUI extends tk.Tk, allowing the use of components present in the Tk() class!
class AtlasGUI(tk.Tk):
	# Init function allows acceptance of arbitrary number of args to support our parent class
	# not yet sure if this is nessecary
	def __init__(self, *args, **kwargs):
		#Init our parent tk class
		tk.Tk.__init__(self, *args, **kwargs)


		# ===== Window tkinter details ===== #
		self.title("Align Atlas Window")
		self.geometry("1000x600")
		self.config(bg = "white")

		# ===== Handling image variables ===== #
		# Initalzie image variables to something predictable
		# Image must be stored to avoid tkinterGarbage Collection
		self.img_path = ''
		self.image = None
		self.photoImage = None

		# ===== Init Tkinter Canvas ===== #
		self.canvas_width = 800
		self.canvas_height = 500
		self.canvas = tk.Canvas(self, width=800, height=500, bg="Blue")

		# ===== Adding all Menus to the window ===== #
		# MenuBar is our main bar containing subsequent menus
		menuBar = tk.Menu(self)

		# Subsequent menus defined here
		filemenu = tk.Menu(menuBar, tearoff=0)

		# Filemenu commands
		filemenu.add_command(label="New", command=donothing)
		filemenu.add_command(label="Open", command=self.File_Open)
		filemenu.add_command(label="Save", command=donothing)
		filemenu.add_command(label="Save as...", command=donothing)
		filemenu.add_command(label="Close", command=self.File_Close)

		# Add menuBar to AtlasGUI
		self.config(menu = menuBar)

		# Attach subsequent menus to menubar
		menuBar.add_cascade(label="File", menu=filemenu)

		# Attach resize button
		menuBar.add_command(label="Resize", command=self.resizer)

		#Background Toolbar button	
		menuBar.add_command(label="Background Toolbar", command=self.onBackgroundToolbar)

		# ===== Background Toolbar References ===== #

		# Reference to toolbar object
		self.BackgroundToolbar = None

		# Dictionaries of all Image Transformations
		self.BackgroundTransformations = cleanBackgroundTransformations()
		#add more transforms

	# Resizes the image on the canvas widget, if possible
	# Image is never streached by this operation
	def resizer(self):

		# Only execute if we have an image path, and canvas exists
		if ((self.img_path != '') and (self.canvas != None)):

			# Define image and photoimage must be saved in class
			# to avoid over-zealous Tkinter garbage collection

			# Open the image
			self.image = Image.open(self.img_path)

			#Calculate multipliers to get image dimensions = canvas dimenstions 
			width_multiplier = self.canvas_width/ self.image.width 
			height_multiplier = self.canvas_height / self.image.height

			#Choose the minimum multiplier, so nothing gets cut off
			min_multiplier = min(width_multiplier, height_multiplier)

			#Choose calculate new width and height
			new_width = math.floor(self.image.width * min_multiplier)
			new_height = math.floor(self.image.height * min_multiplier)

			# If our width and height are greater than zero map it
			if ((new_width > 0) and (new_height > 0)):
				self.image = self.image.resize((new_width, new_height))
				
				# Define photoimage to insert into canvas
				self.photoImage = ImageTk.PhotoImage(self.image)

				# Set photoimage in canvas
				self.canvas.create_image(0,0, image=self.photoImage, anchor="nw")

			# If for some reason it's too small, just clear the canvas
			else:
				self.canvas.delete('all')


	# Is called each time resize keybind event is fired, simply calls resizer
	def onResizeEvent(self, e):
		self.resizer()

	# Is called each time tkinter <Configure> event is fired, stores updated width and height of canvas
	def onSizeChange(self, e):
		self.canvas_width = e.width
		self.canvas_height = e.height

	# Opens new image
	def File_Open(self):

		# Call close file to make sure canvas is cleared
		self.File_Close()

		# Open file dialog and acquire the image path.
		self.img_path = ''
		self.img_path = filedialog.askopenfilename()

		# If the image path was acquired, continue
		if (self.img_path != ''):
			# Define tkinter photoimage
			photoImage = ImageTk.PhotoImage(file=self.img_path)
			
			# Make canvas fill entire box
			self.canvas.pack(fill="both", expand=True)

			# Set photoimage in canvas
			self.canvas.create_image(0,0, image=photoImage, anchor="nw")

			# Resize the image
			self.resizer()

			#ADD LOAD slider features here

	# Opens a Background Toolbar or raises it if it's already opened
	def onBackgroundToolbar(self):
		if(self.BackgroundToolbar == None):
			self.BackgroundToolbar = BackgroundToolbar(self)
		else:
			self.BackgroundToolbar.tkraise()
			print(dir(self.BackgroundToolbar.tkraise()))


	# Closes image - clearing it from the canvas widget if possible
	def File_Close(self):
		# If a canvas exists, clear it's contents and image path
		if(self.canvas):
			self.canvas.delete('all')
			self.img_path = ''
			self.image = None
			self.photoImage = None

		# === Handling Toolbars and saved sliders ===#
		if self.BackgroundToolbar != None:
			#if the toolbar exists, clear it's slider values
			self.BackgroundToolbar.clearSliderValues()
		#remove slider value references (ADD SAVE FEATURE HERE)
		self.BackgroundTransformations = cleanBackgroundTransformations()



	#Takes transformed image from toolbar and applies it to the canvas
	def applyTransformedImage(self, transformed_image: PIL.Image.Image):
		# Save ref to transformed image
		self.image = transformed_image

		# Define photoimage to insert into canvas
		self.photoImage = ImageTk.PhotoImage(self.image)

		# Set photoimage in canvas
		self.canvas.create_image(0,0, image=self.photoImage, anchor="nw")

		return


#Maybe a seperate toolswindow?
#PIL.Image.Image is image
#PIL.ImageTk.PhotoImage is photoimage
# class ToolsWindow(tk.TK):
# 	pass
# https://www.digitalocean.com/community/tutorials/tkinter-working-with-classes
#working with this guy rn
#making multiple frames controlled by 1 class, toggling visibility
#maybe draw the layout and hierarchy first?
