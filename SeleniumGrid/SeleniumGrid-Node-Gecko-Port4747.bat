Echo off
Title Gecko Driver Node on port 4747

Echo Setting Project Location for Node
set projectLocation = D:\Selenium Grid
pushd %projectLocation%


Echo Setting FF path and Creating Node on port 4747
java -Dwebdriver.gecko.driver=D:\Drivers\geckodriver.exe -jar "D:\Selenium Grid\selenium-server-standalone-3.141.59.jar" -role node -hub http://localhost:4444/wd/hub -port 4747
pause