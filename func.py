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

def byte_substitution(block, c):
    """
    Applies the AES S-box substitution to every byte in a 4x4 block

    Parameters:
        block: A 4x4 list containing the bytes of the AES state

    Returns:
        block: The block after applying the S-box substitution
    """

    for i in range (4):
        for j in range (4):
            if(c == 0):
                block[i][j] = S_BOX[block[i][j]]
            elif(c == 1):
                block[i][j] = INV_S_BOX[block[i][j]]

    return block

def shiftrows_op(j, i, c):
    """
    Calculates the new column position of a byte during ShiftRows

    Parameters:
        j: original column index of the byte
        i: row index, which determines the number of positions shifted
        c: shift direction: 0 for left and 1 for right

    Returns:
        The new column index of the byte
    """

    if c == 0:
        return j - i

    return j + i

def shiftrows(block, c):
    """
    Applies the ShiftRows transformation to a 4x4 AES state
    Each row is cyclically shifted by its row index:
        row 0 → shifted by 0 positions
        row 1 → shifted by 1 position
        row 2 → shifted by 2 positions
        row 3 → shifted by 3 positions

    Parameters:
        block: a 4x4 list containing the bytes of the AES state
        c: the shift direction: 0 for left (encryption) and 1 for right (decryption)

    Returns:
        y: a new 4x4 block after applying the ShiftRows transformation
    """

    # Create a copy so that the original block is not modified
    y = [row[:] for row in block]

    for i in range (4):
        j = 0
        for k in range (4):
            y[i][shiftrows_op(j, i, c) % 4] = block[i][j]
            j += 1

    return y

#Função que faz multiplicação de 2 elementos
def matrix_multiplier_aux(element_line, element_column):
    #Converto a coluna de números hexadecimais para binário, para ver se realizo os shifts
    e1 = bin(element_line)[2:].zfill(8)
    e2 = bin(element_column)[2:].zfill(8)

    result = 0

    #Fazendo a multiplicação entre os 2 números
    for l in range(7, -1, -1):
        if(e2[l] == '1'):
            result ^= int(e1, 2) << 7 - l


    #polinomio primo m(x) =x8+x4+x3+x+1
    pp = 0b100011011

    #Realizando a divisão modular do resultado da multiplicação pelo polinomio primo    
    while result.bit_length() >= pp.bit_length():
        result ^= pp <<  (result.bit_length() - pp.bit_length())
        
    return hex(result)

