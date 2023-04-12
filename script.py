import undetected_chromedriver as uc  # import undetected_chromedriver package
from selenium.webdriver.common.by import By  # import By class for locating elements
from selenium.webdriver.common.keys import Keys  # import Keys class for simulating key presses
import time  # import time module for pausing the program

# define function for restoring Snapchat streaks
def snapchat_streak_restore():
    username = ""  # set Snapchat username
    email = ""  # set email address associated with Snapchat account
    phone_number = ""  # set phone number associated with Snapchat account
    device = "SAMSUNG S23 ULTRA"  # set device used for accessing Snapchat
    friends = ["", "", ""]  # set list of friends to restore streaks with
    description = '''Dear Snapchat Support Team,

I am writing to request your assistance in restoring my Snapchat streaks. I have been an active user of the app for some time and have recently experienced technical difficulties which have caused me to lose my streaks with several of my friends.

Thank you for your assistance in this matter. I look forward to hearing from you soon.'''  # set message to send to Snapchat support team

    options = uc.ChromeOptions()  # create options object for configuring ChromeDriver
    options._binary_location = ""  # set path to Chrome / Brave / Any chomium driver
    browser = uc.Chrome(executable_path="/PATH-TO-CHROMEDRIVER/chromedriver.exe", options=options)  # create ChromeDriver object

    url = "https://help.snapchat.com/hc/en-gb/requests/new?ticket_form_id=149423&selectedAnswers=5695496404336640,5731111685324800"

    # loop through each friend to restore streaks with
    for friend in friends:
        browser.get(url)  # navigate to Snapchat support page

        # locate and fill in Snapchat username field
        username_input = browser.find_element(By.XPATH, "/html/body/main/div/div/div[2]/form/div[3]/input")
        username_input.send_keys(username)

        # locate and fill in email field
        email_input = browser.find_element(By.XPATH, "/html/body/main/div/div/div[2]/form/div[4]/input")
        email_input.send_keys(email)

        # locate and fill in phone number field
        phone_input = browser.find_element(By.XPATH, "/html/body/main/div/div/div[2]/form/div[5]/input")
        phone_input.send_keys(phone_number)

        # locate and fill in device field
        device_input = browser.find_element(By.XPATH, "/html/body/main/div/div/div[2]/form/div[6]/input")
        device_input.send_keys(device)

        # locate and fill in friend's name field
        friends_input = browser.find_element(By.XPATH, "/html/body/main/div/div/div[2]/form/div[7]/input")
        friends_input.send_keys(friend)

        # locate and fill in issue start date field
        issue_start_date = browser.find_element(By.XPATH, "/html/body/main/div/div/div[2]/form/div[8]/input")
        issue_start_date.send_keys("Yesterday")

        # locate and fill in issue description field
        description_input = browser.find_element(By.XPATH, "/html/body/main/div/div/div[2]/form/div[11]/textarea")
        description_input.send_keys(description)

        # locate and click submit button
        confirm_button = browser.find_element(By.XPATH, "/html/body/main/div/div/div[2]/form/footer/input")
        confirm_button.click()

        # pausing the script so the user bypass the capatcha
        time.sleep(20)

    browser.quit()

    while True:
        pass


if __name__ == '__main__':
    snapchat_streak_restore()
