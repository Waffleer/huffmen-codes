# huffmen codes

I have two implementatinos of the huffmen codes, one that works with pairs of letter and one that does single letters. Overall the two algorithms work as intended and take advantage of variable length encoding to reduce the size of documents. I used python as my coding language because of my own comfort in the language and the ease of using dictionaries and string operators. I used dictionaries to store my initial weights for my characters and my encoding key. For finding my pairs I use a brute force solution to find every pair and its weights which I then turn into an a my encoding key. This algorithm is far from optimized, the encoding I did for the pairs is as basic as it can be and while it does work, im sure their are more optimal implementations when it come to deciding which pairs should be used in the encoding.
 

# How to use
at the bottom of "huffmen codes.py" you can run either function (singleCharEncode(filePath) or doubleCharEncode(filePath)) for their respected encoding. The function examines and returns the length of each encoding algorithm and returns a txt file with doubleCharEncoding.

# Test Cases
# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
- "BeeScript.txt"
- Text ascii 350973 bits
- Single Encode Length: 237966
- Pair Encode Length: 206418
# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
- "IHaveADream.txt"
- Text ascii 63252 bits
- Single Encode Length: 39838
- Pair Encode Length: 35036
# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
- "Manifesto of the Communist Party"
- Text ascii 1519560 bits
- Single Encode Length: 978666
- Pair Encode Length: 863588

# Percent Savings from standard ascii encoding
asc
(1-(length/ascii))*100 = savings percentage

- "BeeScript.txt"
- Single: 32.2%
- Pair:   41.2%

- "IHaveADream.txt"
- Single: 37.0%
- Pair:   44.6%

- "Manifesto of the Communist Party"
- Single: 35.6%
- Pair:   43.2%

# Average
- Single: 34.9%
- Pair:   43.0%

Overall, the two programs do take advantage of variable length encoding with a solid space gain for both algorithms. Using pairs of letters is consistently better (~9%) then the single character encoding which makes sense. Overall, the two programs work as intended and while the pair algorithm is far from being optimal, it does succeed in its intended use case of reducing the total size of the file.


# Time spend 3 hours to 6 hours, i have no idea