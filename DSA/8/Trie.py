from NiceTrie import *


class Trie(NiceTrie):
    def insert(self, string):
        super(Trie, self).insert(string + '$')

    def search(self, string):
        return super(Trie, self).search(string + '$')
