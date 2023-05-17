import random
import string

# Função para gerar senha
def gerar_senha(tamanho, caracteres):
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

# Função para criar menu e pedir ao usuário para escolher opções
def main():
    print("\033[1;30;42m \U0001F600 Bem-vindo ao Gerador de Senhas! \U0001F600 \033[m")

    tamanho = int(input("Digite o tamanho da senha desejada: "))

    usar_letras = input("Deseja incluir letras na senha? (s/n): ")
    usar_numeros = input("Deseja incluir números na senha? (s/n): ")
    usar_simbolos = input("Deseja incluir símbolos na senha? (s/n): ")

    caracteres = ''

    if usar_letras.lower() == 's':
        caracteres += string.ascii_letters
    if usar_numeros.lower() == 's':
        caracteres += string.digits
    if usar_simbolos.lower() == 's':
        caracteres += string.punctuation

    senha = gerar_senha(tamanho, caracteres)

    print("A senha gerada é:", senha)

if __name__ == '__main__':
    main()
