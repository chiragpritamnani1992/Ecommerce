Echo off
Title Chrome Driver Node on port 4545

Echo Setting Project Location for Node
set projectLocation = D:\Selenium Grid
pushd %projectLocation%


Echo Setting ChromeDriver path and Creating Node on port 4545
java -Dwebdriver.chrome.driver=D:\Drivers\chromedriver.exe -jar "D:\Selenium Grid\selenium-server-standalone-3.141.59.jar" -role node -hub http://localhost:4444/wd/hub -port 4545
pause