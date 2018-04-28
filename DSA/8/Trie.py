from NiceTrie import *


class Trie(NiceTrie):
    def insert(self, string, index=None):
        super(Trie, self).insert(string + '\0', index)

    def search(self, string):
        return super(Trie, self).search(string + '\0')

    def present(self, string):
        return super(Trie, self).present(string + '\0')

    def match_prefix(self, prefix):
        node = self.root
        for ch in prefix:
            if node.children is None:
                return []
            list_node = node.children.search(ch)
            if list_node is None:
                return []
            node = list_node.value
        matches = []
        self.dump(node, prefix[:-1], matches)
        return matches

    def dump(self, node, prefix, my_list):
        if node.children is None:
            return my_list.append(prefix)
        prefix += node.ch
        for child in node.children:
            self.dump(child, prefix, my_list)
