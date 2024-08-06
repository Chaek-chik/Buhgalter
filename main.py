# работа с базой данных
# https://russianblogs.com/article/18821207818/
# https://www.codetd.com/ru/article/6892811

# https://stackoverflow.com/questions/21013356/how-to-display-in-qtablewidget-the-data-from-sqlite
# https://www.youtube.com/watch?v=YySB6tkjZ7Y
# https://www.piknad.ru/pyQtable3.php?ysclid=lsdge4h541231181510
# https://doc.qt.io/qtforpython-5/PySide2/QtWidgets/QTableWidget.html
# структура запроса в поисковике: как в PyQt5 вывести базу данных в QTableWidget



from formcreator import mainForm, dialogFormTask, dialogFormFinance, app

from Flags import Flags
from MainForm.changeRecords import AddRecordClick, DelRecordClick, EditRecordClick
from MainForm.onClickCalendar import onClickCalendar
from MainForm.CheckBoxClick import CheckBoxClick
from DialogFormTask.DialogFormTaskClose import dialogFormTaskClose
from DialogFormFinance.DialogFormFinanceClose import dialogFormFinanceClose
from MainForm.DatePeriod import SetDateIn, SetDateOut

flag = Flags()


mainForm.ButtonAddRecord.clicked.connect(AddRecordClick)
mainForm.ButtonDeleteRecord.clicked.connect(DelRecordClick)
mainForm.ButtonEditRecord.clicked.connect(EditRecordClick)
mainForm.calendarWidget.clicked.connect(onClickCalendar)
mainForm.checkBoxFilterDate.clicked.connect(CheckBoxClick)
mainForm.dateEditIn.dateChanged.connect(SetDateIn)
mainForm.dateEditOut.dateChanged.connect(SetDateOut)


dialogFormTask.ButtonCancel.clicked.connect(dialogFormTaskClose)
dialogFormFinance.ButtonCancel.clicked.connect(dialogFormFinanceClose)

app.exec()