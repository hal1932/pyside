# coding: utf-8
import functools
from pyside_module import *


def signal_handler(handler):
    @functools.wraps(handler)
    def wapper(self, *args, **kwargs):
        handler(self, self.sender(), *args, **kwargs)
    return wapper


def button(label, icon=None, tooltip=None, clicked=None):
    self = QPushButton(label)

    if icon is not None:
        icon_obj = None
        if isinstance(icon, QIcon):
            icon_obj = icon
        elif isinstance(icon, QPixmap):
            icon_obj = QIcon(icon)
        elif isinstance(icon, str):
            icon_obj = QIcon(QPixmap(icon))
        self.setIcon(icon_obj)

    if tooltip is not None:
        self.setToolTip(tooltip)

    if clicked is not None:
        self.clicked.connect(clicked)

    return self

