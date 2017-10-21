from Trie import *

my_list = ['bear', 'bell', 'sell', 'bid', 'hello', 'bull', 'stopping', 'buy', 'stock', 'stop', 'meow', 'stopper']
throws = ['beer', 'pong', 'srinag', 'sold', 'stop', 'stopper', 'stopping', 'skitty']
my_trie = Trie()
for word in my_list:
    my_trie.insert(word)
test_list = throws + my_list
for word in test_list:
    if my_trie.search(word):
        msg = ' is present'
    else:
        msg = ' is not present'
    print(word + msg)
