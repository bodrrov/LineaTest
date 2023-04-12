import random
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from data import secret_key,new_password,Network_Name,RPC_URL,Chain_ID,Currency_Symbol,Block_Explorer_URL,Testnet_Address,slippage_limit,eth,eth_swap
from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
import pyperclip
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import NoSuchElementException


# service = Service(executable_path= 'C:\\Users\Bodrov\\Desktop\\chromedriver_win32\\chromedriver.exe')
# options = webdriver.ChromeOptions()
# #options.add_argument('–incognito')
# options.add_extension("C:\\Users\\Bodrov\\Desktop\\bot_inst\\extension_10_28_1_0.crx")
# driver = webdriver.Chrome(service=service,chrome_options=options)


class walletBot():

    def __init__(self,secret_key, new_password,Network_Name,RPC_URL,Chain_ID,Currency_Symbol,Block_Explorer_URL,Testnet_Address,slippage_limit,eth,eth_swap):

        self.secret_key = secret_key
        self.new_password = new_password
        self.Network_name= Network_Name
        self.RPC_URL = RPC_URL
        self.Chain_ID = Chain_ID
        self.Currency_Symbol= Currency_Symbol
        self.Block_Explorer_URL = Block_Explorer_URL
        self.Testnet_Address = Testnet_Address
        self.slippage_limit = slippage_limit
        self.eth = eth
        self.eth_swap = eth_swap

        options = webdriver.ChromeOptions()
        #опция скрытия окна
        #options.add_argument("--headless")
        service = Service(executable_path='C:\\Users\Bodrov\\Desktop\\chromedriver_win32\\chromedriver.exe')
        options.add_extension("C:\\Users\\Bodrov\\Desktop\\bot_inst\\extension_10_28_1_0.crx")
        self.driver = webdriver.Chrome(service=service,chrome_options=options)

    def close_browser(self):
        self.driver.close()
        self.driver.quit()
        # проверяем по xpath существует ли элемент на странице

    def xpath_exists(self, url):

        driver = self.driver
        try:
            driver.find_element(By.XPATH, url)
            exists = True
        except  NoSuchElementException:
            exists = False
        return exists

    def login(self):
        try:
            driver = self.driver
            time.sleep(random.randrange(2, 4))
            driver.get("chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html#onboarding/welcome")
            time.sleep(random.randrange(2, 4))
            action = ActionChains(driver)
            #переключение между вкладками
            action.key_down(Keys.CONTROL).send_keys('TAB').key_up(Keys.CONTROL).perform()
            time.sleep(random.randrange(2, 4))
            driver.find_element(by= By.XPATH, value = "/html/body/div[1]/div/div[2]/div/div/div/ul/li[2]/button").click()
            time.sleep(random.randrange(2, 4))

            driver.find_element(by= By.XPATH, value = "/html/body/div[1]/div/div[2]/div/div/div/div/button[1]").click()
            secret_key_input = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[2]/div/div/div/div[4]/div/div/div[3]/div[1]/div[1]/div/input")
            secret_key_input.clear()

            time.sleep(random.randrange(2, 4))

            #копирования в буфер обмена
            pyperclip.copy(secret_key)
            driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[2]/div/div/div/div[4]/div/div/div[3]/div[1]/div[1]/div/input").send_keys(Keys.CONTROL, 'v')
            driver.find_element(by= By.XPATH, value = "/html/body/div[1]/div/div[2]/div/div/div/div[4]/div/button").click()

            #ввод пароля
            new_password_input = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[2]/div/div/div/div[2]/form/div[1]/label/input")
            new_password_input.clear()
            new_password_input.send_keys(new_password)

            time.sleep(random.randrange(2, 4))
            #подверждение пароля
            confirm_password_input = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[2]/div/div/div/div[2]/form/div[2]/label/input")
            confirm_password_input.clear()
            confirm_password_input.send_keys(new_password)

            #check_box
            driver.find_element(by= By.XPATH, value = "/html/body/div[1]/div/div[2]/div/div/div/div[2]/form/div[3]/label/input").click()
            time.sleep(random.randrange(4, 6))

            import_button = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[2]/div/div/div/div[2]/form/button")
            import_button.click()

            time.sleep(random.randrange(4, 6))

            done_button = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[2]/div/div/div/div[2]/button")
            done_button.click()

            time.sleep(random.randrange(4, 6))

            next_button = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[2]/div/div/div/div[2]/button")
            next_button.click()

            time.sleep(random.randrange(2, 4))

            skip_button = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[2]/div/div/div/div[2]/button")
            skip_button.click()

            time.sleep(random.randrange(2, 4))

            # def xpath_exists(self, url):
            #     browser = self.browser
            #     try:
            #         browser.find_element(By.XPATH, url)
            #         exists = True
            #     except  NoSuchElementException:
            #         exists = False
            #     return exists

            # if xpath_exists(password_page):
            #     input_password_again = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[2]/div/div/div/div[2]/button")
            #     input_password_again.clear()
            #     input_password_again.send_keys(new_password)
            #     time.sleep(random.randrange(4, 6))
            # else:
            #     print("Пароль повторно вводить не требуется")



        except Exception as ex:
            print(ex)

    def add_network(self):
        try:
            driver = self.driver
            # Add Network
            alert_button = driver.find_element(by=By.XPATH,
                                               value="/html/body/div[2]/div/div/section/div[3]/div/div[1]/button")
            alert_button.click()
            driver.get("chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html#settings/networks/add-network")
            time.sleep(4)
            network_input = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[3]/div/div[2]/div[2]/div/div[2]/div/div[2]/div[1]/label/input")
            network_input.clear()
            network_input.send_keys(Network_Name)

            time.sleep(random.randrange(2, 4))

            RPC_URL_input = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[3]/div/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/label/input")
            RPC_URL_input.clear()
            RPC_URL_input.send_keys(RPC_URL)

            time.sleep(random.randrange(2, 4))

            Block_Explorer_URL_input = driver.find_element(by=By.XPATH,
                                                           value="/html/body/div[1]/div/div[3]/div/div[2]/div[2]/div/div[2]/div/div[2]/div[5]/label/input")
            Block_Explorer_URL_input.clear()
            Block_Explorer_URL_input.send_keys(Block_Explorer_URL)

            time.sleep(random.randrange(4, 8))
            Chain_ID_input = driver.find_element(by=By.XPATH,
                                                 value="/html/body/div[1]/div/div[3]/div/div[2]/div[2]/div/div[2]/div/div[2]/div[3]/label/input")
            Chain_ID_input.clear()
            Chain_ID_input.send_keys(Chain_ID)

            time.sleep(random.randrange(6, 8))

            Currency_Symbol_input = driver.find_element(by=By.XPATH,
                                                        value="/html/body/div[1]/div/div[3]/div/div[2]/div[2]/div/div[2]/div/div[2]/div[4]/label/input")
            Currency_Symbol_input.clear()
            Currency_Symbol_input.send_keys(Currency_Symbol)

            time.sleep(random.randrange(6, 8))

            save_button = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[3]/div/div[2]/div[2]/div/div[2]/div/div[3]/button[2]")
            save_button.click()
            time.sleep(random.randrange(6, 8))
            #connect_network_button
            driver.find_element(by=By.XPATH, value="/html/body/div[2]/div/div/section/div/div/button[1]").click()
            time.sleep(random.randrange(6, 8))

        except Exception as ex:
            print(ex)

