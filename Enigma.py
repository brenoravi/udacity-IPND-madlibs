# encoding: utf-8

# Enigma Rousseff

# Define variáveis que armazenam as mensagens apresentadas ao jogador

mensagem_boasvindas = """-------------------------------------------------
| Bem-vindo ao Enigma Rousseff!                 |
-------------------------------------------------"""

mensagem_desistiu = 'Você desistiu do desafio!'

mensagem_fimdojogo = 'Você decifrou o enigma Rousseff!'

mensagem_dificuldade = "Escolha a dificuldade (Fácil, Intermediário, ou Avançado):"

mensagem_jogarnovamente = "Gostaria de jogar novamente (sim ou não):"

resposta_invalida = "Resposta inválida!"

resposta_errou = "Errroooooooooou, tente novamente."

resposta_certa = "Acertou!"


# Nível fácil
frase_iniciante = '''Não vamos _1_ uma _2_. Vamos deixar a meta aberta
             , mas quando _3_ a meta, vamos _4_ a meta.'''

lacunas_iniciante = ["_1_", "_2_", "_3_", "_4_"]
resposta_iniciante = ['Colocar', 'Meta', 'Atingirmos', 'Dobrar']


# Nível intermediário
frase_intermediario = '''Se hoje é dia das crianças, ontem eu disse que _1_s...
                     O dia da _1_ é dia da mãe, do pai e das professoras,
                     mas também é o dia dos _2_s. Sempre que você ilhar uma _1_,
                     há sempre uma _3_ oculta, que é um _4_ atrás, o que é algo muito importante.'''

lacunas_intermediario = ["_1_", "_2_", "_3_", "_4_"]
resposta_intermediario = ['Criança', 'Animais', 'Figura', 'Cachorro']


# Nível avançado
frase_avancado = '''Eu acho que a importancia da _1_ é justamente essa, o simbolo da capacidade que nos distingue como...
            Nós somos do gênero _2_, da espécie _3_. Então, para mim essa _1_ é um simbolo da nossa _4_.
            Quandos nós criamos uma _1_ dessas, nós nos transformamos em homo _3_ ou mulheres _3_'''

lacunas_avancado = ["_1_", "_2_", "_3_", "_4_"]
resposta_avancado = ['Bola', 'Humano', 'Sapiens', 'Evolução']


# Valida se o jogador respondeu corretamente
def valida_resposta(jogador_resposta, resposta_correta):

    if jogador_resposta == resposta_correta:

        print '\n' + resposta_correta + '\n'
        return True
    else:
        print '\n' + resposta_errou + '\n'
        return False


# Pergunta o próximo passo ao jogador e valida a resposta usando função valida_resposta
def jogo(paragrafo, lacuna, resposta):

    print '\n' + mensagem_boasvindas

    for index in range(len(lacuna)):
        if lacuna[index] in paragrafo:
            jogador_resposta = raw_input('\n' + "Qual a palavra que completa o campo " + lacuna[index] + "?").lower()
            if valida_resposta(jogador_resposta, resposta) is True:
                paragrafo = paragrafo.replace(lacuna[index], jogador_resposta)
                print paragrafo
        print index

    print '\n' + mensagem_fimdojogo + '\n'

    return repeat()


# Pergunta se o jogador gostaria de jogar novamente, e executa novamente o quiz caso deseje jogar
def repeat():

    jogador_input = raw_input(mensagem_jogarnovamente).lower()

    if jogador_input == ("sim" or "s"):
        return game_on()
    elif jogador_input == ("não" or "nao"):
        print '\n' + mensagem_desistiu + '\n'
        exit()
    else:
        print '\n' + resposta_invalida + '\n'
        return repeat()


# Pergunta o jogador qual o nível de dificuldade escolhido
def game_on():

    print mensagem_boasvindas + '\n'

    jogador_input = raw_input("Escolha a dificuldade (Fácil, Intermediário, ou Avançado):").lower()

    if jogador_input == ("facil" or "fácil"):
        return jogo(frase_iniciante, lacunas_iniciante, resposta_iniciante)
    elif jogador_input == ("intermediario" or "intermediário"):
        return jogo(frase_intermediario, lacunas_intermediario, resposta_intermediario)
    elif jogador_input == ("avancado" or "avançado"):
        return jogo(frase_avancado, lacunas_avancado, resposta_avancado)
    else:
        print '\n' + mensagem_dificuldade
        return game_on()


game_on()
