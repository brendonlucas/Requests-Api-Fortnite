def main():
    import requests
    nick = 'LNJ_Pote De Mel'
    # nick = 'patriota'
    link = 'https://api.fortnitetracker.com/v1/profile/'
    plataforma = 'pc'
    url = link + plataforma + '/' + nick
    headers = {"TRN-Api-Key": "9c31c8a9-af19-42e6-9b79-7065901f24a2"}
    r_player = requests.get(url, headers=headers)
    json_player = r_player.json()

    # informações do jogador
    print("Nome/Nick do jogador: " + json_player['epicUserHandle'])

    print("------ Dados das partidas Solo -----")
    print("Total de Partidas Solo: " + json_player['stats']['p2']['matches']['displayValue'])
    print("Total de Vitorias Solo: " + json_player['stats']['p2']['top1']['displayValue'])
    print("Total de Eliminações Solo: " + json_player['stats']['p2']['kills']['displayValue'])
    print()
    print("------ Dados das partidas Dupla -----")
    print("Total de Partidas Dupla: " + json_player['stats']['p10']['matches']['displayValue'])
    print("Total de Vitorias em Dupla: " + json_player['stats']['p10']['top1']['displayValue'])
    print("Total de Eliminações em Dupla: " + json_player['stats']['p10']['kills']['displayValue'])
    print()
    print("------ Dados das partidas Equipe -----")
    print("Total de Partidas em Equipe: " + json_player['stats']['p9']['matches']['displayValue'])
    print("Total de Vitorias em Equipe: " + json_player['stats']['p9']['top1']['displayValue'])
    print("Total de Eliminações em Equipe: " + json_player['stats']['p9']['kills']['displayValue'])

    # todos os dados resumo
    print(json_player['lifeTimeStats'])
    print("Total de Partidas Jogadas: " + json_player['lifeTimeStats'][7]['value'])
    print("Total de Vitorias: " + json_player['lifeTimeStats'][8]['value'])
    print("Total de Eliminações: " + json_player['lifeTimeStats'][10]['value'])

    """
    # loja
    url_loja = "https://api.fortnitetracker.com/v1/store"
    r_loja = requests.get(url_loja, headers=headers)
    json_loja = r_loja.json()
    print(" = = = =  lOJA DE ITENS DE HOJE = = = = ")
    for k in range(len(json_loja)):
        print("Item " + str(k + 1) + ':')
        print("Nome: " + json_loja[k]['name'])
        print("Preço vBucks: " + str(json_loja[k]['vBucks']) + " vBucks")
        print("Link da imagem: " + json_loja[k]['imageUrl'])
        print()
    """

    """
    # desafios temporada
    url = "https://api.fortnitetracker.com/v1/challenges"
    r2 = requests.get(url, headers=headers)
    json = r2.json()
    items = json['items']
    for i in range(len(items)):
        print("Missão " + str(i + 1) + ' - ' + items[i]['metadata'][1]['value'])
    print(r2.text)
    """

    """
    # partidas
    idplayer = json['accountId']
    link = "https://api.fortnitetracker.com/v1/profile/account/" + idplayer + '/matches'
    url = link
    r2 = requests.get(url, headers=headers)
    print(r2.text)
    """


if __name__ == '__main__':
    main()
