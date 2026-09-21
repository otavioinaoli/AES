# S_BOX: AES substitution box containing 256 substitution values, organized as a 16x16 table
#        The first hexadecimal digit of the input selects the row, and the second selects the column
#        S_BOX[0xAB] = row A, column B
S_BOX = [
    0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76,
    0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59, 0x47, 0xf0, 0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0,
    0xb7, 0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1, 0x71, 0xd8, 0x31, 0x15,
    0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05, 0x9a, 0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75,
    0x09, 0x83, 0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6, 0xb3, 0x29, 0xe3, 0x2f, 0x84,
    0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b, 0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf,
    0xd0, 0xef, 0xaa, 0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c, 0x9f, 0xa8,
    0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc, 0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2,
    0xcd, 0x0c, 0x13, 0xec, 0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19, 0x73,
    0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee, 0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb,
    0xe0, 0x32, 0x3a, 0x0a, 0x49, 0x06, 0x24, 0x5c, 0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79,
    0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4, 0xea, 0x65, 0x7a, 0xae, 0x08,
    0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6, 0xb4, 0xc6, 0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a,
    0x70, 0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e, 0x61, 0x35, 0x57, 0xb9, 0x86, 0xc1, 0x1d, 0x9e,
    0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e, 0x94, 0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf,
    0x8c, 0xa1, 0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f, 0xb0, 0x54, 0xbb, 0x16
]

INV_S_BOX = [
    0x52, 0x09, 0x6a, 0xd5, 0x30, 0x36, 0xa5, 0x38, 0xbf, 0x40, 0xa3, 0x9e, 0x81, 0xf3, 0xd7, 0xfb,
    0x7c, 0xe3, 0x39, 0x82, 0x9b, 0x2f, 0xff, 0x87, 0x34, 0x8e, 0x43, 0x44, 0xc4, 0xde, 0xe9, 0xcb,
    0x54, 0x7b, 0x94, 0x32, 0xa6, 0xc2, 0x23, 0x3d, 0xee, 0x4c, 0x95, 0x0b, 0x42, 0xfa, 0xc3, 0x4e,
    0x08, 0x2e, 0xa1, 0x66, 0x28, 0xd9, 0x24, 0xb2, 0x76, 0x5b, 0xa2, 0x49, 0x6d, 0x8b, 0xd1, 0x25,
    0x72, 0xf8, 0xf6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xd4, 0xa4, 0x5c, 0xcc, 0x5d, 0x65, 0xb6, 0x92,
    0x6c, 0x70, 0x48, 0x50, 0xfd, 0xed, 0xb9, 0xda, 0x5e, 0x15, 0x46, 0x57, 0xa7, 0x8d, 0x9d, 0x84,
    0x90, 0xd8, 0xab, 0x00, 0x8c, 0xbc, 0xd3, 0x0a, 0xf7, 0xe4, 0x58, 0x05, 0xb8, 0xb3, 0x45, 0x06,
    0xd0, 0x2c, 0x1e, 0x8f, 0xca, 0x3f, 0x0f, 0x02, 0xc1, 0xaf, 0xbd, 0x03, 0x01, 0x13, 0x8a, 0x6b,
    0x3a, 0x91, 0x11, 0x41, 0x4f, 0x67, 0xdc, 0xea, 0x97, 0xf2, 0xcf, 0xce, 0xf0, 0xb4, 0xe6, 0x73,
    0x96, 0xac, 0x74, 0x22, 0xe7, 0xad, 0x35, 0x85, 0xe2, 0xf9, 0x37, 0xe8, 0x1c, 0x75, 0xdf, 0x6e,
    0x47, 0xf1, 0x1a, 0x71, 0x1d, 0x29, 0xc5, 0x89, 0x6f, 0xb7, 0x62, 0x0e, 0xaa, 0x18, 0xbe, 0x1b,
    0xfc, 0x56, 0x3e, 0x4b, 0xc6, 0xd2, 0x79, 0x20, 0x9a, 0xdb, 0xc0, 0xfe, 0x78, 0xcd, 0x5a, 0xf4,
    0x1f, 0xdd, 0xa8, 0x33, 0x88, 0x07, 0xc7, 0x31, 0xb1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xec, 0x5f,
    0x60, 0x51, 0x7f, 0xa9, 0x19, 0xb5, 0x4a, 0x0d, 0x2d, 0xe5, 0x7a, 0x9f, 0x93, 0xc9, 0x9c, 0xef,
    0xa0, 0xe0, 0x3b, 0x4d, 0xae, 0x2a, 0xf5, 0xb0, 0xc8, 0xeb, 0xbb, 0x3c, 0x83, 0x53, 0x99, 0x61,
    0x17, 0x2b, 0x04, 0x7e, 0xba, 0x77, 0xd6, 0x26, 0xe1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0c, 0x7d
]

