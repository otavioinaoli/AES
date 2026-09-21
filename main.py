"""
Letícia Ramos e Otávio Inácio - GRUPO 02

IMPLEMENTAÇÃO DO ALGORITMO AES PARA CHAVES DE 128 BITS
________________________________________________________________________________________

Compilação/execução: execute o arquivo main.py com Python 3: python main.py'

Requisitos: apenas o Python 3.x e a biblioteca padrão do sistema

Funcionalidades: cifragem e decifragem em modo de bloco AES-128

Parâmetros: 
    Durante a execução, a aplicação solicita:
    - a mensagem e seu formato de entrada
    - a chave de 128 bits
    - o formato da saída

    Cifragem:
        - mensagem: string
        - chave: string ASCII de 16 caracteres ou hexadecimal de 32 dígitos

    Decifragem:
        - mensagem cifrada: decimal ou hexadecimal
        - chave: string ASCII de 16 caracteres ou hexadecimal de 32 dígitos
"""

from func import *

def menu():
    print("\n-----------------"
          "\n1- 🔐 Cifragem"
          "\n2- 🔓 Decifragem"
          "\n3- 🚪🚶 Sair"
          "\n-----------------")

    mode = -1
    while mode not in [1, 2, 3]:
        mode = int(input("\nEscolha a opção: "))

        if mode not in [1, 2, 3]:
            print("\nOpção inválida!")

    return mode


def get_key():
    op = -1
    key = ""

    while op not in [1, 2]:
        print("\nEscolha o formato da sua chave de 128 bits:\n"
            "1- String\n"
            "2- Hexadecimal")
        op = int(input("Opção: "))

        if op not in [1, 2]:
            print("\nOpção inválida!")

    # chave informada como string
    if op == 1:
        while True:
            key = input("\nInsira a chave de 128 bits (string): ")

            # validação de tamanho (16 caracteres ASCII = 16 bytes = 128 bits)
            if len(key) == 16 and key.isascii():
                break
            print("\nTamanho inválido! A chave deve possuir exatamente 16 caracteres ASCII.")

        # string -> bytes
        key = key.encode("ascii")

    # chave informada como hexadecimal
    else:
        while True:
            key = input("\nDigite a chave com 128 bits (hexadecimal): ").lower()

            # validação de formato e tamanho (32 dígitos hexadecimais × 4 bits = 128 bits)
            if len(key) == 32 and all(c in "0123456789abcdef" for c in key):
                break

            print("Chave inválida! Ela deve possuir exatamente 32 dígitos hexadecimais.")

        key = bytes.fromhex(key)

    return key

def main():
    print("Bem-vindo(a) ao sistema de criptografia baseado no algoritmo AES (Advanced Encryption Standard)!")

    while True:
        mode = menu()

        match mode:
            case 1:
                print("\n-------------- MODO CIFRAGEM --------------")

                # solicita a mensagem a ser cifrada
                plaintext = input("\nInsira a mensagem a ser cifrada (string): ")

                # string -> bytes
                plaintext = plaintext.encode("utf-8")

                # solicita a chave e chama o método de cifragem
                ciphertext = encrypt(plaintext, get_key())

                # escolhe o formato da saída
                out = -1
                while out not in [1, 2]:
                    print("\nEscolha o formato de saída desejado para a mensagem cifrada:"
                        "\n1- Hexadecimal"
                        "\n2- Decimal")
                    out = int(input("Opção: "))

                    if out not in [1, 2]:
                        print("Opção inválida!")

                print("\nCriptografando...\n")

                # saída em hexadecimal
                if out == 1:
                    print(f"Mensagem cifrada (hexadecimal): {ciphertext.hex().upper()}")

                # saída em decimal
                else:
                    dec = int.from_bytes(ciphertext, byteorder="big")
                    print(f"Mensagem cifrada (decimal): {dec}")


            case 2:
                print("\n-------------- MODO DECIFRAGEM --------------")

                # escolhe o formato da mensagem cifrada
                op = -1

                while op not in [1, 2]:
                    print("\nEscolha o formato da mensagem cifrada:\n"
                        "1- Decimal\n"
                        "2- Hexadecimal")

                    op = int(input("Opção: "))

                    if op not in [1, 2]:
                        print("Opção inválida!")

                ciphertext = input("\nInsira a mensagem cifrada: ")

                if op == 1:
                    # decimal -> bytes
                    ciphertext = int(ciphertext)
                    num_bytes = (ciphertext.bit_length() + 7) // 8
                    num_bytes = ((num_bytes + 15) // 16) * 16
                    ciphertext = ciphertext.to_bytes(num_bytes, byteorder="big")
                else:
                    # hexadecimal -> bytes
                    ciphertext = bytes.fromhex(ciphertext)

                # solicita a chave e chama o método de decifragem
                deciphered_text = decrypt(ciphertext, get_key())

                # escolhe o formato da saída
                out = -1
                while out not in [1, 2]:
                    print("\nEscolha o formato de saída desejado para a mensagem decifrada:"
                        "\n1- String"
                        "\n2- Hexadecimal")

                    out = int(input("Opção: "))

                    if out not in [1, 2]:
                        print("Opção inválida!")

                print("\nDescriptografando...\n")

                # saída como string
                if out == 1:
                    print(f"Mensagem decifrada (string): {deciphered_text.decode('utf-8')}")

                # saída em hexadecimal
                else:
                    print(f"Mensagem decifrada (hexadecimal): {deciphered_text.hex().upper()}")

            case 3:
                print("\nSaindo...")
                break


if __name__ == "__main__":
    main()