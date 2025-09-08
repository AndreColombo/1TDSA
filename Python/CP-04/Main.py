#Import dos módulos:
    #random: gera números aleatórios para simular I.A.
    #time: gera delays pelo código para fornecer fluidez durante a jogatina
import random, time

# Função para ver as regras e mecânicas do jogo
def regras():
    print(
        "\n🌊⚓════════════════════════════════════════════════════════⚓🌊\n\n"
        "📜 REGRAS DA BATALHA NAVAL 📜\n\n"
        "🗺️  O jogo acontece em um tabuleiro 2D.\n"
        "⚔️  Batalha Naval é um clássico jogo de estratégia.\n"
        "🎯  Seu objetivo: afundar os navios inimigos antes que eles afundem os seus!\n"
        "📐  Escolha o tamanho do mapa: 4x4 ou 6x6.\n"
        "🚢  Posicione os navios manualmente ou de forma aleatória.\n\n"
        "📌 Limite de navios por tamanho de mapa:\n\n"
        "\t🚢-----------------------------------------------🚢\n"
        "\t|   Tipo de Navio   |   4x4   |   5x5   |   6x6   |\n"
        "\t🚢-----------------------------------------------🚢\n"
        "\t| ⚔️ Destroier      |    2    |    1    |    2    |\n"
        "\t| 🌊 Submarino      |    1    |    1    |    1    |\n"
        "\t| 🏴‍☠️ Cruzador       |    -    |    1    |    1    |\n"
        "\t| 🛡️ Encouraçado    |    -    |    1    |    2    |\n"
        "\t🚢-----------------------------------------------🚢\n"
        "\n🌊⚓════════════════════════════════════════════════════════⚓🌊\n"
    )



def introducao():
    time.sleep(1.25)
    print(
        "\n🌊⚓~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~⚓🌊\n\n"
        "      🚢  Bem-vindos à grande aventura: BATALHA NAVAL ANJOPE  🚢\n"
        "                      💻 Desenvolvido por:\n"
        "    👨‍💻 André Colombo | 👨‍💻 José Diogo | 👨‍💻 Pedro Miranda\n"
        "\n🌊⚓~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~⚓🌊\n\n"
        "📜 Antes de começar a jogar, deseja ver as Regras? (S/N)"
    )

    time.sleep(0.75)
    ver_regras = input("👉 S - Sim | N - Não: ").lower()
    time.sleep(1)

    #Checa se a resposta foi alguma variação de "sim"
    if ver_regras in ["sim", "s", "si", "yes", "ye", "y"]:
        time.sleep(0.5)
        regras()
    #se não foi, começa a partida
    else:
        print(
            "\n🌊⚓~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~⚓🌊\n\n"
            "➡️  Então vamos continuar a aventura, Capitão! 🚢🔥\n"
            "\n🌊⚓~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~⚓🌊\n"
        )


#Uma espécie de dicionário dos possíveis valores na matriz_partida
# SIGNIFICADO IDENTIFICADORES
# 0 — Água — 🌊
# 1 — Submarino — 🚢
# 2 — Destróier — 🚢
# 3 — Cruzador — 🚢
# 4 — Encouraçado — 🚢
# 5 — Ataque bem-sucedido — 💥
# 6 — Ataque mal-sucedido — ❌

identificadores_navios = {
    "Submarino": {"Identificador": 1, "Tamanho": 1},
    "Destróier": {"Identificador": 2, "Tamanho": 2},
    "Cruzador": {"Identificador": 3, "Tamanho": 3},
    "Encouraçado": {"Identificador": 4, "Tamanho": 4},
}

#Inicialização das listas de "memória" da Inteligência Artificial
lista_prioridades_inteligencia_artificial = []
lista_ignorar_inteligencia_artificial = []


# Função para escolher o tamanho do mapa
def escolher_mapa():
    print(
    "\n🌊⚓═══════════════════════════════════════════════⚓🌊\n\n"
    "🗺️  Escolha o tamanho do mapa desejado:\n\n"
    "  1 — Pequeno  (4x4)\n"
    "  2 — Médio    (5x5)\n"
    "  3 — Grande   (6x6)\n"
    "\n🌊⚓═══════════════════════════════════════════════⚓🌊\n"
)
    # Variável para controladora do WHILE da escolha de mapa.
    verificar = 0
    while verificar == 0:
        tamanho_mapa = int(input("👉 Digite sua escolha, Capitão: "))
        time.sleep(0.75)
        match tamanho_mapa:
            case 1:
                print(
                    "\n🌊⚓═══════════════════════════════════════════════⚓🌊\n\n"
                    "✅ Você escolheu o mapa: 🗺️  Pequeno (4x4)! 🚢\n"
                    "Prepare-se para a batalha, Capitão! ⚔️🔥\n"
                    "\n🌊⚓═══════════════════════════════════════════════⚓🌊\n"
                )
                return 1
            case 2:
                print(
                    "\n🌊⚓═══════════════════════════════════════════════⚓🌊\n\n"
                    "✅ Você escolheu o mapa: 🗺️  Médio (5x5)! ⚓\n"
                    "As águas estão ficando perigosas... mantenha-se atento, Capitão! 🌊👀\n"
                    "\n🌊⚓═══════════════════════════════════════════════⚓🌊\n"
                )
                return 2
            case 3:
                print(
                    "\n🌊⚓═══════════════════════════════════════════════⚓🌊\n\n"
                    "✅ Você escolheu o mapa: 🗺️  Grande (6x6)! 🐉🚢\n"
                    "Os mares sombrios aguardam sua coragem... 🌑⚔️\n"
                    "A batalha final está prestes a começar, Capitão! 🔥\n"
                    "\n🌊⚓═══════════════════════════════════════════════⚓🌊\n"
                )
                return 3
            case _:
                print(
                    "\n🌊⚓═══════════════════════════════════════════════⚓🌊\n\n"
                    "❌ Valor inválido, Capitão! Escolha apenas entre 1, 2 ou 3! ⚓\n"
                    "Tente novamente e prepare-se para a aventura! 🚢🔥\n"
                    "\n🌊⚓═══════════════════════════════════════════════⚓🌊\n"
                )
                verificar = 0
    time.sleep(1)


def preparar_mapas(tamanho_mapa):
    #DICIONÁRIO QUE GUARDA OS ESTADOS DO JOGO
        #SUPER IMPORTANTE!!!
    estados_jogo_principal = {
        "matriz_partida_jogador1": [],
        "matriz_partida_jogador2": [],
        "matriz_alvo_jogador1": [],
        "posicoes_navios_jogador1": {},
        "posicoes_navios_jogador2": {},
        "lista_prioridades_ia": [],
        "lista_ignorar_ia": [],
        "numero_submarinos": 0,
        "numero_destroiers": 0,
        "numero_encouracados": 0,
        "numero_cruzadores": 0,
    }

    #DEPENDENDO do TAMANHO do MAPA escolhido, a quantidade de navios é diferente
    if tamanho_mapa == 1:
        estados_jogo_principal["numero_submarinos"] = 1
        estados_jogo_principal["numero_destroiers"] = 2
        estados_jogo_principal["numero_encouracados"] = 0
        estados_jogo_principal["numero_cruzadores"] = 0

        #4x4
        estados_jogo_principal["matriz_partida_jogador1"] = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
        ]
        estados_jogo_principal["matriz_partida_jogador2"] = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
        ]
        estados_jogo_principal["matriz_alvo_jogador1"] = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
        ]
    elif tamanho_mapa == 2:
        estados_jogo_principal["numero_submarinos"] = 1
        estados_jogo_principal["numero_destroiers"] = 1
        estados_jogo_principal["numero_encouracados"] = 1
        estados_jogo_principal["numero_cruzadores"] = 1

        #5x5
        estados_jogo_principal["matriz_partida_jogador1"] = [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
        ]
        estados_jogo_principal["matriz_partida_jogador2"] = [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
        ]
        estados_jogo_principal["matriz_alvo_jogador1"] = [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
        ]
    elif tamanho_mapa == 3:
        estados_jogo_principal["numero_submarinos"] = 1
        estados_jogo_principal["numero_destroiers"] = 2
        estados_jogo_principal["numero_encouracados"] = 2
        estados_jogo_principal["numero_cruzadores"] = 1

        #6x6
        estados_jogo_principal["matriz_partida_jogador1"] = [
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
        ]
        estados_jogo_principal["matriz_partida_jogador2"] = [
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
        ]
        estados_jogo_principal["matriz_alvo_jogador1"] = [
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
        ]

    return estados_jogo_principal

#FUNÇÃO DE PREPARAR OS MAPAS
def preparar_partida(estado_jogo):
    time.sleep(1)
    # Preparemos a posição dos navios da Inteligência Artificial
        # Como parâmetros, passaremos as quantidades de cada navio e o dicionário que guarda os estados do jogo
    gerar_navios_inimigo_artificial(
        estado_jogo["numero_submarinos"],
        estado_jogo["numero_encouracados"],
        estado_jogo["numero_destroiers"],
        estado_jogo["numero_cruzadores"],
        estado_jogo,
    )
    time.sleep(0.75)
    print(
        "⚓👾 O adversário posicionou seus navios no tabuleiro! 🚢\n"
        "Prepare-se para a batalha, Capitão! ⚔️🔥\n"
        "\n🌊⚓═══════════════════════════════════════════════⚓🌊\n"
    )
    time.sleep(1.5)

    print(
        "🚢⚓ É a nossa vez de posicionar os navios, Capitão! 🗺️\n"
        "Escolha sabiamente suas posições para dominar os mares! 🌊🔥\n"
        "\n🌊⚓═══════════════════════════════════════════════⚓🌊\n"
    )
    time.sleep(1.75)

    # Preparemos a posição dos navios do Jogador
        # Como parâmetros, passaremos as quantidades de cada navio e o dicionário que guarda os estados do jogo
    gerar_navios_escolha(
        estado_jogo["numero_submarinos"],
        estado_jogo["numero_encouracados"],
        estado_jogo["numero_destroiers"],
        estado_jogo["numero_cruzadores"],
        estado_jogo,
    )


