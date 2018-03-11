# coding: utf-8
from __future__ import print_function
from lib import *

from script_group import *


class MainWindow(MainWindowBase):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.__groups_tab = None
        self.__groups = []

    def _setup_ui(self, root):
        print('setup_ui')

        create_group_button = button(u'グループを作成する', clicked=self.add_group)
        create_group_button.setVisible(False)

        self.__groups_tab = QTabWidget()
        self.__groups_tab.setTabsClosable(True)
        self.__groups_tab.tabCloseRequested.connect(self.delete_group)

        self.__groups = ScriptGroupView.load_all()
        for group in self.__groups:
            self.__groups_tab.addTab(group, group.name)

        root.setLayout(QVBoxLayout().add_range(
            create_group_button,
            self.__groups_tab
        ))

    def _shutdown_ui(self):
        print('shutdown')

    @signal_handler
    def add_group(self, _):
        name, ok = QInputDialog.getText(self, u'グループの追加', u'名前を入力してください')
        if not ok:
            return

        group = ScriptGroupView.create(name)
        self.__groups_tab.addTab(group, group.name)
        self.__groups_tab.setCurrentWidget(group)

    @signal_handler
    def delete_group(self, _, index):
        group = self.__groups_tab.widget(index)
        group.clear()
        self.__groups_tab.removeTab(index)


if __name__ == '__main__':
    def main():
        w = MainWindow()
        w.setup_ui()
        return w.show()
    run_application(main)
