from PySide6.QtWidgets import *
from PySide6.QtCore import *

import sys
import new_sudoku_logix

sudoku = new_sudoku_logix.creator()

app = QApplication(sys.argv)
cell1 = QPushButton("Hi")


@Slot()
def say_hello():
    print("Button clicked, Hello!")
    cell1.setText("Hey!")
    cell1.setStyleSheet("color: #fff")


def window():
    win = QWidget()
    grid = QGridLayout()
    for i in range(len(sudoku)):
        for j in range(len(sudoku)):
            if sudoku[i][j] != 0:
                cell = QLineEdit(str(sudoku[i][j]), readOnly=True)
                cell.setAlignment(Qt.AlignCenter)
                cell.setFixedHeight(70)
                grid.addWidget(cell, i, j)
            else:
                cell = cell1
                # cell.keyPressEvent()
                # cell.setAlignment(Qt.AlignCenter)
                cell.clicked.connect(say_hello)
                cell.setFixedHeight(70)
                grid.addWidget(cell, i, j)
    for i in range(9):
        button = QPushButton(str(i + 1))
        button.clicked.connect(say_hello)
        button.setMinimumHeight(20)
        grid.addWidget(button)
    win.setLayout(grid)
    win.setWindowTitle("Sudoku")
    win.setGeometry(50, 50, 200, 200)
    win.show()
    sys.exit(app.exec_())


window()
