#!/bin/bash
if [[ "`which apt-get`" ]]
then
  sudo apt-get install python-dev python-setuptools
else
  sudo yum install python-devel python-setuptools
vi
easy_install pip 
pip install pyzmq pyreadline ipython tornado ipython_doctester
