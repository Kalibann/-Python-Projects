'''
 ============================================================================
 Name         : Whatsapp Bot
 Author       : Ramon Soares Mendes Meneses Leite
 E-mail:      : ramnsores1000@gmail.com
 University   : Universidade Federal de Goiás - Catalão GO
 Objective    : Just for fun
 ============================================================================
'''

from selenium import webdriver
import time

class WppBot:
    def __init__(self):
        self.mensagem = 'Teste'
        self.dest = ["Cod X"]
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(executable_path=r'C:/Users/Ramon Soares/Documents/Python Scripts/chromedriver.exe')
        
    def enviar(self):
        # <span dir="auto" title="Cod X" class="_19RFN _1ovWX _F7Vk">
        # <div tabindex="-1" class="_13mgZ">
        # <span data-icon="send" class="">
        
        self.driver.get('https://web.whatsapp.com/')
        time.sleep(30)
        for contato in self.dest:
            contato = self.driver.find_element_by_xpath(f"//span[@title='{contato}']")
            time.sleep(3)
            contato.click()
            msg_box = self.driver.find_element_by_class_name('_13mgZ')
            time.sleep(3)
            msg_box.click()
            msg_box.send_keys(self.mensagem)
            clicar_enviar = self.driver.find_element_by_xpath("//span[@data-icon='send']")
            time.sleep(3)
            clicar_enviar.click()
            time.sleep(3)

bot = WppBot()
bot.enviar()
