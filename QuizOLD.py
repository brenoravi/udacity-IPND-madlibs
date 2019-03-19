# encoding: utf-8

# Jogo Enigma Dilmático

# Atribui as perguntas e respostas do jogo as variaveis

# Nível fácil

q_facil = '''Não vamos _1_ uma _2_. Vamos deixar a meta aberta
             , mas quando _3_ a meta, vamos _4_ a meta.'''

r_facil = ['colocar', 'meta', 'atingirmos', 'dobrar']

# Nível intermediário

q_intermediario = '''Se hoje é dia das crianças, ontem eu disse que _1_s...
                     O dia da _1_ é dia da mãe, do pai e das professoras,
                     mas também é o dia dos _2_s. Sempre que você ilhar uma _1_,
                     há sempre uma _3_ oculta, que é um _4_ atrás, o que é algo muito importante.'''

r_intermediario = ['Criança', 'animais', 'figura', 'cachorro']

# Nível avançado

q_avancado = '''Eu acho que a importancia da _1_ é justamente essa, o simbolo da capacidade que nos distingue como...
            Nós somos do gênero _2_, da espécie _3_. Então, para mim essa _1_ é um simbolo da nossa _4_.
            Quandos nós criamos uma _1_ dessas, nós nos transformamos em homo _3_ ou mulheres _3_'''

r_avancado = ['bola', 'humano', 'sapiens', 'evolução']


def level():
    level_opcoes = ['facil', 'intermediario', 'avancado']
    level_escolhido = raw_input(
        "Escolha o nível de dificuldade desejado!"
        "\n"
        "Fácil, intermediário ou difícil"
        "\n").lower()
    while level_escolhido not in level_opcoes:
        level_escolhido = raw_input(
            "Esta não é uma opção válida!"
            "\n"
            "Níveis disponíveis fácil, intermediário, e avançado."
            "\n").lower()
    print "Você escolheu " + level_escolhido + "!" + "\n"
    if level_escolhido == ('facil' or "fácil"):
        frase = q_facil
        resposta = r_facil
    elif level_escolhido == 'intermediário' or 'intermediario':
        frase = q_intermediario
        resposta = r_intermediario
    elif level_escolhido == 'avancado' or 'avançado':
        frase = q_avancado
        resposta = r_avancado
    else:
        return 'Fracasso! #101'
    return frase, resposta

# Define as dificuldades disponíveis no jogo


# Define os críterios de chances
def chances():
    quant_chances = [2, 3, 4, 5]
    chances_restantes = raw_input(
        "\n"
        "Quantas chances até você falhar miseravelmente ? "
        "\n").lower()
    while int(chances_restantes) not in quant_chances:
        chances_restantes = raw_input(
            "Digite um número entre 2 e 5."
            "\n"
            "Quantas chances até você falhar miseravelmente ? "
            "\n").lower()
    print "Você possui " + chances_restantes + " chances."
    return chances_restantes

# word_in_pos
# input: Jogador escolhe, lista respostas possíveis


def word_in_pos(escolha, resposta, n):
    if escolha == resposta[n]:
        return resposta
    else:
        return None


# play_game

def jogar():
    texto, resposta = level()
    chances_restantes = chances()
    replaced = []
    vazio = ["_1_", "_2_", "_3_", "_4_"]
    index = 0
    avancar_index = 1
    vazio_total = 4
    chances_sem = 0
    chance_perdida = 1
    chance_ultima = 1

    while chances_restantes > chances_sem and index < vazio_total:
        vazio_index = vazio[index]
        print "O parágrafo atual é:" + "\n"
        print texto + "\n"
        escolha = raw_input(
            "O que será substituido pela palavra " +
            vazio_index +
            "? ").lower()
        if word_in_pos(escolha, resposta, index):
            print "Correto!" + "\n"
            texto = texto.split()
            for word in texto:
                if vazio_index in word:
                    word = word.replace(vazio_index, resposta)
                replaced.append(word)
            texto = " ".join(replaced)
            replaced = []
            index += avancar_index
            if index == vazio_total:
                print texto
                return "\n Você decifrou o enigma!"
        else:
            chances_restantes = int(chances_restantes) - chance_perdida
            if chances_restantes > chance_ultima:
                print ("ERRRRRRRRROU! Tente novamente;"
                       " Você tem " + str(chances_restantes) + " chances!" + ""
                                                                             "\n")
            elif chances_restantes == chance_ultima:
                print ("ERRRRRRRRROU! Tente novamente;"
                       " Você tem " + str(chance_ultima) +
                       " chance! JUST DO IT !" +
                       "\n")
            elif chances_restantes == chances_sem:
                return "\n Você perdeu!"
            else:
                return "Fracasso! 101"


status = "sim"
novo_jogo = "Quer jogar novamente? (Sim ou Não)"

while status == 'sim':
    print jogar()
    status = raw_input(novo_jogo)
    while status not in ["sim", "não"]:
        status = raw_input(novo_jogo)
    if status == "sim":
        print "Booora!"
    else:
        print "Obrigado por jogar!"

print jogar()
