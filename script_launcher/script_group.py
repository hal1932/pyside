# coding: utf-8
from lib import *


class ScriptItem(object):

    @property
    def name(self): return self.__name

    @property
    def description(self): return self.__description

    def __init__(self, name, description=None):
        self.__name = name
        self.__description = description


class ScriptGroup(object):

    @property
    def name(self): return self.__name

    @property
    def items(self): return self.__items

    def __init__(self, name):
        self.__name = name
        self.__items = []

    def load(self):
        for i in xrange(5):
            item = ScriptItem('{}_{}'.format(self.name, i), 'desc_{}_{}'.format(self.name, i))
            self.__items.append(item)


class ScriptItemView(QWidget):

    def __init__(self, item, parent=None):
        super(ScriptItemView, self).__init__(parent=parent)
        self.__item = item

        layout = QHBoxLayout().add_range(
            button(item.name, icon='images/settings.png', tooltip=item.description, clicked=self.execute_item),
            streach()
        )
        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)

    @signal_handler
    def execute_item(self, _):
        print('execute {}'.format(self.__item.name))


class ScriptGroupView(QWidget):

    @staticmethod
    def create(name):
        return ScriptGroupView(name)

    @staticmethod
    def load_all():
        return [ScriptGroupView.load(x) for x in [u'aaa', u'bbb']]

    @staticmethod
    def load(name):
        instance = ScriptGroupView(name)
        instance.__model.load()
        instance.__setup_ui()
        return instance

    @property
    def name(self): return self.__name

    def __init__(self, name, parent=None):
        super(ScriptGroupView, self).__init__(parent=parent)
        self.__root_layout = None

        self.__name = name
        self.__items = []
        self.__model = ScriptGroup(name)

    def clear(self):
        pass

    def __setup_ui(self):
        self.__root_layout = QVBoxLayout()

        for item in self.__model.items:
            self.__root_layout.addWidget(ScriptItemView(item))

        self.__root_layout.addStretch()
        self.setLayout(self.__root_layout)
