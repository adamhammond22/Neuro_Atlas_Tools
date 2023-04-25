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

		B = tk.Button(self, text ="Rotate")
		B.pack()

		#Initiate all sliders in dictionary
		self.sliders = {}
		self.sliders["Rotate"] = tk.Scale(self, from_=0, to=360, orient=tk.HORIZONTAL,
			length=200, command=self.rotateImg)
		self.sliders["Rotate"].pack()

		# Check for parent's copy of slidervalues
		if self.parent.backgroundSliderValues != None:
			#if this is the case 1: the toolbar was closed and re-opened, 2: the parent loaded saved slider values

			#save local copy of slidervalues
			self.sliderValues = self.parent.backgroundSliderValues

			#get rid of parent copy to save space
			self.parent.backgroundSliderValues = None

			#apply that copy of slidervalues
			self.applySliderValues()
		#Otherwise, make a clean copy of slidervalues and apply it
		else:
			self.clearSliderValues()



	# Remove parent's reference to this toolbar before deleting
	def onClosing(self):

		#save our sliderValues in the parent
		self.parent.backgroundSliderValues = self.sliderValues

		#destroy ourselves, and parents ref to us
		self.parent.BackgroundToolbar = None
		self.destroy()

	#Rotates image based on slider value
	def rotateImg(self, degree):
		# if the slider value is different than the current degree
		if self.sliderValues["Rotate"] != degree:
		
			#save the degree as the slider value
			self.sliderValues["Rotate"] = degree	

			#if the image actually exists
			if (self.parent.image != None):

				#open the image
				image = self.parent.image

				#rotate it
				print("degree:", degree, int(degree))
				image = image.rotate(int(degree),  resample=Image.BICUBIC)

				#send it to parent to be applied
				self.parent.applyTransformedImage(image)

	#makes a clean copy of slider values and applies it
	def clearSliderValues(self):
		self.sliderValues = {
			"Rotate" : 0
		}

		#apply the cleared values
		self.applySliderValues()

	#Apply all slider values, syncing it with sliderValues Dict
	def applySliderValues(self):
		# iter through each slider in dict, setting the slider as it's value
		for sliderName, sliderObject in self.sliders.items():
			print("setting sliders", sliderName)
			if sliderName in self.sliderValues:
				print(sliderName, "is val", self.sliderValues[sliderName])
				sliderObject.set(int(self.sliderValues[sliderName]))
	def saveTransforms(self):
		pass


	def loadTransforms(self):
		pass