# -*- coding: utf-8 -*-
import shlex
import subprocess
import sys
from typing import Tuple
from typing import Union

# TODO: Get base dir at start, then use absolute file paths
# TODO: try out PySimpleGUI (https://cushychicken.github.io/python-guis-for-heretics/)

REPO_PREFIX = 'git_prive:dietervansteenwegen/'
PACKAGES = ['yapf', 'flake8', 'pre-commit', 'rope', 'flake8-bugbear', 'tryceratops']
PROJ_PLACEHOLDER = 'REPLACE_WITH_PROJECT_NAME'
DOC_FILES_TO_COPY = ['/source/conf.py', '/source/*.rst']


def get_user_input() -> Tuple[str, str, bool]:
    project_name = input('Enter project name:')
    repo_name = input('Enter repository name without prefix and without ending \'.git\':')
    venv = input('Use VENV [y/n]').upper() == 'Y'
    repo_address = f'{REPO_PREFIX}{repo_name}.git'
    print('\n')
    ok = input(
        f'Project name: {project_name}\nRepo address: {repo_address}\n'
        f'Use venv and install packages {PACKAGES}: {venv}\n OK? [y/n]',
    )
    if ok.upper() != 'Y':
        print('Exiting, start again.')
        sys.exit()
    return (project_name, repo_address, venv)


def execute_cmd(cmd: str) -> Union[None, str]:
    cmd_list = shlex.split(cmd)
    print(f'Running {cmd_list}')
    process = subprocess.run(cmd_list)
    if process.returncode != 0:
        print(f'CompletedProcess: {process.returncode=}, {process.stdout=}, {process.stderr=}\n')
    else:
        print()  # line feed
    return process.stderr.decode() if process.stderr else None


def clean_up() -> None:
    print('\n--> Cleaning up...')
    execute_cmd('rm -r .git')
    execute_cmd('rm -r .mypy_cache')
    execute_cmd('rm -r .github')
    execute_cmd('rm -r .venv')


def set_up_git(repo_addr: str) -> None:
    print('\n--> Setting up GIT')
    execute_cmd('git init')
    execute_cmd(f'git remote add origin {repo_addr}')


def set_up_venv() -> None:
    print('\n--> Setting up VENV')
    execute_cmd('python -m venv venv')
    execute_cmd('source ./venv/bin/activate')
    execute_cmd(f'pip install {" ".join(PACKAGES)}')
    execute_cmd('pre-commit run --all-files')
    execute_cmd('pre-commit install')


def replace_placeholder(project_name: str) -> None:
    print(f'\n--> Replacing placeholder with {project_name}')
    cmd_list = [
        'grep', '-rl', f'{PROJ_PLACEHOLDER}', '.', '--exclude=initialize.py', '--exclude-dir=.git',
    ]
    files = subprocess.check_output(cmd_list).decode().split()
    for file in files:
        cmd = f'sed -i \'s/{PROJ_PLACEHOLDER}/{project_name}/g\' {file}'
        print(cmd)
        execute_cmd(cmd)


def set_up_docs() -> None:
    print('\n--> Setting up docs')
    execute_cmd('cd docs')
    execute_cmd('spinx-quickstart')
    for f in DOC_FILES_TO_COPY:
        execute_cmd(f'cp ../_docs/{f} ./source')
    execute_cmd('cd source')
    execute_cmd('sphinx-apidoc.exe --force --output-dir . ../.. ../../setup.py')


def main() -> None:
    project_name, repo_address, use_venv = get_user_input()
    clean_up()
    set_up_git(repo_address)
    if use_venv:
        set_up_venv()
    replace_placeholder(project_name)
    set_up_docs()


if __name__ == '__main__':
    main()
