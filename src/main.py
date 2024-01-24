#! /usr/bin/python3
# -*- coding: utf-8 -*-
# vim: ts=4:sw=4:expandtab:cuc:autoindent:ignorecase:colorcolumn=99

__author__ = 'Dieter Vansteenwegen'
__project__ = 'REPLACE_WITH_PROJECT_NAME'
__project_link__ = 'https://www.vansteenwegen.org'

from config import Config
from gui.gui import start_gui
from log.log import add_rotating_file, setup_logger


def gui():
    start_gui()


def main():
    log = setup_logger()
    add_rotating_file(log)
    config = Config()


if __name__ == '__main__':
    main()
