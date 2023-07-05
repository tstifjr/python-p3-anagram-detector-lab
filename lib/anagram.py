# your code goes here!

class Anagram:
    def __init__(self, word) :
        self.word = word

    def match (self, list) :
        word_array = [letter for letter in self.word]
        sorted_word_arr = sorted(word_array)
        anagram_arr = []

        for anagram in list :
            an_arr = [letter for letter in anagram]
            sorted_an_arr = sorted(an_arr)
            if (sorted_an_arr == sorted_word_arr) :
                anagram_arr.append(anagram)

        return anagram_arr
