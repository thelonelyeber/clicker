from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from clicker import Ui_MainWindow
import sys


class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # подключение клик-сигнал к слоту btnClicked
        self.ui.ClickBtn.clicked.connect(self.btnClicked)
        self.ui.BuyBtn.clicked.connect(self.buy)
        self.i = 0
        self.price = 50
        self.increasing = 1

    def btnClicked(self):
        self.i += self.increasing
        self.ui.ScoreLabel.setText(f"{self.i} очков")
        # Если не использовать, то часть текста исчезнет.
        self.ui.ScoreLabel.adjustSize()

    def buy(self):
        if self.i >= self.price:
            self.i -= self.price
            self.price = int(self.price * 1.1)
            self.ui.PriceLabel.setText(f'Цена: {self.price} очков')
            self.ui.PriceLabel.adjustSize()
            self.ui.ScoreLabel.setText(f'{self.i} очков')
            self.ui.ScoreLabel.adjustSize()
            self.increasing += 1
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Ошибка")
            msg.setText(f'Вы не можете купить улучшение!\n'
                        f'Вам не хватает еще {self.price - self.i}')
            msg.setIcon(QMessageBox.Warning)
            msg.exec_()


app = QtWidgets.QApplication([])
application = mywindow()
application.show()

sys.exit(app.exec())
