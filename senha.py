#  Controle de fluxo para criação de senha com os seguintes parâmetros a serem seguidos:
#  - Ter pelo menos 8 caracteres
#  - Conter pelo menos um número
#  - Conter pelo menos uma letra maiúscula
#  - Conter pelo menos uma letra minúscula
#  Caso não sejam atendidas ele solicita a digitação de uma nova senha


senha = input("Digite uma senha: ")

while True:
    if len(senha) < 8:
        print("A senha deve ter pelo menos 8 caracteres")
    elif not any(char.isdigit() for char in senha):
        print("A senha deve conter pelo menos um número")
    elif not any(char.isupper() for char in senha):
        print("A senha deve conter pelo menos uma letra maiúscula")
    elif not any(char.islower() for char in senha):
        print("A senha deve conter pelo menos uma letra minúscula")
    else:
        print("Senha criada com sucesso!")
        break
    senha = input("Digite uma nova senha: ")