def gerar_navios_escolha(submarinos, encouracados, destroiers, cruzadores, estado_jogo):
    """
    —————————————— LÓGICA DA FUNÇÃO ——————————————
    XX Pegar a quantidade de navios
    XX Em ordem, tornar a escolha das posições dos navios para o usuario, clara
    XX Pedir para o usuário escolher a posição inicial do navio atual
    XX Checar os lados para os quais o usuario poderá posicionar o resto do navio
    XX Pedir o lado para qual o navio será colocado
    XX Posicionar o navio na matriz do jogador
    """

    # Inicializando dicionário que ditará o número de navios presentes no mapa, baseando-se no tamanho escolhido
    lista_navios_para_adicionar = {}

    #se o número de qualquer navio for maior que 0, ele estará presente
    if submarinos > 0:
        lista_navios_para_adicionar["Submarino"] = submarinos
    if encouracados > 0:
        lista_navios_para_adicionar["Encouraçado"] = encouracados
    if destroiers > 0:
        lista_navios_para_adicionar["Destróier"] = destroiers
    if cruzadores > 0:
        lista_navios_para_adicionar["Cruzador"] = cruzadores

    print(
        "\n🌊⚓═══════════════════════════════════════════════⚓🌊\n"
        "🗺️🌊 O mapa da batalha será exibido assim, Capitão! 🚢⚔️\n"
        "Prepare-se para a estratégia final nos mares! 🌊🔥\n"
        "\n🌊⚓═══════════════════════════════════════════════⚓🌊\n"
    )
    time.sleep(0.5)

    # Desenharemos o mapa atual da frota
    desenhar_mapa_jogador(estado_jogo["matriz_partida_jogador1"])

    # Iteraremos sobre todos os navios que devemos adicionar
    for navio in lista_navios_para_adicionar:

        # Enquanto houver navios que devem ser posicionados, na iteração atual, o loop acontecerá
        while lista_navios_para_adicionar[navio] > 0:
            # Variável de controle do WHILE sobre posição válida
            posicao_valida = False
            # Enquanto o navio não for posicionado numa posição válida, o jogador deverá tentar novamente
            while not posicao_valida:
                # Try para o valor inserido pelo Jogador ser um valor válido
                try:
                    time.sleep(0.5)

                    # INPUTS
                    posicao_inicial_linha = int(
                        input(
                            f"🧭 Capitão, insira a linha inicial para posicionar o navio: {navio} 🚢 "
                            f"(1 a {len(estado_jogo['matriz_partida_jogador1'])}): "
                        )
                    )
                    posicao_inicial_coluna = int(
                        input(
                            f"🧭 Capitão, agora insira a coluna inicial para posicionar o navio: {navio} 🚢 "
                            f"(1 a {len(estado_jogo['matriz_partida_jogador1'][0])}): "
                        )
                    )

                # Qualquer tipo de erro relacionado ào input e seu casting
                except:
                    print(
                        "\n❌ Valor inválido, Capitão! Por favor, insira um número válido ⚓🚢\n"
                        "🧭 Use os instrumentos de navegação corretamente e tente novamente! 🌊🔥\n"
                    )

                # Se a escolha do jogador for menor 1 ou maior que o tamanho vertical da matriz (fora de limites)
                if posicao_inicial_linha < 1 or posicao_inicial_linha > len(
                    estado_jogo["matriz_partida_jogador1"]
                ):
                    time.sleep(1)
                    print(
                        f"❌ Linha inválida, Capitão! ⚓🚢 "
                        f"Por favor selecione uma posição entre 1 e {len(estado_jogo['matriz_partida_jogador1'])} 🧭🌊\n"
                    )

                    # Tentar novamente
                    continue

                # Se a escolha do jogador for menor 1 ou maior que o tamanho horizontal da matriz (fora de limites)
                if posicao_inicial_coluna < 1 or posicao_inicial_coluna > len(
                    estado_jogo["matriz_partida_jogador1"][0]
                ):
                    time.sleep(1)
                    print(
                        f"❌ Coluna inválida, Capitão! ⚓🚢 "
                        f"Por favor selecione uma posição entre 1 e {len(estado_jogo['matriz_partida_jogador1'][0])} 🧭🌊\n"
                    )

                    # Tentar novamente
                    continue


                posicao_inicial_linha -= 1  # listas começam do zero
                posicao_inicial_coluna -= 1  # listas começam do zero

                # Se a posição selecionada pelo jogador não for um quadrado vazio (água)
                if (
                    not estado_jogo["matriz_partida_jogador1"][posicao_inicial_linha][
                        posicao_inicial_coluna
                    ]
                    == 0
                ):
                    time.sleep(1)
                    print(
                        "❌ Posição inválida, Capitão! ⚓🚢 "
                        "Já há um navio nessa posição! 🧭🌊 Tente novamente e mantenha a frota segura!\n"
                    )

                    # Tentar novamente
                    continue

                # Se a posição selecionada pelo jogador não for um Submarino
                    # ~submarinos ocupam só um quadrado, logo não precisam de espaço para expandir~
                if not navio == "Submarino":
                    # e não tiver possibilidade de expansão pela matriz
                    if not pode_expandir(
                        [posicao_inicial_linha, posicao_inicial_coluna],
                        navio,
                        estado_jogo,
                    ):
                        time.sleep(1)
                        print(
                            "❌ Espaço insuficiente, Capitão! ⚓🚢 "
                            "O navio não cabe nessa posição! 🧭🌊 Reavalie sua estratégia e tente novamente!\n"
                        )

                        # Tentar novamente
                        continue

                # Tenta posicionar o navio
                    # Se conseguir, retorna True
                if verificar_e_posicionar_navio(
                    [posicao_inicial_linha, posicao_inicial_coluna], navio, estado_jogo
                ):
                    # Utiliza a variável de controle para finalizar o looping (mais uma precaução, pois usamos o break)
                    posicao_valida = True
                    break
                else:
                    # Se falharmos no posicionamento de navios, tentaremos novamente
                    continue
            # O navio foi posicionado com sucesso, logo um a menos na lista de posicionamentos
            lista_navios_para_adicionar[navio] -= 1
            time.sleep(0.75)
            print(
                "\n✅ Navio posicionado com sucesso, Capitão! ⚓🚢\n"
                "A frota está se fortalecendo! 🌊🔥\n"
            )
            time.sleep(0.5)

            # Desenha a matriz com o navio já posicionado
            desenhar_mapa_jogador(estado_jogo["matriz_partida_jogador1"])

# Função para checar se há algum lado para expandir o navio
def pode_expandir(posicao_inicial, navio, estado_jogo):
    # Se o navio for um Submarino, não é necessário expandi-lo
    if navio == "Submarino":
        # Retorna sucesso
        return True

    # Utilizamos o dicionário de identificadores para sabermos o tamanho, em quadrados, do navio
    tamanho_navio = identificadores_navios[navio]["Tamanho"]

    # Variáveis de ""controle"", saberemos por que usamos elas no final
    pode_expandir_cima = True
    pode_expandir_baixo = True
    pode_expandir_esquerda = True
    pode_expandir_direita = True

    # CHECA OS CANTOS PRA VER SE NÃO ESTÁ EM ALGUMA PAREDE
        # TAMBÉM CHECA SE TEM ALGUM CAMINHO SEM NAVIOS
    if (posicao_inicial[0] == 0 or verificar_existencia_navio(
        posicao_inicial, navio, 0, estado_jogo
    ) or (posicao_inicial[0] - tamanho_navio) < 0):
        # Se uma das verificações passar (está na parede ou tem navios na direção)
            # Não poderemos expandir para cima
        pode_expandir_cima = False

    if (posicao_inicial[0] == len(estado_jogo["matriz_partida_jogador1"]) - 1 or
            verificar_existencia_navio(posicao_inicial, navio, 2, estado_jogo) or
                (posicao_inicial[0] + tamanho_navio) >= len(estado_jogo["matriz_partida_jogador1"])):
        # Se uma das verificações passar (está na parede ou tem navios na direção)
            # Não poderemos expandir para baixo
        pode_expandir_baixo = False

    if (posicao_inicial[1] == 0 or
            verificar_existencia_navio(posicao_inicial, navio, 3, estado_jogo) or
                (posicao_inicial[1] - tamanho_navio) < 0):
        # Se uma das verificações passar (está na parede ou tem navios na direção)
            # Não poderemos expandir para a esquerda
        pode_expandir_esquerda = False

    if (posicao_inicial[1] == len(estado_jogo["matriz_partida_jogador1"][0]) - 1 or
            verificar_existencia_navio(posicao_inicial, navio, 1, estado_jogo) or
                (posicao_inicial[1] + tamanho_navio) >= len(estado_jogo["matriz_partida_jogador1"])):
        # Se uma das verificações passar (está na parede ou tem navios na direção)
            # Não poderemos expandir para a direita
        pode_expandir_direita = False

    # Caso venha ser necessário debuggar essa função
    #print(f"POSSO EXPANDIR CIMA?: {pode_expandir_cima}")
    #print(f"POSSO EXPANDIR BAIXO?: {pode_expandir_baixo}")
    #print(f"POSSO EXPANDIR ESQUERDA?: {pode_expandir_esquerda}")
    #print(f"POSSO EXPANDIR DIREITA?: {pode_expandir_direita}")

    # Se pudermos expandir para qualquer um dos lados, retorne True
    if (
        pode_expandir_cima
        or pode_expandir_baixo
        or pode_expandir_esquerda
        or pode_expandir_direita
    ):
        #print("RETORNEI TRUE")
        return True
    # Caso contrário, retorne False
    else:
        #print("RETORNEI FALSE")
        return False

