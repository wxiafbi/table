# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Widget
ct3 = ['G117', 'Z017', 'G125', 'Z049', 'G158', 'G158P-2NO.1', 'G158P-2NO.2', 'G158P-2NO.3', 'G158P-3NO.1', 'G158P-3NO.2', 'G158P-3NO.3', 'G158P-6NO.1', 'G158P-6NO.2', 'G158P-6NO.3',
       'G170', 'G170-2', 'G170-3', 'G170-4', 'G170-6', 'G170-7', 'G170-8', 'G124', 'G135', 'G135-2', 'G135-3', 'G135-4', 'G135-6', 'G135-7', 'G135-8', 'G185', 'G185-2', 'G185-3', 'G185-7', 'G185-8', 'G142', 'G226P4No.1', 'G226P4No.2', 'G226P6No.1', 'G226P6No.2', 'Z015', 'Z074', 'Z074-2', 'Z074-3', 'Z074-4', 'Z074-6', 'Z074-7', 'Z074-8', 'G122', 'G123', 'G126-2', 'G126-4', 'G126-6',
       'G126-8', 'G127-2', 'G127-4', 'G127-6', 'G127-8', 'G129', 'G129-2', 'G129-3', 'G129-4', 'G129-6', 'G129-7', 'G129-8', 'Z052', 'Z052-2', 'Z052-3', 'Z052-4', 'Z052-6', 'Z052-7', 'Z052-8', 'G202',
       'G202-2', 'G202-4', 'G202-5', 'G202-6', 'G202-8', 'Z034', 'Z034-2', 'Z034-3', 'Z034-4', 'Z034-6', 'Z034-7', 'Z034-8', 'G207', 'G207-1', 'G207-2', 'G207-4', 'G207-5', 'G207-6', 'G207-8', 'G136', 'G136-2', 'G136-3', 'G136-4', 'G136-6', 'G136-7', 'G136-8', 'Z051', 'G187', 'G187-2', 'G187-3', 'G187-4', 'G187-6', 'G187-7', 'G187-8', 'G118', 'Z037', 'G206', 'G206-1', 'G206-3', 'G206-5', 'G206-6', 'G206-8', 'Z053', 'Z053-2', 'Z053-3', 'Z053-4', 'Z053-6', 'G120', 'G121', 'Z046', 'Z062', 'Z062-2', 'Z062-4', 'Z062-6', 'Z062-7', 'G119', 'G133-2', 'G133-4', 'G133-6', 'G133-8', 'Z019', 'Z019-2', 'Z019-3', 'Z019-4', 'Z019-6', 'Z019-7', 'Z019-8', 'Z036', 'Z035', 'G113', 'Z030', 'Z054', 'G115', 'Z033', 'Y110', 'Z018', 'Z055', 'G108', 'G109', 'Yan96', 'G112', 'G146-2', 'G146-4', 'G146-6', 'G146-8', 'G148-2', 'G148-4', 'G148-6', 'Yan67', 'G111', 'G150-2', 'G150-8', 'G165-2', 'G165-4', 'G165-6', 'G165-8', 'G167-2', 'G167-4', 'G167-6', 'G167-8', 'G153-6', 'G153-8', 'Z064', 'G110', 'Yan66', 'G151-2', 'G151-4', 'G151-6', 'G151-8', 'G102', 'G103', 'G105', 'G106', 'Yan65', 'Z069', 'Yan63', 'Yan64', 'Yan68', 'Yan69', 'G104', 'Q1259', 'Q1260', 'Q1261', 'Q1262', 'Q1264', 'Q1265', 'Q1266', 'Q1267', 'Q1268', 'G116', 'Z062-3', 'Z062-8', 'Z053-8', 'Z052P-8NO.1', 'Z052P-8NO.2', 'Q10P-3NO.1', 'Q10P-3NO.2']
cp = ['井号', 'Time', 'Distance', 'Distance1', 'Distance2',
      'valu', 'amp', 'temp', 'electricity']
aaaa = len(ct3)
cccc = len(cp)
# first = '__qtablewidgetitem'
first = 'item'
name = []
name1 = []


class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.ui.tableWidget.setShowGrid(True)
        self.ui.tableWidget.setColumnCount(9)
        for i in range(0, len(cp)):
            name.append(first+str(i))
            print(str(name[i]))
            name[i] = QTableWidgetItem()
            self.ui.tableWidget.setHorizontalHeaderItem(i, name[i])
            # name[i]=self.ui.tableWidget.horizontalHeaderItem(i)
            # name[i].ui.setText(QCoreApplication.translate("Widget",cp[i], None));
        self.ui.tableWidget.setRowCount(len(ct3))
        for j in range(0, len(ct3)):
            name1.append(str(ct3[j]))
            print(name1[j])
            name1[j] = QTableWidgetItem()
            self.ui.tableWidget.setVerticalHeaderItem(j, name1[j])
        self.ui.pushButton.setText(
            QCoreApplication.translate("Widget", u"执行", None))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
