import stories_generator
import numpy as np
import random
import string
import json

pizzas_disponiveis = [
                        "Calabresa",
                        "Portuguesa",
                        "Muçarela",
                        "Marguerita",
                        "Quatro queijos",
                        "Frango com catupiry",
                        "Alcachofra",
                        "Mexicana",
                        "Francesa",
                        "Parma com rúcula",
                        "Caprese",
                        "Alho Negro",
                        "Scamorza",
                        "Califórnia",
                        "Americana",
                        "Camarão",
                        "Atum",
                        "Pepperoni",
                        "Palmito e Brócolis",
                        "Pimentão e Azeitona",
                        "Rúcula",
                        "Abobrinha com requeijão",
                        "Palmito e champignon",
                        "Alho e óleo",
                        "Repolho",
                        "Cebola caramelizada",
                        "Abobrinha com aveia",
                        "Brócolis e peito de peru",
                        "Berinjela e abobrinha",
                        "Champignon e manjericão",
                        "Calabresa com cheddar",
                        "Presunto com cheddar",
                        "Frango com cheddar",
                        "Canadense",
                        "Escarola",
                        "Siciliana",
                        "Tribeca",
                        "Al Capone",
                        "Estrogonofe",
                        "Palmito com catupiry",
                        "Jardineira",
                        "Atum com palmito",
                        "Peito de peru e champignon",
                        "Carne seca com cream cheese",
                        "Peito de peru com cream cheese",
                        "Atum com cream cheese e alho-poró",
                        "Cream cheese com abobrinha",
                        "Frango com palmito",
                        "Frango à parmegiana",
                        "Caipira",
]