# Função para verificarmos as possibilidades de expansão e, se possível, posicionarmos o navio
def verificar_e_posicionar_navio(posicao_inicial, navio, estado_jogo):
    # Se o navio for um submarino (precisa só de 1 quadrado) E
        # A posição selecionada for um quadrado vazio (só com água)
    if (
        navio == "Submarino"
        and estado_jogo["matriz_partida_jogador1"][posicao_inicial[0]][
            posicao_inicial[1]
        ]
        == 0
    ):
        # Salve na lista de posições da frota do jogador 1 um novo navio
            # Nesse novo navio, teremos o seu tipo e os quadrados que ele ocupa
        estado_jogo["posicoes_navios_jogador1"][
            f"Navio_{len(estado_jogo['posicoes_navios_jogador1']) + 1}"
        ] = {"Tipo_Navio": navio, "Posicoes": [posicao_inicial]}
        # Posicionaremos o navio na matriz da frota do jogador 1
        posicionar_navio(posicao_inicial, navio, 0, estado_jogo)
        # Retorne que o posicionamento foi um sucesso
        return True

    # O navio é um submarino, mas o quadrado selecionado não estava vazio
    elif navio == "Submarino":
        time.sleep(1)
        print(
            "❌ Capitão! ⚓🚢 Há um navio nessa posição, impossível posicionar o submarino aqui! 🧭🌊\n"
            "Reavalie a estratégia e escolha uma posição segura para sua frota! ⚔️🔥\n"
        )
        # Retorne que o posicionamento foi um fracasso
        return False

    # Utilizamos o dicionário de identificadores para sabermos o tamanho, em quadrados, do navio
    quantidade_posicoes = identificadores_navios[navio]["Tamanho"]

    # Se não pudermos expandir para nenhuma direção
    if not pode_expandir(posicao_inicial, navio, estado_jogo):
        time.sleep(2)
        print(
            f"❌ Capitão! ⚓🚢 O {navio} não pode ser posicionado aqui, "
            "pois não há espaço suficiente em nenhuma direção! 🧭🌊\n"
            "Reavalie sua estratégia e escolha outro local seguro para a frota! ⚔️🔥\n"
        )
        # Retorne que o posicionamento foi um fracasso
        return False

    # Variáveis de ""controle"". Uso idêntico ào da função pode_expandir()
    pode_mover_cima = True
    pode_mover_baixo = True
    pode_mover_esquerda = True
    pode_mover_direita = True

    # Se a posição Y selecionada, menos a quantidade de quadrados que o navio ocupa (exceto o quadrado inicial),
         #estiver fora da matriz OU há navios no caminho
    if posicao_inicial[0] - (quantidade_posicoes - 1) < 0 or verificar_existencia_navio(
        posicao_inicial, navio, 0, estado_jogo
    ):
        # Não poderá direcionar o navio para cima
        pode_mover_cima = False

    # Se a posição Y selecionada, mais a quantidade de quadrados que o navio ocupa (exceto o quadrado inicial),
        # estiver fora da matriz OU há navios no caminho
    if posicao_inicial[0] + (quantidade_posicoes - 1) >= (
        len(estado_jogo["matriz_partida_jogador1"])
    ) or verificar_existencia_navio(posicao_inicial, navio, 2, estado_jogo):
        # Não poderá direcionar o navio para baixo
        pode_mover_baixo = False

    # Se a posição X selecionada, menos a quantidade de quadrados que o navio ocupa (exceto o quadrado inicial),
        # estiver fora da matriz OU há navios no caminho
    if posicao_inicial[1] - (quantidade_posicoes - 1) < 0 or verificar_existencia_navio(
        posicao_inicial, navio, 3, estado_jogo
    ):
        # Não poderá direcionar o navio para a esquerda
        pode_mover_esquerda = False

    # Se a posição X selecionada, mais a quantidade de quadrados que o navio ocupa (exceto o quadrado inicial),
        # estiver fora da matriz OU há navios no caminho
    if posicao_inicial[1] - (quantidade_posicoes - 1) > (
        len(estado_jogo["matriz_partida_jogador1"])
    ) or verificar_existencia_navio(posicao_inicial, navio, 1, estado_jogo):
        # Não poderá direcionar o navio para a direita
        pode_mover_direita = False

    # String das opções guardada numa variável antes de ser mostrada
    escolher_direcao_pergunta = (
        "\n🧭 Capitão, escolha a direção para posicionar seu navio 🚢:\n\n"
    )
    # Checa as direções na qual o navio pode ser expandido, e adiciona-as na listagem
    if pode_mover_cima:
        escolher_direcao_pergunta += "1 — Cima ↑\n"
    if pode_mover_direita:
        escolher_direcao_pergunta += "2 — Direita →\n"
    if pode_mover_baixo:
        escolher_direcao_pergunta += "3 — Baixo ↓\n"
    if pode_mover_esquerda:
        escolher_direcao_pergunta += "4 — Esquerda ←\n"

    # Variável de controle do WHILE de seleção de direção
    direcao_valida = False
    while not direcao_valida:
        time.sleep(0.75)
        escolha_direcao = int(input(escolher_direcao_pergunta + "👉 Capitão, escolha a direção do navio 🚢: "))

        # Se a escolha for menor que 1 ou maior que 4, está fora dos limites
        if escolha_direcao < 1 or escolha_direcao > 4:
            time.sleep(1)
            print("❌ Direção inválida, Capitão! ⚓🚢 "
                    "Escolha uma direção correta para o navio e tente novamente!\n")

            # Tente novamente
            continue

        # Se escolheu cima e não pode mover para cima
        if escolha_direcao == 1 and not pode_mover_cima:
            time.sleep(1)
            print(
                "❌ Capitão! Não há espaço para posicionar o navio para cima. ⬆️🧭🌊\n"
                "Reavalie a estratégia e escolha outra direção segura para a frota! ⚔️🔥\n"
            )

            # Tente novamente
            continue

        # Se escolheu direita e não pode mover para a direita
        if escolha_direcao == 2 and not pode_mover_direita:
            time.sleep(1)
            print(
                "❌ Capitão! Não há espaço para posicionar o navio para a direita ➡️🧭🌊\n"
                "Reavalie a estratégia e escolha outra direção segura para a frota! ⚔️🔥\n"
            )

            # Tente novamente
            continue

        # Se escolheu baixo e não pode mover para baixo
        if escolha_direcao == 3 and not pode_mover_baixo:
            time.sleep(1)
            print(
                "❌ Capitão! Não há espaço para posicionar o navio para baixo ⬇️🧭🌊\n"
                "Reavalie a estratégia e escolha outra direção segura para a frota! ⚔️🔥\n"
            )

            # Tente novamente
            continue

        # Se escolheu esquerda e não pode mover para a esquerda
        if escolha_direcao == 4 and not pode_mover_esquerda:
            time.sleep(1)
            print(
                "❌ Capitão! Não há espaço para posicionar o navio para a esquerda ⬅️🧭🌊\n"
                "Reavalie a estratégia e escolha outra direção segura para a frota! ⚔️🔥\n"
            )

            # Tente novamente
            continue

        # Finalize o WHILE
        direcao_valida = True

    # Posicione o navio na matriz do jogador
    posicionar_navio(posicao_inicial, navio, escolha_direcao - 1, estado_jogo)
    # O POSICIONAMENTO FOI UM SUCESSO
    return True


def verificar_existencia_navio(posicao_inicial, navio, direcao, estado_jogo):
    # Utilizamos o dicionário de identificadores para sabermos o tamanho, em quadrados, do navio
    quantidade_posicoes = identificadores_navios[navio]["Tamanho"]
    """
        DIREÇÕES:
            0 - CIMA
            1 - DIREITA
            2 - BAIXO
            3 - ESQUERDA
    """

    # Tente verificar a existência de um navio numa direção específica
    try:
        # Switch da direção escolhida
        match direcao:
            # Caso for 0 (CIMA)
            case 0:
                # Itere de 1 ao tamanho do navio
                    # Verificaremos quadrado por quadrado
                for pos in range(1, quantidade_posicoes):
                    # Se houver algum quadrado diferente de 0 (água), há um navio
                    if (
                        not estado_jogo["matriz_partida_jogador1"][
                            posicao_inicial[0] - pos
                        ][posicao_inicial[1]]
                        == 0
                    ):

                        # Retorne que há um navio
                        return True

            # Caso for 1 (DIREITA)
            case 1:
                # Itere de 1 ao tamanho do navio
                    # Verificaremos quadrado por quadrado
                for pos in range(1, quantidade_posicoes):
                    # Se houver algum quadrado diferente de 0 (água), há um navio
                    if (
                        not estado_jogo["matriz_partida_jogador1"][posicao_inicial[0]][
                            posicao_inicial[1] + pos
                        ]
                        == 0
                    ):
                        # Retorne que há um navio
                        return True

            # Caso for 2 (BAIXO)
            case 2:
                # Itere de 1 ao tamanho do navio
                    # Verificaremos quadrado por quadrado
                for pos in range(1, quantidade_posicoes):
                    # Se houver algum quadrado diferente de 0 (água), há um navio
                    if (
                        not estado_jogo["matriz_partida_jogador1"][
                            posicao_inicial[0] + pos
                        ][posicao_inicial[1]]
                        == 0
                    ):
                        # Retorne que há um navio
                        return True

            # Caso for 3 (ESQUERDA)
            case 3:
                # Itere de 1 ao tamanho do navio
                    # Verificaremos quadrado por quadrado
                for pos in range(1, quantidade_posicoes):
                    # Se houver algum quadrado diferente de 0 (água), há um navio
                    if (
                        not estado_jogo["matriz_partida_jogador1"][posicao_inicial[0]][
                            posicao_inicial[1] - pos
                        ]
                        == 0
                    ):
                        # Retorne que há um navio
                        return True

        # Caso não haja nenhum navio na direção, retorne que não há nenhum navio
        return False

    # Caso haja um erro que leve a verificação para fora da matriz, retorne que há "um navio", por segurança
    except IndexError:
        return True

# Função para posicionar o navio na matriz do jogador
def posicionar_navio(posicao_inicial, navio, direcao, estado_jogo):
    # A posição inicial do quadrado na matriz é alterada para o identificador do navio a ser posicionado
    estado_jogo["matriz_partida_jogador1"][posicao_inicial[0]][posicao_inicial[1]] = (
        identificadores_navios[navio]["Identificador"]
    )
    """
        DIREÇÕES:
            0 - CIMA
            1 - DIREITA
            2 - BAIXO
            3 - ESQUERDA
    """
    # Se o navio ocupar mais de um quadrado
    if identificadores_navios[navio]["Tamanho"] > 1:
        # Switch da direção escolhida
        match direcao:
            # Caso for 0 (CIMA)
            case 0:
                # Salvaremos as posições do navio selecionado numa lista
                lista_posicoes_navio = [[posicao_inicial[0], posicao_inicial[1]]]

                # Itere de 1 ao tamanho do navio
                    # Posicionaremos quadrado por quadrado
                for pos in range(1, (identificadores_navios[navio]["Tamanho"])):
                    # Cada iteração, subiremos uma linha e mudaremos o identificador na matriz
                    estado_jogo["matriz_partida_jogador1"][posicao_inicial[0] - pos][
                        posicao_inicial[1]
                    ] = identificadores_navios[navio]["Identificador"]

                    # Adicionaremos a posição na lista
                    lista_posicoes_navio.append(
                        [posicao_inicial[0] - pos, posicao_inicial[1]]
                    )

                # Salvaremos as informações do navio posicionado no dicionário da frota do jogador
                estado_jogo["posicoes_navios_jogador1"][
                    f"Navio_{len(estado_jogo['posicoes_navios_jogador1']) + 1}"
                ] = {"Tipo_Navio": navio, "Posicoes": lista_posicoes_navio}

            # Caso for 1 (DIREITA)
            case 1:
                # Salvaremos as posições do navio selecionado numa lista
                lista_posicoes_navio = [[posicao_inicial[0], posicao_inicial[1]]]

                # Itere de 1 ao tamanho do navio
                    # Posicionaremos quadrado por quadrado
                for pos in range(1, (identificadores_navios[navio]["Tamanho"])):
                    # Cada iteração, iremos uma coluna para a direita e mudaremos o identificador na matriz
                    estado_jogo["matriz_partida_jogador1"][posicao_inicial[0]][
                        posicao_inicial[1] + pos
                    ] = identificadores_navios[navio]["Identificador"]

                    # Adicionaremos a posição na lista
                    lista_posicoes_navio.append(
                        [posicao_inicial[0], posicao_inicial[1] + pos]
                    )

                # Salvaremos as informações do navio posicionado no dicionário da frota do jogador
                estado_jogo["posicoes_navios_jogador1"][
                    f"Navio_{len(estado_jogo['posicoes_navios_jogador1']) + 1}"
                ] = {"Tipo_Navio": navio, "Posicoes": lista_posicoes_navio}

            # Caso for 2 (BAIXO)
            case 2:
                # Salvaremos as posições do navio selecionado numa lista
                lista_posicoes_navio = [[posicao_inicial[0], posicao_inicial[1]]]

                # Itere de 1 ao tamanho do navio
                    # Posicionaremos quadrado por quadrado
                for pos in range(1, (identificadores_navios[navio]["Tamanho"])):
                    # Cada iteração, desceremos uma linha e mudaremos o identificador na matriz
                    estado_jogo["matriz_partida_jogador1"][posicao_inicial[0] + pos][
                        posicao_inicial[1]
                    ] = identificadores_navios[navio]["Identificador"]

                    # Adicionaremos a posição na lista
                    lista_posicoes_navio.append(
                        [posicao_inicial[0] + pos, posicao_inicial[1]]
                    )

                # Salvaremos as informações do navio posicionado no dicionário da frota do jogador
                estado_jogo["posicoes_navios_jogador1"][
                    f"Navio_{len(estado_jogo['posicoes_navios_jogador1']) + 1}"
                ] = {"Tipo_Navio": navio, "Posicoes": lista_posicoes_navio}

            # Caso for 3 (ESQUERDA)
            case 3:
                # Salvaremos as posições do navio selecionado numa lista
                lista_posicoes_navio = [[posicao_inicial[0], posicao_inicial[1]]]

                # Itere de 1 ao tamanho do navio
                    # Posicionaremos quadrado por quadrado
                for pos in range(1, (identificadores_navios[navio]["Tamanho"])):
                    # Cada iteração, iremos uma coluna para a esquerda e mudaremos o identificador na matriz
                    estado_jogo["matriz_partida_jogador1"][posicao_inicial[0]][
                        posicao_inicial[1] - pos
                    ] = identificadores_navios[navio]["Identificador"]

                    # Adicionaremos a posição na lista
                    lista_posicoes_navio.append(
                        [posicao_inicial[0], posicao_inicial[1] - pos]
                    )

                # Salvaremos as informações do navio posicionado no dicionário da frota do jogador
                estado_jogo["posicoes_navios_jogador1"][
                    f"Navio_{len(estado_jogo['posicoes_navios_jogador1']) + 1}"
                ] = {"Tipo_Navio": navio, "Posicoes": lista_posicoes_navio}


