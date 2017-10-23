from NiceTrie import *


class Trie(NiceTrie):
    def insert(self, string):
        super(Trie, self).insert(string + '\0')

    def search(self, string):
        return super(Trie, self).search(string + '\0')
