class Node(object):
    def __init__(self, val):
        self.val = val
        self.children = dict()
        

class Trie(object):
    def __init__(self):
        self.root = Node(None)


def autocomplete(prefix: str, possible: list) -> list:
    """ Given a prefix string and a set of possibilities,
    returns a list of possible strings (like autocomplete
    suggestions)
    prefix: the input string
    possible: a list of possible strings, or the dictionary
    for this problem
    return: a list of autocomplete suggestions
    """
    
    # first build a trie from the given dictionary
    trie = Trie()
    
    for word in possible:
        add_word_to_trie(trie, word)
        
    return get_suggestions_from_trie(trie, prefix)

        
def add_word_to_trie(trie: Trie, word: str) -> Trie:
    # initialize to the roots
    curr_node = trie.root
    for letter in word:
        if letter in curr_node.children:
            curr_node = curr_node.children[letter]
        else:
            tmp = Node(letter)
            curr_node.children[letter] = tmp
            curr_node = tmp
            

def get_suggestions_from_trie(trie: Trie, prefix: str) -> list:
    # first traverse to the node that corresponds to the last letter
    # of the prefix
    node = trie.root
    i = 0
    
    while i < len(prefix) - 1 and prefix[i] in node.children:
        node = node.children[prefix[i]]
        i += 1
    
    # now traverse from this node and get possible endings
    print(node.val)
    dfs(prefix, node)
    
    # merge the prefixes and the endings
    
    
def dfs(prefix: str, node: Node):
    for child in node.children:
        new_prefix = prefix + node.val
        new_node = node.children[child]
        dfs(new_prefix, new_node)
    print(prefix)
    
    
autocomplete("sal", ["salami", "salad", "bat"])
    
    
    
    