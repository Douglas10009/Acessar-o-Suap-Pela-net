'''
Código feito por Douglas Éverton,  estudante IFBA campus Santo Amaro
do 2° ano de TI.

Feito em: 06/11/2022
'''


from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime

# Erro ao rodar pelo Codespaces ou qualquer outra maneira online, porque não tem o ChromeDrivers
# Tentativa de criar um chrome Driver, caso tente rodar no seu pc, tire o código a partir dessa linha até ...
from selenium.webdriver.chrome.options import Options

options = Options()
options.binary_location = "C:\\Program Files\\Chrome\\chrome64_55.0.2883.75\\chrome.exe"
driver = webdriver.Chrome(chrome_options=options,
                          executable_path=r'C:\path\to\chromedriver.exe')
driver.get('http://google.com/')
print("Chrome Browser Invoked")

# Até essa linha aqui

# Cria um documento para armazenar arquivos
today = datetime.now().strftime("%d-%m-%Y_%H,%M,%S") + ".txt"
arquivo = open(today, "x", encoding='utf-8')


# Abrir navegador
nav = webdriver.Chrome()

# Acessar o suap
nav.get('https://suap.ifba.edu.br/')


# Entra com a senha e login
login = ""  # INSIRA SEU LOGIN
nav.find_element(By.NAME, "username").send_keys(login)
senha = ""  # INSIRA SUA SENHA
nav.find_element(By.NAME, "password").send_keys(senha)
nav.find_element(By.XPATH, '//*[@id="login"]/form/div[3]/input').click()


# Ir para a aba de boletim
nav.get("https://suap.ifba.edu.br/edu/aluno/" + login + "/?tab=boletim")


# Pegar o nome
nome = nav.find_element(By.XPATH, '//*[@id="content"]/div[2]/h2').text
# Colocar o nome no arquivo
arquivo.write(f'Usuário: {nome}\n')
arquivo.write('-' * 50)
arquivo.write('\n \n')  # Quebra de linha

# Pegar as notas
for j in range(1, 13):  # Muda as matérias
    materia = nav.find_element(
        By.XPATH, '//*[@id="content"]/div[13]/div[2]/div/table/tbody/tr[' + str(j) + ']/td[2]').text
    contador = 1
    pontosNescessarios = 0.0
    soma = 0.0
    nota = ""

    for i in range(8, 15, 2):  # Muda as unidades
        link = '//*[@id="content"]/div[13]/div[2]/div/table/tbody/tr[' + str(j) + ']/td[' + \
            str(i) + ']'
        nota1 = nav.find_element(By.XPATH, link).text

        nota = str(nota1).replace(',', '.')
        print(f"Sua nota {contador} é  {nota}")
        arquivo.write(f"\nSua nota {contador} é  {nota}\n")

        soma += float(nota)
        print(f"Sua soma até agora é de {soma} pontos.")
        arquivo.write(f"Sua soma até agora é de {soma} pontos.")
        contador += 1

    pontosNescessarios = soma - 24
    if pontosNescessarios < 0:
        pontosNescessarios *= -1
        print(
            f"\nVocê precisa de {pontosNescessarios} pontos, na matéria de {materia}\n")
        arquivo.write(
            f"\n \nVocê precisa de {pontosNescessarios} pontos, na matéria de {materia}\n \n \n")
    else:
        print(
            f"\nParábens meu rei, tu já tá passado fio, com {pontosNescessarios} pontos execentes, na matéria de {materia}\n")
        arquivo.write(
            f"\n \nParábens meu rei, tu já tá passado fio, com {pontosNescessarios} pontos execentes, na matéria de {materia}\n \n \n")

nav.quit()


# Problemas conhecidos: Na matéria de química, ele só vai até a 3° unidade, não finalizando até a 4°.

# Coisas para implementar:
# 1 - Colocar os resultados em um arquivo, para que fique melhor visualização, com o título sendo a data em que foi feito o relatório. 🆗 YESSIR FEITO
# 2 - Colocar o pedido de senha e login em interface gráfica
# 3 - Compilar em um executável, com todos os pacotes, inputs e interface gráfica.
