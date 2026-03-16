class DictionaryUtils:
    #Return frequency of characters in string.
    def character_frequency(self,word):
        frequency_count = dict.fromkeys(word,0)
        for char in word:
            frequency_count[char] += 1

        return frequency_count

        


        