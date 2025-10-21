personagem = "Sasuke"
chakra = 50
modo = "Rinnegan"

if personagem == "Sasuke" and chakra >= 50:
    if modo == "Sharingan":
        print("Sasuke ativa o Sharingan e contra-ataca!")
    elif modo == "Rinnegan":
        print("Sasuke usa o Rinnegan para teletransporte.")
    else:
        print("Modo desconhecido.")
else:
    print("Sasuke está exausto ou não é o personagem escolhido.")