import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QProgressBar
from PyQt5.QtCore import QBasicTimer


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 진행 표시줄 생성
        self.pbar = QProgressBar(self)
        # 진행 표시줄 위치 및 크기 설정
        self.pbar.setGeometry(30, 40, 200, 25)

        # 버튼 생성
        self.btn = QPushButton('Start', self)
        # 버튼 위치 설정
        self.btn.move(40, 80)
        # 버튼 동작 설정 : doAction 실행
        self.btn.clicked.connect(self.doAction)

        self.timer = QBasicTimer()
        self.step = 0

        self.setWindowTitle('QProgressBar')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    # 이벤트 값을 매개 변수로 timerEvent 메서드를 실행
    # MyApp에 변화가 생길시 그 값을 매개 변수로 step += 1 을 수행하고 pbar에 값을 전달
    # MyApp에 변화: timer 동작
    def timerEvent(self, e):
        if self.step >= 100:
            self.timer.stop()
            self.btn.setText('Finished')
            return

        self.step = self.step + 1
        self.pbar.setValue(self.step)

    def doAction(self):
        # isActive() : QTimer가 작동중인지 체크합니다. QTimer가 작동중이면 True를, 멈춰있으면 False를 반환합니다.
        # timer가 동작중 일때 btn을 누르면 타이머는 멈추고, btn에 start text를 보여라
        if self.timer.isActive():
            self.timer.stop()
            self.btn.setText('Start')
        # timer가 멈춰있을때 btn을 누르면 타이머는 동작하고, btn에 stop text를 보여라
        else:
            # start 메서드 ( 진행시간, 이벤트 수행 객체)
            self.timer.start(100, self)
            self.btn.setText('Stop')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())