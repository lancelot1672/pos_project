from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import pymysql.cursors
import sys


class MyWindow(QDialog):
    def __init__(self):         #클래스 실행되면 실행되는 함수
        super().__init__()
        self.setupUI()
    
    # 새로운창 띄우는 함수
    def showModal(self):
        return super().exec_()

    def setupUI(self):  # 보여주기
        self.resize(993, 651)  # 다이얼로그의 크기 설정
        self.setFixedSize(993,651)      #사이즈 고정
        self.setWindowTitle("판매 내역 보기")
        self.CreateCalendar()  # 캘린더 만들기
        self.CreateTableWidget()
        self.CreateBtn()
        self.CreateLabel()
        self.CreateTextField()


    def showDate(self,date):
        date = date.toString()
        listDate = str(date).split()
        self.dateText = listDate[3] + '-' + listDate[1] + '-' +listDate[2]
        self.field.setText(self.dateText)



    def CreateCalendar(self):                                       #캘린더의 속성
        self.calendar = QCalendarWidget(self)
        self.calendar.setGeometry(720,30,272,183)
        self.date = self.calendar.selectedDate()
        self.calendar.clicked[QDate].connect(self.showDate)


    def CreateTableWidget(self):                                    #테이블위젯 속성
        self.tableWidget = QTableWidget(self)
        self.tableWidget.setGeometry(0,30,721,621)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(31)

        #행의 넓이 정의
        self.tableWidget.setColumnWidth(0, self.tableWidget.width() / 5)
        self.tableWidget.setColumnWidth(1, self.tableWidget.width() / 2)
        self.tableWidget.setColumnWidth(2, 97)
        self.tableWidget.setColumnWidth(3, 97)
        for i in range(0,100):                                                   #열 100개
            item = QTableWidgetItem()
            self.tableWidget.setVerticalHeaderItem(i, item)

        TextList = ['시간','내역','금액','결제']

        for i in range(0, 4):                                                   #행 4개
            item = self.item_AlignCenter(str(TextList[i]))
            self.tableWidget.setHorizontalHeaderItem(i, item)

    def CreateBtn(self):                                        #버튼 속성
        self.btn1 = QPushButton(self)
        self.btn1.setGeometry(720,240,274,31)
        self.btn1.setText("조회하기")
        self.btn1.clicked.connect(self.btn1_Event)

        self.btn2 = QPushButton(self)
        self.btn2.setGeometry(720, 510, 274, 71)
        self.btn2.setText("반품하기")
        self.btn2.clicked.connect(self.btn2_Event)

        self.btn3 = QPushButton(self)
        self.btn3.setGeometry(720, 580, 274, 71)
        self.btn3.setText("뒤로가기")
        self.btn3.clicked.connect(self.btn3_Event)

    def CreateLabel(self):                                  # 레이블 속성
        self.label1 = QLabel(self)
        self.label1.setText("일일 매출 조회")
        self.label1.setGeometry(450,10,91,16)

    def CreateTextField(self):
        self.field = QTextEdit(self)
        self.field.setGeometry(720,210,274,31)

        # 현재시간 가져오기
        import datetime
        now = datetime.datetime.now()
        s = now.strftime('%Y-%m-%d')

        #현재시간 필드에 설정해주기
        self.field.setText(s)
        self.dateText = s

    def btn1_Event(self):               #조회하기 버튼
        self.tableWidget.clearContents()        #내용 초기화
        import DBCon
        conn = pymysql.connect(
            host='localhost',
            user='root',
            password='ehdfbf8749',
            db='pos_db',
            charset='utf8'
        )
        rcount, list2 = DBCon.DB_Test(conn,self.dateText)

        try:
            for i in range(0, rcount):
                for j in range(0,4):
                    item = self.item_AlignCenter(str(list2[i][j]))
                    self.tableWidget.setItem(i, j, item)

        except Exception as e:
            print(e)

    def btn2_Event(self):  # 반품하기 버튼
        try:
            a = self.tableWidget.currentRow()
            print(a)
            item = self.tableWidget.item(a,0).text()
            import DBCon
            conn = pymysql.connect(
                host='localhost',
                user='root',
                password='ehdfbf8749',
                db='pos_db',
                charset='utf8'
            )
            DBCon.DB_Delect(conn,item)
            self.tableWidget.clearContents()  # 내용 초기화
            rcount, list2 = DBCon.DB_Test(conn, self.dateText)
            try:
                for i in range(0, rcount):
                    for j in range(0,4):
                        item = self.item_AlignCenter(str(list2[i][j]))
                        self.tableWidget.setItem(i, j, item)
            except Exception as e:
                print(e)
        except Exception as e:
            print(e)


    def btn3_Event(self):  # 뒤로가기 버튼
        self.close()

    def item_AlignCenter(self, text):          #가운데 정렬하는 함수
        item = QTableWidgetItem()
        item.setTextAlignment(Qt.AlignCenter)  # 가운데 정렬
        item.setText(text)
        return item


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    sys.exit(app.exec_())
