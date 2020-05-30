from googletrans import Translator
from PyQt5 import QtCore, QtGui, QtWidgets
from ui import Ui_Form
import sys

app = QtWidgets.QApplication(sys.argv)
Form = QtWidgets.QWidget()
ui = Ui_Form()
ui.setupUi(Form)
Form.show()

tran = Translator()


def tran_g():
    text = ui.TextInput.text()
    ja = tran.translate(text, dest='ja')
    en = tran.translate(text, dest='en')
    ru = tran.translate(text, dest='ru')
    ui.JapaneseText.setText(ja.text)
    ui.EnglishText.setText(en.text)
    ui.RussianText.setText(ru.text)

ui.pushButton.clicked.connect(tran_g)

sys.exit(app.exec_())