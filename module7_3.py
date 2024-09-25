import string


class WordsFinder:
    def __init__(self, *name):
        self.file_names = [i for i in name]

    def get_all_words(self):
        all_words = {}
        words_lst = []
        for i in self.file_names:
            with open(i, encoding='utf-8') as file:
                for line in file:
                    words = line.lower().translate(str.maketrans('', '', string.punctuation))
                    words_lst += words.split()
                all_words[i] = words_lst
        return all_words

    def find(self, word):
        finds = {}
        for name, words in self.get_all_words().items():
            finds[name] = words.index(word.lower()) + 1
        return finds

    def count(self, word):
        counts = {}
        for name, words in self.get_all_words().items():
            counts[name] = words.count(word.lower())
        return counts



finder = WordsFinder('sample.txt')
print(finder.get_all_words())  # Все слова
print(finder.find('captain'))  # 3 слово по счёту
print(finder.count('captain'))  # 4 слова teXT в тексте всего
