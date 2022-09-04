from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from notify_run import Notify
import notifypy


# Check every 10 minutes
def ticket_checker(dates, endpoint):  # dates is a list of days in the month to check
    found = False
    notify = Notify(endpoint=endpoint)
    # notify.register()  # Uncomment this line if you want to register to a new channel
    try:
        while not found:
            t = time.localtime()
            notify.send(f"Started ticket search at "
                        f"{t.tm_year}-{t.tm_mon}-{t.tm_mday} {t.tm_hour}:{t.tm_min}:{t.tm_sec}")
            notification = notifypy.Notify()
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
                        notify.send(f"Found a ticket for 1401-06-{date} with a price of {price / 10000}k Tomans")
                        # These are desktop notifications (notify-run cannot execute without VPN in IR."
                        notification.title = "Found ticket"
                        notification.message = f"1401-06-{date} with a price of {price / 10000}k Tomans"
                        notification.audio = "./test.wav"  # Path to your alarm sound
                        notification.send()
                        time.sleep(17)
                        # Comment here
                        found = True
            if found:
                driver.quit()
            time.sleep(600)
    finally:
        driver.quit()


if __name__ == "__main__":
    # url = "https://www.alibaba.ir/train/MHD-THR?adult=1&child=0&infant=0&departing=1401-06-22&ticketType=Family" \
    #       "&isExclusive=false "
    ENDPOINT = "https://notify.run/<YOUR_CREDENTIALS>"  # Change to your endpoint or register to a new channel or
    # uncomment if you don't want to use VPN
    OPTIONS = webdriver.EdgeOptions()
    OPTIONS.add_argument('--disable-gpu')
    OPTIONS.add_argument('--disable-dev-shm-usage')
    OPTIONS.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Edge(options=OPTIONS)
    driver.minimize_window()
    DATES = list(range(20, 27))
    ticket_checker(dates=DATES, endpoint=ENDPOINT)
