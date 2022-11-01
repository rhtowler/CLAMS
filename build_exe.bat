rd /S /Q .\dist\CLAMS2
rd /S /Q .\build\CLAMSmain
pyinstaller CLAMSMain.spec
rem pyinstaller --windowed CLAMSMain.spec
rem md .\dist\CLAMS\icons
rem xcopy /E icons .\dist\CLAMS\icons
rem md .\dist\CLAMS\images
rem xcopy /E images .\dist\CLAMS\images
rem md .\dist\CLAMS\sounds
rem xcopy /E sounds .\dist\CLAMS\sounds
xcopy CLAMS.ini .\dist\CLAMS2\CLAMS.ini
