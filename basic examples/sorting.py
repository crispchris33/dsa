#basic sorting using the sorting operation in python - Tim Sort

#for integers
elements = [5, 3, 6, 2, 1]

elements.sort()

print(elements) # [1, 2, 3, 5, 6]

#for strings

elements = ["grape", "apple", "banana", "orange"]

elements.sort()

print(elements) # ['apple', 'banana', 'grape', 'orange']

#descending
#def sort(key=None, reverse=False) -> None:


#custom sorting
def get_word_length(word: str) -> int:
    return len(word)

words = ["apple", "banana", "kiwi", "pear", "watermelon", "blueberry", "cherry"]

words.sort(key=get_word_length)

print(words) # ['kiwi', 'pear', 'apple', 'banana', 'cherry', 'blueberry', 'watermelon']
