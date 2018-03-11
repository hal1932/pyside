# coding: utf-8
from lib import *


class TestListModel(QAbstractListModel):

    def __init__(self):
        super(TestListModel, self).__init__(None)
        self.__items = []

    def rowCount(self, parent=QModelIndex()):
        return len(self.__items)

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid() or not 0 <= index.row() < len(self.__items):
            return None

        if role == Qt.DisplayRole:
            return self.__items[index.row()]

        return None

    def append(self, item):
        self.beginInsertRows(QModelIndex(), len(self.__items), len(self.__items))
        self.__items.append(item)
        self.endInsertRows()


class MainWindow(MainWindowBase):

    def __init__(self):
        super(MainWindow, self).__init__(None)

    def _setup_ui(self, root):
        list_view = QListView()
        list_model = TestListModel()
        list_view.setModel(list_model)

        button = QPushButton()
        button.setText('add')
        button.clicked.connect(
            lambda: list_model.append(list_model.rowCount()))

        root.setLayout(QVBoxLayout().add_range(
            list_view,
            button
        ))


if __name__ == '__main__':
    def main():
        w = MainWindow()
        w.setup_ui()
        return w.show()
    run_application(main)


