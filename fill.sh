#!/bin/bash
cd mac
curl http://downloads.sourceforge.net/project/smultron/smultron/3.5.1/Smultron-3.5.1.zip?r=&amp;ts=1364787627&amp;use_mirror=iweb
unzip Smultron-3.5.1.zip
cd ..
cd windows
wget http://python.org/ftp/python/2.7.3/python-2.7.3.msi
wget http://python.org/ftp/python/2.7.3/python-2.7.3.amd64.msi
wget http://download.tuxfamily.org/notepadplus/6.3.1/npp.6.3.1.Installer.exe
wget https://pypi.python.org/packages/source/d/distribute/distribute-0.6.35.tar.gz
tar xvfz distribute-0.6.35.tar.gz
cd ..
cd linux
cp -r ../windows/distribute-0.6.35 .
cd ..
