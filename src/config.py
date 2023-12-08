#! /usr/bin/python3
# -*- coding: utf-8 -*-
# vim: ts=4:sw=4:expandtab:cuc:autoindent:ignorecase:colorcolumn=99

__author__ = 'Dieter Vansteenwegen'
__project__ = 'REPLACE_WITH_PROJECT_NAME'
__project_link__ = 'https://www.vansteenwegen.org'


import argparse
import logging
from configparser import ConfigParser
from pathlib import Path

log = logging.getLogger(__name__)
PROGRAM_DESCRIPTION: str = 'REPLACE_WITH_PROJECT_NAME'


class HelpfullArgumentParser(argparse.ArgumentParser):
    def error(self, msg):
        import sys

        print(f'\nERROR: {msg}\n\n')
        self.print_help()
        sys.exit(2)


def get_arguments() -> argparse.Namespace:
    parser = HelpfullArgumentParser(
        add_help=True,
        description=PROGRAM_DESCRIPTION,
    )

    ## ADD REQUIRED ARG BELOW THIS GROUP. OPTIONAL ABOVE...
    required_args = parser.add_argument_group('Required arguments')
    required_args.add_argument(
        '-c',
        '--config_file',
        help='Location of the config file functionality.',
        action='store',
        dest='config_file',
        required=True,
    )

    return parser.parse_args()


class Config:
    def __init__(self):
        self._get_config_file()
        self._parse_config()

    def _get_config_file(self) -> None:
        self.conf_path = Path(get_arguments().config_file)
        if not self.conf_path.is_file:
            err_msg = f'Config file {self.conf_path} is not a file.'
            raise FileNotFoundError(err_msg)
        log.debug(f'Using config file {self.conf_path}')

    def _parse_config(self) -> None:
        self.parser = ConfigParser()
        self.parser.read(self.conf_path)

    def _get_matrix_config(self) -> None:
        self._matrix_conf = self.parser['matrix']
        for req_item in [
            'login',
            'password',
            'room',
            'homeserver',
        ]:
            if req_item not in self._matrix_conf:
                err_msg = f'Required item [{req_item}] not in matrix config section'
                raise ValueError(err_msg)

    def matrix_config(self) -> dict:
        return self.parser['matrix']
