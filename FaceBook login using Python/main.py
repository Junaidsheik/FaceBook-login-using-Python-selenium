from time import sleep

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# done by Junaidsheik @ TEAM NOOBS ®


usr = input ('Enter your FACEBOOK Email Id:')
pwd = input ('Enter your FACEBOOK Password:')

# done by Junaidsheik @ TEAM NOOBS ®    

driver = webdriver.Chrome (ChromeDriverManager ( ).install ( ))
driver.get ('https://www.facebook.com/')
print ("Opened facebook")
sleep (1)

# done by Junaidsheik @ TEAM NOOBS ®

username_box = driver.find_element_by_id ('email')
username_box.send_keys (usr)
print ("FACEBOOK Email Id entered")
sleep (1)

# done by Junaidsheik @ TEAM NOOBS ®

password_box = driver.find_element_by_id ('pass')
password_box.send_keys (pwd)
print ("FACEBOOK Password entered")

# done by Junaidsheik @ TEAM NOOBS ®


login_box = driver.find_element_by_id ('loginbutton')
login_box.click ( )

print ("Done")
input ('Press anything to quit')
driver.quit ( )
print ("Finished")

# done by Junaidsheik @ TEAM NOOBS ®


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
