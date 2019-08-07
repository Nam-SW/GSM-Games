import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QGridLayout, QApplication, QMessageBox, QAction, qApp, QMainWindow
from PyQt5.QtGui import QIcon
from random import randint
from PyQt5.QtMultimedia import QSound

class main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.play = gamewindow()
        self.setCentralWidget(self.play)

        menubar = self.menuBar()

        exit = QAction(QIcon('asset/image/exit.png'), '종료', self)
        exit.setShortcut('Esc')
        exit.triggered.connect(qApp.quit)

        regame = QAction(QIcon('asset/image/replay.png'), '재시작', self)
        regame.setShortcut('R')
        regame.triggered.connect(self.play.replay)

        over = QAction(QIcon('asset/image/over.png'), '판 엎기', self)
        over.setShortcut('Space')
        over.triggered.connect(self.play.over_board)

        back_main = QAction(QIcon('asset/image/back.png'), '메인으로 돌아가기', self)
        back_main.setShortcut('Backspace')
        back_main.triggered.connect(self.back_to_main)

        menubar.setNativeMenuBar(False)
        fileMenu = menubar.addMenu('&Game')
        fileMenu.addAction(exit)
        fileMenu.addAction(regame)
        fileMenu.addAction(over)
        if __name__ != '__main__':
            fileMenu.addAction(back_main)

        self.setWindowTitle('오목')
        self.setWindowIcon(QIcon('asset/image/grid.png'))
        self.setFixedSize(self.sizeHint())
        self.show()

    def back_to_main(self):
        pass

