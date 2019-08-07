import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QLabel, QGridLayout, QMessageBox, qApp, QMainWindow, QAction, QHBoxLayout, QVBoxLayout
from PyQt5.QtGui import QIcon
import copy as cp
from random import randint
from PyQt5.QtMultimedia import QSound
from PyQt5.QtTest import QTest
import mainWindow

class main(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        title=QLabel('땅따먹기')
        f=title.font()
        f.setPointSize(50)
        f.setBold(True)
        f.setFamily('배달의 민족 한나체 Air')
        title.setFont(f)

        btn_list=[QPushButton('2인 플레이'), QPushButton('3인 플레이'), QPushButton('4인 플레이')]
        for i in range(3):
            f=btn_list[i].font()
            f.setFamily('배달의 민족 한나체 Air')
            f.setPointSize(20)
            btn_list[i].setFont(f)
            btn_list[i].setFixedSize(150, 60)

        btn_list[0].clicked.connect(self.call_game2)
        btn_list[1].clicked.connect(self.call_game3)
        btn_list[2].clicked.connect(self.call_game4)

        back_main_button = QPushButton('돌아가기')
        f = back_main_button.font()
        f.setFamily('배달의 민족 한나체 Air')
        f.setPointSize(15)
        back_main_button.setFont(f)
        back_main_button.setFixedSize(100, 40)
        back_main_button.clicked.connect(self.back_to_main)

        hback = QHBoxLayout()
        hback.addStretch(1)
        hback.addWidget(back_main_button)

        htitle = QHBoxLayout()
        htitle.addStretch(1)
        htitle.addWidget(title)
        htitle.addStretch(1)

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        for i in range(3):
            hbox.addWidget(btn_list[i])
        hbox.addStretch(1)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(htitle)
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        if __name__ == '__main__':
            vbox.addStretch(1)
        else:
            vbox.addLayout(hback)

        self.setLayout(vbox)

        self.resize(800, 500)
        self.setWindowTitle('땅따먹기')
        self.setWindowIcon(QIcon('asset/image/flag.png'))
        self.show()

    def call_game2(self):
        self.game_window = game_main(2)
        self.close()

    def call_game3(self):
        self.game_window = game_main(3)
        self.close()

    def call_game4(self):
        self.game_window = game_main(4)
        self.close()

    def back_to_main(self):
        self.mainwindow = mainWindow.main()
        self.close()

class game_main(QMainWindow):
    def __init__(self, player):
        super().__init__()
        self.play = gamewindow(player)
        self.setCentralWidget(self.play)

        menubar = self.menuBar()

        exit = QAction(QIcon('asset/image/exit.png'), '종료', self)
        exit.setShortcut('Esc')
        exit.triggered.connect(qApp.quit)

        regame = QAction(QIcon('asset/image/replay.png'), '재시작', self)
        regame.setShortcut('R')
        regame.triggered.connect(self.play.set_board)

        over = QAction(QIcon('asset/image/over.png'), '판 엎기', self)
        over.setShortcut('Space')
        over.triggered.connect(self.play.over_board)

        back = QAction(QIcon('asset/image/back.png'), '메인으로 돌아가기', self)
        back.setShortcut('Backspace')
        back.triggered.connect(self.back)

        menubar.setNativeMenuBar(False)
        fileMenu = menubar.addMenu('&Game')
        fileMenu.addAction(exit)
        fileMenu.addAction(regame)
        fileMenu.addAction(over)
        fileMenu.addAction(back)

        self.setWindowTitle('땅따먹기')
        self.setWindowIcon(QIcon('asset/image/flag.png'))
        self.setFixedSize(self.sizeHint())
        self.show()

    def back(self):
        self.main_window = main()
        self.close()

class gamewindow(QWidget):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.num_list = []
        t3, t4 = [], []
        for i in range(8):
            t1, t2 = [], []
            for j in range(8):
                t1.append(0)
                t2.append('black')
            t3.append(t1)
            t4.append(t2)
        self.num_list.append(t3)
        self.num_list.append(t4)
        self.initUI()

    def initUI(self):
        grid=QGridLayout()
        self.setLayout(grid)

        self.player_button=[]
        for i in range(4):
            name = 'player ' + str(i+1)
            self.player_button.append(QPushButton(name))
            if i == 0:
                self.player_button[i].setStyleSheet('QPushButton{color:red;}')
                grid.addWidget(self.player_button[i], 0, 0, 2, 1)
            elif i == 1:
                self.player_button[i].setStyleSheet('QPushButton{color:blue;}')
                grid.addWidget(self.player_button[i], 6, 9, 2, 1)
            elif i == 2:
                self.player_button[i].setStyleSheet('QPushButton{color:green;}')
                grid.addWidget(self.player_button[i], 0, 9, 2, 1)
            elif i == 3:
                self.player_button[i].setStyleSheet('QPushButton{color:yellow;}')
                grid.addWidget(self.player_button[i], 6, 0, 2, 1)

            f = self.player_button[i].font()
            f.setPointSize(20)
            f.setFamily('배달의 민족 한나체 Air')
            self.player_button[i].setFont(f)
            self.player_button[i].setFixedSize(130, 60)
            self.player_button[i].clicked.connect(self.next_turn)

        self.btn_list=[]
        for i in range(8):
            temp = []
            for j in range(8):
                b = QPushButton(self.set_num(self.num_list[0][i][j]))
                b.setFixedSize(50, 50)
                f = b.font()
                f.setPointSize(20)
                b.setStyleSheet('QPushButton{color:' + self.num_list[1][i][j] + ';}')
                b.setFont(f)
                b.clicked.connect(self.expansion)
                temp.append(b)
                grid.addWidget(b, i, j+1)
            self.btn_list.append(temp)

        self.set_board()

    def expansion(self):
        e = self.sender()
        # 자기 좌표 알아내기
        Coor = []
        for i in range(8):
            for j in range(8):
                if self.btn_list[i][j] == e:
                    Coor = [i, j]
                    break
            if Coor != []: break
        if e.text() != '' and self.num_list[1][Coor[0]][Coor[1]] == self.turn:
            # 확장 시작
            this_turn, next_turn = [], []
            this_turn.append(Coor)
            while len(this_turn) != 0:
                overlap = []
                for i in range(len(this_turn)):
                    y, x = this_turn[i][0], this_turn[i][1]
                    self.num_up(y, x)
                    self.btn_list[y][x].setText(self.set_num(self.num_list[0][y][x]))
                    self.num_list[1][y][x] = self.turn
                    self.btn_list[y][x].setStyleSheet('QPushButton{color:' + self.num_list[1][y][x] + ';}')

                    sw = True
                    for j in range(len(overlap)):
                        if overlap[j] == this_turn[i]:
                            sw = False
                            break
                    if self.num_list[0][y][x] >= 4 and self.num_list[0][y][x] <= 7 and sw:
                        if x > 0: next_turn.append([y, x - 1])
                        if x < 7: next_turn.append([y, x + 1])
                        if y > 0: next_turn.append([y - 1, x])
                        if y < 7: next_turn.append([y + 1, x])

                        overlap.append(this_turn[i])

                QSound.play('asset/sound/chess.wav')

                for i in range(len(this_turn)):
                    y, x = this_turn[i][0], this_turn[i][1]
                    if self.num_list[0][y][x] >= 4:
                        self.num_list[0][y][x] -= 4
                        if self.num_list[0][y][x] == 0:
                            self.num_list[1][y][x] = 'black'

                    self.btn_list[y][x].setText(self.set_num(self.num_list[0][y][x]))
                    self.btn_list[y][x].setStyleSheet('QPushButton{color:' + self.num_list[1][y][x] + ';}')

                this_turn = cp.copy(next_turn)
                next_turn = []

            # 확장 종료 이후 턴 변경
            self.check_winner()
            self.next_turn()

    def check_winner(self):
        sw = False
        for i in range(8):
            for j in range(8):
                if self.num_list[1][i][j] != 'black' and self.num_list[1][i][j] != self.turn:
                    sw = True
                    break
            if sw:
                break
        if not sw:
            winner = '플레이어 0'
            if self.turn == 'red':
                winner = winner.replace('0', '1')
            elif self.turn == 'blue':
                winner = winner.replace('0', '2')
            elif self.turn == 'green':
                winner = winner.replace('0', '3')
            else:
                winner = winner.replace('0', '4')
            replay = QMessageBox.question(self, '', winner + ' 이(가) 승리하였습니다.\n다시 플레이 하시겠습니까?', QMessageBox.Yes | QMessageBox.No)
            if replay == QMessageBox.Yes:
                self.set_board()
            else:
                qApp.quit()

    def set_num(self, n):
        if n == 0:
            return ''
        elif n > 7:
            return '!'
        else:
            return str(n)

    def num_up(self, i, j):
        self.num_list[0][i][j] += 1
        if self.num_list[0][i][j] > 7:
            self.num_list[0][i][j] = 7

    def set_board(self):
        for i in range(8):
            for j in range(8):
                self.num_list[0][i][j] = 0
                self.num_list[1][i][j] = 'black'
                self.btn_list[i][j].setText(self.set_num(self.num_list[0][i][j]))
                self.btn_list[i][j].setStyleSheet('QPushButton{color:' + self.num_list[1][i][j] + ';}')

        self.turn = 'red'
        self.num_list[0][1][1] = 3
        self.num_list[1][1][1] = 'red'
        self.btn_list[1][1].setText(self.set_num(self.num_list[0][1][1]))
        self.btn_list[1][1].setStyleSheet('QPushButton{color:' + self.num_list[1][1][1] + ';}')

        self.num_list[0][6][6] = 3
        self.num_list[1][6][6] = 'blue'
        self.btn_list[6][6].setText(self.set_num(self.num_list[0][6][6]))
        self.btn_list[6][6].setStyleSheet('QPushButton{color:' + self.num_list[1][6][6] + ';}')

        if self.player >= 3:
            self.num_list[0][1][6] = 3
            self.num_list[1][1][6] = 'green'
            self.btn_list[1][6].setText(self.set_num(self.num_list[0][1][6]))
            self.btn_list[1][6].setStyleSheet('QPushButton{color:' + self.num_list[1][1][6] + ';}')

        if self.player == 4:
            self.num_list[0][6][1] = 3
            self.num_list[1][6][1] = 'yellow'
            self.btn_list[6][1].setText(self.set_num(self.num_list[0][6][1]))
            self.btn_list[6][1].setStyleSheet('QPushButton{color:' + self.num_list[1][6][1] + ';}')

        if self.player <= 3:
            self.player_button[3].setEnabled(False)
        if self.player == 2:
            self.player_button[2].setEnabled(False)

        self.player_btn_set()

    def check_over(self):
        sw = False
        for i in range(8):
            for j in range(8):
                if self.num_list[1][i][j] == self.turn:
                    sw = True

        if not sw:
            self.next_turn()

    def next_turn(self):
        if self.turn == 'red':
            self.turn = 'blue'
        elif self.turn == 'blue':
            if self.player == 2:
                self.turn = 'red'
            else:
                self.turn = 'green'
        elif self.turn == 'green':
            if self.player == 3:
                self.turn = 'red'
            else:
                self.turn = 'yellow'
        else:
            self.turn = 'red'

        self.check_over()
        self.player_btn_set()

    def player_btn_set(self):
        if self.turn == 'red':
            self.player_button[0].setEnabled(True)
            self.player_button[1].setEnabled(False)
            self.player_button[2].setEnabled(False)
            self.player_button[3].setEnabled(False)
        elif self.turn == 'blue':
            self.player_button[0].setEnabled(False)
            self.player_button[1].setEnabled(True)
            self.player_button[2].setEnabled(False)
            self.player_button[3].setEnabled(False)
        elif self.turn == 'green':
            self.player_button[0].setEnabled(False)
            self.player_button[1].setEnabled(False)
            self.player_button[2].setEnabled(True)
            self.player_button[3].setEnabled(False)
        else:
            self.player_button[0].setEnabled(False)
            self.player_button[1].setEnabled(False)
            self.player_button[2].setEnabled(False)
            self.player_button[3].setEnabled(True)

    def over_board(self):
        self.set_board()
        for i in range(8):
            for j in range(8):
                t = randint(0, 19)
                if t == 0:
                    self.btn_list[i][j].setText(self.set_num(randint(0, 3)))
                    self.btn_list[i][j].setStyleSheet('QPushButton{color: red;}')
                elif t == 1:
                    self.btn_list[i][j].setText(self.set_num(randint(0, 3)))
                    self.btn_list[i][j].setStyleSheet('QPushButton{color: blue;}')
                elif t == 2:
                    self.btn_list[i][j].setText(self.set_num(randint(0, 3)))
                    self.btn_list[i][j].setStyleSheet('QPushButton{color: green;}')
                elif t == 3:
                    self.btn_list[i][j].setText(self.set_num(randint(0, 3)))
                    self.btn_list[i][j].setStyleSheet('QPushButton{color: yellow;}')

        QTest.qSleep(10)

        song = QSound('asset/sound/strike.wav')
        song.play()

        replay = QMessageBox.question(self, '', '판을 엎었습니다!!\n다시 플레이 하시겠습니까?', QMessageBox.Yes | QMessageBox.No)
        if replay == QMessageBox.Yes:
            self.set_board()
        else:
            qApp.quit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = main()
    sys.exit(app.exec_())