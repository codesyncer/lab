from NiceTrie import *


class Trie(NiceTrie):
    def insert(self, string, index=None):
        super(Trie, self).insert(string + '\0', index)

    def search(self, string):
        return super(Trie, self).search(string + '\0')

    def present(self, string):
        return super(Trie, self).present(string + '\0')
