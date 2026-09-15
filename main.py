# Letícia Ramos e Otávio Inácio - GRUPO 02
# 
# AES para chaves de 128 bits

from func import *

# cifragem: chave (string ou hexadecimal)
op = 0
key = ""
plaintext = ""
hexa = ""
string = ""


while (op != 1 and op != 2):
    op = int(input("Escolha uma das opções para a sua chave de 128 bits:\n" "1- String\n2- Hexadecimal\nOpção: "))

if (op == 1):
    while (len(string) != 16):
        string = input("\nDigite uma chave com 128 bits (16 caracteres): ")
        key = string
elif (op == 2):
    while (len(hexa) != 32):
        hexa = input("\nDigite uma chave com 128 bits (32 digitos): ")
        key = hexa

plaintext = input("\nMuito bem!\nAgora escreva a mensagem a ser cifrada: ")
size = len(plaintext)

ciphertext = encrypt(plaintext, key)

print("\nCriptografando...\nMensagem criptografa: " + ciphertext)


# decifragem ...





