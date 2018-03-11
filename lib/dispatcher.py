# coding: utf-8
from pyside_module import *

__all__ = ['Dispatcher']


class Dispatcher(QObject):

    @staticmethod
    def begin_invoke(func):
        global invoker
        QCoreApplication.postEvent(invoker, InvokeEvent(func))


class InvokeEvent(QEvent):

    EVENT_TYPE = QEvent.Type(QEvent.registerEventType())

    def __init__(self, callback):
        super(InvokeEvent, self).__init__(self, InvokeEvent.EVENT_TYPE)
        self.callback = callback


class Invoker(QObject):

    def __init__(self):
        super(Invoker, self).__init__()

    def event(self, e):
        e.callback()


invoker = Invoker()