# driver.get("https://faucetlink.to/goerli")
# time.sleep(random.randrange(2, 4))
#
# action.key_down(Keys.CONTROL).send_keys('TAB').key_up(Keys.CONTROL).perform()
# time.sleep(random.randrange(2, 4))
#
# driver.find_element(by=By.XPATH, value="/html/body/div/div[7]/table/tbody/tr[2]/td/div/a").click()
# time.sleep(random.randrange(70))
#
# driver.find_element(by=By.XPATH, value="/html/body/section/div[2]/div[2]/ul[1]").click()
# time.sleep(random.randrange(2, 4))
#
# testnet_address_input = driver.find_element(by=By.XPATH, value="/html/body/div[2]/div[3]/div[1]/div[2]/form/div[2]/input")
# testnet_address_input.clear()
# testnet_address_input.send_keys(Testnet_Address)
# time.sleep(random.randrange(2, 4))
#
# driver.find_element(by=By.XPATH, value="/html/body/div[2]/div[3]/div[1]/div/div/span/div[1]").click()
# time.sleep(random.randrange(2, 4))
#
# driver.find_element(by=By.XPATH, value="/html/body/section/div[3]/div[2]/button").click()
# time.sleep(random.randrange(2, 4))

    def hop_exchange(self):

        try:
            driver = self.driver
            driver.get("https://goerli.hop.exchange/#/send?token=ETH&destNetwork=linea&sourceNetwork=ethereum")
            time.sleep(4)
            connect_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[1]/div[3]/div[3]/div/button")))
            connect_button.click()

            time.sleep(random.randrange(2, 4))

            metamask_button= WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/aside/section/ul/li[1]/button")))
            metamask_button.click()

            time.sleep(random.randrange(6, 8))

            # open_metamask_button = WebDriverWait(driver, 10).until(
            #     EC.element_to_be_clickable((By.XPATH, "/html/body/aside/section/section/footer/a/button")))
            # open_metamask_button.click()
            #
            # time.sleep(random.randrange(2, 6))

            # install_metamask_button = WebDriverWait(driver, 10).until(
            #     EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[1]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div[2]/div/a")))
            # install_metamask_button.click()
            #переключение на всплывающее окно
            driver.switch_to.window(driver.window_handles[1])
            #driver.get("chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/popup.html")
            time.sleep(random.randrange(2, 4))
            driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[2]/div/div[3]/div[2]/button[2]").click()
            time.sleep(random.randrange(2, 4))
            driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[2]/div/div[2]/div[2]/div[2]/footer/button[2]").click()
            time.sleep(random.randrange(6, 8))
            driver.switch_to.window(driver.window_handles[0])
            time.sleep(random.randrange(6, 8))
            driver.find_element(by=By.XPATH, value="/html/body/div/div/div[3]/div/div/div[2]/div[2]/div[1]/div/div").click()
            time.sleep(random.randrange(6, 8))
            driver.find_element(by=By.XPATH, value= "/html/body/div[2]/div[3]/ul/li[2]").click()
            time.sleep(random.randrange(2, 4))
            driver.find_element(by=By.XPATH, value="/html/body/div/div/div[3]/div/div/div[4]/div[2]/div[1]/div/div").click()
            time.sleep(random.randrange(2, 4))
            driver.find_element(by=By.XPATH, value="/html/body/div[2]/div[3]/ul/li[6]").click()
            time.sleep(random.randrange(2, 4))
            eth_input =driver.find_element(by=By.XPATH,
                                value="/html/body/div/div/div[3]/div/div/div[2]/div[2]/div[2]/div/div/input")
            eth_input.clear()
            eth_input.send_keys(eth)
            time.sleep(random.randrange(6, 8))
            driver.find_element(by=By.XPATH, value="/html/body/div/div/div[3]/div/div/div[8]/div/div/button").click()
            time.sleep(random.randrange(6, 8))
            driver.switch_to.window(driver.window_handles[2])
            #time.sleep(20)
            time.sleep(random.randrange(6, 8))
            driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[2]/div/div[2]/div/button[2]").click()
            driver.switch_to.window(driver.window_handles[0])
            time.sleep(random.randrange(2, 4))
            driver.find_element(by=By.XPATH,
                                value="/html/body/div/div/div[4]/div/div/div[2]/div/div[3]/div/button").click()
            time.sleep(random.randrange(2, 4))
            driver.switch_to.window(driver.window_handles[2])
            time.sleep(20)
            time.sleep(random.randrange(6, 8))
            driver.find_element(by=By.XPATH,
                                value="/html/body/div[1]/div/div[2]/div/div[3]/div[3]/footer/button[2]").click()
            driver.switch_to.window(driver.window_handles[0])

        except Exception as ex:
            print(ex)

    def swap(self):

        try:
            driver = self.driver
            driver.get("https://swap.goerli.linea.build/#/swapl")
            time.sleep(random.randrange(2, 4))
            driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[1]/nav/div/div[2]/div/span/div/button[1]").click()
            time.sleep(random.randrange(2, 4))
            driver.find_element(by=By.XPATH, value="/html/body/reach-portal[2]/div[3]/div/div/div/div/div/div[3]/div/div[1]/button").click()
            time.sleep(random.randrange(2, 4))
            driver.switch_to.window(driver.window_handles[1])
            time.sleep(random.randrange(2, 4))
            driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[2]/div/div[3]/div[2]/button[2]").click()
            time.sleep(random.randrange(2, 4))
            driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[2]/div/div[2]/div[2]/div[2]/footer/button[2]").click()
            driver.switch_to.window(driver.window_handles[0])
            time.sleep(random.randrange(2, 4))
            driver.find_element(by=By.XPATH,value="/html/body/div[1]/div/div[2]/div[4]/main/div[1]/div/div[2]/div/button").click()
            time.sleep(random.randrange(2, 4))
            slippage_limit_input = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[2]/div[4]/main/div[1]/div/div[2]/div/span/div/div[2]/div/div[2]/button[2]/div/input")
            slippage_limit_input.clear()
            slippage_limit_input.send_keys(slippage_limit)
            time.sleep(random.randrange(2, 4))
            driver.find_element(by=By.XPATH,
                                value="/html/body/div[1]/div/div[2]/div[4]/main/div[1]/div/div[2]/div/button").click()
            time.sleep(random.randrange(2, 4))
            driver.find_element(by=By.XPATH,value="/html/body/div[1]/div/div[2]/div[4]/main/div[2]/div[1]/div/div/div[1]/input").click()
            time.sleep(random.randrange(2, 4))
            eth_input = driver.find_element(by=By.XPATH,value="/html/body/div[1]/div/div[2]/div[4]/main/div[2]/div[1]/div/div/div[1]/input")
            eth_input.clear()
            eth_input.send_keys(eth_swap)
            time.sleep(random.randrange(6, 8))
            driver.find_element(by=By.XPATH,
                                value="/html/body/div[1]/div/div[2]/div[4]/main/div[3]/div[1]/div/div/div/div[1]/button").click()
            time.sleep(random.randrange(6, 8))
            driver.find_element(by=By.XPATH,
                                value="/html/body/reach-portal[2]/div[3]/div/div/div/div/div[1]/div[3]/div/div[2]").click()
            time.sleep(random.randrange(4,6))
            driver.find_element(by=By.XPATH,
                                value="/html/body/div[1]/div/div[2]/div[4]/main/div[3]/div[2]/button").click()
            time.sleep(random.randrange(8,10))

            #если цена обновлена
            if not self.xpath_exists("/html/body/reach-portal[2]/div[3]/div/div/div/div/div[1]/div[2]/div[6]/div/div/div"):
                driver.find_element(by=By.XPATH,value='/html/body/reach-portal[2]/div[3]/div/div/div/div/div[2]/div/button').click()
            else:
                driver.find_element(by=By.XPATH,
                                    value="/html/body/reach-portal[2]/div[3]/div/div/div/div/div[1]/div[2]/div[6]/div/button").click()
                driver.find_element(by=By.XPATH,value="/html/body/reach-portal[2]/div[3]/div/div/div/div/div[2]/div/button").click()
                time.sleep(random.randrange(2, 4))
                driver.switch_to.window(driver.window_handles[1])
                time.sleep(random.randrange(6, 8))
                driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[2]/div/div[3]/div[3]/footer/button[2]").click()
                time.sleep(random.randrange(2, 4))
                driver.switch_to.window(driver.window_handles[0])
                driver.find_element(by=By.XPATH,
                                    value="/html/body/reach-portal[2]/div[3]/div/div/div/div/div/div[3]/button").click()
                time.sleep(30)

            # try:
            #     wait.until(EC.alert_is_present())
            #     driver.switch_to.alert.accept()
            #     print("Alert accepted")
            # except:
            #     print("no Alert found")

        except Exception as ex:
            print(ex)


my_bot = walletBot(secret_key, new_password,secret_key, new_password,Network_Name,RPC_URL,Chain_ID,Currency_Symbol,slippage_limit,eth,eth_swap)
my_bot.login()
my_bot.add_network()
my_bot.hop_exchange()
my_bot.swap()




