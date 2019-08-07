import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QGridLayout, QApplication, QMessageBox, QMainWindow, QAction, qApp
from PyQt5.QtGui import QIcon

class main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.play = gamewinodw()
        self.setCentralWidget(self.play)

        menubar = self.menuBar()

        exit = QAction(QIcon('asset/image/exit.png'), '종료', self)
        exit.setShortcut('Esc')
        exit.triggered.connect(qApp.quit)

        regame = QAction(QIcon('asset/image/replay.png'), '재시작', self)
        regame.setShortcut('R')
        regame.triggered.connect(self.play.replay)

        back_main = QAction(QIcon('asset/image/back.png'), '메인으로 돌아가기', self)
        back_main.setShortcut('Backspace')
        back_main.triggered.connect(self.back_to_main)

        menubar.setNativeMenuBar(False)
        fileMenu = menubar.addMenu('&Game')
        fileMenu.addAction(exit)
        fileMenu.addAction(regame)
        if __name__ != '__main__':
            fileMenu.addAction(back_main)

        self.setWindowTitle('틱택토')
        self.setWindowIcon(QIcon('asset/image/tic-tac-toe.png'))
        self.setFixedSize(self.sizeHint())
        self.show()

    def back_to_main(self):
        pass

class gamewinodw(QWidget):
    def __init__(self):
        super().__init__()
        self.turn = '○'
        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)

        self.btn_list = []
        for i in range(3):
            temp = []
            for j in range(3):
                temp.append(QPushButton(""))
                temp[j].setFixedSize(120, 120)
                font = temp[j].font()
                font.setPointSize(50)
                temp[j].setFont(font)
            self.btn_list.append(temp)

        for i in range(3):
            for j in range(3):
                grid.addWidget(self.btn_list[i][j], i, j)
                self.btn_list[i][j].clicked.connect(self.btn_function)

    def btn_function(self):
        e = self.sender()
        e.setText(self.turn)
        e.setEnabled(False)

        for i in range(3):
            if self.btn_list[i][0].text() == self.turn and self.btn_list[i][1].text() == self.turn and self.btn_list[i][2].text() == self.turn or \
                self.btn_list[0][i].text() == self.turn and self.btn_list[1][i].text() == self.turn and self.btn_list[2][i].text() == self.turn:
                self.win_player()
                return
        if self.btn_list[0][0].text() == self.turn and self.btn_list[1][1].text() == self.turn and self.btn_list[2][2].text() == self.turn or \
            self.btn_list[0][2].text() == self.turn and self.btn_list[1][1].text() == self.turn and self.btn_list[2][0].text() == self.turn:
            self.win_player()
            return
        sw = 0
        for i in range(3):
            for j in range(3):
                if self.btn_list[i][j].isEnabled() == True:
                    sw = 1
        if sw == 0:
            self.draw()
            return

        if self.turn == '○':
            self.turn = '◇'
        elif self.turn == '◇':
            self.turn = '○'

    def win_player(self):
        replay = QMessageBox.question(self, '', self.turn+'플레이어가 승리하였습니다.\n다시 플레이 하시겠습니까?', QMessageBox.Yes | QMessageBox.No)
        if replay == QMessageBox.Yes:
            self.replay()
        else:
            qApp.quit()

    def draw(self):
        replay = QMessageBox.question(self, '', '무승부입니다.\n다시 플레이 하시겠습니까?', QMessageBox.Yes | QMessageBox.No)
        if replay == QMessageBox.Yes:
            self.replay()
        else:
            qApp.quit()

    def replay(self):
        self.turn = '○'
        for i in range(3):
            for j in range(3):
                self.btn_list[i][j].setEnabled(True)
                self.btn_list[i][j].setText('')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = main()
    sys.exit(app.exec_())