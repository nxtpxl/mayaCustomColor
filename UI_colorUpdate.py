import Qt
from Qt import QtWidgets
from PySide2.QtCore import * 
from PySide2.QtGui import * 
from PySide2.QtWidgets import *
from PySide2.QtUiTools import *
from shiboken2 import wrapInstance 
currentColor = []
try:
    currentColor
    pass
except NameError:
    currentColor = ['none']


def rgba():
    allColors = currentColor
    print allColors
    if allColors == []:
        print 'bbb'
        #slColor = currentColor[-1]    
        del currentColor[:]
        qApp.setStyleSheet("""
        QMenuBar {
            background: rgb( 200, 40, 0 );
            color:   rgb( 255, 255, 255 );
        }
        """)
        currentColor.append('red')
    else:
        slColor = currentColor[-1]    
        del currentColor[:]
        qApp.setStyleSheet("""
        QMenuBar {
            background: rgb( 200, 40, 0 );
            color:   rgb( 255, 255, 255 );
        }
        """)
        currentColor.append('red')            

    if slColor == 'red':
        del currentColor[:]
        qApp.setStyleSheet("""
        QMenuBar {
            background: rgb( 50, 180, 0 );
            color:      rgb( 20, 20, 20 );
        }
        """)
        currentColor.append('green')
    if slColor == 'green':
        del currentColor[:]
        qApp.setStyleSheet("""
        QMenuBar {
            background: rgb( 0, 0, 255 );
            color:      rgb( 255, 255, 255 );
        }
        """)
        currentColor.append('blue')
    if slColor == 'blue':
        del currentColor[:]
        currentColor.append('none')
        qApp.setStyleSheet("")
    else:
        pass

rgba()



