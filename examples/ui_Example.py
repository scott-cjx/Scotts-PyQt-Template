from SharedMemory import SharedMemoryDict, sharedMemoryDict
from ui_BaseWidget import BaseWidget

from PySide6.QtWidgets import QLabel

class ExampleWidget(BaseWidget):

    __ui_hello_lbl: QLabel
    __ui_sharedMemoryPath_lbl: QLabel

    def ui_setup(self):
        self.__ui_hello_lbl = QLabel("Hello World")
        self.__ui_sharedMemoryPath_lbl = QLabel(sharedMemoryDict.appData_dir)
        
        self._subwidgets = [
            self.__ui_hello_lbl,
            self.__ui_sharedMemoryPath_lbl
        ]


if __name__ == "__main__":
    ExampleWidget.demo(sharedMemoryDict)
