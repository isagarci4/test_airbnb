from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import pytest
import time

navegador = None

# configurações iniciais
@pytest.fixture(scope='session', autouse=True)
def setup():
    global navegador
    # configurando webdriver
    navegador = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    # abre o site
    navegador.get("https://www.airbnb.com.br/")
    # maximiza a janela do navegador
    navegador.maximize_window()
    # espera 5 segundos para começar a executar
    navegador.implicitly_wait(5)
    # aguarda todo o código ser executado
    yield
    # fecha o navegador, assim que tudo é executado
    navegador.quit()

def test_texto_botao_anunciar():
    # seleciona o texto do botão "Anuncie seu espaço no Airbnb"
    botao_anunciar = navegador.find_element('xpath', '/html/body/div[5]/div/div/div[1]/div/div[2]/div/div/div/div[1]/div[1]/div/div/div/header/div/div[3]/nav/div[1]/a/div').text  
    # verifica se o texto está correto
    assert "Anuncie seu espaço no Airbnb" == botao_anunciar

def test_mostrar_preco_total():
    # seleciona botão "Mostrar preço total"
    btn_mostrar_preco = navegador.find_element('xpath', '//*[@id="site-content"]/div[2]/div[1]/div/div/div/div[1]/div[1]/div/div/div/div/div/div[2]/button/div')
    # clica no botão
    btn_mostrar_preco.click()
    
    # seleciona o texto do botão
    text_mostar_preco_total = navegador.find_element('xpath', '//*[@id="text-container"]/div[1]/div/span').text
    time.sleep(3)
    
    # verifica se o texto está correto 
    assert 'Mostrar preço total' == text_mostar_preco_total
    
def test_exibir_mapa():
    btn_exibir_mapa = navegador.find_element('xpath', '/html/body/div[5]/div/div/div[1]/div/div[2]/div/div/div/div[1]/div[3]/div[1]/button')
    btn_exibir_mapa.click()
    time.sleep(5)
    
    btn_mostrar_lista = navegador.find_element('xpath', '/html/body/div[5]/div/div/div[1]/div/div[2]/div/div/div/div[1]/div[3]/div[1]/button')
    btn_mostrar_lista.click()
    time.sleep(5)
    
    text_exibir_mapa = navegador.find_element('xpath', '/html/body/div[5]/div/div/div[1]/div/div[2]/div/div/div/div[1]/div[3]/div[1]/button/span/span').text
    
    assert 'Exibir mapa' == text_exibir_mapa

def test_resultado_busca():
    # selciona o botão pesquisar
    botao_pesquisar = navegador.find_element('xpath', '/html/body/div[5]/div/div/div[1]/div/div[2]/div/div/div/div[1]/div[1]/div/div/div/header/div/div[2]/div[1]/div/button[1]/div')
    # clica na barra de pesquisa
    botao_pesquisar.click()
    time.sleep(2)
    
    # seleciona o input "Onde"
    campo_input_onde = navegador.find_element('xpath', '//*[@id="bigsearch-query-location-input"]')
    # adiciona "Rio de Janeiro" ao input
    campo_input_onde.send_keys('Rio de Janeiro')
    # enter para ir pro próximo campo
    campo_input_onde.send_keys(Keys.ENTER)
    time.sleep(3)
    
    # seleciona o dia 20
    dia_20 = navegador.find_element('xpath', '//*[@id="panel--tabs--0"]/div/div[1]/div/div/div/div/div[2]/div[2]/div/div[2]/div/table/tbody/tr[4]/td[3]')
    # clica no dia 20
    dia_20.click()
    time.sleep(1)
    
    # seleciona o dia 25
    dia_25 = navegador.find_element('xpath', '//*[@id="panel--tabs--0"]/div/div[1]/div/div/div/div/div[2]/div[2]/div/div[2]/div/table/tbody/tr[5]/td[1]')
    # clica no dia 25
    dia_25.click()
    time.sleep(2)
    
    # seleciona o botão de busca
    btn_buscar = navegador.find_element('xpath', '//*[@id="search-tabpanel"]/div/div[5]/div[1]/div[2]/button/span[1]')
    # clica no botão de busca
    btn_buscar.click()
    time.sleep(1)

    # verifica se a pesquisa corresponde a procura
    assert "Rio de Janeiro" in navegador.title

def test_sua_busca():
    # seleciona o texto do botão "Sua busca"
    text_btn_sua_busca = navegador.find_element('xpath', '//*[@id="categoryScroller"]/div/div/div/div[3]/div/div/div/div/label[1]/div/span/div/span').text
    time.sleep(3)
    
    # verifica se o texto do botão está correto 
    assert 'Sua busca' == text_btn_sua_busca
    
def test_frente_praia():
    # seleciona o botão "Em frente  a praia"
    btn_frente_praia = navegador.find_element('xpath', '//*[@id="categoryScroller"]/div/div/div/div[3]/div/div/div/div/label[4]/div/span')
    # clica no botão
    btn_frente_praia.click()
    
    # seleciona o texto do botão "Em frente a praia"
    texto_frente_praia = navegador.find_element('xpath', '//*[@id="categoryScroller"]/div/div/div/div[3]/div/div/div/div/label[4]/div/span/div/span').text
    time.sleep(8)
    
    # verifica se o texto do botão está correto
    assert 'Em frente à praia' == texto_frente_praia    
    
