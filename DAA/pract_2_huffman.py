class node:
    def __init__(self):
        self.freq = 0
        self.symbol = ''
        self.left = ''
        self.right = ''
        self.is_leaf = False
        
    def create_leaf(self,symbol:str,freq:int)->None:
        self.is_leaf = True
        self.symbol = symbol
        self.freq = freq
        self.left = None
        self.right = None
        
    def create_node(self,freq,left,right):
        self.is_leaf = False
        self.freq = freq
        self.left = left
        self.right = right
        self.symbol = None
        
def insert_node(arr : list[node],node:node)->list[node]:
    i = len(arr)-1
    arr.append(node)
    while(i>=0 and arr[i].freq < node.freq):
        arr[i+1] = arr[i]
        i-=1
    arr[i+1] = node
    return arr

code_map = {}

def generate_huffman(node:node,code:str):
    global code_map
    if(node is None):
        return
    if(node.is_leaf):
        code_map[node.symbol] = code
        return
    generate_huffman(node.left,code+'0')
    generate_huffman(node.right,code+'1')
    

def main():
    s = input("Enter the string: ")
    m = {}
    for i in s:
        if i in m:
            m[i] += 1
        else:
            m[i] = 1
    # display frequency
    print("Frequency:")
    for i,j in m.items():
        print(i,":",j) 
    
    arr = []
    for i,j in m.items():
        n = node()
        n.create_leaf(i,j)
        arr = insert_node(arr,n)
        
    while(len(arr) > 1):
        n1 = arr.pop()
        n2 = arr.pop()
        n = node()
        n.create_node(n1.freq+n2.freq,n1,n2)
        arr = insert_node(arr,n)
        
    # generate codes
    generate_huffman(arr[0],'')
    
    # print codes
    print("Huffman Codes:")
    for i,j in code_map.items():
        print(i,":",j)
        
    # string encoding
    enc = ''
    for i in s:
        enc += code_map[i] + ' '
        
    print("Encoded String:")
    print(enc)

main()
