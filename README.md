# Frameless Resizable and movable Qt Window
## How to use 
Set your QMainWindow to FramelessResizableWindow
 
 You can give a margin as a parameter

Any children you want to add to the window, you should add them to the main_widget member in FramelessResizableWindow

Since stylesheets has nothing todo with layout and sizes you can edit them as you want

# example
```python
    app = QApplication()
    fr = FramelessResizableWindow(3)
    #or (5 is the default value)
    fr = FramelessResizableWindow()
    fr.resize(300,300)
    fr.show()
    sys.exit(app.exec_()) 
```
##license
licenced under [LGPL(Lesser gnu public license)](https://opensource.org/licenses/lgpl-3.0.html)
