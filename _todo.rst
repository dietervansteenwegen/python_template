#########
GIT
#########
rm -r .git
git init
git config user.name "dietervansteenwegen"
git config user.email github@vansteenwegen.org
git remote add origin git_prive:Panthyr/xxxx
git push -u origin main

#########
SPHINX
#########

`cd docs`
`sphinx-quickstart`

* copy conf.py parts
* add modules and usage to index.rst

########
VENV
########

`python3 -m virtualenv --python python3 venv`

`.\\venv\\Scripts\\activate`
`pip install yapf flake8 pre-commit`
`pre-commit run --all files`


########
Others
########
* Write **README.md**

Check https://stackoverflow.com/questions/59821618/how-to-use-yapf-or-black-in-vscode/66377157 for yapf config
