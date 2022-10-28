# This function returns the entirety of "Dracula" as a string
def readBook():
  f = open("dracula.txt", "r")
  s = f.read().replace("-", " ")            
  f.close()
  return ''.join(c for c in s if c.isalnum() or c == " ")

# Create variables for words in the book
draculaText = readBook()
draculaWords = draculaText.split()

print("=== Results ===")
print()
# Create dictionary to hold words and number of times it appears
wordList = {}

# for each word in the book...
for word in draculaWords:
  
  # Make all words lowercase
  word = word.lower()

  # if it's the first time you see the word..
  if word not in wordList:

    # make the corresponding value 1
   wordList[word] = 1

  # if you've already seen the word, add 1 to the value
  else:
    wordList[word] += 1

largest = 0

# For each pair of words and number of times it's seen, keep track of the largest number of times a word is seen
for key, value in wordList.items():

  if value  > largest:
    
    largest = value
    frequentWord = key

# Display the most frequently used word and the number of times it shows up
print(f"The word ' {frequentWord} ' shows up {largest} times, and is the most frequently used word in the book")    
print()

# Create a blank list that will contain unique four-letter words
fourLetter = []

# For each word in the book...
for word in draculaWords:

  # Make it lowercase
  word = word.lower()
  
  # If a word is four letters long, then add it to the list
  if len(word) == 4: 

    # Make sure it's not already in the list
    if word not in fourLetter:
      fourLetter.append(word)

# Display the number of unique four-letter words
print(f"There are {len(fourLetter)} of unique four letter words")
print()  
     
# Every word that shows up more than 500 times, and how many times that word shows up throughout the book (see the "Walkthrough" section for an example)

# From your word list that counts word frequency
for key, value in wordList.items():

  # Find the words that show up more than 500 times
  if value  > 500:

    # Diplay each word and its frequency if it shows up more than 500 times
    print(f"{key} - {value}")    