# Função para posicionar os navios da frota do Adversário
def gerar_navios_inimigo_artificial(
    submarinos, encouracados, destroiers, cruzadores, estado_jogo
):
    """
    —————————————— LÓGICA DA FUNÇÃO ——————————————
    XX Pegar a quantidade de navios
    XX Em ordem, tornar a escolha das posições dos navios para o usuario, clara
    XX Pedir para o usuário escolher a posição inicial do navio atual
    XX Checar os lados para os quais o usuario poderá posicionar o resto do navio
    XX Pedir o lado para qual o navio será colocado
    XX Posicionar o navio na matriz do jogador
    """

    # Inicializando dicionário que ditará o número de navios presentes no mapa, baseando-se no tamanho escolhido
    lista_navios_para_adicionar = {}

    # se o número de qualquer navio for maior que 0, ele estará presente
    if submarinos > 0:
        lista_navios_para_adicionar["Submarino"] = submarinos
    if encouracados > 0:
        lista_navios_para_adicionar["Encouraçado"] = encouracados
    if destroiers > 0:
        lista_navios_para_adicionar["Destróier"] = destroiers
    if cruzadores > 0:
        lista_navios_para_adicionar["Cruzador"] = cruzadores

    # Iteraremos sobre todos os navios que devemos adicionar
    for navio in lista_navios_para_adicionar:
        # Enquanto houver navios que devem ser posicionados, na iteração atual, o loop acontecerá
        while lista_navios_para_adicionar[navio] > 0:
            while True:  # SAIRÁ MANUALMENTE PRA PREVENIR SPAWN EM BLOCO INVALIDO
                # Selecionará uma linha aleatória, pegando um número entre 0 ao tamanho da matriz (menos 1 automático)
                posicao_inicial_linha = random.randrange(
                    0, len(estado_jogo["matriz_partida_jogador2"])
                )
                # Selecionará uma coluna aleatória, pegando um número entre 0 ao tamanho da matriz (menos 1 automático)
                posicao_inicial_coluna = random.randrange(
                    0, len(estado_jogo["matriz_partida_jogador2"][0])
                )

                # Se o quadrado selecionado aleatóriamente não estiver vazio (água)
                if (
                    not estado_jogo["matriz_partida_jogador2"][posicao_inicial_linha][
                        posicao_inicial_coluna
                    ]
                    == 0
                ):
                    # Tente novamente
                    continue
                else:
                    # Achou um quadrado válido, saia do looping
                    break

            # Variável de controle do looping
            navio_criado_com_sucesso = False
            # Usaremos tentativas para tentar adicionar um navio
            tentativa_atual = 0

            # Enquanto o navio não existir e não tivermos atingido o máximo de tentativas
            while not navio_criado_com_sucesso and tentativa_atual < 50:
                # Tente posicionar o navio
                navio_criado_com_sucesso = verificar_e_posicionar_navio_inimigo(
                    [posicao_inicial_linha, posicao_inicial_coluna],
                    navio,
                    identificadores_navios[navio]["Tamanho"],
                    estado_jogo,
                )
                # Usamos uma tentativa
                tentativa_atual += 1

            # Se o navio não foi criado com sucesso
            if not navio_criado_com_sucesso:
                # Tentaremos do ínicio, novamente
                continue

            # O navio foi criado com sucesso, logo um a menos para se adicionar
            lista_navios_para_adicionar[navio] -= 1

# Função para verificarmos as possibilidades de expansão do inimigo e, se possível, posicionarmos o navio
def verificar_e_posicionar_navio_inimigo(
    posicao_inicial, navio, quantidade_posicoes, estado_jogo
):
    # Se o navio for um submarino (precisa só de 1 quadrado) E
        # A posição selecionada for um quadrado vazio (só com água)
    if (
        navio == "Submarino"
        and estado_jogo["matriz_partida_jogador2"][posicao_inicial[0]][
            posicao_inicial[1]
        ]
        == 0
    ):
        # Salve na lista de posições da frota do jogador 2 um novo navio
            # Nesse novo navio, teremos o seu tipo e os quadrados que ele ocupa
        estado_jogo["posicoes_navios_jogador2"][
            f"Navio_{len(estado_jogo['posicoes_navios_jogador2']) + 1}"
        ] = {"Tipo_Navio": navio, "Posicoes": [posicao_inicial]}

        # Posicionaremos o navio na matriz da frota do jogador 2
        posicionar_navio_inimigo(posicao_inicial, navio, 0, estado_jogo)
        # Retorne que o posicionamento foi um sucesso
        return True

    # O navio é um submarino, mas o quadrado selecionado não estava vazio
    elif navio == "Submarino":
        # Retorne que o posicionamento foi um fracasso
        return False

    # Uma lista com possibilidades de expansão disponíveis para a I.A.
        # Tem função semelhante aos "pode_mover_cima, pode_mover_baixo etc"
    possibilidades_direcao_navio = [0, 1, 2, 3]

    # Checa se não é possível expandir para cima
    if posicao_inicial[0] - (
        quantidade_posicoes - 1
    ) < 0 or verificar_existencia_navio_inimigo(
        posicao_inicial, quantidade_posicoes, 0, estado_jogo
    ):
        # Se não for possível, remove da lista de possibilidades
        possibilidades_direcao_navio.remove(0)

    # Checa se não é possível expandir para baixo
    if posicao_inicial[0] + (quantidade_posicoes - 1) >= len(
        estado_jogo["matriz_partida_jogador2"]
    ) or verificar_existencia_navio_inimigo(
        posicao_inicial, quantidade_posicoes, 2, estado_jogo
    ):
        # Se não for possível, remove da lista de possibilidades
        possibilidades_direcao_navio.remove(2)

    # Checa se não é possível expandir para a esquerda
    if posicao_inicial[1] - (
        quantidade_posicoes - 1
    ) < 0 or verificar_existencia_navio_inimigo(
        posicao_inicial, quantidade_posicoes, 3, estado_jogo
    ):
        # Se não for possível, remove da lista de possibilidades
        possibilidades_direcao_navio.remove(3)

    # Checa se não é possível expandir para a direita
    if posicao_inicial[1] + (quantidade_posicoes - 1) >= len(
        estado_jogo["matriz_partida_jogador2"]
    ) or verificar_existencia_navio_inimigo(
        posicao_inicial, quantidade_posicoes, 1, estado_jogo
    ):
        # Se não for possível, remove da lista de possibilidades
        possibilidades_direcao_navio.remove(1)

    # Se não houver nenhuma possibilidade de expansão
    if len(possibilidades_direcao_navio) == 0:
        # O posicionamento foi um fracasso
        return False

    # Escolha aleatóriamente a direção a ser expandida, da lista de possibilidades
    escolha_direcao_pergunta = random.choice(possibilidades_direcao_navio)
    # Posicione o navio
    posicionar_navio_inimigo(
        posicao_inicial, navio, escolha_direcao_pergunta, estado_jogo
    )

    # O navio foi posicionado com sucesso
    return True

# Verificaremos se existe um navio presente numa determinada direção
def verificar_existencia_navio_inimigo(
    posicao_inicial, quantidade_posicoes, direcao, estado_jogo
):
    """
    DIREÇÕES:
        0 - CIMA
        1 - DIREITA
        2 - BAIXO
        3 - ESQUERDA
    """

    # Tente verificar a existência de um navio numa direção específica
    try:
        # Switch da direção escolhida
        match direcao:
            # Caso for 0 (CIMA)
            case 0:
                # Itere de 1 ao tamanho do navio
                    # Verificaremos quadrado por quadrado
                for pos in range(1, quantidade_posicoes):
                    # Se houver algum quadrado diferente de 0 (água), há um navio
                    if (
                        not estado_jogo["matriz_partida_jogador2"][
                            posicao_inicial[0] - pos
                        ][posicao_inicial[1]]
                        == 0
                    ):
                        # Retorne que há um navio
                        return True

            # Caso for 1 (DIREITA)
            case 1:
                # Itere de 1 ao tamanho do navio
                    # Verificaremos quadrado por quadrado
                for pos in range(1, quantidade_posicoes):
                    # Se houver algum quadrado diferente de 0 (água), há um navio
                    if (
                        not estado_jogo["matriz_partida_jogador2"][posicao_inicial[0]][
                            posicao_inicial[1] + pos
                        ]
                        == 0
                    ):
                        # Retorne que há um navio
                        return True

            # Caso for 2 (BAIXO)
            case 2:
                # Itere de 1 ao tamanho do navio
                    # Verificaremos quadrado por quadrado
                for pos in range(1, quantidade_posicoes):
                    # Se houver algum quadrado diferente de 0 (água), há um navio
                    if (
                        not estado_jogo["matriz_partida_jogador2"][
                            posicao_inicial[0] + pos
                        ][posicao_inicial[1]]
                        == 0
                    ):
                        # Retorne que há um navio
                        return True

            # Caso for 3 (ESQUERDA)
            case 3:
                # Itere de 1 ao tamanho do navio
                    # Verificaremos quadrado por quadrado
                for pos in range(1, quantidade_posicoes):
                    # Se houver algum quadrado diferente de 0 (água), há um navio
                    if (
                        not estado_jogo["matriz_partida_jogador2"][posicao_inicial[0]][
                            posicao_inicial[1] - pos
                        ]
                        == 0
                    ):
                        # Retorne que há um navio
                        return True
        # Caso não haja nenhum navio na direção, retorne que não há nenhum navio
        return False

    # Caso haja um erro que leve a verificação para fora da matriz, retorne que há "um navio", por segurança
    except IndexError:
        return True