# RC: the 10 round constants used in the AES-128 key expansion
#     RC[i] = round constant for round i + 1
RC = [0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1B, 0x36]

MIX_COLUMNS_MATRIX = [
    [0x02, 0x03, 0x01, 0x01],
    [0x01, 0x02, 0x03, 0x01],
    [0x01, 0x01, 0x02, 0x03],
    [0x03, 0x01, 0x01, 0x02]
]

INV_MIX_COLUMNS_MATRIX = [
    [0x0E, 0x0B, 0x0D, 0x09],
    [0x09, 0x0E, 0x0B, 0x0D],
    [0x0D, 0x09, 0x0E, 0x0B],
    [0x0B, 0x0D, 0x09, 0x0E]
]

def key_expansion(key):
    """
    Expande a chave AES de 128 bits em 44 words, agrupadas em 11 chaves de rodada, com 4 words por chave
    Cada palavra contém 4 bytes

    Parâmetros:
        key: lista contendo os 16 bytes da chave original AES-128

    Retorna:
        W: lista contendo as 44 words expandidas da chave
    """

    W = [None] * 44

    # Copia a chave original para as quatro primeiras words
    W[0] = key[0:4]
    W[1] = key[4:8]
    W[2] = key[8:12]
    W[3] = key[12:16]

    # Gera as 40 words restantes
    for i in range(1, 11):
        # A primeira word de cada chave de rodada usa g() antes da operação XOR
        W[4 * i] = xor(W[4 * (i - 1)], g(W[4 * i - 1], i))

        # Gera as outras três palavras da chave de rodada
        for j in range(1, 4):
            W[4 * i + j] = xor(W[4 * i + j - 1], W[4 * (i - 1) + j])

    return W

def key_addition(block, round_key):
    """
    Aplica a transformação AddRoundKey fazendo XOR de cada byte
    do estado com o byte correspondente da chave de rodada.

    Parâmetros:
        block: lista 4x4 contendo os bytes do estado AES
        round_key: lista 4x4 contendo os bytes da chave de rodada

    Retorna:
        block: o estado após aplicar a transformação AddRoundKey
    """

    for i in range(4):
        for j in range(4):
            block[i][j] = block[i][j] ^ round_key[j][i]

    return block

def byte_substitution(block, c):
    """
    Aplica a substituição S-box da AES a cada byte de um bloco 4x4.

    Parâmetros:
        block: lista 4x4 contendo os bytes do estado AES

    Retorna:
        block: bloco após aplicar a substituição S-box
    """

    for i in range (4):
        for j in range (4):
            if(c == 0): # cifragem
                block[i][j] = S_BOX[block[i][j]]
            elif(c == 1): # decifragem
                block[i][j] = INV_S_BOX[block[i][j]]

    return block

def shiftrows(block, c):
    """
    Aplica a transformação ShiftRows a um estado AES 4x4.
    Cada linha é deslocada ciclicamente de acordo com seu índice:
        linha 0 → deslocada 0 posições
        linha 1 → deslocada 1 posição
        linha 2 → deslocada 2 posições
        linha 3 → deslocada 3 posições

    Parâmetros:
        block: lista 4x4 contendo os bytes do estado AES
        c: direção do deslocamento: 0 para a esquerda (criptografia) e 1 para a direita (descriptografia)

    Retorna:
        y: novo bloco 4x4 após aplicar a transformação
    """

    y = [row[:] for row in block]

    for i in range(4):
        for j in range(4):
            if c == 0: # cifragen
                new_j = (j - i) % 4
            else: # decifragem
                new_j = (j + i) % 4

            y[i][new_j] = block[i][j]

    return y

