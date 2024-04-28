
#шаблон python файлу
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QIcon, QPixmap
from ui import Ui_MainWindow
import random
class Widget(QMainWindow):
    def   __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_3.setText("США")
        self.ui.pushButton_5.setText("СССР")
        self.ui.pushButton_7.setText("3-тій РЕЙХ")
        self.list1 = ['США','СССР','3-тій РЕЙХ']
        self.ui.pushButton_3.clicked.connect(self.USA)
        self.ui.pushButton_5.clicked.connect(self.CCCP)
        self.ui.pushButton_7.clicked.connect(self.Reih)

    def USA(self):
        n = random.choice(self.list1)
        self.ui.label_2.setText(n)
        if self.ui.label_2.text() == "3-тій РЕЙХ":
            self.ui.label.setText("Пограв")
        elif self.ui.label_2.text() == "СССР":
            self.ui.label.setText("Виграв")
        elif self.ui.label_2.text() == "США":
            self.ui.label.setText("Нічия")
    def CCCP(self):
        n = random.choice(self.list1)
        self.ui.label_2.setText(n)
        if self.ui.label_2.text() == "3-тій РЕЙХ":
            self.ui.label.setText("Виграв")
        elif self.ui.label_2.text() == "СССР":
            self.ui.label.setText("Нічия")
        elif self.ui.label_2.text() == "США":
            self.ui.label.setText("Програв")
    def Reih(self):
        n = random.choice(self.list1)
        self.ui.label_2.setText(n)
        if self.ui.label_2.text() == "3-тій РЕЙХ":
            self.ui.label.setText("Нічия")
        elif self.ui.label_2.text() == "СССР":
            self.ui.label.setText("Програв")
        elif self.ui.label_2.text() == "США":
            self.ui.label.setText("Виграв")


app = QApplication([])
ex = Widget()
ex.show()
app.exec_()
