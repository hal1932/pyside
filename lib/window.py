# coding: utf-8
from pyside_module import *

try:
    from maya.app.general import mayaMixin
    __USE_MAYA_WINDOW = True
except ImportError:
    __USE_MAYA_WINDOW = False


if __USE_MAYA_WINDOW:
    class __MainWindowBase_Maya(mayaMixin.MayaQWidgetBaseMixin, QMainWindow):
        pass
    MainWindowBase = __MainWindowBase_Maya
else:
    class __MainWindowBase(QMainWindow):
        pass
    MainWindowBase = __MainWindowBase


def __window_init(self, *args, **kwargs):
    super(MainWindowBase, self).__init__(*args, **kwargs)


def __window_close(self, e):
    self._shutdown_ui()


def __window_setup_ui(self):
    w = QWidget()
    self.setCentralWidget(w)
    self._setup_ui(w)
    return self


def __window_show(self):
    super(MainWindowBase, self).show()
    return self


# protected methods
def __window_setup_ui_protected(self, central_widget): pass
def __window_shutdown_ui_protected(self): pass


# setup class
MainWindowBase.__init__ = __window_init
MainWindowBase.closeEvent = __window_close
MainWindowBase.setup_ui = __window_setup_ui
MainWindowBase.show = __window_show
MainWindowBase._setup_ui = __window_setup_ui_protected
MainWindowBase._shutdown_ui = __window_shutdown_ui_protected


def run_application(main_func):
    if not __USE_MAYA_WINDOW:
        app = QApplication.instance()
        if app is None:
            app = QApplication([])

    _ = main_func()

    if not __USE_MAYA_WINDOW:
        import sys
        sys.exit(app.exec_())

