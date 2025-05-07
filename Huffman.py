import heapq

class Node:
    def __init__(self, symbol=None, freq=None):
        self.symbol = symbol
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq
    
def binaryTree(chars, freq):
    queue = [Node(char, f) for char, f in zip(chars, freq)]
    heapq.heapify(queue)

    while len(queue) > 1:
        left = heapq.heappop(queue)
        right = heapq.heappop(queue)
        node = Node(freq=left.freq + right.freq)
        node.left = left
        node.right = right
        heapq.heappush(queue, node)

    return queue[0]
    
def generateCode(node, code='', huffmanCode={}):
    if node is not None:
        if node.symbol is not None:
            huffmanCode[node.symbol] = code
        generateCode(node.left, code + '0', huffmanCode)
        generateCode(node.right, code + '1', huffmanCode)
    return huffmanCode

def encoder(text):
    freq = {}
    for c in text:
        freq[c] = freq.get(c, 0) + 1
    chars = list(freq.keys())
    freqs = list(freq.values())
    root = binaryTree(chars, freqs)
    codes = generateCode(root)
    encoded = ''.join(codes[c] for c in text)
    return encoded, codes

def decoder(huffman_code, codes):
    reverse_codes = {v: k for k, v in codes.items()}
    result = ''
    current = ''
    for bit in huffman_code:
        current += bit
        if current in reverse_codes:
            result += reverse_codes[current]
            current = ''
    return result

def calculateRatios(original_string, huffman_code):
    original_bits = len(original_string) * 8
    compressed_bits = len(huffman_code)
    compress_ratio = original_bits / compressed_bits
    saving_space = 1 - (compressed_bits / original_bits)
    
    return compress_ratio, saving_space

if __name__ == '__main__':
    text = input("Enter the text: ")

    huffmanCode, code = encoder(text)
    decoded = decoder(huffmanCode, code)
    compressRatio, savingSpace = calculateRatios(text, huffmanCode)

    print("Texto codificado: ", huffmanCode)
    print("Texto decodificado: ", decoded)
    print("Taxa de compressão: ", compressRatio)
    print("Espaço salvo:", savingSpace, " Porcentagem:", savingSpace * 100, "%")