import tkinter as tk
#from tkinter import filedialog
from GUIWindow import AtlasGUI

#initalize GUI
testObj = AtlasGUI()

#event binding calling resizer (and passing dims) every time testObj changes size
testObj.bind('<Configure>', testObj.resizer)

#Call tkinter main loop
testObj.mainloop()


