from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

app = QApplication([])

main_win = QWidget()
main_win.setWindowTitle("Вікторина")
main_win.resize(500, 400)

lbl = QLabel("В якому році канал отримав золоту кнопку в ютуб?")
btn = QRadioButton("1991")
btn1 = QRadioButton("2011")
btn2 = QRadioButton("2001")
btn3 = QRadioButton("2015")

main_layout = QVBoxLayout()
main_layout.addWidget(lbl)

row1_layout = QHBoxLayout()
row2_layout = QHBoxLayout()

row1_layout.addWidget(btn)
row1_layout.addWidget(btn1)

row2_layout.addWidget(btn2)
row2_layout.addWidget(btn3)

main_layout.addLayout(row1_layout)
main_layout.addLayout(row2_layout)

def show_right():
    win_info = QMessageBox(main_win)
    win_info.setWindowTitle("Результат")
    win_info.setText("Правильна відповідь")
    win_info.show()

def show_wrong():
    win_info = QMessageBox(main_win)
    win_info.setWindowTitle("Результат")
    win_info.setText("Неправильна відповідь")
    win_info.show()


btn.clicked.connect(show_wrong)
btn1.clicked.connect(show_wrong)
btn2.clicked.connect(show_wrong)
btn3.clicked.connect(show_right)

main_win.setLayout(main_layout)
main_win.show()
app.exec_()