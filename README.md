# AES-128

Implementação do algoritmo **AES (Advanced Encryption Standard)** para chaves de 128 bits.

**Autores:** Letícia Ramos e Otávio Inácio — Grupo 02

## Requisitos

* Python 3.x
* Apenas bibliotecas da biblioteca padrão do Python

## Execução

No terminal, execute:

```bash
python main.py
```

Durante a execução, o programa solicita os dados necessários para a cifragem ou decifragem.

## Entradas

### Cifragem

* Mensagem em formato de string
* Chave de 128 bits:

  * string ASCII com 16 caracteres; ou
  * hexadecimal com 32 dígitos

### Decifragem

* Mensagem cifrada em formato decimal ou hexadecimal
* Chave de 128 bits:

  * string ASCII com 16 caracteres; ou
  * hexadecimal com 32 dígitos

## Saídas

* **Cifragem:** resultado em hexadecimal ou decimal
* **Decifragem:** mensagem original em string ou hexadecimal

## Estrutura

* `main.py` — interface de execução e fluxo principal do programa
* `func.py` — funções utilizadas na implementação do AES-128