# Função para posicionar o navio na matriz do adversário
def posicionar_navio_inimigo(posicao_inicial, navio, direcao, estado_jogo):
    # A posição inicial do quadrado na matriz é alterada para o identificador do navio a ser posicionado
    estado_jogo["matriz_partida_jogador2"][posicao_inicial[0]][posicao_inicial[1]] = (
        identificadores_navios[navio]["Identificador"]
    )
    """
        DIREÇÕES:
            0 - CIMA
            1 - DIREITA
            2 - BAIXO
            3 - ESQUERDA
    """
    # Se o navio ocupar mais de um quadrado
    if identificadores_navios[navio]["Tamanho"] > 1:
        # Switch da direção escolhida
        match direcao:
            # Caso for 0 (CIMA)
            case 0:
                # Salvaremos as posições do navio selecionado numa lista
                lista_posicoes_navio = [[posicao_inicial[0], posicao_inicial[1]]]

                # Itere de 1 ao tamanho do navio
                    # Posicionaremos quadrado por quadrado
                for pos in range(1, (identificadores_navios[navio]["Tamanho"])):
                    # Cada iteração, subiremos uma linha e mudaremos o identificador na matriz
                    estado_jogo["matriz_partida_jogador2"][posicao_inicial[0] - pos][
                        posicao_inicial[1]
                    ] = identificadores_navios[navio]["Identificador"]

                    # Adicionaremos a posição na lista
                    lista_posicoes_navio.append(
                        [posicao_inicial[0] - pos, posicao_inicial[1]]
                    )

                # Salvaremos as informações do navio posicionado no dicionário da frota do adversário
                estado_jogo["posicoes_navios_jogador2"][
                    f"Navio_{len(estado_jogo['posicoes_navios_jogador2']) + 1}"
                ] = {"Tipo_Navio": navio, "Posicoes": lista_posicoes_navio}

            # Caso for 1 (DIREITA)
            case 1:
                lista_posicoes_navio = [[posicao_inicial[0], posicao_inicial[1]]]

                # Itere de 1 ao tamanho do navio
                    # Posicionaremos quadrado por quadrado
                for pos in range(1, (identificadores_navios[navio]["Tamanho"])):
                    # Cada iteração, iremos uma coluna para a direita e mudaremos o identificador na matriz
                    estado_jogo["matriz_partida_jogador2"][posicao_inicial[0]][
                        posicao_inicial[1] + pos
                    ] = identificadores_navios[navio]["Identificador"]

                    # Adicionaremos a posição na lista
                    lista_posicoes_navio.append(
                        [posicao_inicial[0], posicao_inicial[1] + pos]
                    )

                # Salvaremos as informações do navio posicionado no dicionário da frota do adversário
                estado_jogo["posicoes_navios_jogador2"][
                    f"Navio_{len(estado_jogo['posicoes_navios_jogador2']) + 1}"
                ] = {"Tipo_Navio": navio, "Posicoes": lista_posicoes_navio}

            # Caso for 2 (BAIXO)
            case 2:
                lista_posicoes_navio = [[posicao_inicial[0], posicao_inicial[1]]]

                # Itere de 1 ao tamanho do navio
                    # Posicionaremos quadrado por quadrado
                for pos in range(1, (identificadores_navios[navio]["Tamanho"])):
                    # Cada iteração, desceremos uma linha e mudaremos o identificador na matriz
                    estado_jogo["matriz_partida_jogador2"][posicao_inicial[0] + pos][
                        posicao_inicial[1]
                    ] = identificadores_navios[navio]["Identificador"]

                    # Adicionaremos a posição na lista
                    lista_posicoes_navio.append(
                        [posicao_inicial[0] + pos, posicao_inicial[1]]
                    )

                # Salvaremos as informações do navio posicionado no dicionário da frota do adversário
                estado_jogo["posicoes_navios_jogador2"][
                    f"Navio_{len(estado_jogo['posicoes_navios_jogador2']) + 1}"
                ] = {"Tipo_Navio": navio, "Posicoes": lista_posicoes_navio}

            # Caso for 3 (ESQUERDA)
            case 3:
                lista_posicoes_navio = [[posicao_inicial[0], posicao_inicial[1]]]

                # Itere de 1 ao tamanho do navio
                    # Posicionaremos quadrado por quadrado
                for pos in range(1, (identificadores_navios[navio]["Tamanho"])):
                    # Cada iteração, iremos uma coluna para a esquerda e mudaremos o identificador na matriz
                    estado_jogo["matriz_partida_jogador2"][posicao_inicial[0]][
                        posicao_inicial[1] - pos
                    ] = identificadores_navios[navio]["Identificador"]

                    # Adicionaremos a posição na lista
                    lista_posicoes_navio.append(
                        [posicao_inicial[0], posicao_inicial[1] - pos]
                    )

                # Salvaremos as informações do navio posicionado no dicionário da frota do adversário
                estado_jogo["posicoes_navios_jogador2"][
                    f"Navio_{len(estado_jogo['posicoes_navios_jogador2']) + 1}"
                ] = {"Tipo_Navio": navio, "Posicoes": lista_posicoes_navio}

# Função para desenhar um minimapa de uma matriz
def desenhar_minimapa(matriz):
    # Inicialização da string do minimapa
    matriz_desenhada = ""

    # Salva o tamanho da matriz
    numero_colunas = len(matriz[0])
    numero_linhas = len(matriz)

    # Itere sobre cada linha da matriz
    for linha in range(numero_linhas):
        # Em cada linha, itere sobre o número de colunas da matriz
        for coluna_quadrado in range(numero_colunas):

            # Se a posição atual for:
            # 0 = Água
            if matriz[linha][coluna_quadrado] == 0:
                matriz_desenhada += "[🌊]"
            # 1 = Navio
            elif matriz[linha][coluna_quadrado] == 1:
                matriz_desenhada += "[🚢]"
            # 2 = Navio
            elif matriz[linha][coluna_quadrado] == 2:
                matriz_desenhada += "[🚢]"
            # 3 = Navio
            elif matriz[linha][coluna_quadrado] == 3:
                matriz_desenhada += "[🚢]"
            # 4 = Navio
            elif matriz[linha][coluna_quadrado] == 4:
                matriz_desenhada += "[🚢]"
            # 5 = Acerto
            elif matriz[linha][coluna_quadrado] == 5:
                matriz_desenhada += "[💥]"
            # 6 = Erro
            elif matriz[linha][coluna_quadrado] == 6:
                matriz_desenhada += "[❌]"
            # Qualquer outro valor = Vazio
            else:
                matriz_desenhada += "[]"
        # Desça uma linha
        matriz_desenhada += "\n"

    # Imprima o minimapa
    print(matriz_desenhada)

# Função para desenhar um imapa de uma matriz
def desenhar_mapa_jogador(matriz):
    # Inicialização da string do mapa
    matriz_desenhada = ""

    # Salva o tamanho da matriz
    numero_colunas = len(matriz[0])
    numero_linhas = len(matriz)

    # Itere sobre cada linha da matriz
    for linha in range(numero_linhas):

        # Em cada linha, itere sobre o número de colunas da matriz
        for quadrado_coluna in range(numero_colunas):
            # Adicione o "telhado" de cada quadrado
            matriz_desenhada += " |￣￣￣￣|"
        # Desça uma linha
        matriz_desenhada += "\n"

        # Em cada linha, itere sobre o número de colunas da matriz
        for segunda_parede_quadrado in range(numero_colunas):
            # Se a posição atual for:
            # 0 = Água
            if matriz[linha][segunda_parede_quadrado] == 0:
                matriz_desenhada += " |   🌊   |"
            # 1 = Navio
            elif matriz[linha][segunda_parede_quadrado] == 1:
                matriz_desenhada += " |   🚢   |"
            # 2 = Navio
            elif matriz[linha][segunda_parede_quadrado] == 2:
                matriz_desenhada += " |   🚢   |"
            # 3 = Navio
            elif matriz[linha][segunda_parede_quadrado] == 3:
                matriz_desenhada += " |   🚢   |"
            # 4 = Navio
            elif matriz[linha][segunda_parede_quadrado] == 4:
                matriz_desenhada += " |   🚢   |"
            # 5 = Acerto
            elif matriz[linha][segunda_parede_quadrado] == 5:
                matriz_desenhada += " |   💥   |"
            # 6 = Erro
            elif matriz[linha][segunda_parede_quadrado] == 6:
                matriz_desenhada += " |   ❌   |"
            # Qualquer outro valor = Vazio
            else:
                matriz_desenhada += " |        |"
        # Desça uma linha
        matriz_desenhada += "\n"

        # Terceira parede de cada quadrado
        for terceira_parede_quadrado in range(numero_colunas):
            matriz_desenhada += " |        |"
        # Desça uma linha
        matriz_desenhada += "\n"

    # "Chão" de cada coluna
    for quadrado_coluna in range(numero_colunas):
        matriz_desenhada += "  ￣￣￣￣ "

    # Imprima o mapa
    print(matriz_desenhada)

