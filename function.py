def countWordsFromFile():
    fileName = input("Enter file path : ")
    wordCount = 0
    file = open(fileName, 'r')
    for line in file:
        words = line.split()
        wordCount = wordCount+len(words)
    print("Number of words are ",wordCount)
countWordsFromFile()
        