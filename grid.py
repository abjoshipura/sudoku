from PySide6.QtWidgets import *
from PySide6.QtCore import *

import sys
import new_sudoku_logix

sudoku = new_sudoku_logix.creator()

app = QApplication(sys.argv)
selected_cell = QWidget()


@Slot()
def select_box(cell):
    selected_cell = cell
    if selected_cell != cell:
        cell.setStyleSheet(
            "border: 2px solid blue; border-style:groove;")
    else:
        print("Halo!")
        cell.setStyleSheet(
            "border: default; border-style:solid;")


def choose_num(num):
    selected_cell.setText(str(num))


def window():
    win = QWidget()
    grid = QGridLayout()
    for i in range(len(sudoku)):
        for j in range(len(sudoku)):
            dummy_cell = QPushButton("")
            if sudoku[i][j] != 0:
                cell = QPushButton(str(sudoku[i][j]))
                cell.setDisabled(True)
                cell.setStyleSheet("color: #000")
                cell.setFixedHeight(70)
                grid.addWidget(cell, i, j)
            else:
                cell = dummy_cell
                cell.clicked.connect(lambda *args, arg=cell: select_box(arg))
                cell.setFixedHeight(70)
                grid.addWidget(cell, i, j)
    for i in range(9):
        button = QPushButton(str(i + 1))
        button.clicked.connect(lambda *args, num=i: choose_num(num))
        button.setMinimumHeight(20)
        grid.addWidget(button)
    win.setLayout(grid)
    win.setWindowTitle("Sudoku")
    win.setGeometry(50, 50, 200, 200)
    win.show()
    sys.exit(app.exec_())


window()
