Echo off
Title Server HUB on port 4444

Echo Setting Project Location
set projectLocation = D:\Selenium Grid
pushd %projectLocation%


Echo Loading HUB on default port 4444
java -jar "D:\Selenium Grid\selenium-server-standalone-3.141.59.jar" -role hub
pause