import tkinter as tk
# from tkinter import filedialog
from PIL import ImageTk, Image #python img library needed for resizing

class BackgroundToolbar(tk.Toplevel):
	def __init__(self, parent):
		#Init parent toplevel
		tk.Toplevel.__init__(self)

		# Add basic characteristics
		self.geometry("300x500")
		self.title("Background TB")
		self.resizable(False, False)

		# Add a protocol on deletion
		self.protocol("WM_DELETE_WINDOW", self.onClosing)

		# Save reference to parent
		self.parent = parent

		B = tk.Button(self, text ="Rotate", command=self.rotateImg)
		B.pack()
		self.slider1 = tk.Scale(self, from_=0, to=360, orient=tk.HORIZONTAL, length=200)
		self.slider1.pack()


	# Remove parent's reference to this toolbar before deleting
	def onClosing(self):
		self.parent.BackgroundToolbar = None
		self.destroy()


	def rotateImg(self):
		if (self.parent.image != None):
			print("ROTATING")
			#open the image
			image = self.parent.image

			#rotate it
			image = image.rotate(45)

			#send it to parent to be applied
			self.parent.applyTransformedImage(image)