from selenium import webdriver
from selenium.webdriver.common.by import By


def dl_pack(health_result,bot,chat_id):
    driver = webdriver.Chrome('chromedriver.exe')
    driver.implicitly_wait(10)
    driver.get('https://www.dietshin.com/calorie/sports-view.asp?cal_idx=59&cal_type=E')
    dlft = driver.find_element(By.XPATH,'//*[@id="container"]/div[1]/ul/li').text
    dl_info = f'더 강도높은 운동을 원하신다면 헬스장에 가보세요. {health_result}를 추천합니다.\n{dlft}'
    driver.quit()
    bot.send_message(chat_id, dl_info)
    return dl_info