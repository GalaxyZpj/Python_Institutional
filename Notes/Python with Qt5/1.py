import sys
from PyQt5.QtWidgets import *
app = QApplication(sys.argv)
w = QWidget()
w.resize(250, 150)
w.move(100, 100)
w.setWindowTitle('Example')
fl = QFormLayout()
w.setLayout(fl)
L1 = QLabel('See Here')
fl.addRow("Message", L1)
T1 = QLineEdit()
fl.addRow("Name", T1)
Box_Gen = QHBoxLayout()
m = QRadioButton("Male")
f = QRadioButton("Female")
Box_Gen.addWidget(m)
Box_Gen.addWidget(f)
fl.addRow("Gender: ", Box_Gen)
CB = QComboBox()
CB.addItem("Manager")
CB.addItem("Clerk")
L = ['Superviser', 'Peon', 'Accountant']
CB.addItems(L)
fl.addRow('Designation: ', CB)
Box_Int = QHBoxLayout()
elc = QCheckBox("Electronics")
Box_Int.addWidget(elc)
fl.addRow("Interest: ", Box_Int)
B = QPushButton("Submit")
B.clicked.connect(lambda: btn_click())
def btn_click():
    print(CB.currentText(), L1.text(), T1.text())
fl.addRow("Action: ", B)


w.show()
sys.exit(app.exec_())