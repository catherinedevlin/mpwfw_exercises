 @echo off
  if /i %processor_architecture%==AMD64 GOTO AMD64
   if /i %PROCESSOR_ARCHITEW6432%==AMD64 GOTO AMD64
    if /i %processor_architecture%==x86 GOTO x86
	 GOTO ERR
	  :AMD64
		  python-2.7.3.amd64.msi
		  rem  GOTO EXEC
		  rem   :x86
		  rem   python-2.7.3.msi
		  rem        GOTO EXEC
		  rem         :EXEC
		  rem             rem do arch independent stuff
		  rem              GOTO END
		  rem               :ERR
		  rem                @echo Unsupported architecture!
		  rem                 pause
		  rem                  :END