class gamewindow(QWidget):
    def __init__(self):
        super().__init__()
        self.turn = 'black'
        self.color_list = []
        for i in range(19):
            temp = []
            for j in range(19):
                temp.append('')
            self.color_list.append(temp)
        self.initUI()

    def initUI(self):
        grid=QGridLayout()
        grid.setHorizontalSpacing(0)
        grid.setVerticalSpacing(0)
        self.setLayout(grid)

        self.btn_list=[]
        for i in range(19):
            temp=[]
            for j in range(19):
                if i == 0 and j == 0: c='┌'
                elif i == 0 and j == 18: c='┐'
                elif i == 18 and j == 0: c='└'
                elif i == 18 and j == 18: c='┘'
                elif i == 0: c='┬'
                elif i == 18: c='┴'
                elif j == 0: c='├'
                elif j == 18: c='┤'
                else: c='┼'
                btn=QPushButton(c)
                btn.setFixedSize(35, 35)
                font=btn.font()
                font.setPointSize(25)
                btn.setFont(font)
                temp.append(btn)
                btn.setStyleSheet('background-color: #D89D1E;')
            self.btn_list.append(temp)

        for i in range(19):
            for j in range(19):
                self.btn_list[i][j].clicked.connect(self.btn_function)
                grid.addWidget(self.btn_list[i][j], i, j)

    def btn_function(self):
        e = self.sender()
        if e.text() != '●':
            Coor = []
            for i in range(19):
                for j in range(19):
                    if self.btn_list[i][j] == e:
                        Coor = [i, j]
                        break
                if Coor != []: break
            self.color_list[Coor[0]][Coor[1]] = self.turn
            e.setText('●')
            e.setStyleSheet('background-color: #D89D1E; color: ' + self.turn +';')
            QSound.play('asset/sound/chess.wav')
            #self.winner_check()
            for i in range(2, 17):
                for j in range(19):
                    if self.color_list[j][i - 2] == self.turn and self.color_list[j][i - 1] == self.turn and \
                            self.color_list[j][i] == self.turn and self.color_list[j][i + 1] == self.turn and \
                            self.color_list[j][i + 2] == self.turn:
                        self.win_player()
                        return
                    elif self.color_list[i - 2][j] == self.turn and self.color_list[i - 1][j] == self.turn and \
                            self.color_list[i][j] == self.turn and self.color_list[i + 1][j] == self.turn and \
                            self.color_list[i + 2][j] == self.turn:
                        self.win_player()
                        return
            for i in range(2, 17):
                for j in range(2, 17):
                    if self.color_list[j - 2][i - 2] == self.turn and self.color_list[j - 1][i - 1] == self.turn and \
                            self.color_list[j][i] == self.turn and self.color_list[j + 1][i + 1] == self.turn and \
                            self.color_list[j + 2][i + 2] == self.turn:
                        self.win_player()
                        return
                    elif self.color_list[j + 2][i - 2] == self.turn and self.color_list[j + 1][i - 1] == self.turn and \
                            self.color_list[j][i] == self.turn and self.color_list[j - 1][i + 1] == self.turn and \
                            self.color_list[j - 2][i + 2] == self.turn:
                        self.win_player()
                        return
            self.turn_change()

    def turn_change(self):
        if self.turn == 'black':
            self.turn = 'white'
        elif self.turn == 'white':
            self.turn = 'black'

    def winner_check(self):
        for i in range(2, 17):
            for j in range(19):
                if self.color_list[j][i - 2] == self.turn and self.color_list[j][i - 1] == self.turn and \
                    self.color_list[j][i] == self.turn and self.color_list[j][i + 1] == self.turn and \
                    self.color_list[j][i + 2] == self.turn:
                    self.win_player()
                elif self.color_list[i - 2][j] == self.turn and self.color_list[i - 1][j] == self.turn and \
                    self.color_list[i][j] == self.turn and self.color_list[i + 1][j] == self.turn and \
                    self.color_list[i + 2][j] == self.turn:
                    self.win_player()
        for i in range(2, 17):
            for j in range(2, 17):
                if self.color_list[j - 2][i - 2] == self.turn and self.color_list[j - 1][i - 1] == self.turn and \
                    self.color_list[j][i] == self.turn and self.color_list[j + 1][i + 1] == self.turn and \
                    self.color_list[j + 2][i + 2] == self.turn:
                    self.win_player()
                elif self.color_list[j + 2][i - 2] == self.turn and self.color_list[j + 1][i - 1] == self.turn and \
                    self.color_list[j][i] == self.turn and self.color_list[j - 1][i + 1] == self.turn and \
                    self.color_list[j - 2][i + 2] == self.turn:
                    self.win_player()

    def win_player(self):
        dol = '흑돌' if self.turn == 'black' else '백돌'
        replay = QMessageBox.question(self, '', dol+' 바둑기사가 승리하였습니다.\n다시 플레이 하시겠습니까?', QMessageBox.Yes | QMessageBox.No)
        if replay == QMessageBox.Yes: self.replay()
        else: qApp.quit()

    def replay(self):
        self.turn = 'black'
        for i in range(19):
            for j in range(19):
                self.color_list[i][j] = ''
                self.btn_list[i][j].setStyleSheet('background-color: #D89D1E; color: black;')
                if i == 0 and j == 0: self.btn_list[i][j].setText('┌')
                elif i == 0 and j == 18: self.btn_list[i][j].setText('┐')
                elif i == 18 and j == 0: self.btn_list[i][j].setText('└')
                elif i == 18 and j == 18: self.btn_list[i][j].setText('┘')
                elif i == 0: self.btn_list[i][j].setText('┬')
                elif i == 18: self.btn_list[i][j].setText('┴')
                elif j == 0: self.btn_list[i][j].setText('├')
                elif j == 18: self.btn_list[i][j].setText('┤')
                else: self.btn_list[i][j].setText('┼')

    def over_board(self):
        self.replay()
        for i in range(19):
            for j in range(19):
                t = randint(0, 19)
                if t == 0:
                    self.btn_list[i][j].setText('●')
                    self.btn_list[i][j].setStyleSheet('background-color: #D89D1E; color: black;')
                elif t == 1:
                    self.btn_list[i][j].setText('●')
                    self.btn_list[i][j].setStyleSheet('background-color: #D89D1E; color: white;')

        QSound.play('asset/sound/strike.wav')

        replay = QMessageBox.question(self, '', '판을 엎었습니다!!\n다시 플레이 하시겠습니까?', QMessageBox.Yes | QMessageBox.No)
        if replay == QMessageBox.Yes:
            self.replay()
        else:
            qApp.quit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = main()
    sys.exit(app.exec_())