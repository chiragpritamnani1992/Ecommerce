Echo off
Title IE Driver Node on port 4646

Echo Setting Project Location for Node
set projectLocation = D:\Selenium Grid
pushd %projectLocation%


Echo Setting IE path and Creating Node on port 4646
java -Dwebdriver.ie.driver=D:\Drivers\IEDriverServer.exe -jar "D:\Selenium Grid\selenium-server-standalone-3.141.59.jar" -role node -hub http://localhost:4444/wd/hub -port 4646
pause