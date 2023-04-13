from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import playsound


# Check every 10 minutes
def ticket_checker(dates):  # dates is a list of days in the month to check
    found = False
    # notify.register()  # Uncomment this line if you want to register to a new channel
    try:
        while not found:
            for date in dates:
                driver.get(
                    f"https://www.alibaba.ir/train/THR-MHD?adult=1&child=0&infant=0&departing=1401-12-{date}&ticketType"
                    f"=Family&isExclusive=false")
                time.sleep(5)
                available_tickets = driver.find_elements(by=By.CLASS_NAME, value='text-secondary-400')
                for available_ticket in available_tickets:
                    price = int(''.join(available_ticket.text.split(',')))
                    t = time.localtime()
                    print(
                        f"{t.tm_year}-{t.tm_mon}-{t.tm_mday} {t.tm_hour}:{t.tm_min}:{t.tm_sec} | "
                        f"Ticket on 1401-06-{date} price:{price / 10000}k Tomans")
                    if 3500000 > price > 2300000:
                        time.sleep(17)
                        # Comment here
                        # play alarm.mp3
                        playsound.playsound('alarm.mp3')
                        found = True

            if found:
                driver.quit()
            time.sleep(60)
    finally:
        driver.quit()


if __name__ == "__main__":
    # url = "https://www.alibaba.ir/train/MHD-THR?adult=1&child=0&infant=0&departing=1401-12-22&ticketType=Family" \
    #       "&isExclusive=false "
    OPTIONS = webdriver.EdgeOptions()
    OPTIONS.add_argument('--disable-gpu')
    OPTIONS.add_argument('--disable-dev-shm-usage')
    OPTIONS.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Edge(options=OPTIONS)
    driver.minimize_window()
    DATES = list(range(15, 21))
    ticket_checker(dates=DATES)