list_bairros = ['Aclimação', 'Alto da Lapa', 'Alto da Mooca', 'Alto de Pinheiros', 'Altos de Vila Prudente', 'Americanópolis', 'Balneário Mar Paulista', 'Barra Funda', 'Bela Vista', 'Belenzinho', 'Bom Retiro', 'Bortolândia', 'Brasilândia', 'Brooklin Paulista', 'Brás', 'Cambuci', 'Campo Belo', 'Cantinho do Céu', 'Capela do Socorro', 'Capão do Embira', 'Caxingui', 'Centro', 'Chácara Belenzinho', 'Chácara Gaivotas', 'Chácara Itaim', 'Chácara Santo Antônio (Zona Sul)', 'Chácara São João', 'Cidade Ademar', 'Cidade Dutra', 'Cidade Luz', 'Cidade Mãe do Céu', 'Cidade Nova América', 'Cidade Nova Heliópolis', 'Cidade Patriarca', 'Cidade Satélite Santa Bárbara', 'Cidade São Mateus', 'Cidade Tiradentes', 'Condomínio Jequirituba', 'Conjunto Habitacional Fazenda do Carmo', 'Conjunto Habitacional Instituto Adventista', 'Conjunto Habitacional Marechal Mascarenhas de Morais', 'Conjunto Habitacional Santa Etelvina II', 'Conjunto Habitacional Sitio Conceição', 'Conjunto Habitacional Turística', 'Conjunto Promorar Sapopemba', 'Conjunto Promorar São Luis', 'Conjunto Residencial José Bonifácio', 'Conjunto Residencial Paraíso', 'Eldorado', 'Engenheiro Marsilac', 'Granja Julieta', 'Higienópolis', 'Instituto de Previdência', 'Interlagos', 'Ipiranga', 'Itaberaba', 'Itaim Paulista', 'Itaquera', 'Itupu', 'Jabaquara', 'Jaguaré', 'Jardim Alfredo', 'Jardim Almeida', 'Jardim Almeida Prado', 'Jardim Alto Pedroso', 'Jardim Alvorada (Zona Sul)', 'Jardim Ana Lúcia', 'Jardim Antártica', 'Jardim Apurá', 'Jardim Aracati', 'Jardim Aristocrata', 'Jardim Avenida', 'Jardim Belém', 'Jardim Botucatu', 'Jardim Cachoeira', 'Jardim Caguassu', 'Jardim Campo Limpo (Zona Norte)', 'Jardim Campos', 'Jardim Cinco de Julho', 'Jardim Cleide', 'Jardim Clímax', 'Jardim Colibri', 'Jardim Colombo', 'Jardim Colorado', 'Jardim Denise', 'Jardim Dona Deolinda', 'Jardim Edith', 'Jardim Elisa Maria', 'Jardim Eliza', 'Jardim Elizabeth', 'Jardim Europa', 'Jardim Eva', 'Jardim Flor de Maio', 'Jardim Franca', 'Jardim Gilda Maria', 'Jardim Gonzaga', 'Jardim Guarapiranga', 'Jardim Guarujá', 'Jardim Guedala', 'Jardim Helena', 'Jardim Heloisa', 'Jardim Imperador (Zona Leste)', 'Jardim Indaiá', 'Jardim Irapiranga', 'Jardim Itapemirim', 'Jardim Japão', 'Jardim Jaú (Zona Leste)', 'Jardim Lajeado', 'Jardim Los Angeles', 'Jardim Lourdes', 'Jardim Luzitânia', 'Jardim Lídia', 'Jardim Lúcia', 'Jardim Marabá', 'Jardim Marajoara', 'Jardim Maria Duarte', 'Jardim Maria Estela', 'Jardim Maria Luiza', 'Jardim Maria Rita', 'Jardim Marília', 'Jardim Miriam', 'Jardim Monjolo', 'Jardim Monte Azul', 'Jardim Monte Verde', 'Jardim Nelia IV', 'Jardim Noronha', 'Jardim Nova Conquista', 'Jardim Nove de Julho', 'Jardim Nélia', 'Jardim Oriental', 'Jardim Palmares (Zona Sul)', 'Jardim Papai Noel', 'Jardim Paulista', 'Jardim Porteira Grande', 'Jardim Prainha', 'Jardim Previdência', 'Jardim Primavera (Zona Sul)', 'Jardim Pérola III', 'Jardim Raposo Tavares', 'Jardim Reimberg', 'Jardim Rizzo', 'Jardim Rubio', 'Jardim Santa Adélia', 'Jardim Santa Edwiges (Capela do Socorro)', 'Jardim Santa Etelvina', 'Jardim Santa Lucrécia', 'Jardim Santa Margarida', 'Jardim Santa Maria', 'Jardim Santa Terezinha (Parelheiros)', 'Jardim Santo Elias (São Miguel)', 'Jardim Silva Teles', 'Jardim São Bento', 'Jardim São Bento Novo', 'Jardim São Carlos (Zona Leste)', 'Jardim São Francisco', 'Jardim São Manoel', 'Jardim São Paulo(Zona Leste)', 'Jardim São Paulo(Zona Norte)', 'Jardim São Savério', 'Jardim São Vicente', 'Jardim Sônia (Zona Sul)', 'Jardim Taboão', 'Jardim Taipas', 'Jardim Taquaral', 'Jardim Textil', 'Jardim Triana', 'Jardim Trussardi', 'Jardim Três Marias', 'Jardim Vera Cruz', 'Jardim Vera Cruz(Zona Leste)', 'Jardim Vergueiro (Sacomã)', 'Jardim Virginia Bianca', 'Jardim Vista Alegre', 'Jardim Vivan', 'Jardim da Laranjeira (Zona Leste)', 'Jardim da Pedreira', 'Jardim das Acácias', 'Jardim das Camélias', 'Jardim das Laranjeiras', 'Jardim das Vertentes', 'Jardim dos Eucaliptos', 'Lajeado', 'Lapa', 'Luz', 'Mooca', 'Parada Inglesa', 'Parada XV de Novembro', 'Paraisópolis', 'Paraíso', 'Parque Boa Esperança', 'Parque Boturussu', 'Parque Casa de Pedra', 'Parque Cocaia', 'Parque Colonial', 'Parque Continental', 'Parque Cruzeiro do Sul', 'Parque Grajaú', 'Parque Guaianazes', 'Parque Jabaquara', 'Parque Mandaqui', 'Parque Novo Mundo', 'Parque Peruche', 'Parque Primavera', 'Parque Ramos Freitas', 'Parque Recreio', 'Parque Regina', 'Parque Savoy City', 'Parque São Domingos', 'Parque São Lucas', 'Parque São Luís', 'Parque São Rafael', 'Parque da Vila Prudente', 'Parque das Flores', 'Penha de França', 'Pinheiros', 'Piqueri', 'Pirituba', 'Planalto Paulista', 'Praia Azul', 'Real Parque', 'Recanto Verde do Sol', 'Residencial Sol Nascente', 'Rio Pequeno', 'Sacomã', 'Santa Amélia', 'Santa Cecília', 'Santana', 'Santo Amaro', 'Saúde', 'Siciliano', 'Sumarezinho', 'Super Quadra Morumbi', 'São João Clímaco', 'São Judas', 'São Miguel Paulista', 'Sé', 'Sítio Itaberaba II', 'Tatuapé', 'Terceira Divisão', 'Tremembé', 'Valo Velho', 'Vila Albertina', 'Vila Amélia', 'Vila Ana Rosa', 'Vila Anastácio', 'Vila Antonieta', 'Vila Aricanduva', 'Vila Aurora', 'Vila Bancária Munhoz', 'Vila Barbosa', 'Vila Baruel', 'Vila Bela', 'Vila Bela Vista (Zona Norte)', 'Vila Boaçava', 'Vila Bonilha', 'Vila Butantã', 'Vila Caiúba', 'Vila Caju', 'Vila Campanela', 'Vila Campo Grande', 'Vila Carmosina', 'Vila Carrão', 'Vila Cavaton', 'Vila Clara', 'Vila Clementino', 'Vila Conceição', 'Vila Congonhas', 'Vila Constança', 'Vila Continental', 'Vila Cosmopolita', 'Vila Cruzeiro', 'Vila Curuçá', 'Vila Dalva', 'Vila Dom Pedro I', 'Vila Dom Pedro II', 'Vila Domitila', 'Vila Esperança', 'Vila Fachini', 'Vila Firmiano Pinto', 'Vila Formosa', 'Vila Francos', 'Vila Germinal', 'Vila Gil', 'Vila Gomes Cardim', 'Vila Guilherme', 'Vila Guilhermina', 'Vila Gumercindo', 'Vila Gustavo', 'Vila Hebe', 'Vila Heliópolis', 'Vila Iolanda(Lajeado)', 'Vila Ipojuca', 'Vila Itaberaba', 'Vila Ivone', 'Vila Jaguara', 'Vila Lageado', 'Vila Laís', 'Vila Liviero', 'Vila Londrina', 'Vila Madalena', 'Vila Marari', 'Vila Maria', 'Vila Maria Alta', 'Vila Maria Baixa', 'Vila Mariana', 'Vila Matilde', 'Vila Mazzei', 'Vila Medeiros', 'Vila Monumento', 'Vila Moraes', 'Vila Moreira', 'Vila Morse', 'Vila Nancy', 'Vila Nhocune', 'Vila Nina', 'Vila Nivi', 'Vila Nova Conceição', 'Vila Nova Jaguaré', 'Vila Nova Utinga', 'Vila Olímpia', 'Vila Paiva', 'Vila Palmeiras', 'Vila Paranaguá', 'Vila Parque Jabaquara', 'Vila Paulicéia', 'Vila Paulo Silas', 'Vila Pedra Branca', 'Vila Pedroso', 'Vila Pirajussara', 'Vila Pita', 'Vila Ponte Rasa', 'Vila Prudente', 'Vila Regente Feijó', 'Vila Regina ( Zona Leste)', 'Vila Rui Barbosa', 'Vila Ré', 'Vila Sabrina', 'Vila Salete', 'Vila Santa Inês', 'Vila Santa Lúcia', 'Vila Santa Maria', 'Vila Santa Terezinha (Zona Norte)', 'Vila Sapopemba', 'Vila Sofia', 'Vila Souza', 'Vila São Francisco (Zona Leste)', 'Vila São Luís(Zona Oeste)', 'Vila Sílvia', 'Vila Tolstoi', 'Vila União (Zona Leste)', 'Vila Zilda (Tatuapé)', 'Vila da Paz', 'Vila das Mercês', 'Vila do Encontro', 'Vila do Sol', 'Vila dos Remédios', 'Vila Água Funda', 'Água Branca', 'Água Fria', 'Alphaville', 'Centro', 'Centro Prisional', 'Chácara Terra Branca', 'Chácaras Bauruenses', 'Chácaras Urupês', 'Cidade Jardim', 'Conjunto Habitacional Darcy César Improta', 'Conjunto Habitacional Engenheiro Otávio Rasi', 'Conjunto Habitacional Pastor Arlindo Lopes Viana', 'Conjunto Habitacional Presidente Eurico Gaspar Dutra', 'Conjunto Habitacional Primavera', 'Distrito Industrial Claudio Guedes Misquiati', 'Distrito Industrial Domingos Biancardi', 'Distrito Industrial Marcus Vinícius Feliz Machado', 'Ferradura Mirim', 'Floratta Nações Residencial', 'Fundação Casas Populares Salvador Filardi', 'Jardim América', 'Jardim Andorfato', 'Jardim Araruna', 'Jardim Bela Vista', 'Jardim Bom Samaritano', 'Jardim Central', 'Jardim Colonial', 'Jardim Contorno', 'Jardim Dona Lili', 'Jardim Estoril', 'Jardim Estoril II', 'Jardim Estoril IV', "Jardim Estrela D'Alva", 'Jardim Godoy', 'Jardim Guadalajara', 'Jardim Helena', 'Jardim Marabá', 'Jardim Marambá', 'Jardim Marilu', 'Jardim Marília', 'Jardim Mendonça', 'Jardim Nova Bauru', 'Jardim Nova Esperança', 'Jardim Nova Marília', 'Jardim Olímpico', 'Jardim Ouro Verde', 'Jardim Panorama', 'Jardim Paulista', 'Jardim Petrópolis', 'Jardim Progresso', 'Jardim Prudência', 'Jardim Redentor', 'Jardim Rosa Branca', 'Jardim Samburá', 'Jardim Santana', 'Jardim Shangri-Lá', 'Jardim Solange', 'Jardim TV', 'Jardim Vitória', 'Jardim das Orquídeas', 'Loteamento Chácaras Bauruenses II', 'Loteamento Empresarial Bauru', 'Loteamento Mário Luiz Rodrigues do Prado', 'Novo Jardim Pagani', 'Núcleo Eldorado', 'Núcleo Habitacional Fortunato Rocha Lima', 'Núcleo Habitacional José Regino', 'Núcleo Habitacional Mary Dota', 'Núcleo Habitacional Vereador Edson Francisco da Silva', 'Núcleo Residencial Beija-Flor', 'Núcleo Residencial Edison Bastos Gasparini', 'Núcleo Residencial Presidente Geisel', 'Panorama Parque', 'Parque Alto Sumaré', 'Parque Bauru', 'Parque Baurulândia', 'Parque Boa Vista', 'Parque Continental', 'Parque Hipódromo', 'Parque Industrial Manchester', 'Parque Jaraguá', 'Parque Jardim Europa', 'Parque Júlio Nóbrega', 'Parque Novo São Geraldo', 'Parque Paulista', 'Parque Primavera', 'Parque Residencial Jardim Araruna', 'Parque Residencial Paineiras', 'Parque Roosevelt', 'Parque Rossi', 'Parque Santa Cecília', 'Parque Santa Cândida', 'Parque Santa Rita', 'Parque São Geraldo', 'Parque São João', 'Parque União', 'Parque Val de Palmas', 'Parque Viaduto', 'Parque Vista Alegre', 'Pousada da Esperança I', 'Pousada da Esperança II', 'Quinta da Bela Olinda', 'Residencial Cidade Jardim', 'Residencial Estoril Premium', 'Residencial Jardim Jussara', 'Residencial Jardins do Sul', 'Residencial Lago Sul', 'Residencial Odete', 'Residencial Parque Colina Verde', 'Residencial Village Via Verde', 'Residencial Villaggio', 'Samambaia Parque Residencial', 'Sítios Village Paineiras', 'Tangarás', 'Tibiriçá', 'Vale do Igapó', 'Vila Aeroporto Bauru', 'Vila América', 'Vila Antártica', 'Vila Aviação', 'Vila Aviação B', 'Vila Becheli', 'Vila Bela', 'Vila Bonfim', 'Vila Brunhari', 'Vila Camargo', 'Vila Cardia', 'Vila Carmem', 'Vila Carolina', 'Vila Cidade Universitária', 'Vila Coralina', "Vila D'Aro", 'Vila Dutra', 'Vila Falcão', 'Vila Gimenes', 'Vila Guedes de Azevedo', 'Vila Industrial', 'Vila Ipiranga', 'Vila Martha', 'Vila Mesquita', 'Vila Nova Paulista', 'Vila Nova Santa Clara', 'Vila Nova Santa Luzia', 'Vila Pacífico II', 'Vila Paulista', 'Vila Popular', 'Vila Rocha', 'Vila Santa Izabel', 'Vila Santa Rosa', 'Vila Santa Tereza', 'Vila Seabra', 'Vila Silva Pinto', 'Vila Souto', 'Vila São Francisco', 'Vila São João da Boa Vista', 'Vila São João do Ipiranga', 'Vila São Manoel', 'Vila São Paulo', 'Vila Tecnológica Engenheiro José Queda', 'Alphaville Dom Pedro 3', 'Arruamento Fain José Feres', 'Bairro das Palmeiras', 'Barão Geraldo', 'Bonfim', 'Bosque das Palmeiras', 'Cambuí', 'Centro', 'Chácara Santa Letícia', 'Chácara Santa Margarida', 'Chácaras Campos dos Amarais', 'Chácaras São Martinho', 'Cidade Satélite Íris', 'Cidade Universitária', 'Colinas do Ermitage (Sousas)', 'Colônia Fazenda Santa Elisa', 'Conjunto Habitacional Edivaldo Antônio Orsi', 'Conjunto Habitacional Padre Anchieta', 'Conjunto Habitacional Parque Itajaí', 'Conjunto Habitacional Parque da Floresta', 'Conjunto Habitacional Vila Santana (Sousas)', 'Dic I (Conjunto Habitacional Monsenhor Luiz Fernando Abreu)', 'Dic II (Conj Habitacional Doutor Antônio Mendonça de Barros)', 'Dic V (Conjunto Habitacional Chico Mendes)', 'Dic VI (Conjunto Habitacional Santo Dias Silva)', 'Eldorado dos Carajás', 'Fazenda Santana (Sousas)', 'Jardim Adhemar de Barros', 'Jardim Atibaia (Sousas)', 'Jardim Aurélia', 'Jardim Bassoli', 'Jardim Bela Vista', 'Jardim Bom Retiro', 'Jardim Brasil', 'Jardim Campina Grande', 'Jardim Campo Belo', 'Jardim Campos Elíseos', 'Jardim Carlos Gomes', 'Jardim Carlos Lourenço', 'Jardim Chapadão', 'Jardim Conceição (Sousas)', 'Jardim Dom Bosco', 'Jardim Esplanada', 'Jardim Eulina', 'Jardim Fernanda', 'Jardim Florence', 'Jardim García', 'Jardim Guanabara', 'Jardim Guarani', 'Jardim Independência', 'Jardim Ipaussurama', 'Jardim Itaguaçu I', 'Jardim Lisa', 'Jardim Martinelli (Sousas)', 'Jardim Miranda', 'Jardim Monte Líbano', 'Jardim Nossa Senhora Auxiliadora', 'Jardim Nova América', 'Jardim Nova Europa', 'Jardim Novo Campos Elíseos', 'Jardim Novo Flamboyant', 'Jardim Novo Maracanã', 'Jardim Novo Sol', 'Jardim Paraíso de Viracopos', 'Jardim Paulicéia', 'Jardim Planalto de Viracopos', 'Jardim Primavera', 'Jardim Proença I', 'Jardim Quarto Centenário', 'Jardim Roseira', 'Jardim Rossin', 'Jardim Rosália IV', 'Jardim Santa Eudóxia', 'Jardim Santa Genebra', 'Jardim Santa Genebra II (Barão Geraldo)', 'Jardim Santa Lúcia', 'Jardim Santa Mônica', 'Jardim Santana', 'Jardim Santo Antonio', 'Jardim São Cristóvão', 'Jardim São Domingos', 'Jardim São Jorge', 'Jardim São José', 'Jardim São Marcos', 'Jardim São Pedro de Viracopos', 'Jardim Tamoio', 'Jardim Vista Alegre', 'Jardim Yeda', 'Jardim das Bandeiras', 'Jardim das Cerejeiras', 'Loteamento Center Santa Genebra', 'Loteamento Chácaras Gargantilhas', 'Loteamento Claude de Barros Penteado (Sousas)', 'Loteamento Parque das Águas', 'Loteamento Parque dos Alecrins', 'Loteamento Residencial Pedra Alta (Sousas)', 'Loteamento Residencial Vila Bella Dom Pedro', 'Loteamento e Arruamento TELESP', 'Nova Campinas', 'Novo Taquaral', 'Núcleo Residencial Bairro da Vitória', 'Núcleo Residencial Getúlio Vargas', 'Núcleo Residencial Guararapes', 'Núcleo Residencial Paranapanema', 'Núcleo Residencial Parque Família', 'Parque Brasília', 'Parque Imperador', 'Parque Industrial', 'Parque Itália', 'Parque Jambeiro', 'Parque Residencial Caiapó', 'Parque Residencial Vila União', 'Parque Rural Fazenda Santa Cândida', 'Parque São Jorge', 'Parque Taquaral', 'Parque Via Norte', 'Parque da Figueira', 'Parque da Hípica', 'Parque das Constelações', 'Parque das Quaresmeiras', 'Parque das Universidades', 'Parque dos Jacarandás', 'Ponte Preta', 'Real Parque', 'Residencial Cittá Di Firenze', 'Residencial Cittá di Salerno', 'Residencial Jatibela', 'Residencial Moradas do Valle', 'Residencial Nova Bandeirante', 'Residencial Parque da Fazenda', 'Residencial São José', 'Residencial Terras do Barão', 'Residencial Vila Park', 'Rosália', 'Sousas', 'Swiss Park', 'São Bernardo', 'Taquaral', 'Terminal Intermodal de Cargas (TIC)', 'Vila Campos Sales', 'Vila Castelo Branco', 'Vila Eliza', 'Vila Estanislau', 'Vila Formosa', 'Vila Industrial', 'Vila Joaquim Inácio', 'Vila João Jorge', 'Vila Lemos', 'Vila Nogueira', 'Vila Nova', 'Vila Orozimbo Maia', 'Vila Padre Manoel de Nóbrega', 'Vila Palmeiras I', 'Vila Palmeiras II', 'Vila Proost de Souza', 'Vila Satúrnia', 'Vila Trinta e Um de Março', 'Village Campinas', 'Ville Sainte Hélène']