#Função que faz multiplicação de matrizes     
def matrix_multiplier(matrix1, matrix2):
    matrix_result =  [
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
    if c == 0:
        return matrix_multiplier(MIX_COLUMNS_MATRIX, block)
    
    return matrix_multiplier(INV_MIX_COLUMNS_MATRIX, block)

def g(W, i_round):
    """
    Applies the g() transformation to a 4-byte word

    Parameters:
        W: a list with a 4-byte word
        i_round: the 1-based index of the round
    Returns:
        W: the transformed 4-byte word
    """
    # RotWord: rotate the word one byte to the left
    W = ((W << 8) | (W >> 24)) & 0xFFFFFFFF

    # SubWord: apply the S-box to each byte
    b0 = S_BOX[(W >> 24) & 0xFF]
    b1 = S_BOX[(W >> 16) & 0xFF]
    b2 = S_BOX[(W >> 8) & 0xFF]
    b3 = S_BOX[W & 0xFF]

    W = (b0 << 24) | (b1 << 16) | (b2 << 8) | b3

    # Round Constant: XOR the first byte with the round constant
    W ^= RC[i_round - 1] << 24

    return W


def key_expansion(key):
    """
    Expands the 128-bit AES key into 44 words, grouped into 11 round keys, with 4 words per round key
    Each word contains 4 bytes

    Parameters:
        key: a list containing the 16 bytes of the original AES-128 key

    Returns:
        W: a list containing the 44 expanded key words
    """

    W = [None] * 44

    # Copy the original key into the first four words
    W[0] = (key >> 96) & 0xFFFFFFFF
    W[1] = (key >> 64) & 0xFFFFFFFF
    W[2] = (key >> 32) & 0xFFFFFFFF
    W[3] = key & 0xFFFFFFFF

    # Generate the remaining 40 words
    for i in range(1, 11):
        # The first word of each round key uses the g() transformation before the XOR operation
        W[4 * i] = W[4 * (i - 1)] ^ g(W[4 * i - 1], i)

        # Generate the other three words of the round key
        for j in range(1, 4):
            W[4 * i + j] = W[4 * i + j - 1] ^ W[4 * (i - 1) + j]

    return W

def key_addition(block, round_key):
    """
    Applies the AddRoundKey transformation by XORing each byte
    of the state with the corresponding byte of the round key

    Parameters:
        block: a 4x4 list containing the bytes of the AES state
        round_key: a 4x4 list containing the bytes of the round key

    Returns:
        block: the state after applying the AddRoundKey transformation
    """

    for j in range(4):
        block[0][j] ^= (round_key[j] >> 24) & 0xFF
        block[1][j] ^= (round_key[j] >> 16) & 0xFF
        block[2][j] ^= (round_key[j] >> 8) & 0xFF
        block[3][j] ^= round_key[j] & 0xFF

    return block

def to_text(block):
    text = ""
    for j in range (4):
        for i in range (4):
            #transforma o block em string o 0 indica oq será preenchido nos espaços vazios e o número de caracteres e o x que deve converter para hexadecimal e minusculo 
            text += f"{block[i][j]:02x}"

    return text
    
def to_block(block, text, base):
    i_block = 0
    for j in range (4):
        for i in range (4):
            first_hexa = "0"
            second_hexa = "0"
            if(base + i_block < len(text)):
                first_hexa = text[base + i_block]
            if(base + i_block + 1 < len(text)):
                second_hexa = text[base + i_block + 1]
            block[i][j] = int(first_hexa + second_hexa, 16)
            i_block += 2
    return block

def encrypt_block(block, key):
    #Gerando as chaves
    W = key_expansion(key)
    #round 1
    block = key_addition(block, W[0:4])
    block = byte_substitution(block, 0)
    block = shiftrows(block, 0)
    block = mixcolumm(block, 0)
    block = key_addition(block, W[4:8])

    #round 2 a 9
    for i in range (8, 40, 4):
        block = byte_substitution(block, 0)
        block = shiftrows(block, 0)
        block = mixcolumm(block, 0)
        block = key_addition(block, W[i : i + 4])

    #round 10
    block = byte_substitution(block, 0)
    block = shiftrows(block, 0)
    block = key_addition(block, W[40 : 44])

    return to_text(block)

def encrypt(plaintext, key):
    cyphertext = ""

    base = 0
    while(base < len(plaintext)):
        block = [
            [0x00, 0x00, 0x00, 0x00],
            [0x00, 0x00, 0x00, 0x00],
            [0x00, 0x00, 0x00, 0x00],
            [0x00, 0x00, 0x00, 0x00]
        ]
        block = to_block(block, plaintext, base)
        cyphertext += encrypt_block(block, key)
        base += 32

    return cyphertext

def decrypt_block(block, key):
    #Gerando as chaves
    W = key_expansion(key)
    #round 1
    block = key_addition(block, W[40 : 44])
    block = shiftrows(block, 1)
    block = byte_substitution(block, 1)

    #round 2 a 9
    for i in range (36, 4, -4):
        block = key_addition(block, W[i : i + 4])
        block = mixcolumm(block, 1)
        block = shiftrows(block, 1)
        block = byte_substitution(block, 1)
        
    #round 10
    block = key_addition(block, W[4:8])
    block = mixcolumm(block, 1)
    block = shiftrows(block, 1)
    block = byte_substitution(block, 1)
    block = key_addition(block, W[0:4])

    return to_text(block)


def decrypt(ciphertext, key):
    plaintext = ""

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
        base += 32
        
    return plaintext