
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
    check = ""
    cycle = ""
    for x in range(1,len(text)):
        check = text[x-1] + text[x]
        if(check in weights.keys()): #makes sure their isn't a double check
            continue
        for y in range(1,len(text)):
            cycle = text[y-1] + text[y]
            if(check == cycle):
                if(check in weights.keys()):
                    weights.update({check: weights[check]+1})
                else:
                    weights.update({check: 1})

    if(not len(text)%2 == 0): #if their is an odd number of characters then their will be on with no pair
        weights.update({text[-1]: 1})

    # extrastr = ""
    # c=1
    # print(weights.keys())

    # while(c < len(text)):
    #     if()
    #     check = text[c-1] + text[c]
        
    #     if(check in list(weights.keys())):
    #         c = c+2
    #     else:
    #         extrastr = extrastr + text[c]
    #         c = c+1
    #     print(f"c: {c} | check: {check} | extrastr: {extrastr}")
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


def encodeToFileSingle(encodeKey: dict, text: str, filePath: str) -> None:


    writeStr = ""
    

    for x in text:
        writeStr = writeStr + encodeKey[x]
    print(f"Lenght: {len(writeStr)}")
    f = open(f"{filePath}-encoded.txt", "w")
    f.write(str(encodeKey))
    f.write("\n\n")
    f.write(writeStr)
    f.close
def encodeToFileDouble(encodeKey: dict, text: str, filePath: str) -> None:
    
    usedEncode = {}
    writeStr = ""
    for c in range(1,len(text),2):
        check = text[c-1] + text[c]
        writeStr = writeStr + encodeKey[check]
        usedEncode.update({check: encodeKey[check]})
        #print(f"c: {c} | check: {check}")
    if(not len(text)%2 == 0):
        writeStr = writeStr + encodeKey[text[-1]]
        usedEncode.update({text[-1]: encodeKey[text[-1]]})

    print(f"Length: {len(writeStr)}")

    f = open(f"{filePath}-encoded.txt", "w")
    f.write(str(usedEncode))
    f.write("\n\n")
    f.write(writeStr)
    f.close()

def singleCharEncode(filePath: str):
    text = fileToText(filePath)
    weights = singleChartoWeight(text)
    #print(f"Weights:  {weights}")
    encodeKey = {}
    navigate(huffmaneImplementation(weightsToNodes(weights)),"",encodeKey)
    encodeToFileSingle(encodeKey,text,filePath)
    #print(f"EncodeKey:  {encodeKey}")

def doubleCharEncode(filePath: str):
    text = fileToText(filePath)
    weights = doubleChartoWeight(text)
    #print(f"Weights:  {weights}")
    encodeKey = {}
    navigate(huffmaneImplementation(weightsToNodes(weights)),"",encodeKey)
    encodeToFileDouble(encodeKey,text,filePath)
    #print(f"EncodeKey:  {encodeKey}")

def examine(filePath:str):
    print(f"Text ascii {len(fileToText(filePath)) * 7}bits")

    print("Single Encode ",end="")
    singleCharEncode(filePath) 
    print("Pair Encode ",end="")
    doubleCharEncode(filePath)

examine("test")

#Manifesto of the Communist Party
#Total Chars 216897 * 7bit ascii encoding = 1518279 bits
#Single Char encoding 978666
#Pair Char Encoding 863588
# 1518279
#  978666
#  863588