# Função com a lógica da partida
def partida_principal(estado_jogo):
    # Sairemos do looping da partida manualmente
    while True:
        # Tentaremos decidir quem vai começar a partida
        try:
            time.sleep(1)
            print("\n🌊⚓═══════════════════════════════════════════════⚓🌊\n")
            # Input e casting da seleção do jogador
            jogador_inicial = int(
                input(
                    "🧭 Capitão, quem irá iniciar a batalha? ⚔️🚢\n\n"
                    "  1️⃣ — Jogador\n"
                    "  2️⃣ — Adversário 👾\n"
                    "  3️⃣ — Aleatório 🎲\n\n"
                    "👉 Decisão: "
                )
            )
            print("\n🌊⚓═══════════════════════════════════════════════⚓🌊\n\n")
            if 1 <= jogador_inicial <= 3:
                break  # valor válido, sai do loop
            else:
                time.sleep(1)
                print(
                    "❌ Opção inválida, Capitão! ⚓🚢 "
                    "Escolha apenas entre 1️⃣, 2️⃣ ou 3️⃣ 🧭🌊\n"
                    "Tome cuidado e faça a escolha certa para iniciar a batalha! ⚔️🔥\n"
                )

        # Caso tenha algum erro no valor inserido pelo usuário
        except ValueError:
            time.sleep(1)
            print(
                "❌ Entrada inválida, Capitão! ⚓🚢 "
                "Digite apenas números inteiros 🧭🌊\n"
                "Use os instrumentos de navegação corretamente e tente novamente! ⚔️🔥\n"
            )

    # Se ele escolheu aleatoriamente
    if jogador_inicial == 3:
        # Escolher um numero aleatório entre 1 e 2 (vai um a menos)
        jogador_atual = random.randrange(1, 3)
        time.sleep(1)
        print(
            f"🎲 Seleção aleatória concluída! ⚓🚢\n"
            f"➡️ {jogador_atual} ⚔️🔥\n"
        )
    else:
        jogador_atual = jogador_inicial

    time.sleep(1)
    print("\n🌊⚓═══════════════════════════════════════════════⚓🌊\n")
    print("🧭 Determinando quem iniciará a partida... ⚔️🚢")
    time.sleep(0.75)
    if jogador_atual == 1:
        print("➡️ O Capitão Jogador irá comandar a primeira jogada! 🔥")
    else:
        print("➡️ O Capitão Adversário assumirá o comando da primeira jogada! 👾⚔️")
    print("\n🌊⚓═══════════════════════════════════════════════⚓🌊\n")

    partida_em_progresso = True

    time.sleep(0.85)
    print(
        "\n🌊⚓═══════════════════════════════════════════════⚓🌊\n\n"
        "⚔️🚢 A batalha começou, Capitão! 🧭\n"
        "Prepare-se para conquistar os mares e afundar os navios inimigos! 🌊🔥\n\n"
        "🌊⚓═══════════════════════════════════════════════⚓🌊\n"
    )
    time.sleep(1.1)

    while partida_em_progresso:
        # Looping da partida
            # Switch para detectar quem é o responsável pelo turno atual
        match jogador_atual:
            # se for 1, o responsável é o jogador
            case 1:
                time.sleep(1)
                print(
                    "\n🧭 Capitão, este é o Mapa de Inteligência! ⚓🚢\n"
                    "Ele revelará seus acertos e erros durante os ataques inimigos e os seus! 🌊⚔️\n"
                    "Use-o estrategicamente para dominar os mares! 🔥🗺️\n"
                )
                time.sleep(0.5)
                # Desenhar o mapa da frota do usuário
                desenhar_mapa_jogador(estado_jogo["matriz_alvo_jogador1"])

                posicao_valida = False
                # Enquanto não tiver encontrado uma posição de ataque válida
                while not posicao_valida:
                    time.sleep(0.75)
                    posicao_ataque_linha = input(
                        f"🧭 Capitão, insira a linha para realizar seu ataque 🚢⚔️ "
                        f"(1 a {len(estado_jogo['matriz_alvo_jogador1'])}): "
                    )
                    # Se a linha inserida não for um digito
                    if not posicao_ataque_linha.isdigit():
                        print(
                            "❌ Entrada inválida, Capitão! ⚓🚢 "
                            "Insira apenas números inteiros 🧭🌊\n"
                            "Use os instrumentos de navegação corretamente e tente novamente! ⚔️🔥\n"
                        )
                        continue

                    # Casting para inteiro
                    posicao_ataque_linha = int(posicao_ataque_linha)

                    posicao_ataque_coluna = input(
                        f"🧭 Capitão, insira a coluna para realizar seu ataque 🚢⚔️ "
                        f"(1 a {len(estado_jogo['matriz_alvo_jogador1'][0])}): "
                    )
                    # Se a coluna inserida não for um digito
                    if not posicao_ataque_coluna.isdigit():
                        print(
                            "❌ Entrada inválida, Capitão! ⚓🚢 "
                            "Insira apenas números inteiros para a coluna 🧭🌊\n"
                            "Use os instrumentos de navegação corretamente e tente novamente! ⚔️🔥\n"
                        )
                        continue

                    # Casting para inteiro
                    posicao_ataque_coluna = int(posicao_ataque_coluna)

                    # Checar se a linha inserida está dentro dos limites
                    if posicao_ataque_linha < 1 or posicao_ataque_linha > len(
                        estado_jogo["matriz_partida_jogador1"]
                    ):
                        time.sleep(1)
                        print(
                            f"❌ Linha inválida, Capitão! ⚓🚢 "
                            f"Por favor selecione uma posição entre 1 e {len(estado_jogo['matriz_alvo_jogador1'])} 🧭🌊\n"
                            "Escolha sabiamente e mire com precisão! ⚔️🔥\n"
                        )
                        continue

                    # Checar se a coluna inserida está dentro dos limites
                    if posicao_ataque_coluna < 1 or posicao_ataque_coluna > len(
                        estado_jogo["matriz_alvo_jogador1"][0]
                    ):
                        time.sleep(1)
                        print(
                            f"❌ Coluna inválida, Capitão! ⚓🚢 "
                            f"Por favor selecione uma posição entre 1 e {len(estado_jogo['matriz_alvo_jogador1'][0])} 🧭🌊\n"
                            "Escolha sabiamente e mire com precisão! ⚔️🔥\n"
                        )
                        continue
                    posicao_ataque_linha -= 1  # as listas começam do zero
                    posicao_ataque_coluna -= 1  # as listas começam do zero

                    posicao_valida = True

                time.sleep(0.75)
                # Checa se a posição atacada já não foi atacada anteriormente
                if (
                    estado_jogo["matriz_alvo_jogador1"][posicao_ataque_linha][
                        posicao_ataque_coluna
                    ]
                    == 5
                    or estado_jogo["matriz_alvo_jogador1"][posicao_ataque_linha][
                        posicao_ataque_coluna
                    ]
                    == 6
                ):

                    print(
                        "❌ Atenção, Capitão! ⚓🚢\n"
                        "Nossa inteligência indica que já atacamos essas coordenadas! 🧭🌊\n"
                        "Escolha um novo alvo com sabedoria para dominar os mares! ⚔️🔥\n"
                    )

                # Checa se a posição atacada não é água e nem foi atacada anteriormente
                elif (
                    not estado_jogo["matriz_partida_jogador2"][posicao_ataque_linha][
                        posicao_ataque_coluna
                    ]
                    == 0
                    and not estado_jogo["matriz_partida_jogador2"][
                        posicao_ataque_linha
                    ][posicao_ataque_coluna]
                    == 5
                    and not estado_jogo["matriz_partida_jogador2"][
                        posicao_ataque_linha
                    ][posicao_ataque_coluna]
                    == 6
                ):

                    print(
                        "\n✅ Capitão! ⚓🚢 Nossa inteligência indica que o ataque foi um sucesso! 🌊⚔️\n"
                        "O inimigo foi atingido! Prepare-se para o próximo movimento estratégico! 🔥🧭\n"
                    )
                    # Declara que a posição na matriz alvo do jogador 1 foi um acerto
                    estado_jogo["matriz_alvo_jogador1"][posicao_ataque_linha][
                        posicao_ataque_coluna
                    ] = 5
                    # Itera sobre os navios do adversário
                    for nav in estado_jogo["posicoes_navios_jogador2"]:
                        for posicao in estado_jogo["posicoes_navios_jogador2"][nav][
                            "Posicoes"
                        ]:
                            # Se a posição da iteração atual coincidir com a posição de ataque do jogador
                            if (
                                posicao[0] == posicao_ataque_linha
                                and posicao[1] == posicao_ataque_coluna
                            ):
                                # Remova a posição do navio atacado
                                estado_jogo["posicoes_navios_jogador2"][nav][
                                    "Posicoes"
                                ].remove([posicao_ataque_linha, posicao_ataque_coluna])

                # Caso tenhamos errado
                else:
                    print(
                        "❌ Capitão! ⚓🚢 Nossa inteligência indica que o ataque falhou! 🌊⚔️\n"
                        "O inimigo saiu ileso. Reavalie sua estratégia e prepare o próximo ataque! 🔥🧭\n"
                    )

                    # Declara que a posição na matriz alvo do jogador 1 foi um erro
                    estado_jogo["matriz_alvo_jogador1"][posicao_ataque_linha][
                        posicao_ataque_coluna
                    ] = 6

            # se for 2, o responsável é o adversário
            case 2:
                print(
                    "\n⚠️ Capitão! O inimigo está prestes a atacar! 🔥🚢\n"
                    "Prepare-se para defender a frota e reagir estrategicamente! 🧭⚔️🌊\n"
                )
                time.sleep(0.75)
                # Se não houver nenhuma prioridade de ataque na memória da I.A.
                if len(lista_prioridades_inteligencia_artificial) == 0:
                    posicao_valida = False

                    # Seleciona uma linha aleatória da matriz
                    posicao_ataque_linha_jogador_humano = random.randrange(
                        0, len(estado_jogo["matriz_partida_jogador1"])
                    )
                    # Seleciona uma coluna aleatória da matriz
                    posicao_ataque_coluna_jogador_humano = random.randrange(
                        0, len(estado_jogo["matriz_partida_jogador1"][0])
                    )

                    # Enquanto não encontrar uma posição de ataque válida
                    while not posicao_valida:
                        # Tentar novamente
                        posicao_ataque_linha_jogador_humano = random.randrange(
                            0, len(estado_jogo["matriz_partida_jogador1"])
                        )

                        posicao_ataque_coluna_jogador_humano = random.randrange(
                            0, len(estado_jogo["matriz_partida_jogador1"][0])
                        )

                        # Checa se a linha está dentro dos limites da matriz
                        if (
                            posicao_ataque_linha_jogador_humano < 0
                            or posicao_ataque_linha_jogador_humano
                            > len(estado_jogo["matriz_partida_jogador1"])
                        ):
                            continue

                        # Checa se a coluna está dentro dos limites da matriz
                        if (
                            posicao_ataque_coluna_jogador_humano < 0
                            or posicao_ataque_coluna_jogador_humano
                            > len(estado_jogo["matriz_alvo_jogador1"][0])
                        ):
                            continue

                        # Checa se a posição selecionada já não foi atacada antes
                        if [
                            posicao_ataque_linha_jogador_humano,
                            posicao_ataque_coluna_jogador_humano,
                        ] in lista_ignorar_inteligencia_artificial:
                            continue

                        posicao_valida = True

                    ataque_valido = False
                    while not ataque_valido:
                        # Checa se o inimigo acertou um navio nosso
                        if (
                            not estado_jogo["matriz_partida_jogador1"][
                                posicao_ataque_linha_jogador_humano
                            ][posicao_ataque_coluna_jogador_humano]
                            == 0
                            and not estado_jogo["matriz_partida_jogador1"][
                                posicao_ataque_linha_jogador_humano
                            ][posicao_ataque_coluna_jogador_humano]
                            == 5
                            and not estado_jogo["matriz_partida_jogador1"][
                                posicao_ataque_linha_jogador_humano
                            ][posicao_ataque_coluna_jogador_humano]
                            == 6
                        ):
                            time.sleep(0.65)
                            print(
                                "💥 Capitão! ⚓🚢 O inimigo acertou em cheio! 🌊⚔️\n"
                                "A frota sofreu danos! Reorganize suas defesas e prepare o próximo ataque! 🔥🧭\n"
                            )
                            # Declara que a posição na matriz da frota do jogador 1 foi um acerto do inimigo
                            estado_jogo["matriz_partida_jogador1"][
                                posicao_ataque_linha_jogador_humano
                            ][posicao_ataque_coluna_jogador_humano] = 5

                            # Itera sobre os navios do jogador
                            for nav in estado_jogo["posicoes_navios_jogador1"]:
                                for posicao in estado_jogo["posicoes_navios_jogador1"][
                                    nav
                                ]["Posicoes"]:
                                    # Se a posição da iteração atual coincidir com a posição de ataque do adversário
                                    if (
                                        posicao[0]
                                        == posicao_ataque_linha_jogador_humano
                                        and posicao[1]
                                        == posicao_ataque_coluna_jogador_humano
                                    ):
                                        # Remova a posição do navio atacado
                                        estado_jogo["posicoes_navios_jogador1"][nav][
                                            "Posicoes"
                                        ].remove(
                                            [
                                                posicao_ataque_linha_jogador_humano,
                                                posicao_ataque_coluna_jogador_humano,
                                            ]
                                        )

                            # Decide se o quadrado acima do alvo anterior deverá ser atacada nos próximos turnos
                            if posicao_ataque_linha_jogador_humano > 0:
                                # 60% DE CHANCE DE QUERER TENTAR ATACAR NAVIOS PRÓXIMOS - ACIMA
                                if random.randrange(1, 11) <= 6:
                                    lista_prioridades_inteligencia_artificial.append(
                                        [
                                            posicao_ataque_linha_jogador_humano - 1,
                                            posicao_ataque_coluna_jogador_humano,
                                        ]
                                    )

                            # Decide se o quadrado abaixo do alvo anterior deverá ser atacada nos próximos turnos
                            if (
                                posicao_ataque_linha_jogador_humano
                                < len(estado_jogo["matriz_partida_jogador1"]) - 2
                            ):
                                # 60% DE CHANCE DE QUERER TENTAR ATACAR NAVIOS PRÓXIMOS - ABAIXO
                                if random.randrange(1, 11) <= 6:
                                    lista_prioridades_inteligencia_artificial.append(
                                        [
                                            posicao_ataque_linha_jogador_humano + 1,
                                            posicao_ataque_coluna_jogador_humano,
                                        ]
                                    )

                            # Decide se o quadrado à esquerda do alvo anterior deverá ser atacado nos próximos turnos
                            if posicao_ataque_linha_jogador_humano > 0:
                                # 60% DE CHANCE DE QUERER TENTAR ATACAR NAVIOS PRÓXIMOS - ESQUERDA
                                if random.randrange(1, 11) <= 6:
                                    lista_prioridades_inteligencia_artificial.append(
                                        [
                                            posicao_ataque_linha_jogador_humano,
                                            posicao_ataque_coluna_jogador_humano - 1,
                                        ]
                                    )

                            # Decide se o quadrado à direita do alvo anterior deverá ser atacado nos próximos turnos
                            if (
                                posicao_ataque_linha_jogador_humano
                                > len(estado_jogo["matriz_partida_jogador1"][0]) - 2
                            ):
                                # 60% DE CHANCE DE QUERER TENTAR ATACAR NAVIOS PRÓXIMOS - DIREITA
                                if random.randrange(1, 11) <= 6:
                                    lista_prioridades_inteligencia_artificial.append(
                                        [
                                            posicao_ataque_linha_jogador_humano,
                                            posicao_ataque_coluna_jogador_humano + 1,
                                        ]
                                    )

                        # O adversário errou o ataque
                        else:
                            time.sleep(0.65)
                            print(
                                "✅ Capitão! ⚓🚢 O ataque do inimigo foi em vão! 🌊⚔️\n"
                                "A frota permanece intacta! Aproveitem esta oportunidade para contra-atacar! 🔥🧭\n"
                            )
                            # Adiciona o quadrado errado à memória de ignorar da I.A.
                            lista_ignorar_inteligencia_artificial.append(
                                [
                                    posicao_ataque_linha_jogador_humano,
                                    posicao_ataque_coluna_jogador_humano,
                                ]
                            )

                        ataque_valido = True

                # Há prioridades de ataque para a I.A.
                else:
                    if not lista_prioridades_inteligencia_artificial:
                        continue

                    posicao_valida = False
                    tentativa = 0
                    # Seleciona uma posição aleatória da lista de prioridades
                    prioridade_atacar = random.choice(
                        lista_prioridades_inteligencia_artificial
                    )

                    while not posicao_valida and tentativa <= 50:
                        prioridade_atacar = random.choice(
                            lista_prioridades_inteligencia_artificial
                        )
                        posicao_ataque_linha_jogador_humano = prioridade_atacar[0]
                        posicao_ataque_coluna_jogador_humano = prioridade_atacar[1]

                        if (
                            posicao_ataque_linha_jogador_humano < 0
                            or posicao_ataque_linha_jogador_humano
                            >= len(estado_jogo["matriz_partida_jogador1"])
                        ):
                            tentativa += 1
                            continue

                        if (
                            posicao_ataque_coluna_jogador_humano < 0
                            or posicao_ataque_coluna_jogador_humano
                            >= len(estado_jogo["matriz_alvo_jogador1"][0])
                        ):
                            tentativa += 1
                            continue

                        posicao_valida = True

                    if not posicao_valida:
                        lista_prioridades_inteligencia_artificial.remove(
                            prioridade_atacar
                        )
                        continue

                    ataque_valido = False
                    while not ataque_valido:
                        if (
                            not estado_jogo["matriz_partida_jogador1"][
                                posicao_ataque_linha_jogador_humano
                            ][posicao_ataque_coluna_jogador_humano]
                            == 0
                            and not estado_jogo["matriz_partida_jogador1"][
                                posicao_ataque_linha_jogador_humano
                            ][posicao_ataque_coluna_jogador_humano]
                            == 5
                            and not estado_jogo["matriz_partida_jogador1"][
                                posicao_ataque_linha_jogador_humano
                            ][posicao_ataque_coluna_jogador_humano]
                            == 6
                        ):
                            time.sleep(0.65)
                            print(
                                "💥 Capitão! ⚓🚢 O inimigo acertou em cheio! 🌊⚔️\n"
                                "A frota sofreu danos! Reorganize suas defesas e prepare o próximo ataque! 🔥🧭\n"
                            )
                            estado_jogo["matriz_partida_jogador1"][
                                posicao_ataque_linha_jogador_humano
                            ][posicao_ataque_coluna_jogador_humano] = 5

                            for nav in estado_jogo["posicoes_navios_jogador1"]:
                                for posicao in estado_jogo["posicoes_navios_jogador1"][
                                    nav
                                ]["Posicoes"]:
                                    if (
                                        posicao[0]
                                        == posicao_ataque_linha_jogador_humano
                                        and posicao[1]
                                        == posicao_ataque_coluna_jogador_humano
                                    ):
                                        estado_jogo["posicoes_navios_jogador1"][nav][
                                            "Posicoes"
                                        ].remove(
                                            [
                                                posicao_ataque_linha_jogador_humano,
                                                posicao_ataque_coluna_jogador_humano,
                                            ]
                                        )

                            if posicao_ataque_linha_jogador_humano > 0:
                                # 60% DE CHANCE DE QUERER TENTAR ATACAR NAVIOS PRÓXIMOS - ACIMA
                                if random.randrange(1, 11) <= 6:
                                    lista_prioridades_inteligencia_artificial.append(
                                        [
                                            posicao_ataque_linha_jogador_humano - 1,
                                            posicao_ataque_coluna_jogador_humano,
                                        ]
                                    )

                            if (
                                posicao_ataque_linha_jogador_humano
                                < len(estado_jogo["matriz_partida_jogador1"]) - 2
                            ):
                                # 60% DE CHANCE DE QUERER TENTAR ATACAR NAVIOS PRÓXIMOS - ABAIXO
                                if random.randrange(1, 11) <= 6:
                                    lista_prioridades_inteligencia_artificial.append(
                                        [
                                            posicao_ataque_linha_jogador_humano + 1,
                                            posicao_ataque_coluna_jogador_humano,
                                        ]
                                    )

                            if posicao_ataque_linha_jogador_humano > 0:
                                # 60% DE CHANCE DE QUERER TENTAR ATACAR NAVIOS PRÓXIMOS - ESQUERDA
                                if random.randrange(1, 11) <= 6:
                                    lista_prioridades_inteligencia_artificial.append(
                                        [
                                            posicao_ataque_linha_jogador_humano,
                                            posicao_ataque_coluna_jogador_humano - 1,
                                        ]
                                    )

                            if (
                                posicao_ataque_linha_jogador_humano
                                > len(estado_jogo["matriz_partida_jogador1"][0]) - 2
                            ):
                                # 60% DE CHANCE DE QUERER TENTAR ATACAR NAVIOS PRÓXIMOS - DIREITA
                                if random.randrange(1, 11) <= 6:
                                    lista_prioridades_inteligencia_artificial.append(
                                        [
                                            posicao_ataque_linha_jogador_humano,
                                            posicao_ataque_coluna_jogador_humano + 1,
                                        ]
                                    )

                        else:
                            time.sleep(0.65)
                            print(
                                "✅ Capitão! ⚓🚢 O ataque do inimigo foi em vão! 🌊⚔️\n"
                                "A frota permanece intacta! Aproveitem esta oportunidade para contra-atacar! 🔥🧭\n"
                            )

                        if [
                            posicao_ataque_linha_jogador_humano,
                            posicao_ataque_coluna_jogador_humano,
                        ] in lista_prioridades_inteligencia_artificial:
                            lista_prioridades_inteligencia_artificial.remove(
                                [
                                    posicao_ataque_linha_jogador_humano,
                                    posicao_ataque_coluna_jogador_humano,
                                ]
                            )
                        ataque_valido = True
                time.sleep(1)
                print(
                    "\n🗺️ Capitão, aqui está o Mini-Mapa de Inteligência da frota! ⚓🚢\n"
                    "Ele indica os danos que sofremos e ajuda a planejar nosso próximo movimento estratégico! 🌊⚔️🔥\n"
                )
                time.sleep(0.5)
                desenhar_minimapa(estado_jogo["matriz_partida_jogador1"])
                time.sleep(1)

        if jogador_atual == 1:
            navio_existente = False

            # Checa se o adversário ainda possui navios existentes
            for navio in estado_jogo["posicoes_navios_jogador2"]:
                if len(estado_jogo["posicoes_navios_jogador2"][navio]["Posicoes"]) > 0:
                    navio_existente = True

            # Se não tiver, jogador ganhou
            if not navio_existente:
                return 1

        elif jogador_atual == 2:
            navio_existente = False

            # Checa se o jogador ainda possui navios existentes
            for navio in estado_jogo["posicoes_navios_jogador1"]:
                if len(estado_jogo["posicoes_navios_jogador1"][navio]["Posicoes"]) > 0:
                    navio_existente = True

            # Se não tiver, adversário ganhou
            if not navio_existente:
                return 2

        # TROCA DE TURNO
        if jogador_atual == 1:
            jogador_atual = 2
        elif jogador_atual == 2:
            jogador_atual = 1
    return None


