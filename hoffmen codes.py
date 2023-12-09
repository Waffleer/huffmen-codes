
class Node():
    key = ""
    value = 0
    left = None
    right = None

    def __init__(self, value) -> None:
        self.value = value

    def __str__(self) -> str:
        
        if(not self.left == None and not self.right == None):
            return f"{self.key}|{self.value} - left: ( {self.left} ) - right: ( {self.right} )"
        else:
            return f"{self.key}|{self.value}"


"""
weights = {"a": .35,
           "b": .1,
           "c": .2,
           "d": .2,
           "-": .15           
           }
"""




def fileToText(path: str) -> str:
    ret = ""
    f = open(f"{path}.txt", "r")
    for x in f:
        ret = ret + x
    f.close()
    return ret

def doubleChartoWeight(text: str) -> dict:
    weights = {}
    for x in text: #Gets weights for single value 
        if(x in weights.keys()):
            weights.update({x: weights[x]+1})
        else:
            weights.update({x: 1})
    return weights

def singleChartoWeight(text: str) -> dict:
    weights = {}
    for x in text: #Gets weights for single value 
        if(x in weights.keys()):
            weights.update({x: weights[x]+1})
        else:
            weights.update({x: 1})
    return weights

def weightsToNodes(weights: dict) -> list:
    nodes = []
    for x in list(weights.keys()):
        n = Node(0)
        n.key = x
        n.value = weights[x]
        nodes.append(n)
    return nodes

def huffmaneImplementation(nodes: list):
    while(len(nodes) > 1): #Huffman Implementation
        #print("-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-")
        #Find two smallest nodes
        a = 0 #Smallest
        b = 1 #2nd Smallest
        for x in range(2, len(nodes)):
            
            if(nodes[a].value > nodes[x].value):
                a = x
                continue
            if(nodes[b].value > nodes[x].value):
                b = x
        #print(f"a: {a}")
        #print(f"b: {b}")

        if(nodes[a].value > nodes[b].value): #Makes sure a is the smallest
            c = b
            b = a
            a = c

        #Combine two nodes
        c = Node(0)
        c.value = nodes[a].value + nodes[b].value
        c.left = nodes[a]
        c.right = nodes[b]

        #Remove a&b from index
        if(a>b):
            nodes.pop(a)
            nodes.pop(b)
        else:
            nodes.pop(b)
            nodes.pop(a)
        nodes.append(c) #add c to nodes list
        #break
        #print("----------------------------")
        #for x in nodes:
        #    print(x)
    return nodes[0]

def navigate(node: Node, running: str, ret: dict):
    if(node.left == None and node.right == None):
        ret.update({node.key: running})
    else:
        r1 = running + "0"
        r2 = running + "1"
        navigate(node.left,r1,ret)
        navigate(node.right,r2,ret)

def encodeToFile(encodeKey: dict, text: str, filePath: str) -> None:
    f = open(f"{filePath}-encoded.txt", "w")

    f.write(str(encodeKey))
    f.write("\n\n")

    for x in text:
        f.write(encodeKey[x])
    f.close
#print(tree)

def singleCharEncode(filePath: str):
    text = fileToText(filePath)
    weights = singleChartoWeight(text)
    print(f"Weights:  {weights}")
    encodeKey = {}
    navigate(huffmaneImplementation(weightsToNodes(weights)),"",encodeKey)
    encodeToFile(encodeKey,text,filePath)
    print(f"EncodeKey:  {encodeKey}")

def doubleCharEncode(filePath: str):
    text = fileToText(filePath)
    weights = doubleChartoWeight(text)
    print(f"Weights:  {weights}")
    encodeKey = {}
    navigate(huffmaneImplementation(weightsToNodes(weights)),"",encodeKey)
    encodeToFile(encodeKey,text,filePath)
    print(f"EncodeKey:  {encodeKey}")

singleCharEncode("IHaveADream")