def slot_value_itens_pedido():
    global pizzas_disponiveis

    total = 1+int(random.random()*3)

    pedido = []
    for _ in range(total):

        if random.random()<0.7:
            p1 = random.choice(pizzas_disponiveis)

            p1 = f"{int(1+random.random()*2)} {p1}"


            pedido.append(p1)

        else:
            p1 = random.choice(pizzas_disponiveis)
            p2 = random.choice(pizzas_disponiveis)
            while p2==p1:
                p2 = random.choice(pizzas_disponiveis)
            
            pedido.append(f"Meia {p1} e meia {p2}")

    pedido = " ; ".join(pedido)
    return pedido


def slot_value_valor_total_pedido():
    v1 = 50+int(random.random()*90)
    v2 = int(random.random()*99)
    if v2<10:
        v2 = f"0{v2}"
    return f"R$ {v1},{v2}"

def slot_value_endereco(): # resumo de https://github.com/joke2k/faker/blob/master/faker/providers/address/pt_BR/__init__.py
    v = random.choice(list_bairros)

    v += f" Número {int(random.random()*1000)}"

    if random.random()<0.10:
        v += f" Apartamento {int(random.random()*1000)}"

    return v

def slot_troco():
    if random.random()<0.4:
        return "Não precisa de troco"
    
    v = None
    if random.random()<0.5:
        v = "150,00"
    else:
        v = "200,00"
    return f"Troco para R$ {v}"


