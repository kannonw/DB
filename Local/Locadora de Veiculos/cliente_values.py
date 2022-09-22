import mysql.connector
import random as r  

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "locadora_de_veiculos"
)
mycursor = mydb.cursor()

nome = ["Miguel", "Sophia",	"Davi",	"Alice", "Arthur",	"Julia",	"Pedro",	"Isabella",	"Gabriel",	"Manuela",	"Bernardo",	"Laura",	"Lucas",	"Luiza",	"Matheus",	"Valentina",	"Rafael",	"Giovanna",	"Heitor",	"Maria" ,"Eduarda",	"Enzo",	"Helena", "Guilherme",	"Beatriz",	"Nicolas",	"Maria Luiza",	"Lorenzo",	"Lara",	"Gustavo",	"Mariana",	"Felipe",	"Nicole",	"Samuel",	"Rafaela",	"João Pedro",	"Heloísa",	"Daniel",	"Isadora",	"Vitor"	,"Lívia",	"Leonardo",	"Maria Clara",	"Henrique",	"Ana Clara",	"Theo",	"Lorena",	"Murilo",	"Gabriela",	"Eduardo",	"Yasmin",	"Pedro",	"Isabelly",	"Pietro", "Play Osu Game", "Jorge Gameplays555", "Piton", "Onichan", "Henrique"]

sobrenome = [ "Almeida", "Azevedo", "Braga", "Barros", "Bahiense", "Campos", "Cardoso", "Correia", "Castro", "Costa", "Fontes" , "Guimarães" , "Magalhães" , "Macedo", "Matos", "Pedreira", "Queirós", "Ribeiro", "Rocha", "Siqueira", "Serra", "Souza", "Teixeira", "Valle"]

endereco = ["Adevilson Estevan dos Santos", "Água Chata", "Ala", "Albertina Duarte Leite", "Alberto Hinoto", "Aldeias Altas", "Alexandre Kiss", "Altemar Dutra", "Altina Alves Brogna", "Alto Longá", "Ângelo Roberto Orsomarso", "Antônio Mestriner", "Antônio Tava", "Aroazes", "Arauá", "Atlas", "Araucária", "Assis Abude", "Aveloz", "Belgrado", "Berilo", "Blecaute", "Cocaína", "Bonsai", "Boqueirão dos Cochos", "Borba Gato", "Botumirim", "Branquinha", "Caminho Velho", "Capelinha", "Capibaribe", "Carlos Drumond de Andrade", "Carmela Thomeu", "Catharina Maria de Jesus (Dona)", "Caviúna", "Cereja do Mato", "Chico Mendes", "Cícera Adriana Oliveira Cruz", "Cícero Dantas", "Circular", "Colina", "Cristalina", "Curvelo", "Cumbe", "Datas", "David Nasser", "Deise", "Demerval Lobão", "Deolinda Ramos Bueno", "Doze de Fevereiro", "Dracena", "Duarte Leopoldo e Silva (Dom)", "Ecologia", "Edmar Bressam", "Eduardo Froner", "Eliane Mendes Ferreira", "Elias Dabarian", "Elvis Presley", "Elza Gomes", "Etelvina", "Eucalipto Vermelho", "Euráchio Maurício", "Felício Alves", "Felício Alves", "Felício Antônio Alves (Prefeito)", "Felício dos Santos", "Felisburgo", "Fernando Luz", "Flexeiras", "Flor de Lis", "Flor de Maio", "Flor do Caribe", "Florestan Fernandes", "Florianópolis", "Francinópolis", "Francisco Badaró", "Francisco Xavier Correa", "Geralda Conceição Mota", "Geraldo Ederli Praça", "Glória da Conceição Aires", "Gonçalo Alves", "Gonçalves Dias", "Gontran de Sarandy Raposo", "Graviolas", "Groíras", "Guapó", "Guaratinga", "Hélder Câmara (Dom)" "Hemel", "Hungria", "Ibimirim", "Ibirapoã", "Icatu", "Idalina Muniz Rodrigues", "Igarapé Grande", "Ilha Bela", "Inhuma", "Ipuã", "Iracema", "Irapuã", "Itacarambi", "Itaeté", "Itália", "Itanhaém", "Itanhaém", "Itaperuna", "Izabel Camareiro Losano", "Casa Claúdio", "WYSI 727"]

