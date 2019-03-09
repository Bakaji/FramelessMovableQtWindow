##How to use 
set your QMainWindow to FramelessResizableWindow
 
 you can give a margin as a parameter

Any children you want to add to the window, you should add them to the main_widget member in FramelessResizableWindow

Since stylesheets has nothing todo with layout and sizes you can edit them as you want

##example 
    app = QApplication()
    fr = FramelessResizableWindow(3)
    #or (5 is the default value)
    fr = FramelessResizableWindow()
    fr.resize(300,300)
    fr.show()
    sys.exit(app.exec_()) 
##license
licenced under LGPL(Library Gnu public license)