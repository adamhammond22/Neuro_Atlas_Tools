import tkinter as tk
#from tkinter import ttk

#Class ImageWindow extends tk.Tk, allowing the use of
#components present in the Tk() class!
class ImageWindow(tk.Tk):
	#init allows acceptance of arbitrary number of args
	tk.Tk.__init__(self, *args, **kwargs)

		#Add Title to Window
		self.wm_title("Image Window")

		#Create a frame
		windowFrame = tk.Frame(self, height=400, width=600)


#Maybe a seperate toolswindow?
# class ToolsWindow(tk.TK):
# 	pass
# https://www.digitalocean.com/community/tutorials/tkinter-working-with-classes
#working with this guy rn
#making multiple frames controlled by 1 class, toggling visibility
#maybe draw the layout and hierarchy first?