def matrix_multiplier_aux(element_line, element_column):
    """
    Multiplica dois elementos do corpo finito da AES em GF(2^8) usando o polinômio irredutível.

    Parâmetros:
        element_line: o primeiro elemento a ser multiplicado
        element_column: o segundo elemento a ser multiplicado

    Retorna:
        result: o produto representado como valor hexadecimal
    """

    e1 = bin(element_line)[2:].zfill(8)
    e2 = bin(element_column)[2:].zfill(8)

    result = 0

    # Se o bit atual de e2 for 1, adiciona e1 deslocado
    # para a posição correspondente
    for l in range(7, -1, -1):
        if(e2[l] == '1'):
            result ^= int(e1, 2) << 7 - l

    # Polinomio primo 
    # m(x) = x^8 + x^4 + x^3 + x + 1
    pp = 0b100011011

    # Enquanto o resultado tiver grau maior ou igual ao polinômio
    # usado na redução, realiza a divisão polinomial usando XOR
    while result.bit_length() >= pp.bit_length():
        result ^= pp << (result.bit_length() - pp.bit_length())

    return hex(result)


def matrix_multiplier(matrix1, matrix2):
    """
    Multiplica duas matrizes 4x4 sobre o corpo finito da AES.

    Parâmetros:
        matrix1: matriz da esquerda
        matrix2: matriz da direita

    Retorna:
        matrix_result: a matriz produto
    """

    matrix_result = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
    for i in range (4):
        for j in range (4):
            for k in range (4):
                matrix_result[i][j] ^= int(matrix_multiplier_aux(matrix1[i][k], matrix2[k][j]), 16)

    return matrix_result

def mixcolumm(block, c):
    """
    Aplica a transformação MixColumns a um estado AES 4x4.

    Parâmetros:
        block: a matriz atual do estado AES
        c: seletor de direção, em que 0 aplica o MixColumns padrão e
           1 aplica a transformação inversa MixColumns

    Retorna:
        block: o estado após a operação MixColumns
    """

    if c == 0: # cifragem
        return matrix_multiplier(MIX_COLUMNS_MATRIX, block)

    # decifragem
    return matrix_multiplier(INV_MIX_COLUMNS_MATRIX, block)

def g(W, i_round):
    """
    Aplica a função g() em uma palavra de 4 bytes.

    Parâmetros:
        W: uma lista com uma palavra de 4 bytes
        i_round: índice da rodada, começando em 1
    Retorna:
        W: a palavra transformada
    """

    # RotWord: rotaciona a palavra um byte para a esquerda
    W = W[1:] + W[:1]

    # SubWord: aplica a S-box a cada byte
    for i in range (4):
        W[i] = S_BOX[W[i]]

    # Round Constant: faz XOR do primeiro byte com a constante da rodada
    W[0] = W[0] ^ RC[i_round-1]

    return W

def xor(w1, w2):
    """
    Aplica a operação XOR entre duas palavras de 4 bytes.

    Parâmetros:
        w1: lista contendo a primeira palavra de 4 bytes
        w2: lista contendo a segunda palavra de 4 bytes

    Retorna:
        result: lista contendo o resultado do XOR byte a byte
    """

    result = [None] * 4

    for i in range(4):
        result[i] = w1[i] ^ w2[i]

    return result


def pad(text):
    """
    Adiciona padding PKCS#7 para que o tamanho do texto seja múltiplo de 16 bytes.

    Parâmetros:
        text: bytes a serem preenchidos

    Retorna:
        text: bytes com padding
    """

    # calcula o quanto falta para completar o bloco 
    padding_size = 16 - (len(text) % 16)

    # adiciona ao texto o valor do padding repetido padding_size vezes 
    # (se o texto já for múltiplo de 16, adiciona um bloco inteiro de padding)
    text = text + bytes([padding_size]) * padding_size

    # ex.: len(text) = 17
    # padding_size = 16 - (17 % 16) = 15
    # bytes([15]) = 0F
    # text + 0F (x15)

    return text


def unpad(text):
    """
    Remove o padding PKCS#7 do texto quando ele estiver presente.

    Parâmetros:
        text: bytes com padding

    Retorna:
        text: bytes originais sem o padding PKCS#7, se for válido
    """

    # último elemento informa o tamanho do padding
    padding_size = text[-1]

    # verifica se os últimos bytes realmente são o padding e remove
    if 1 <= padding_size <= 16 and text.endswith(bytes([padding_size]) * padding_size):
        return text[:-padding_size]

    return text

def to_bytes(block):
    """
    Converte um estado AES 4x4 em bytes.

    Parâmetros:
        block: lista 4x4 contendo o estado AES

    Retorna:
        text: os bytes representados pelo estado
    """

    text = []

    for j in range(4):
        for i in range(4):
            text.append(block[i][j])

    return bytes(text)
    
