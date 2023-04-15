import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image #python img library needed for resizing
import threading as th #for cooldown timer on resize, may have later applications
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


		#Initalzie image variables to something predictable
		self.img_path = ''
		#create canvas
		self.canvas = tk.Canvas(self, width=800, height=500, bg="Blue")

		#menuBar is our bar containing subsequent menus
		menuBar = tk.Menu(self)

		#subsequent menus
		filemenu = tk.Menu(menuBar, tearoff=0)

		#filemenu commands
		filemenu.add_command(label="New", command=donothing)
		filemenu.add_command(label="Open", command=self.File_Open)
		filemenu.add_command(label="Save", command=donothing)
		filemenu.add_command(label="Save as...", command=donothing)
		filemenu.add_command(label="Close", command=self.File_Close)

		# Add menuBar to AtlasGUI
		self.config(menu = menuBar)

		#attach subsequent menus to menubar
		menuBar.add_cascade(label="File", menu=filemenu)

		#cooldown timer
		self.resizeCooldown = False
		self.resizeTimer = th.Timer(1.0, self.endCooldown) 

	#Timer function that ends the resize cooldown
	def endCooldown(self):
		print("ending cooldown!", self.resizeCooldown)
		self.resizeCooldown = False
		print("ended cooldown!", self.resizeCooldown)
	#adds image to screen
	def File_Open(self):

		#If a canvas exists, we need to close the previous image first
		if(self.canvas != None):
			self.File_Close()

		#Open file dialog and acquire the image.
		self.img_path = ''
		self.img_path = filedialog.askopenfilename()

		#If the image was acquired, continue
		if (self.img_path != ''):
			#define tkinter photoimage
			photoImage = ImageTk.PhotoImage(file=self.img_path)
			
			#fill the canvas up - probably delete
			self.canvas.pack(fill="both", expand=True)

			#unexplicably - image will not load without this 
			self.img=photoImage

			# Set image in canvas
			self.canvas.create_image(0,0, image=photoImage, anchor="nw")

	#event function called on each new resize
	#e is the event with the height and width	
	def resizer(self, e):
		print("resizer called, cooldown:", self.resizeCooldown)
		if(self.resizeCooldown):
			return
		else:
			#begin our resizecooldown
			self.resizeCooldown = True

		if ((self.img_path != '') and (self.canvas != None)):
			#Define these as globals to avoid over-zealous Tkinter garbage collection
			global rzr_image, rzr_resized_image, rzr_photoImage

			#open the image
			rzr_image = Image.open(self.img_path)

			#resize image and antialias it
			rzr_resized_image = rzr_image.resize((e.width, e.height), Image.ANTIALIAS)

			#define image again
			rzr_photoImage = ImageTk.PhotoImage(rzr_resized_image)
			
			# Set image in canvas
			self.canvas.create_image(0,0, image=rzr_photoImage, anchor="nw")
			print("resizing!!")


		self.resizeTimer.start()

	def File_Close(self):
		#if a canvas exists, delete it
		if(self.canvas):
			self.canvas.delete('all')


#Maybe a seperate toolswindow?
# class ToolsWindow(tk.TK):
# 	pass
# https://www.digitalocean.com/community/tutorials/tkinter-working-with-classes
#working with this guy rn
#making multiple frames controlled by 1 class, toggling visibility
#maybe draw the layout and hierarchy first?