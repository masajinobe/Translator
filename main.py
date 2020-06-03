from googletrans import Translator
from PyQt5 import QtCore, QtGui, QtWidgets
from ui import Ui_Translator
import sys

app = QtWidgets.QApplication(sys.argv)
Form = QtWidgets.QWidget()
ui = Ui_Translator()
ui.setupUi(Form)
Form.show()

tr = Translator()


def translate():
	text = ui.textEdit.text()
	ja = tr.translate(text, dest='ja')
	en = tr.translate(text, dest='en')
	ru = tr.translate(text, dest='ru')
	cn = tr.translate(text, dest='zh-CN')
	fr = tr.translate(text, dest='fr')
	es = tr.translate(text, dest='es')
	ui.JaEdit.setText(ja.text)
	ui.EnEdit.setText(en.text)
	ui.RuEdit.setText(ru.text)
	ui.CnEdit.setText(cn.text)
	ui.FrEdit.setText(fr.text)
	ui.EsEdit.setText(es.text)

ui.pushButton.clicked.connect(translate)

sys.exit(app.exec_())
