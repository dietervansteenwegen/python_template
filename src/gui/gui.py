#! /usr/bin/python3
# -*- coding: utf-8 -*-
# vim: ts=4:sw=4:expandtab:cuc:autoindent:ignorecase:colorcolumn=99

__author__ = 'Dieter Vansteenwegen'
__project__ = 'REPLACE_WITH_PROJECT_NAME'
__project_link__ = 'https://www.vansteenwegen.org'

import sys
import traceback
from typing import List
# from .main_window import Ui_MainWindow
from PyQt5 import QtWidgets as qtw
from log.log import add_rotating_file, setup_logger  # DialogLog,
from .ui_sources.mainwindow import Ui_wdw_main_window

log = setup_logger()
add_rotating_file(log)


class MainWindow(qtw.QMainWindow, Ui_wdw_main_window):

    def __init__(self, *args, obj=None, **kwargs):
        super().__init__(*args, **kwargs)
        log.debug('Starting MainWindow')
        self.setupUi(self)


def excepthook(exc_type, exc_value, exc_tb) -> None:
    tabbed_msg: List[str] = [
        i.replace('\n', '\t').replace('  ', '')
        for i in traceback.format_exception(exc_type, exc_value, exc_tb)
    ]
    log.error('|'.join(tabbed_msg), exc_info=True, stack_info=True)
    QtWidgets.QApplication.quit()


def start_gui() -> None:
    log = setup_logger()
    add_rotating_file(log)
    log.debug('Root logger initialized.')
    sys.excepthook = excepthook
    app = QtWidgets.QApplication([])
    window: MainWindow = MainWindow()
    window.show()
    rtn = app.exec_()
    log.info(f'Exited: {rtn if rtn != 0 else "clean"}')