def to_block(block, text, base):
    """
    Converte 16 bytes de texto em um estado AES 4x4.

    Parâmetros:
        block: lista 4x4 com o estado AES
        text: bytes com os dados de entrada
        base: índice inicial do bloco em bytes

    Retorna:
        block: o estado AES 4x4
    """

    i_block = 0

    for j in range(4):
        for i in range(4):
            block[i][j] = text[base + i_block]
            i_block += 1

    return block

def encrypt_block(block, key):
    """
    Criptografa um único bloco AES de 16 bytes.

    Parâmetros:
        block: bloco de estado AES 4x4 a ser criptografado
        key: chave original de 128 bits

    Retorna:
        cipher_block: bloco criptografado de 16 bytes
    """

    # lista das 44 words de 4 bytes
    W = key_expansion(list(key))

    # Round 1
    block = key_addition(block, W[0:4])
    block = byte_substitution(block, 0)
    block = shiftrows(block, 0)
    block = mixcolumm(block, 0)
    block = key_addition(block, W[4:8])

    # Rounds 2 to 9
    for i in range (8, 40, 4): # i começa em 8 e pula de 4 em 4 words
        block = byte_substitution(block, 0)
        block = shiftrows(block, 0)
        block = mixcolumm(block, 0)
        block = key_addition(block, W[i : i+4])

    # Round 10
    block = byte_substitution(block, 0)
    block = shiftrows(block, 0)
    block = key_addition(block, W[40 : 44]) # última word

    return to_bytes(block)

def encrypt(plaintext, key):
    """
    Criptografa uma mensagem em texto claro com padding PKCS#7.

    Parâmetros:
        plaintext: bytes a serem criptografados
        key: chave original de 128 bits

    Retorna:
        ciphertext: bytes criptografados
    """

    # insere o padding no texto claro
    plaintext = pad(plaintext)

    # cria uma sequência vazia de bytes
    ciphertext = b""

    # indica o início do bloco de 16 bytes atual
    base = 0

    while base < len(plaintext):
        block = [
            [0x00, 0x00, 0x00, 0x00],
            [0x00, 0x00, 0x00, 0x00],
            [0x00, 0x00, 0x00, 0x00],
            [0x00, 0x00, 0x00, 0x00]
        ]
        block = to_block(block, plaintext, base)
        ciphertext += encrypt_block(block, key)
        base += 16

    return ciphertext

def decrypt_block(block, key):
    """
    Descriptografa um único bloco AES de 16 bytes.

    Parâmetros:
        block: bloco de estado AES 4x4 a ser descriptografado
        key: chave original de 128 bits

    Retorna:
        plain_block: bloco descriptografado de 16 bytes
    """

    W = key_expansion(list(key))

    # Round 1
    block = key_addition(block, W[40 : 44]) # começa usando a última word
    block = shiftrows(block, 1)
    block = byte_substitution(block, 1)

    # Rounds 2 to 9
    for i in range (36, 4, -4): # i começa em 36 e diminui de 4 em 4
        block = key_addition(block, W[i : i + 4])
        block = mixcolumm(block, 1)
        block = shiftrows(block, 1)
        block = byte_substitution(block, 1)
        
    # Round 10
    block = key_addition(block, W[4:8])
    block = mixcolumm(block, 1)
    block = shiftrows(block, 1)
    block = byte_substitution(block, 1)
    block = key_addition(block, W[0:4])

    return to_bytes(block)


def decrypt(ciphertext, key):
    """
    Descriptografa uma mensagem cifrada e remove o padding PKCS#7.

    Parâmetros:
        ciphertext: bytes criptografados a serem descriptografados
        key: chave original de 128 bits

    Retorna:
        plaintext: bytes descriptografados e sem padding
    """

    plaintext = b""

    base = 0
    while(base < len(ciphertext)):
        block = [
            [0x00, 0x00, 0x00, 0x00],
            [0x00, 0x00, 0x00, 0x00],
            [0x00, 0x00, 0x00, 0x00],
            [0x00, 0x00, 0x00, 0x00]
        ]
        block = to_block(block, ciphertext, base)
        plaintext += decrypt_block(block, key)
        base += 16

    # retorna o texto claro com o padding removido, se houver
    return unpad(plaintext)