# Huffman
## pt-BR

Implementação do algoritmo de compressão de Huffman em Python para compactar textos com base na frequência dos caracteres.

### Funcionalidades

- **Encoder**: Recebe uma string e gera:
  - Texto codificado em binário (Huffman)
  - Dicionário de códigos binários por caractere

- **Decoder**: Reconstrói o texto original a partir do código e dicionário

- **Estatísticas**:
  - Taxa de compressão
  - Espaço economizado comparado ao ASCII (8 bits por caractere)

### Como usar

Execute o script e insira o texto:

```bash
python huffman.py
```
Exemplo de entrada:

```
Digite o texto: exemplo de texto
```
Saída esperada:

```
Texto codificado: 0101010001...
Texto decodificado: exemplo de texto
Taxa de compressão: 1.8
Espaço salvo: 0.45
```

### Estrutura do código
-**Node:** Classe que representa um nó da árvore de Huffman.
-**binaryTree:** Constrói a árvore com base nas frequências dos caracteres.
-**generateCode:** Gera os códigos binários recursivamente.
-**encoder:** Cria a codificação de Huffman.
-**decoder:** Decodifica uma string binária com o dicionário.
-**calculateRatios:** Calcula estatísticas da compressão.

### Requisitos
-Python 3.x

### Licença
Código aberto para fins educacionais.

## en-US

Implementation of the Huffman compression algorithm in Python to compress text based on character frequency.

### Features

- **Encoder**: Takes a string and generates:
  - Text encoded in binary (Huffman)
  - Dictionary of binary codes per character

- **Decoder**: Reconstructs the original text from the code and dictionary

- **Statistics**:
  - Compression rate
  - Space saved compared to standard ASCII (8 bits per character)

### How to use

Run the script and enter the desired text:

```bash
python huffman.py
```
Example Input:

```
Digite o texto: exemplo de texto
```
Expected Output:

```
Texto codificado: 0101010001...
Texto decodificado: exemplo de texto
Taxa de compressão: 1.8
Espaço salvo: 0.45
```

### Code structure
-**Node:** Class representing a node in the Huffman tree
-**binaryTree:** Builds the tree based on character frequencies
-**generateCode:** Recursively generates binary codes
-**encoder:** Creates the Huffman encoding
-**decoder:** Decodes a binary string using the dictionary
-**calculateRatios:** Computes compression statistics

### Requirements
-Python 3.x

### License
Open source for educational purposes.
