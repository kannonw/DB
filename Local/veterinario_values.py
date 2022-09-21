from asyncio.windows_events import NULL
import mysql.connector
import random as r  

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "hospital_veterinario"
)
mycursor = mydb.cursor()

nome = ["Miguel", "Sophia",	"Davi",	"Alice", "Arthur",	"Julia",	"Pedro",	"Isabella",	"Gabriel",	"Manuela",	"Bernardo",	"Laura",	"Lucas",	"Luiza",	"Matheus",	"Valentina",	"Rafael",	"Giovanna",	"Heitor",	"Maria" ,"Eduarda",	"Enzo",	"Helena", "Guilherme",	"Beatriz",	"Nicolas",	"Maria Luiza",	"Lorenzo",	"Lara",	"Gustavo",	"Mariana",	"Felipe",	"Nicole",	"Samuel",	"Rafaela",	"João Pedro",	"Heloísa",	"Daniel",	"Isadora",	"Vitor"	,"Lívia",	"Leonardo",	"Maria Clara",	"Henrique",	"Ana Clara",	"Theo",	"Lorena",	"Murilo",	"Gabriela",	"Eduardo",	"Yasmin",	"Pedro Henrique",	"Isabelly",	"Pietro"]

telefone = ["(62)587-66300","(62)191-80187","(62)749-68923","(62)904-95361","(62)910-23942","(62)506-87173","(62)763-76325","(62)520-51254","(62)588-54822","(62)309-37674","(62)077-92998","(62)136-79555","(62)482-02206","(62)635-83263","(62)622-84652","(63)485-43124","(63)121-89974","(63)754-46812","(63)506-64428","(63)301-82390","(63)977-25269","(63)512-56213","(63)554-29547","(63)877-27599","(63)260-21146","(63)671-23665","(63)104-88160","(63)208-23435","(63)492-25037"",(63)049-76915","(61)856-51585","(61)367-12718","(61)951-36685","(61)975-05161","(61)199-42524","(61)965-65179","(61)373-96147","(61)638-95780","(61)425-11177","(61)856-68407","(61)128-88168","(61)477-51902","(61)299-98464","(61)150-27305","(61)220-97862","(61)632-75275","(61)125-53055","(61)963-18628","(61)056-91019","(61)361-48393","(61)092-88920","(61)826-32291","(61)033-57072","(61)013-71300","(61)921-71444"]

endereco = ["Adevilson Estevan dos Santos", "Água Chata", "Ala", "Albertina Duarte Leite", "Alberto Hinoto", "Aldeias Altas", "Alexandre Kiss", "Altemar Dutra", "Altina Alves Brogna", "Alto Longá", "Ângelo Roberto Orsomarso", "Antônio Mestriner", "Antônio Tava", "Aroazes", "Arauá", "Atlas", "Araucária", "Assis Abude", "Aveloz", "Belgrado", "Berilo", "Blecaute", "Bocaína", "Bonsai", "Boqueirão dos Cochos", "Borba Gato", "Botumirim", "Branquinha", "Caminho Velho", "Capelinha", "Capibaribe", "Carlos Drumond de Andrade", "Carmela Thomeu", "Catharina Maria de Jesus (Dona)", "Caviúna", "Cereja do Mato", "Chico Mendes", "Cícera Adriana Oliveira Cruz", "Cícero Dantas", "Circular", "Colina", "Cristalina", "Curvelo", "Cumbe", "Datas", "David Nasser", "Deise", "Demerval Lobão", "Deolinda Ramos Bueno", "Doze de Fevereiro", "Dracena", "Duarte Leopoldo e Silva (Dom)", "Ecologia", "Edmar Bressam", "Eduardo Froner", "Eliane Mendes Ferreira", "Elias Dabarian", "Elvis Presley", "Elza Gomes", "Etelvina", "Eucalipto Vermelho", "Euráchio Maurício", "Felício Alves", "Felício Alves", "Felício Antônio Alves (Prefeito)", "Felício dos Santos", "Felisburgo", "Fernando Luz", "Flexeiras", "Flor de Lis", "Flor de Maio", "Flor do Caribe", "Florestan Fernandes", "Florianópolis", "Francinópolis", "Francisco Badaró", "Francisco Xavier Correa", "Geralda Conceição Mota", "Geraldo Ederli Praça", "Glória da Conceição Aires", "Gonçalo Alves", "Gonçalves Dias", "Gontran de Sarandy Raposo", "Graviolas", "Groíras", "Guapó", "Guaratinga", "Hélder Câmara (Dom)" "Hemel", "Hungria", "Ibimirim", "Ibirapoã", "Icatu", "Idalina Muniz Rodrigues", "Igarapé Grande", "Ilha Bela", "Inhuma", "Ipuã", "Iracema", "Irapuã", "Itacarambi", "Itaeté", "Itália", "Itanhaém", "Itanhaém", "Itaperuna", "Izabel Camareiro Losano"]

salario = [2200, 2500, 3000, 3500, 4000, 5000, 6000, 7000, 8000, 9000, 10000]

pet_verificador = []

for i in range(1, 16):
    pet = r.randint(1,50)
    n = r.randint(1, 2)

    while True:
        if pet in pet_verificador:
            pet = r.randint(1,50)
        else:
            pet_verificador.append(pet)
            break
    
    num = r.choice(telefone)
    telefone.remove(num)

    dia = r.randint(1, 30); mes = r.randint(1, 12); ano = r.randint(2005, 2022)

    if n == 1:
        diaf = r.randint(1, 30); mesf = r.randint(1, 12); anof = r.randint(ano+1, 2022)
    else:
        diaf, mesf, anof = 0, 0, 0

    mycursor.execute(f"""insert into veterinario (codigo_veterinario, nome_veterinario, telefone_veterinario, endereco_veterinario, salario_veterinario, data_de_ingresso, data_de_saida, carga_horaria_semanal)
    values ({i}, "{r.choice(nome)}", "{num}", "{r.choice(endereco)}, Nº {r.randint(1, 999)}", {r.choice(salario)}, '{ano}-{mes}-{dia}', '{anof}-{mesf}-{diaf}', {r.randint(30, 60)});""")
    mydb.commit()
    