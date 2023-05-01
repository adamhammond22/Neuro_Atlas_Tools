import tkinter as tk
# from tkinter import filedialog
from PIL import ImageTk, Image #python img library needed for resizing
import PIL

class BackgroundToolbar(tk.Toplevel):
	def __init__(self, parent):
		#Init parent toplevel
		tk.Toplevel.__init__(self)

		# Add basic window characteristics
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

		# Set Sliders to match background transformations
		applySliderValues(self.parent.BackgroundTransformations, 
			self.sliders)



	# Remove parent's reference to this toolbar before deleting
	def onClosing(self):


		#destroy ourselves, and parents ref to us
		self.parent.BackgroundToolbar = None
		self.destroy()

	#Rotates image based on slider value
	def rotateImg(self, degree):
		# if the slider value is different than the current degree
		print(self.parent.BackgroundTransformations)
		if self.parent.BackgroundTransformations["Rotate"] != degree:
		


			#if the image actually exists
			if (self.parent.image != None):

				#open the image
				image = self.parent.image

				image = TransformImage(self.parent.image, "Rotate",
					self.parent.BackgroundTransformations["Rotate"], degree)

				#save the degree as the slider value
				self.parent.BackgroundTransformations["Rotate"] = degree	

				#rotate it
				# print("degree:", degree, int(degree)*)
				# image = image.rotate(int(degree),  resample=Image.BICUBIC)

				#send it to parent to be applied
				self.parent.applyTransformedImage(image)

#makes a clean copy of slider refs and applies it
def clearSliderValues(sliderRefs: dict):
	sliderValues = {}
	for sliderName, sliderRef in sliderRefs.items():
		sliderValues[sliderName] = 0

		#here we'd add exceptions for sliders that default to other places


	#apply the cleared values
	applySliderValues(sliderValues, sliderRefs)


def saveTransforms(self):
	pass


def loadTransforms(self):
	pass

#Takes a Dictionary of Slider Values, and applies them to the provided slider dict
def applySliderValues(sliderValues: dict, sliderRefs: dict):

	# iter through each slider value setting the slider as it's value
	for sliderName, sliderValue in sliderValues.items():
		
		#If the slider name is in the slider references
		if sliderName in sliderRefs.keys():
			
			print("slider", sliderName, "successfully set to", sliderValue)
			sliderRefs[sliderName].set(int(sliderValue))

		else:
			print("applySliderValues() Error: Provided sliderValues name ", sliderName,
				"is not in slider reference keys", sliderRefs.keys())

def TransformImage(working_image: PIL.Image.Image, sliderName: str, oldValue, newValue):
	match sliderName:
		case "Rotate":
			degrees = int(newValue) - int(oldValue)
			print("real degrees")
			working_image = working_image.rotate(degrees, expand= True, resample=Image.BICUBIC)


	return working_image



def cleanBackgroundTransformations():
	value = {"Rotate": 0}
	#add more here
	return value