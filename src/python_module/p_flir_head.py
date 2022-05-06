#! /usr/bin/python3
# -*- coding: utf-8 -*-

__author__ = 'Dieter Vansteenwegen'
__project__ = 'REPLACE_WITH_PROJECT_NAME'
__project_link__ = 'https://www.vansteenwegen.org'

import logging


def initialize_logger() -> logging.Logger:
    """Set up logger
    If the module is ran as a module, name logger accordingly as a sublogger.
    Returns:
        logging.Logger: logger instance
    """
    if __name__ == '__main__':
        return logging.getLogger('{}'.format(__name__))
    else:
        return logging.getLogger('__main__.{}'.format(__name__))


class ADCNotImplemented(NotImplementedError):
    """Info here."""
    pass
