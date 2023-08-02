from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pygame

def play_sound(sound_file):
    pygame.mixer.init()
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        continue
    pygame.mixer.music.stop()


def check_date(date, price_ub, price_lb):
    if date < 10:
        date = f"0{date}"
    url = f"https://www.alibaba.ir/train/THR-MHD?adult=1&child=0&infant=0&departing=1402-05-{date}&ticketType=Family&isExclusive=false"
    driver.get(url)
    time.sleep(5)
    available_tickets = driver.find_elements(by=By.CLASS_NAME, value='text-secondary-400')
    for available_ticket in available_tickets:
        price = int(''.join(available_ticket.text.split(',')))
        t = time.localtime()
        print(
            f"{t.tm_year}-{t.tm_mon}-{t.tm_mday} {t.tm_hour}:{t.tm_min}:{t.tm_sec} | "
            f"Ticket on 1401-06-{date} price:{price / 10000}k Tomans")
        if price_ub * 10000 > price > price_lb * 10000:
            play_sound('alarm.mp3')
            time.sleep(3)

# Check every 1 minutes
def ticket_checker(dates, price_ub=400, price_lb=200):
    while True:
        for date in dates:
            check_date(date, price_ub, price_lb)

        time.sleep(60)


if __name__ == "__main__":
    OPTIONS = webdriver.EdgeOptions()
    OPTIONS.add_argument('--disable-gpu')
    OPTIONS.add_argument('--disable-dev-shm-usage')
    OPTIONS.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Edge(options=OPTIONS)
    driver.minimize_window()
    DATES = list(range(15, 21))
    ticket_checker(dates=DATES)
