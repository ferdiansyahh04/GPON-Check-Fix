from selenium import webdriver
import time
import schedule

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.webdriver import WebDriver
def alarm():
    driver: WebDriver = webdriver.Chrome("D:\pycharm\chromedriver.exe")
    driver.get("http://127.0.0.0:3474/webfig/#Terminal")
    time.sleep(4)
    username = "username"
    user = driver.find_element_by_id("name")
    for char in helpdesk :
        user.send_keys(char)
        time.sleep(0.30)
    time.sleep(2)
    username = "username"
    Pass = driver.find_element_by_id("password")
    for char in username :
        Pass.send_keys(char)
        time.sleep(0.30)
    time.sleep(2)
    time.sleep(2)
    driver.find_element_by_id("dologin").click()
    time.sleep(2)
    systelnet = "sys telnet 192.168.1.126"
    telnet = driver.find_element_by_xpath("//*[contains(.,'distribusi')]")
    for char in systelnet :
        telnet.send_keys(char)
        time.sleep(0.30)
    time.sleep(2)
    enter1 = ActionChains (driver)
    enter1.send_keys(u'\ue007').perform()
    time.sleep(2)
    time.sleep(2)
    username = "username"
    login2 = driver.find_element_by_xpath("//*[contains(.,'Username')]")
    for char in username :
        login2.send_keys(char)
        time.sleep(0.30)
    time.sleep(4)
    enter2 = ActionChains (driver)
    enter2.send_keys(u'\ue007').perform()
    time.sleep(2)
    sgdc = "sgdc"
    login2 = driver.find_element_by_xpath("//*[contains(.,'Password')]")
    for char in username:
        login2.send_keys(char)
        time.sleep(0.30)
    enter3 = ActionChains (driver)
    enter3.send_keys(u'\ue007').perform()
    time.sleep(2)
    db111 = "show gpon onu state gpon-olt_1/1/1"
    db11 = driver.find_element_by_xpath("//*[contains(.,'Yourgpon')]")
    for char in db111 :
        db11.send_keys(char)
        time.sleep(0.50)
    enter4 = ActionChains(driver)
    enter4.send_keys(u'\ue007').perform()
    time.sleep(3)
    db1 = driver.find_elements_by_xpath("//span[contains(.,'LOS') and contains(.,'1/1/1')]")
    print("-----------1/1/1")
    for span in db1:
        print(span.text)
    dbgp1 =len(db1)
    if dbgp1 > 0:
        print("ada loss")
    else:
        print("aman")
    enter41 = ActionChains(driver)
    enter41.send_keys('\ue00d').perform()
    time.sleep(10)
    driver.implicitly_wait(4)
    db112 = "show gpon onu state gpon-olt_1/1/2"
    db12 = driver.find_element_by_xpath("//*[contains(.,'Yourgpon')]")
    for char in db112:
        db12.send_keys(char)
        time.sleep(0.80)
    enter5 = ActionChains(driver)
    enter5.send_keys(u'\ue007').perform()
    time.sleep(3)
    db2 = driver.find_elements_by_xpath("//span[contains(.,'LOS') and contains(.,'1/1/2')]")
    print("-----------1/1/2")
    for span in db2:
        print(span.text)
    dbgp2 = len(db2)
    if dbgp2 > 2:
        print("ada loss")
    else:
        print("aman")
    time.sleep(3)
    db113 = "show gpon onu state gpon-olt_1/1/3"
    db13 = driver.find_element_by_xpath("//*[contains(.,'Yourgpon')]")
    for char in db113:
        db13.send_keys(char)
        time.sleep(0.50)
    enter6 = ActionChains(driver)
    enter6.send_keys(u'\ue007').perform()
    time.sleep(3)
    db3 = driver.find_elements_by_xpath("//span[contains(.,'LOS') and contains(.,'1/1/3')]")
    print("-------------1/1/3")
    for span in db3:
        print(span.text)
    dbgp3 = len(db3)
    if dbgp3 > 0:
        print("ada loss")
    else:
        print("aman")
    time.sleep(5)
    db114 = "show gpon onu state gpon-olt_1/1/4"
    db14 = driver.find_element_by_xpath("//*[contains(.,'Yourgpon')]")
    for char in db114:
        db14.send_keys(char)
        time.sleep(0.50)
    enter7 = ActionChains(driver)
    enter7.send_keys(u'\ue007').perform()
    time.sleep(3)
    db4 = driver.find_elements_by_xpath("//span[contains(.,'LOS') and contains(.,'1/1/4')]")
    print("---------1/1/4")
    for span in db4:
        print(span.text)
    dbgp4 = len(db4)
    if dbgp4 > 0:
        print("ada loss")
    else:
        print("aman")
    time.sleep(2)
    db115 = "show gpon onu state gpon-olt_1/1/5"
    db15 = driver.find_element_by_xpath("//*[contains(.,'Yourgpon')]")
    for char in db115:
        db15.send_keys(char)
        time.sleep(0.50)
    enter8 = ActionChains(driver)
    enter8.send_keys(u'\ue007').perform()
    time.sleep(3)
    db5 = driver.find_elements_by_xpath("//span[contains(.,'LOS') and contains(.,'1/1/5')]")
    print("--------1/1/5")
    for span in db5:
        print(span.text)
    dbgp5 = len(db5)
    if dbgp5 > 0:
        print("ada loss")
    else:
        print("aman")
    time.sleep(2)
    db116 = "show gpon onu state gpon-olt_1/1/6"
    db16 = driver.find_element_by_xpath("//*[contains(.,'Yourgpon')]")
    for char in db116:
        db16.send_keys(char)
        time.sleep(0.50)
    enter9 = ActionChains(driver)
    enter9.send_keys(u'\ue007').perform()
    time.sleep(3)
    db6 = driver.find_elements_by_xpath("//span[contains(.,'LOS') and contains(.,'1/1/6')]")
    print("-------------1/1/6")
    for span in db6:
        print(span.text)
    dbgp6 = len(db6)
    if dbgp6 > 0:
        print("ada loss")
    else:
        print("aman")
    time.sleep(2)
    db117 = "show gpon onu state gpon-olt_1/1/7"
    db17 = driver.find_element_by_xpath("//*[contains(.,'Yourgpon')]")
    for char in db117:
        db17.send_keys(char)
        time.sleep(0.50)
    enter10 = ActionChains(driver)
    enter10.send_keys(u'\ue007').perform()
    time.sleep(3)
    db7 = driver.find_elements_by_xpath("//span[contains(.,'LOS') and contains(.,'1/1/7')]")
    print("---------1/1/7")
    for span in db7:
        print(span.text)
    dbgp7 = len(db7)
    if dbgp7 > 0:
        print("ada loss")
    else:
        print("aman")
    time.sleep(2)
    db118 = "show gpon onu state gpon-olt_1/1/8"
    db18 = driver.find_element_by_xpath("//*[contains(.,'Yourgpon')]")
    for char in db118:
        db18.send_keys(char)
        time.sleep(0.50)
    enter11 = ActionChains(driver)
    enter11.send_keys(u'\ue007').perform()
    time.sleep(3)
    db8 = driver.find_elements_by_xpath("//span[contains(.,'LOS')  and contains(.,'1/1/8')]")
    print("-----------1/1/8")
    for span in db8:
        print(span.text)
    dbgp8 = len(db8)
    if dbgp8 > 0:
        print("ada loss")
    else:
        print("aman")
    time.sleep(3)
    db119 = "show gpon onu state gpon-olt_1/1/9"
    db19 = driver.find_element_by_xpath("//*[contains(.,'Yourgpon')]")
    for char in db119:
        db19.send_keys(char)
        time.sleep(0.50)
    enter12 = ActionChains(driver)
    enter12.send_keys(u'\ue007').perform()
    time.sleep(3)
    db9 = driver.find_elements_by_xpath("//span[contains(.,'LOS')  and contains(.,'1/1/9')]")
    print("---------1/1/9")
    for span in db9:
        print(span.text)
    dbgp9 = len(db9)
    if dbgp9 > 4:
        print("ada loss")
    else:
        print("aman")
    time.sleep(3)
    db1110 = "show gpon onu state gpon-olt_1/1/10"
    db110 = driver.find_element_by_xpath("//*[contains(.,'Yourgpon')]")
    for char in db1110:
        db110.send_keys(char)
        time.sleep(0.50)
    enter13 = ActionChains(driver)
    enter13.send_keys(u'\ue007').perform()
    time.sleep(3)
    db10 = driver.find_elements_by_xpath("//span[contains(.,'LOS')  and contains(.,'1/1/10')]")
    print("----------1/1/10")
    for span in db10:
        print(span.text)
    dbgp10 = len(db10)
    if dbgp10 > 0:
        print("ada loss")
    else:
        print("aman")
    time.sleep(3)
    db221 = "show gpon onu state gpon-olt_1/1/11"
    db21 = driver.find_element_by_xpath("//*[contains(.,'Yourgpon')]")
    for char in db221:
        db21.send_keys(char)
        time.sleep(0.50)
    enter14 = ActionChains(driver)
    enter14.send_keys(u'\ue007').perform()
    time.sleep(3)
    db30 = driver.find_elements_by_xpath("//span[contains(.,'LOS')  and contains(.,'1/1/11')]")
    print("-------1/1/11")
    for span in db30:
        print(span.text)
    dbgp11 = len(db30)
    if dbgp11 > 0:
        print("ada loss")
    else:
        print("aman")
    time.sleep(3)
    db222 = "show gpon onu state gpon-olt_1/1/12"
    db22 = driver.find_element_by_xpath("//*[contains(.,'Yourgpon')]")
    for char in db222:
        db22.send_keys(char)
        time.sleep(0.50)
    enter15 = ActionChains(driver)
    enter15.send_keys(u'\ue007').perform()
    time.sleep(3)
    db31 = driver.find_elements_by_xpath("//span[contains(.,'LOS')  and contains(.,'1/1/12')]")
    print("---------------1/1/12")
    for span in db31:
        print(span.text)
    dbgp12 = len(db31)
    if dbgp12 > 0:
        print("ada loss")
    else:
        print("aman")
    time.sleep(2)
    db223 = "show gpon onu state gpon-olt_1/1/13"
    db23 = driver.find_element_by_xpath("//*[contains(.,'Yourgpon')]")
    for char in db223:
        db23.send_keys(char)
        time.sleep(0.50)
    enter16 = ActionChains(driver)
    enter16.send_keys(u'\ue007').perform()
    time.sleep(3)
    db32 = driver.find_elements_by_xpath("//span[contains(.,'LOS')  and contains(.,'1/1/13')]")
    print("-----------1/1/13")
    for span in db32:
        print(span.text)
    dbgp13 = len(db32)
    if dbgp13 > 0:
        print("ada loss")
    else:
        print("aman")
    time.sleep(3)
    db223 = "show gpon onu state gpon-olt_1/1/14"
    db23 = driver.find_element_by_xpath("//*[contains(.,'Yourgpon')]")
    for char in db223:
        db23.send_keys(char)
        time.sleep(0.50)
    enter17 = ActionChains(driver)
    enter17.send_keys(u'\ue007').perform()
    time.sleep(3)
    db33 = driver.find_elements_by_xpath("//span[contains(.,'LOS')  and contains(.,'1/1/14')]")
    print("---------1/1/14")
    for span in db33:
        print(span.text)
        dbgp14 = len(db33)
    if dbgp14 > 2:
        print("ada loss")
    else:
        print("aman")
    time.sleep(3)
    db224 = "show gpon onu state gpon-olt_1/1/15"
    db24 = driver.find_element_by_xpath("//*[contains(.,'Yourgpon')]")
    for char in db224:
        db24.send_keys(char)
        time.sleep(0.50)
    enter18 = ActionChains(driver)
    enter18.send_keys(u'\ue007').perform()
    time.sleep(3)
    db34 = driver.find_elements_by_xpath("//span[contains(.,'LOS')  and contains(.,'1/1/15')]")
    print("------------1/1/15")
    for span in db34:
        print(span.text)
    dbgp15 = len(db34)
    if dbgp15 > 0:
        print("ada loss")
    else:
        print("aman")
    time.sleep(3)
    db225 = "show gpon onu state gpon-olt_1/1/16"
    db25 = driver.find_element_by_xpath("//*[contains(.,'Yourgpon')]")
    for char in db225:
        db25.send_keys(char)
        time.sleep(0.50)
    enter19 = ActionChains(driver)
    enter19.send_keys(u'\ue007').perform()
    time.sleep(3)
    db35 = driver.find_elements_by_xpath("//span[contains(.,'LOS')  and contains(.,'1/1/16')]")
    print("----------1/1/16")
    for span in db35:
        print(span.text)
    dbgp16 = len(db35)
    if dbgp16 > 0:
        print("ada loss")
    else:
        print("aman")
    driver.close()

schedule.every(1).minutes.do(alarm)

while 1:
    schedule.run_pending()
    time.sleep(2)
