def getText(path):
    with open(path) as f:
        return f.read()

def countWords(text):
    return len(text.split())

def countCharacters(text):
    lowerText = text.lower()
    charDict = {}

    for i in lowerText:
        if i in charDict:
            charDict[i] += 1
        else:
            charDict[i] = 1

    return charDict

def main():
    PATH = "books/frankenstein.txt"
    text = getText(PATH)
    print(countWords(text))
    print(countCharacters(text))
    # print(text)

if __name__ == "__main__":
    main()
