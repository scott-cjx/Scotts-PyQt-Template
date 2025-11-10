
from PySide6.QtWidgets import QWidget, QStackedWidget, QVBoxLayout, QLabel, QPushButton, QApplication, QMessageBox
from PySide6.QtGui import QShortcut, QKeySequence

from typing import Optional
import sys
import platform

from BaseSharedMemory import BaseSharedMemoryDict, baseSharedMemoryDict


class BaseWidget(QWidget):
    
    # private
    _baseParentWidget: Optional[QWidget] = None
    _sharedMemory: BaseSharedMemoryDict = None
    _subwidgets: list = []
    _subwidgets_nolayout: list = []
    __cleaned: bool = False

    __all_subwidgets: list = []

    # super private
    __ui_isSetup = False

    @property
    def baseParentWidget(self):
        return self._baseParentWidget
    
    @baseParentWidget.setter
    def baseParentWidget(self, value):
        self._baseParentWidget = value

    @property
    def sharedMemory(self):
        """Return the shared resource for database management."""
        return self._sharedMemory
    
    @sharedMemory.setter
    def sharedMemory(self, value: BaseSharedMemoryDict):
        """Set the shared resource for database management."""
        self._sharedMemory = value

    def ui_addSubwidget(self, widget: QWidget, addToLayout: bool = True):
        
        if isinstance(widget, BaseWidget):
            widget.baseParentWidget = self
            if widget.sharedMemory is None:
                widget.sharedMemory = self.sharedMemory
            
        self.__all_subwidgets.append(widget)

        if addToLayout:
            self.layout().addWidget(widget)

    def __init__(self, parent = None, sharedMem = None):
        super().__init__()
        self.setLayout(QVBoxLayout())

        self.baseParentWidget = parent
        if self.baseParentWidget:
            self._sharedMemory = self.baseParentWidget._sharedMemory if self.baseParentWidget._sharedMemory else sharedMem
        else:
            self._sharedMemory = sharedMem

        self.be_setup()
        self.ui_setup()

        for widget in self._subwidgets:
            self.ui_addSubwidget(widget, True)

        for widget in self._subwidgets_nolayout:
            self.ui_addSubwidget(widget, False)

    def be_setup(self):
        pass
    
    def be_update(self):
        pass

    def be_cleanup(self):
        pass
    
    def ui_setup(self):
        assert not self.__ui_isSetup
        self.__ui_isSetup = True
        self._setup_close_shortcuts()

    def ui_update(self):
        assert self.__ui_isSetup
        for widget in self._subwidgets:
            if hasattr(widget, "ui_update"):
                widget.ui_update()

    def __ui_cleanup(self):
        for widget in self._subwidgets:
            if hasattr(widget, "ui_cleanup"):
                widget.ui_cleanup()
        self._subwidgets.clear()

    def uibe_cleanup(self):
        if not self.__cleaned:
            self.be_cleanup()
            self.__ui_cleanup()
            self.__cleaned = True

            if not self.baseParentWidget:
                for widget in self.__all_subwidgets:
                    if hasattr(widget, "uibe_cleanup"):
                        widget.uibe_cleanup()

    def __del__(self):
        self.uibe_cleanup()
    
    def closeEvent(self, event):
        self.uibe_cleanup()
        super().closeEvent(event)
    
    def _demo(self):
        pass

    def _setup_close_shortcuts(self):
        """Set up standard close/quit shortcuts for macOS, Windows, Linux."""

        # Cmd+Q, Cmd+W for macOS
        if platform.system() == "Darwin":
            QShortcut(QKeySequence("Meta+Q"), self, self.close)
            QShortcut(QKeySequence("Meta+W"), self, self.close)

        # Ctrl+W and Alt+F4 for Windows/Linux
        else:
            QShortcut(QKeySequence("Ctrl+W"), self, self.close)
            QShortcut(QKeySequence("Alt+F4"), self, self.close)

    @classmethod
    def demo(cls, window_sz=(600, 400), min_window_sz=(600, 400)):
        """Launch the widget standalone for demo/testing purposes."""
        app = QApplication.instance() or QApplication(sys.argv)
        widget = cls()

        widget = cls(sharedMem=baseSharedMemoryDict)

        if hasattr(widget, '_demo') and callable(getattr(widget, '_demo')):
            widget._demo()

        widget.setWindowTitle(cls.__name__)
        widget.resize(window_sz[0], window_sz[1])
        widget.setMinimumSize(min_window_sz[0], min_window_sz[1])
        widget.show()
        app.exec()

if __name__ == "__main__":
    BaseWidget.demo()
