import sys

from PyQt5.QtWidgets import *


class MSWord(QMainWindow):
    def __init__(self):
        super(MSWord, self).__init__()
        self.editor = QTextEdit()
        self.setCentralWidget(self.editor)
        self.showMaximized()
        self.editor.setFontPointSize(20)
        self.create_tool_bar()

    def create_tool_bar(self):
        tool_bar = QToolBar()

        undo_action = QAction('Undo', self)
        undo_action.triggered.connect(self.editor.undo)
        tool_bar.addAction(undo_action)

        self.addToolBar(tool_bar)


app = QApplication(sys.argv)
window = MSWord()
window.show()
sys.exit(app.exec_())