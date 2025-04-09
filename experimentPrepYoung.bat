@echo on
@echo Running the experiment preparation script for Young images...

set ORIGINPATH=%cd%

REM Study Task
cd /d  "%ORIGINPATH%\z(2)_backed_up - Copy\Composites\Young"
python test.py
move "%ORIGINPATH%\z(2)_backed_up - Copy\Composites\Young\studytask_young_img.csv" %ORIGINPATH%
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
cd /d  "%ORIGINPATH%\z(2)_backed_up - Copy\Faces Scenes - Kopya\Young"
python test.py
move "%ORIGINPATH%\z(2)_backed_up - Copy\Faces Scenes - Kopya\Young\testtask_face_used_young.xlsx" "%ORIGINPATH%"
cd /d "%ORIGINPATH%"
@echo Test Task Faces Seen Completed.

REM Faces Unseen
cd /d  "%ORIGINPATH%\z(2)_backed_up - Copy\Faces (not used)_copy\Young"
python test.py
move "%ORIGINPATH%\z(2)_backed_up - Copy\Faces (not used)_copy\Young\testtask_face_not_used_young.xlsx" "%ORIGINPATH%"
cd /d "%ORIGINPATH%"
@echo Test Task Faces Unseen Completed.

REM Combine the faces for test task
python UniteTestTask_young.py
del "%ORIGINPATH%\testtask_face_not_used_young.xlsx"
del "%ORIGINPATH%\testtask_face_used_young.xlsx"
@echo Test Task Combination Completed.

@echo Experiment preparation script for Young images completed.
pause
exit
