import mysql.connector
import random as r  

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "hospital_veterinario"
)
mycursor = mydb.cursor()

nome = ["Miguel", "Sophia",	"Davi",	"Alice", "Arthur",	"Julia",	"Pedro",	"Isabella",	"Gabriel",	"Manuela",	"Bernardo",	"Laura",	"Lucas",	"Luiza",	"Matheus",	"Valentina",	"Rafael",	"Giovanna",	"Heitor",	"Maria" ,"Eduarda",	"Enzo",	"Helena", "Guilherme",	"Beatriz",	"Nicolas",	"Maria Luiza",	"Lorenzo",	"Lara",	"Gustavo",	"Mariana",	"Felipe",	"Nicole",	"Samuel",	"Rafaela",	"João Pedro",	"Heloísa",	"Daniel",	"Isadora",	"Vitor"	,"Lívia",	"Leonardo",	"Maria Clara",	"Henrique",	"Ana Clara",	"Theo",	"Lorena",	"Murilo",	"Gabriela",	"Eduardo",	"Yasmin",	"Pedro Henrique",	"Isabelly",	"Pietro", "Play Osu Game", "Jorge Gameplays555", "Piton", "Onichan"]

telefone = ["(64)279-19270", "(63)490-45299", "(61)031-74545", "(62)152-68969", "(61)869-40855", "(63)844-74792", "(62)467-58274", "(61)700-69654", "(63)493-88726", "(62)954-10185", "(62)124-20526", "(64)928-77805", "(63)882-08859", "(61)684-60712", "(62)654-05782", "(61)630-32862", "(63)586-45581", "(62)527-38379", "(61)571-94597", "(63)740-49813", "(62)615-26890", "(62)386-13332", "(64)826-69064", "(63)562-83345", "(61)251-98950", "(62)945-83749", "(61)461-31860", "(63)047-17227", "(62)122-42690", "(61)659-39553", "(63)307-50131", "(62)546-76990", "(62)592-56849", "(64)051-78144", "(63)674-53810", "(61)005-26551", "(62)360-16523", "(61)489-64709", "(63)911-41294", "(62)400-53664", "(61)277-71568", "(63)499-59073", "(62)937-77773", "(62)405-73350", "(64)073-01307", "(63)145-43820", "(61)980-02160", "(62)954-56287", "(61) 281-49504", "(63)906-15846", "(62)4002-8922"]

endereco = ["Adevilson Estevan dos Santos", "Água Chata", "Ala", "Albertina Duarte Leite", "Alberto Hinoto", "Aldeias Altas", "Alexandre Kiss", "Altemar Dutra", "Altina Alves Brogna", "Alto Longá", "Ângelo Roberto Orsomarso", "Antônio Mestriner", "Antônio Tava", "Aroazes", "Arauá", "Atlas", "Araucária", "Assis Abude", "Aveloz", "Belgrado", "Berilo", "Blecaute", "Cocaína", "Bonsai", "Boqueirão dos Cochos", "Borba Gato", "Botumirim", "Branquinha", "Caminho Velho", "Capelinha", "Capibaribe", "Carlos Drumond de Andrade", "Carmela Thomeu", "Catharina Maria de Jesus (Dona)", "Caviúna", "Cereja do Mato", "Chico Mendes", "Cícera Adriana Oliveira Cruz", "Cícero Dantas", "Circular", "Colina", "Cristalina", "Curvelo", "Cumbe", "Datas", "David Nasser", "Deise", "Demerval Lobão", "Deolinda Ramos Bueno", "Doze de Fevereiro", "Dracena", "Duarte Leopoldo e Silva (Dom)", "Ecologia", "Edmar Bressam", "Eduardo Froner", "Eliane Mendes Ferreira", "Elias Dabarian", "Elvis Presley", "Elza Gomes", "Etelvina", "Eucalipto Vermelho", "Euráchio Maurício", "Felício Alves", "Felício Alves", "Felício Antônio Alves (Prefeito)", "Felício dos Santos", "Felisburgo", "Fernando Luz", "Flexeiras", "Flor de Lis", "Flor de Maio", "Flor do Caribe", "Florestan Fernandes", "Florianópolis", "Francinópolis", "Francisco Badaró", "Francisco Xavier Correa", "Geralda Conceição Mota", "Geraldo Ederli Praça", "Glória da Conceição Aires", "Gonçalo Alves", "Gonçalves Dias", "Gontran de Sarandy Raposo", "Graviolas", "Groíras", "Guapó", "Guaratinga", "Hélder Câmara (Dom)" "Hemel", "Hungria", "Ibimirim", "Ibirapoã", "Icatu", "Idalina Muniz Rodrigues", "Igarapé Grande", "Ilha Bela", "Inhuma", "Ipuã", "Iracema", "Irapuã", "Itacarambi", "Itaeté", "Itália", "Itanhaém", "Itanhaém", "Itaperuna", "Izabel Camareiro Losano", "Casa Claúdio", "WYSI 727"]

pet_verificador = []

for i in range(1, 51):
    pet = r.randint(1,50)

    while True:
        if pet in pet_verificador:
            pet = r.randint(1,50)
        else:
            pet_verificador.append(pet)
            break
    
    num = r.choice(telefone)
    telefone.remove(num)

    mycursor.execute(f"""insert into cliente (codigo_cliente, nome_cliente, telefone_cliente, endereco_cliente, pet_cliente)
    values ({i}, "{r.choice(nome)}", "{r.choice(telefone)}", "{r.choice(endereco)}, Nº {r.randint(1, 999)}", {pet});""")
    mydb.commit()

    # print(f"values ({i}, '{r.choice(nome)}', '{r.choice(telefone)}', '{r.choice(endereco)}, Nº {r.randint(1, 999)}', {pet})")