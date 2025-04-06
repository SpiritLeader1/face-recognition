@echo on
@echo Running the experiment preparation script for Old images...

set ORIGINPATH=%cd%

REM Study Task
cd /d  "%ORIGINPATH%\z(2)_backed_up - Copy\Composites\Old"
python test.py
move "%ORIGINPATH%\z(2)_backed_up - Copy\Composites\Old\studytask_Old_img.csv" %ORIGINPATH%
cd /d %ORIGINPATH%
@echo Study Task Images Completed.

REM Interval Task
cd /d  "%ORIGINPATH%\z(2)_backed_up - Copy\Patterns - Kopya"
python csvCreator.py
move "%ORIGINPATH%\z(2)_backed_up - Copy\Patterns - Kopya\interval_test.csv" "%ORIGINPATH%"
cd /d "%ORIGINPATH%"
@echo Interval Task Images Completed.

REM Test Task
REM Faces Seen
cd /d  "%ORIGINPATH%\z(2)_backed_up - Copy\Faces Scenes - Kopya\Old"
python test.py
move "%ORIGINPATH%\z(2)_backed_up - Copy\Faces Scenes - Kopya\Old\testtask_face_used_Old.xlsx" "%ORIGINPATH%"
cd /d "%ORIGINPATH%"
@echo Test Task Faces Seen Completed.

REM Faces Unseen
cd /d  "%ORIGINPATH%\z(2)_backed_up - Copy\Faces (not used)_copy\Old"
python test.py
move "%ORIGINPATH%\z(2)_backed_up - Copy\Faces (not used)_copy\Old\testtask_face_not_used_Old.xlsx" "%ORIGINPATH%"
cd /d "%ORIGINPATH%"
@echo Test Task Faces Unseen Completed.

REM Combine the faces for test task
python UniteTestTask_old.py
del "%ORIGINPATH%\z(2)_backed_up - Copy\Faces (not used)_copy\Young\testtask_face_not_used_old.xlsx"
del "%ORIGINPATH%\z(2)_backed_up - Copy\Faces Scenes - Kopya\Young\testtask_face_used_old.xlsx"
@echo Test Task Combination Completed.

@echo Experiment preparation script for Old images completed.
pause
exit