telefone = ["(64)279-19270", "(63)490-45299", "(61)031-74545", "(62)152-68969", "(61)869-40855", "(63)844-74792", "(62)467-58274", "(61)700-69654", "(63)493-88726", "(62)954-10185", "(62)124-20526", "(64)928-77805", "(63)882-08859", "(61)684-60712", "(62)654-05782", "(61)630-32862", "(63)586-45581", "(62)527-38379", "(61)571-94597", "(63)740-49813", "(62)615-26890", "(62)386-13332", "(64)826-69064", "(63)562-83345", "(61)251-98950", "(62)945-83749", "(61)461-31860", "(63)047-17227", "(62)122-42690", "(61)659-39553", "(63)307-50131", "(62)546-76990", "(62)592-56849", "(64)051-78144", "(63)674-53810", "(61)005-26551", "(62)360-16523", "(61)489-64709", "(63)911-41294", "(62)400-53664", "(61)277-71568", "(63)499-59073", "(62)937-77773", "(62)405-73350", "(64)073-01307", "(63)145-43820", "(61)980-02160", "(62)954-56287", "(61) 281-49504", "(63)906-15846", "(62)4002-8922"]

cpf = ["510.114.343-00", "545.123.816-27", "881.814.638-62", "230.140.011-55", "765.156.816-82", "125.562.315-21", "068.770.713-79", "850.504.747-87", "485.687.308-33", "747.475.211-51", "211.746.771-71", "504.121.387-94", "702.133.101-04", "660.143.464-73", "531.186.135-56", "114.365.061-15", "606.162.286-43", "662.774.326-48", "347.680.344-97", "376.103.724-47", "474.725.718-73", "581.825.762-29", "420.703.062-08", "230.742.568-34", "722.854.360-25", "056.124.116-34", "422.110.214-41", "587.755.056-06", "203.268.721-67", "308.045.056-67", "307.015.787-42", "570.340.435-58", "841.016.410-80", "757.427.282-47", "214.414.870-85", "881.345.466-09", "407.512.311-18", "837.177.222-04", "604.705.566-41", "871.875.330-20", "042.364.443-21", "103.270.327-07", "180.580.788-91", "607.133.021-19", "776.718.126-09", "676.444.684-98", "540.542.330-07", "564.860.280-41", "106.034.876-45", "408.646.521-35", "208.476.742-31", "235.523.073-03", "000.051.117-06", "450.145.523-31", "070.248.830-57", "777.086.508-52", "506.037.324-02", "754.680.144-32", "501.687.634-78", "365.247.033-83", "133.267.030-07", "163.884.014-81", "041.432.763-21", "331.635.264-38", "526.742.064-62", "411.031.200-00", "406.668.365-74", "673.417.168-00", "622.733.385-97", "735.521.575-22", "584.837.327-26", "102.822.785-08", "248.052.022-62", "666.185.500-25", "635.246.502-10", "730.322.477-72", "623.467.282-50", "331.130.886-74", "882.014.181-74", "465.848.104-96", "880.030.643-84", "611.227.702-60", "061.383.600-60", "705.856.777-86", "548.428.503-88", "675.006.686-00", "453.501.266-01", "615.057.211-05", "407.514.104-70", "077.844.845-26", "416.276.500-67", "372.268.754-38", "732.172.225-20", "266.170.525-28", "020.331.854-43", "782.434.353-79", "741.165.751-43", "101.452.440-75", "432.742.602-40", "538.122.110-09"]

email = ["@gmail.com", "@hotmail.com", "@outlook.com", "@protonmail.com"]

for i in range(1, 51):
    
    num = r.choice(telefone)
    telefone.remove(num)

    cpfx = r.choice(cpf)
    cpf.remove(cpfx)

    dia = r.randint(1, 30); mes = r.randint(1, 12); ano = r.randint(1960, 2004)

    n = r.choice(nome)
    s = r.choice(sobrenome)

    mycursor.execute(f"""insert into cliente (nome, endereco, cpf, telefone, data_de_nascimento, email)
    values ("{n} {s}", "{r.choice(endereco)}, Nº {r.randint(1, 999)}", "{cpfx}", "{num}", '{ano}-{mes}-{dia}', "{n.lower()}.{s.lower()}{r.choice(email)}");""")
    mydb.commit()

    # print(f"{n} {s}, {r.choice(endereco)}, Nº {r.randint(1, 999)}, {cpfx}, {r.choice(telefone)}, '{ano}-{mes}-{dia}', {n.lower()}.{s.lower()}{r.choice(email)});")