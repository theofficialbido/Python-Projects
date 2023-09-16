from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
import sys
def main():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(300, 300, 600, 600)
    #                x    y  width height
    win.setWindowTitle("First app")
    label = QLabel(win)
    label.setText("First Label!")
    label.move(150,150)
    win.show()
    sys.exit(app.exec_())
main()
