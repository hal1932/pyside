# coding: utf-8
from pyside_module import *


class __Stretch(object):
    pass


__Streach_instance = __Stretch()


def streach():
    return __Streach_instance


def __box_layout_add(self, item):
    if isinstance(item, QWidget):
        self.addWidget(item)
    elif isinstance(item, QLayout):
        self.addLayout(item)
    elif isinstance(item, __Stretch):
        self.addStretch()
    return self


def __box_layout_add_range(self, *items):
    for item in items:
        __box_layout_add(self, item)
    return self


QBoxLayout.add = __box_layout_add
QBoxLayout.add_range = __box_layout_add_range

