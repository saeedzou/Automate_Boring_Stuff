from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# Check every 10 minutes
def ticket_checker(dates):  # dates is a list of days in the month to check
    found = False
    try:
        while not found:
            for date in dates:
                driver.get(
                    f"https://www.alibaba.ir/train/MHD-THR?adult=1&child=0&infant=0&departing=1401-06-{date}&ticketType"
                    f"=Family&isExclusive=false")
                time.sleep(5)
                available_tickets = driver.find_elements(by=By.CLASS_NAME, value='text-secondary-400')
                for available_ticket in available_tickets:
                    price = int(''.join(available_ticket.text.split(',')))
                    t = time.localtime()
                    print(
                        f"{t.tm_year}-{t.tm_mon}-{t.tm_mday} {t.tm_hour}:{t.tm_min}:{t.tm_sec} | "
                        f"Ticket on 1401-06-{date} price:{price / 10000}k Tomans")
                    if 3500000 > price > 2500000:
                        found = True
            if found:
                driver.quit()
            time.sleep(600)
    finally:
        driver.quit()


if __name__ == "__main__":
    driver = webdriver.Edge()
    driver.minimize_window()
    url = "https://www.alibaba.ir/train/MHD-THR?adult=1&child=0&infant=0&departing=1401-06-22&ticketType=Family" \
          "&isExclusive=false "
    ticket_checker(dates=[18, 19, 20, 21, 22, 23, 24, 25, 26])
