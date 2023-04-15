import tkinter as tk
#from tkinter import filedialog
from GUIWindow import AtlasGUI

#initalize GUI
testObj = AtlasGUI()

#event binding calling resizer (and passing dims) every time testObj changes size
testObj.bind('<Configure>', testObj.onSizeChange)
testObj.bind('<r>', testObj.onResizeEvent)

#testObj.bind('<ButtonRelease-1>', testObj.resizer)

#Call tkinter main loop
testObj.mainloop()