def main():
    jogo_loopando = True

    while jogo_loopando:
        # TAMANHOS
        # PEQUENO = 1 - 4x4
        # MÉDIO = 2 - 5x5
        # GRANDE = 3 - 6x6

        introducao()
        time.sleep(1.5)
        tamanho_mapa = escolher_mapa()
        estado_jogo = preparar_mapas(tamanho_mapa)

        preparar_partida(estado_jogo)

        vencedor = partida_principal(estado_jogo)

        time.sleep(1)
        print(
            "\n🌊⚓═══════════════════════════════════════════════⚓🌊\n"
            "🏴‍☠️ FIM DA PARTIDA, Capitão! ⚔️🚢\n"
            "A batalha terminou nos mares! 🔥🧭\n"
            "🌊⚓═══════════════════════════════════════════════⚓🌊\n"
        )

        time.sleep(1.5)
        print(
            "\n🗺️ Capitão, aqui está o Mini-Mapa de Inteligência do inimigo! ⚓🚢\n"
            "Ele indica os ataques que realizamos e ajuda a planejar nossos próximos movimentos estratégicos! 🌊⚔️🔥\n"
        )
        time.sleep(0.5)
        desenhar_minimapa(estado_jogo["matriz_alvo_jogador1"])

        # Inicialização das varíáveis de contagem de pontuação
        submarinos_inimigos_afundados = 0
        destroiers_inimigos_afundados = 0
        cruzadores_inimigos_afundados = 0
        encouracados_inimigos_afundados = 0

        submarinos_aliados_afundados = 0
        destroiers_aliados_afundados = 0
        cruzadores_aliados_afundados = 0
        encouracados_aliados_afundados = 0

        # Itera sobre os navios do adversário e contabiliza os afundados
        for navio in estado_jogo["posicoes_navios_jogador2"]:
            if (
                estado_jogo["posicoes_navios_jogador2"][navio]["Tipo_Navio"]
                == "Submarino"
                and len(estado_jogo["posicoes_navios_jogador2"][navio]["Posicoes"]) == 0
            ):
                submarinos_inimigos_afundados += 1

            if (
                estado_jogo["posicoes_navios_jogador2"][navio]["Tipo_Navio"]
                == "Destróier"
                and len(estado_jogo["posicoes_navios_jogador2"][navio]["Posicoes"]) == 0
            ):
                destroiers_inimigos_afundados += 1

            if (
                estado_jogo["posicoes_navios_jogador2"][navio]["Tipo_Navio"]
                == "Cruzador"
                and len(estado_jogo["posicoes_navios_jogador2"][navio]["Posicoes"]) == 0
            ):
                cruzadores_inimigos_afundados += 1

            if (
                estado_jogo["posicoes_navios_jogador2"][navio]["Tipo_Navio"]
                == "Encouraçado"
                and len(estado_jogo["posicoes_navios_jogador2"][navio]["Posicoes"]) == 0
            ):
                encouracados_inimigos_afundados += 1

        # Itera sobre os navios do jogador e contabiliza os afundados
        for navio in estado_jogo["posicoes_navios_jogador1"]:
            if (
                estado_jogo["posicoes_navios_jogador1"][navio]["Tipo_Navio"]
                == "Submarino"
                and len(estado_jogo["posicoes_navios_jogador1"][navio]["Posicoes"]) == 0
            ):
                submarinos_aliados_afundados += 1

            if (
                estado_jogo["posicoes_navios_jogador1"][navio]["Tipo_Navio"]
                == "Destróier"
                and len(estado_jogo["posicoes_navios_jogador1"][navio]["Posicoes"]) == 0
            ):
                destroiers_aliados_afundados += 1

            if (
                estado_jogo["posicoes_navios_jogador1"][navio]["Tipo_Navio"]
                == "Cruzador"
                and len(estado_jogo["posicoes_navios_jogador1"][navio]["Posicoes"]) == 0
            ):
                cruzadores_aliados_afundados += 1

            if (
                estado_jogo["posicoes_navios_jogador1"][navio]["Tipo_Navio"]
                == "Encouraçado"
                and len(estado_jogo["posicoes_navios_jogador1"][navio]["Posicoes"]) == 0
            ):
                encouracados_aliados_afundados += 1

        time.sleep(1)
        print("\n🌊⚓═══════════════════════════════════════════════⚓🌊\n")
        print("🧭 Capitão, a tensão nos mares aumenta... Quem será o vencedor? ⚔️🚢")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print("..")
        time.sleep(1)
        print("...")
        time.sleep(1)
        print("\n🌊⚓═══════════════════════════════════════════════⚓🌊\n")

        # JOGADOR GANHOU
        if vencedor == 1:
            print("\n🌊⚓═══════════════════════════════════════════════⚓🌊\n"
                    "🎆🏴‍☠️ PARABÉNS, Capitão Jogador 1! ⚔️🚢\n"
                    "Você conquistou os mares e afundou a frota inimiga! 🌊🔥🧭\n"
                    "🌊⚓═══════════════════════════════════════════════⚓🌊\n")
            time.sleep(1)

            print(
                "🛳️⚓ Resumo da Batalha ⚓🛳️\n"
                f"Submarinos inimigos afundados: {submarinos_inimigos_afundados} 🐋\n"
                f"Destroiers inimigos afundados: {destroiers_inimigos_afundados} 🚢\n"
                f"Cruzadores inimigos afundados: {cruzadores_inimigos_afundados} ⛴️\n"
                f"Encouraçados inimigos afundados: {encouracados_inimigos_afundados} 🛳️\n"
                "🌊⚓═══════════════════════════════════════════════⚓🌊\n"
            )

            time.sleep(1)

            print(
                "⚔️🛡️ Relatório de Danos da Frota ⚓🚢\n"
                f"Submarinos aliados afundados: {submarinos_aliados_afundados} 🐋\n"
                f"Destroiers aliados afundados: {destroiers_aliados_afundados} 🚢\n"
                f"Cruzadores aliados afundados: {cruzadores_aliados_afundados} ⛴️\n"
                f"Encouraçados aliados afundados: {encouracados_aliados_afundados} 🛳️\n"
                "🌊⚓═══════════════════════════════════════════════⚓🌊\n"
            )

        # ADVERSÁRIO GANHOU
        elif vencedor == 2:
            print(
                "\n🌊⚓═══════════════════════════════════════════════⚓🌊\n"
                "💀🏴‍☠️ ALERTA, Capitão! O adversário venceu! ⚔️🚢\n"
                "Nossa frota foi derrotada nos mares! 🌊🔥🧭\n"
                "🌊⚓═══════════════════════════════════════════════⚓🌊\n"
            )
            time.sleep(1)

            print(
                "⚔️🛡️ Relatório de Perdas da Frota ⚓🚢\n"
                f"Submarinos aliados afundados: {submarinos_aliados_afundados} 🐋\n"
                f"Destroiers aliados afundados: {destroiers_aliados_afundados} 🚢\n"
                f"Cruzadores aliados afundados: {cruzadores_aliados_afundados} ⛴️\n"
                f"Encouraçados aliados afundados: {encouracados_aliados_afundados} 🛳️\n"
                "🌊⚓═══════════════════════════════════════════════⚓🌊\n"
            )

            time.sleep(1)

            print(
                "🛳️⚓ Relatório de Conquistas ⚓🛳️\n"
                f"Submarinos inimigos afundados: {submarinos_inimigos_afundados} 🐋\n"
                f"Destroiers inimigos afundados: {destroiers_inimigos_afundados} 🚢\n"
                f"Cruzadores inimigos afundados: {cruzadores_inimigos_afundados} ⛴️\n"
                f"Encouraçados inimigos afundados: {encouracados_inimigos_afundados} 🛳️\n"
                "🌊⚓═══════════════════════════════════════════════⚓🌊\n"
            )

        time.sleep(2)
        print(
            "\n🌊⚓═══════════════════════════════════════════════⚓🌊\n"
            "🧭 Capitão, após a batalha, nossa inteligência revelou a antiga localização de todos os navios inimigos! ⚓🚢\n"
            "Use essas informações para planejar futuras estratégias e dominar os mares! 🌊⚔️🔥\n"
            "🌊⚓═══════════════════════════════════════════════⚓🌊\n"
        )
        time.sleep(0.5)
        desenhar_minimapa(estado_jogo["matriz_partida_jogador2"])

        time.sleep(1)
        decisao = input("🧭 Capitão, deseja zarpar novamente para uma nova batalha? ⚓🚢 (Sim ou Não): ")
        decisao = decisao.lower().replace(" ", "")

        decisao_nao_feita = True
        while decisao_nao_feita:
            if (
                decisao == "sim"
                or decisao == "s"
                or decisao == "si"
                or decisao == "yes"
                or decisao == "ye"
                or decisao == "y"
            ):
                time.sleep(1)
                print("🌊⚓ Recomeçando a batalha. ⚓🚢")
                time.sleep(0.5)
                print("🌊⚓ Recomeçando a batalha.. ⚓🚢")
                time.sleep(0.5)
                print("🌊⚓ Recomeçando a batalha... ⚓🚢")
                time.sleep(0.5)
                print("🌊⚓ Recomeçando a batalha.... ⚓🚢")
                time.sleep(1)
                print("\n\n\n")

                decisao_nao_feita = False
                break

            elif (
                decisao == "não"
                or decisao == "nao"
                or decisao == "na"
                or decisao == "n"
                or decisao == "no"
            ):
                time.sleep(1)
                print("⚓🚢 Obrigado por jogar, Capitão! 🌊🧭")
                time.sleep(1)
                print("⚓ Finalizando a batalha e recolhendo a frota... ⚔️🔥")
                time.sleep(2)

                decisao_nao_feita = False
                jogo_loopando = False
                break


main()