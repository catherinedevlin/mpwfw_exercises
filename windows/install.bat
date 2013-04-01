install_python.bat
setx /M PATH %PATH%;C:\Python27;C:\Python27\Scripts;C:\Python27\Tools\Scripts
cd distribute-0.6.35
c:\Python27\python setup.py install
cd ..
c:\Python27\Scripts\easy_install pip
c:\Python27\Scripts\easy_install pyzmq
c:\Python27\Scripts\pip install pyreadline ipython tornado ipython_doctester
npp.6.3.Installer.exe

