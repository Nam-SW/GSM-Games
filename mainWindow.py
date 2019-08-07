import sys
from PyQt5.QtWidgets import QPushButton, QLabel, QWidget, QHBoxLayout, QVBoxLayout, QApplication
from PyQt5.QtGui import QIcon
from PyQt5.QtMultimedia import QSound
import 틱택토_김승길 as tic
import 오목_김유진 as omok
import 땅따먹기_남승우 as earth

class mainwindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        title=QLabel('GSM Games')
        f = title.font()
        f.setPointSize(50)
        f.setBold(True)
        f.setFamily('배달의 민족 한나체 Air')
        title.setFont(f)

        btn_list=[QPushButton('틱택토'), QPushButton('오목'), QPushButton('땅따먹기')]
        for i in range(3):
            f=btn_list[i].font()
            f.setFamily('배달의 민족 한나체 Air')
            f.setPointSize(20)
            btn_list[i].setFont(f)
            btn_list[i].setFixedSize(120, 60)

        btn_list[0].clicked.connect(self.open_tic)
        btn_list[1].clicked.connect(self.open_omok)
        btn_list[2].clicked.connect(self.open_earth)

        self.musicplay()

        htitle=QHBoxLayout()
        htitle.addStretch(1)
        htitle.addWidget(title)
        htitle.addStretch(1)

        hbox=QHBoxLayout()
        hbox.addStretch(1)
        for i in range(3):
            hbox.addWidget(btn_list[i])
        hbox.addStretch(1)

        vbox=QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(htitle)
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        vbox.addStretch(1)

        self.setLayout(vbox)

        self.resize(800, 500)
        self.setWindowTitle('CodeName-C')
        self.setWindowIcon(QIcon('asset/image/game.png'))
        self.show()

    def open_tic(self):
        self.game_window = Tic_Tac_Toe()
        self.close()

    def open_omok(self):
        self.game_window = Omok()
        self.close()

    def open_earth(self):
        self.game_window = earth.main()
        self.close()

    def musicplay(self):
        self.bgm = QSound('')
        self.bgm.play('asset/sound/game_bgm.wav')
s
#############################메인 창 열기 오버라이드#############################
class main(mainwindow):
    def musicplay(self):
        pass

class Tic_Tac_Toe(tic.main):
    def back_to_main(self):
        self.returnmain = main()
        self.close()

class Omok(omok.main):
    def back_to_main(self):
        self.returnmain = main()
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = mainwindow()
    sys.exit(app.exec_())