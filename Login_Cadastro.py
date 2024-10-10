nome = input("Digite seu nome:")
senha = input("Crie uma senha:")
confirmar_senha = input("Repita sua senha:")

if senha == confirmar_senha:
    print("Senha cadastrada!")


while confirmar_senha != senha:
    print("Sua senha está diferente! Repita sua senha novamente")
    confirmar_senha = input("Repita sua senha:")