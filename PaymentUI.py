from PyQt5.QtWidgets import *

class PayUI(QDialog):
    def __init__(self, conn, text, detail, totalString, total_Price):
        super().__init__()
        self.conn = conn
        self.text = text
        self.detail = detail
        self.total_Price = total_Price
        self.totalString = totalString


        # 문자 변환 테이블
        table = str.maketrans('\n', ' ')

        # string 형으로 변환하여  리스트에 추가하기
        self.detailList = []
        for i in range(len(self.detail)):
            self.detailList.append(str(self.detail[i]).translate(table))
        self.setupUi()

    def showModal(self):
        return super().exec_()

    def setupUi(self):
        self.resize(302, 430)
        self.setFixedSize(302,430)

        self.label = QLabel(self)
        self.label.setGeometry(120, 10, 91, 41)

        self.label2 = QLabel(self)
        self.label2.setGeometry(90, 350, 131, 16)

        self.totalLable = QLabel(self)
        self.totalLable.setGeometry(150, 265, 31, 16)

        self.TextBrowser1 = QTextBrowser(self)
        self.TextBrowser1.setGeometry(20, 60, 256, 192)
        self.TextBrowser2 = QTextBrowser(self)
        self.TextBrowser2.setGeometry(185, 260, 91, 31)

        # 상세 내역 다시 출력하기
        for i in self.detailList:
            self.TextBrowser1.append(i)

        self.TextBrowser2.append(str(self.total_Price))

        self.btn1 = QPushButton(self)
        self.btn1.setGeometry(50, 380, 91, 31)

        self.btn2 = QPushButton(self)
        self.btn2.setGeometry(160, 380, 91, 31)

        self.retranslateUi()


    def retranslateUi(self):
        self.label.setText(self.text)
        self.label2.setText("위 내역이 맞는 지 확인")
        self.totalLable.setText("합계 : ")
        self.btn1.setText("결제")
        self.btn2.setText("취소")
        self.btn1.clicked.connect(self.btn1_Event)
        self.btn2.clicked.connect(self.btn2_Event)

    def btn1_Event(self):  # 결제 하기 최종
        try:
            import DBCon

            DB_list = [self.totalString, self.total_Price, self.text[0:2]]
            print(DB_list)
            DBCon.DB_Insert(self.conn, DB_list)
            self.close()
        except Exception as e:
            print(e)

    def btn2_Event(self):       #취소 버튼
        self.close()