def slot_tempo_preparo():
    ts = ["30 minutos", "60 minutos", "1 hora", "2 horas"]

    return random.choice(ts)

def slot_chave_pix():
    tipo = random.choice(["cpf", "cnpj", "telefone", "aleatória"])

    chave = ""
    if tipo=="cpf": # xxx.xxx.xxx-xx

        while len(chave)<13:
            chave += str(int(random.random()*10))
        
            if len(chave)==3 or len(chave)==6:
                chave += "."
            
            if len(chave)==9:
                chave+= "-"
        chave = "CPF "+chave
    
    if tipo=="cnpj": # xx.xxx.xxx/xxxx-xx
        while len(chave)<18:
            chave += str(int(random.random()*10))
            if len(chave)==2 or len(chave)==6:
                chave += "."
            if len(chave)==15:
                chave+= "-"
            if len(chave)==10:
                chave+= "/"
        chave = "CNPJ "+chave

    if tipo=="telefone": # xxxx-xxxx
        while len(chave)<9:
            chave += str(int(random.random()*10))
            if len(chave)==4:
                chave+= "-"
        chave = "Telefone "+chave
    
    if tipo=="aleatória": # dbbf965d-677c-49ff-b9da-5131da1505f3
        lst = [random.choice(list((string.ascii_letters[0:6] + string.digits))) for n in range(36)]
        chave = "".join(lst)
        chave = f"Aleatória {chave[0:8]}-{chave[9:13]}-{chave[14:18]}-{chave[19:23]}-{chave[24:]}"

    return chave 

