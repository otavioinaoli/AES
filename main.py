# Letícia Ramos e Otávio Inácio - GRUPO 02
# 
# AES para chaves de 128 bits

from func import *

def menu():
    print ("-------------- Bem vindo(a) ao sistema de criptografia baseado no algoritmo AES (Advanced Encryption Standard)! --------------\n" \
        "1- 🔐 Cifragem\n" \
        "2- 🔓 Decifragem\n" \
        "3- 🚪🚶 Sair\n")

    mode = -1
    while mode not in [1,2,3]:
        mode = int(input("Escolha a opção: "))

    return mode

def get_key():
    op = 0
    key = ""
    keyInt = 0

    while op not in [1,2]:
        op = int(input("\nEscolha o formato da sua chave de 128 bits:\n"
                       "1- String\n" \
                       "2- Hexadecimal\n" \
                       "Opção: "))
        if op not in [1,2]:
                print ("Opção inválida!")

    if (op == 1):
        while (len(key) != 16):
            key = input("\nDigite uma chave com 128 bits (16 caracteres): ")
        key = key.encode('ascii').hex()
    elif (op == 2):
        while (len(key) != 32):
            key = input("\nDigite uma chave com 128 bits (32 digitos): ")

    return int(key, 16)

def get_text():
    op = 0
    text = ""
    keyInt = 0

    while op not in [1,2]:
        op = int(input("\nEscolha o formato da sua mensagem:\n"
                       "1- String\n" \
                       "2- Hexadecimal\n" \
                       "Opção: "))
        if op not in [1,2]:
                print ("Opção inválida!")

    if (op == 1):
        text = input("\nEscreva a mensagem a ser cifrada: ")
        text = text.encode('ascii').hex()
    elif (op == 2):
        text = input("\nEscreva a mensagem a ser cifrada: ")

    return text


def main():
    mode = menu()

    match mode:
        case 1:
            print("-------------- MODO CIFRAGEM --------------")
            # solicita a mensagem a ser cifrada (texto claro)
            # solicita a chave de 128 bits e chama o método de cifragem
            ciphertext = encrypt(get_text(), get_key())

            # escolha do formato da saída
            out = -1

            while out not in [1,2]:
                print("\nEscolha o formato de saída desejado para a mensagem cifrada:")
                print("1- Hexadecimal\n" \
                      "2- Decimal")
                out = int(input("Opção: "))
                if (out not in [1,2]):
                    print("Opção inválida!")

            print("\nCriptografando...\n")

            # retorna a mensagem criptografada em hexadecimal
            if out == 1:
                print(f"Mensagem cifrada (hexadecimal): {ciphertext}")

            # retorna a mensagem criptografada em decimal
            else:

                dec = ... # ******* HEXA ----> DECIMAL

                print(f"Mensagem cifrada (decimal): {dec}")


        case 2:
            print("-------------- MODO DECIFRAGEM --------------")

            # solicita a mensagem a ser decifrada
            ciphertext = input("\nEscreva a mensagem a ser decifrada (formato hexadecimal): ")

            # solicita a chave de 128 bits e chama o método de decifragem
            text = decrypt(ciphertext, get_key())

            # escolha do formato da saída
            out = -1

            while out not in [1,2]:
                print("\nEscolha o formato de saída desejado para a mensagem cifrada:")
                print("1- String\n" \
                      "2- Hexadecimal")
                out = int(input("Opção: "))
                if (out not in [1,2]):
                    print("Opção inválida!")

            print("\nDescriptografando...\n")

            # retorna a mensagem criptografada em hexadecimal
            if out == 1:

                string = bytes.fromhex(text).decode('ascii')

                print(f"Mensagem decifrada (string): {string}")

            # retorna a mensagem criptografada em decimal
            else:
                print(f"Mensagem decifrada (hexadecimal): {text}")

        case 3:
            print("Saindo...")

        case _:
            print("Opção inválida")


if __name__ == "__main__":
    main()