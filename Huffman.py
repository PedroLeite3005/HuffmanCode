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
    counts = {}
    for char in text:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1

    raiz = binaryTree(counts)
    codigos = generateCode(raiz)
    huffman_code = ''.join(codigos[c] for c in text)
    return huffman_code, codigos

def decoder(huffmanCode, code):
    invertCode = {v: k for k, v in code.items()}
    current = ''
    result = ''
    for bit in huffmanCode:
        current += bit
        if current in invertCode:
            result += invertCode[current]
            current = ''
    return result

def calculateRatios(originalString,huffmanCode):
    originalBits = len(originalString) * 8
    compressedBits = len(huffmanCode) * 8

    print("ASCI: ", originalBits, "Huffman bits: ", compressedBits)

    compressRatio = originalBits / compressedBits
    savingSpace = 1 - compressedBits/originalBits
    
    return compressRatio, savingSpace

if __name__ == '__main__':
    text = input("Enter the text: ")

    huffmanCode, code = encoder(text)
    decoded = decoder(huffmanCode, code)
    compressRatio, savingSpace = calculateRatios(text, huffmanCode)

    print("Texto codificado: ", huffmanCode)
    print("Texto decodificado: ", decoded)
    print("Taxa de compressão: ", compressRatio)
    print("Espaço salvo:", savingSpace)