def slot_sabores_disponiveis():
    global pizzas_disponiveis
    p = pizzas_disponiveis
    p = '\n'.join(p)
    return p

value_slot = {
    "[valor_total_pedido]": slot_value_valor_total_pedido,
    "[itens_pedido]": slot_value_itens_pedido,
    "[endereco]": slot_value_endereco,
    "[sabores_disponiveis]": slot_sabores_disponiveis,
    "[chave_pix]": slot_chave_pix,
    "[troco]": slot_troco,
    "[tempo_preparo]": slot_tempo_preparo,
}

def create(atual="A", end="X"):
    steps = []
    while atual!=end:
        steps.append(atual)
        next = stories_generator.stories[atual]
        atual = np.random.choice(list(next.keys()), p=list(next.values()))
    
    steps.append(end)
    return steps


def states_to_dialogue(states):
    talk = []
    cliente_talk = []
    sistema_talk = []

    for estado in states:
        t = stories_generator.examples[estado]

        for key in value_slot.keys():
            if key in t:
                val = value_slot[key]()
                t = t.replace(key, val)
                
        talk.append(t)
        if t[0:9]=="[Cliente]":
            cliente_talk.append(t)
        elif t[0:9]=="[Sistema]":
            sistema_talk.append(t)
    
    return talk, cliente_talk, sistema_talk


steps_lens = []
steps = []
for i in range(1000):
    flow = create(atual="A", end="X")
    steps_lens.append(len(flow))
    steps.append(flow)

print("Total", len(steps), "Min", min(steps_lens), "Max", max(steps_lens), "Média", sum(steps_lens)/len(steps_lens), "<20", len([f for f in steps_lens if f<20]), ">40", len([f for f in steps_lens if f>40]))

cont = 0
for st in steps:

    talk, cliente_talk, sistema_talk = states_to_dialogue(st)

    with open(f"{cont}.txt", "w") as f:
        for t in talk:
            f.write(t+"\n")

    cont += 1