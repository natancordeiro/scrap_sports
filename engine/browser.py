import random, os, inspect
import undetected_chromedriver as webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from functools import partial
import time

CURRENTDIR = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))

class Browser:
	def __init__(self, socks5=None, terminal=False, chromedriver=None, remote=None, path_dir_cache=None, inconginto=False):
		chrome_options = webdriver.ChromeOptions()
		chrome_options.add_argument('--disable-notifications')
		chrome_options.add_argument('--disable-blink-features=AutomationControlled')
		chrome_options.add_argument("window-size=1280,800")

		agentes = [ "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36" ,
		"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36",
		"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36 OPR/68.0.3618.63",
		"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:63.0) Gecko/20100101 Firefox/63.0",
		"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36",
		"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"
		]
		
		agente = agentes[random.randint(0, len(agentes) - 1)]
		chrome_options.add_argument("user-agent=" + agente)

		if socks5 != None:
			chrome_options.add_argument("--proxy-server=socks5://127.0.0.1:" + str(socks5))
		
		if terminal:
			chrome_options.add_argument("--headless")
			chrome_options.add_argument("--no-sandbox")
			chrome_options.add_argument("--mute-audio")

		if chromedriver == None:
			chromedriver = CURRENTDIR

		if inconginto:
			chrome_options.add_argument("--incognito")

		if path_dir_cache != None:
			if os.path.exists(path_dir_cache) == False:
				os.makedirs(path_dir_cache)
			chrome_options.add_argument("--profile-directory=Default")
			chrome_options.add_argument("--user-data-dir=" + path_dir_cache)
			
		if remote == 'chrome':
			capabilities = {
			    "browserName": "chrome",
			    "browserVersion": "110.0",
			    "selenoid:options": {
				"enableVideo": False,
				"enableVNC": True
			    }
			}
			self.driver = webdriver.Remote(
			    command_executor="http://localhost:4444/wd/hub",
			    desired_capabilities=capabilities
			    )
			print("Para visualizar o browser, acesse: http://localhost:8080/")

		elif remote == 'firefox':
			capabilities = {
			    "browserName": "firefox",
			    "browserVersion": "110.0",
			    "selenoid:options": {
				"enableVideo": False,
				"enableVNC": True
			    }
			}
			self.driver = webdriver.Remote(
			    command_executor="http://localhost:4444/wd/hub",
			    desired_capabilities=capabilities
			    )
			print("Para visualizar o browser, acesse: http://localhost:8080/")

		elif remote == 'opera':
			capabilities = {
			    "browserName": "opera",
			    "browserVersion": "96.0",
			    "selenoid:options": {
				"enableVideo": False,
				"enableVNC": True
			    }
			}
			self.driver = webdriver.Remote(
			    command_executor="http://localhost:4444/wd/hub",
			    desired_capabilities=capabilities
			    )
			print("Para visualizar o browser, acesse: http://localhost:8080/")

		else:
			self.driver = webdriver.Chrome(options=chrome_options)
        
		self.action = ActionChains(self.driver)
		self.wdw = WebDriverWait(self.driver, 10)

		self.driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
		self.driver.maximize_window()
		
	def esperar_elemento(self, by, element, webdriver):
		return bool(webdriver.find_elements(by, element))
	
	def navegate(self, url):
		self.driver.get(url)
		title = self.driver.title
		print("Navegando em: ", title)

	def find_by_text(self, text=str):
		self.driver.find_element(By.XPATH, f"//*[contains(text(), '{text}')]")

	def find_all_by_text(self, text=str):
		self.driver.find_elements(By.XPATH, f"//*[contains(text(), '{text}')]")

	def wait(self, by, value=str):
		de = by
		self.wdw.until(partial(self.esperar_elemento, By.de, value))

	def random_wait(self, tempo_inicial=int, tempo_final=int):
		time.sleep(random.randint(tempo_inicial, tempo_final))

	def close(self):
		self.driver.quit()

	def __del__(self):
		print("Encerrando browser.")
		self.driver.quit()

