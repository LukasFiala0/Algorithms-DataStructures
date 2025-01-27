## 1.) Duplicates detection
def contains_duplicate(arr:list) -> bool:
    hashset = set()
    for i in arr:
        if i in hashset:
            return True
        hashset.add(i)
    return False

# arr = [1,2,3,4,5,6,7]
# print(contains_duplicate(arr))


## 2.) Unique words in a text file
def unique_words(file):
    with open(file, "r") as f:
        text = f.read().lower()
    
    # Removing punctuation
    punctuation = ".,!?;:\"'()-[]{}"
    for char in punctuation:
        text = text.replace(char, "")
    
    unique_words_set = set(text.split())
    
    return len(unique_words_set)

#print(unique_words("sample_text.txt"))

## 3.) Pair to sum ... with duplicities
def pair_to_sum(arr:list, target:int):
    hashset = set()
    result = []
    for x in arr:
        y = target - x
        if y in hashset:
            result.append((x,y))
        hashset.add(x)
    return result

# print(pair_to_sum([1,2,3,4,5], 5))

## 4.) Anagram

def anagram(text1: str, text2: str) -> bool:
    text1 = text1.replace(" ", "").lower()
    text2 = text2.replace(" ", "").lower()
    
    hashtable1 = {}
    for char in text1:
        if char in hashtable1:
            hashtable1[char] += 1
        else:
            hashtable1[char] = 1
    
    hashtable2 = {}
    for char in text2:
        if char in hashtable2:
            hashtable2[char] += 1
        else:
            hashtable2[char] = 1
    print(hashtable1)
    print(hashtable2)
    if hashtable1 == hashtable2:
        return True
    else:
        return False

# print(anagram("listen", "silent"))
# print(anagram("hello", "world"))
# print(anagram("anagram", "nag a ram"))

### 5.) Unique elements in a list
def unique_el(arr:list) -> set:
    return set(arr)

##print(unique_el([1, 2, 2, 3, 4, 4, 5, 6, 6, 7]))

## 6.) UNION, INTERSECTION, DIFFERENCE
def union(set1:set, set2:set) -> set:
    return set1 | set2

def intersection(set1:set, set2:set) -> set:
    return set1 & set2

def difference(set1:set, set2:set) -> set:
    return set1 - set2

## 7.) NUMBER OF OCCURRENCES
def occurrences(text: str) -> dict:
    text = text.lower()
    result = {}
    for char in text:
        if char.isalpha():
            result[char] = result.get(char, 0) + 1
    return result

#print(occurrences('''HashSet is a collection designed to store unique elements.
#A HashSet is implemented as a hash table in most programming languages.
#Its operations like add, remove, and contains have an average time complexity of O(1).
#It is often used for tasks such as finding unique words in a text, detecting duplicates, or as a quick lookup structure.'''))

##  8.) FIRST NON-PAIRED ELEMENT
def nonpaired(arr:list[int]) -> int:
    hashtable = {}
    for num in arr:
        hashtable[num] = hashtable.get(num, 0) + 1
        if hashtable[num] > 1 and hashtable[num] % 2 != 0:
            return num    
#print(nonpaired([4, 5, 4, 6, 7, 5, 6, 7, 7]))

## 9.) TELEPHONE_LIST
class Contact:
    def __init__(self):
        self.contacts: dict[str, str] = {}

    def add(self, name: str, number: str) -> str:
        if name in self.contacts:
            return f"A contact with name: {name} already exists!"
        self.contacts[name] = number
        return f"Contact {name} added successfully."

    def delete(self, name: str) -> str:
        if self.contacts.pop(name, None) is None:
            return f"A contact with name {name} does not exist!"
        return f"Contact {name} deleted successfully."

    def search(self, name: str) -> str:
        return self.contacts.get(name, "Contact was not found.")
    

# ### 10.) Find multiple anagrams
def mult_anagram_1(words:list[str]) -> list[list[str]]:
    sorted_words = []
    for word in words:
        sorted_word = "".join(sorted(word))
        sorted_words.append(sorted_word)

    hashtable = {key : [] for key in sorted_words}
    for i in range(len(sorted_words)):
        hashtable[sorted_words[i]] += [words[i]]

    result = []
    for value in hashtable.values():
        result.append(value)

    return result




def mult_anagram_2(words: list[str]) -> list[list[str]]:
    hashtable = {}

    for word in words:
        sorted_word = "".join(sorted(word))
        if sorted_word not in hashtable:
            hashtable[sorted_word] = []
        hashtable[sorted_word].append(word)
    return list(hashtable.values())

words = ["listen", "silent", "enlist", "hello", "below", "elbow", "world", "dworl"]
# print(mult_anagram_1(words))
# print(mult_anagram_2(words))


### 11.) Occurrences of words in a sentence
def word_occurrences(text:str) -> dict[str, int]:
    hashtable = {}
    text = text.lower()
    interpunction = ".,!?\"()-"
    for char in interpunction:
        text = text.replace(char, "")

    key = ''
    for char in text:
        if char.isalpha():
            key += char
        elif key:
            hashtable[key] = hashtable.get(key, 0) + 1
            key = ''

    if key:
        hashtable[key] = hashtable.get(key, 0) + 1 

    
    return dict(sorted(hashtable.items(), key=lambda item : item[1], reverse=True))  # sort the dictionary by values


text = '''HashSet is a collection designed to store unique elements.
A HashSet is implemented as a hash table in most programming languages.
Its operations like add, remove, and contains have an average time complexity of O(1).
It is often used for tasks such as finding unique words in a text, detecting duplicates, or as a quick lookup structure.
'''
#print(word_occurrences(text))


### 12.) Number of vowels in a text.
def number_of_vowels(text:str) -> tuple:
    vowels = {'a','e', 'i', 'o', 'u'}
    text = text.lower()
    hashtable = {}

    for char in text:
        if char in vowels:
            hashtable[char] = hashtable.get(char, 0) + 1

    return list(dict(sorted(hashtable.items(), key=lambda item: item[1], reverse=True)).items())

#print(number_of_vowels(text))

