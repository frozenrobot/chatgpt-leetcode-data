class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def build_trie(words):
            root = TrieNode()
            for word in words:
                node = root
                for char in word:
                    if char not in node.children:
                        node.children[char] = TrieNode()
                    node = node.children[char]
                node.word = word
            return root

        def backtrack(board, i, j, node):
            char = board[i][j]
            if char not in node.children:
                return

            node = node.children[char]
            if node.word:
                self.result = True
                return

            board[i][j] = '#'  # Mark as visited

            if i > 0:
                backtrack(board, i - 1, j, node)
            if i < len(board) - 1:
                backtrack(board, i + 1, j, node)
            if j > 0:
                backtrack(board, i, j - 1, node)
            if j < len(board[0]) - 1:
                backtrack(board, i, j + 1, node)

            board[i][j] = char  # Restore the character

        # Build the Trie from the given word list
        trie_root = build_trie([word])

        self.result = False

        # Iterate through each cell in the board to find the starting point for the word
        for i in range(len(board)):
            for j in range(len(board[0])):
                backtrack(board, i, j, trie_root)
                if self.result:
                    return True
        
        return False
