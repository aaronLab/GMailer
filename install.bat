@echo off

set my_path=%~dp0

:start
cls

set python_ver=36

python %my_path%/get-pip.py

cd \
cd \python%python_ver%\Scripts\
pip install -r %my_path%/requirements.txt

pause
exit
