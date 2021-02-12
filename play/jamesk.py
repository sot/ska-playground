def knockknock():
    import time
    import random

    knockknock.jokes = {
        'Tank': "You're Welcome... not",
        'Owls': "You're right, Owls 'who'",
        'Cow says': "No, a cow says 'moo'!",
        'Woo': "Wow, someone's excited about knock knock jokes",
        'Water': "Water you doing telling jokes right now? \
                  Don’t you have things to do?",
        'Leaf': "Leaf me alone!",
        'Thermos': "Thermos be a better way to get a laugh",
        'Boo': "Don't cry, it's just a joke",
        'Spell': "W.H.O.",
        'Otto': "Otto know; I forgot.",
        'Adore': "Adore is between us, open up!",
        'Two-knee': "Two-knee fish!",
        'Abby': "Abby birthday to you!",
    }

    print('Knock Knock...')
    time.sleep(1)
    print('\t\tWho\'s there?')
    time.sleep(1)
    choice = random.choice(list(knockknock.jokes))
    print(choice)
    time.sleep(1)
    print(f'\t\t{choice} who?')
    time.sleep(1.25)
    print(knockknock.jokes[choice])


class Node:
    def __init__(self, char):
        self.left = None
        self.right = None
        self.char = char

    def __str__(self):
        return str(self.char)


class MorseTree:
    def __init__(self):
        # not supporting parenthesis
        chars = "TIANMSURWDKGOHVF*L*PJBXCYZQ**54*3***2**+****16=/*****7***8*90\
                 ************?_****\"**.****@***'**-********;!*******,****:"
        self.root = Node("*")
        self.root.left = Node("E")

        this_node = self.root
        node_queue = []

        for char in chars:
            if this_node.right is None:
                this_node.right = Node(char)
            else:
                # add child nodes to the queue
                node_queue.append(this_node.left)
                node_queue.append(this_node.right)
                # pop off the next node in the queue to process
                this_node = node_queue.pop(0)
                # add the current character to the left of the current node
                this_node.left = Node(char)

    def find_char(self, char, this_node=None, morse_str=""):
        """Find a character in the tree"""
        # "*" is used in place of invalid characters, so we cannot match it
        if(char == "*"):
            raise ValueError("'*' cannot be converted to morse code.")
            return None

        # depth first search
        if(not this_node):
            this_node = self.root

        if(this_node.char == char):
            return morse_str

        if(this_node.left):
            morse_str += "."
            next_node = this_node.left
            tmp_out = self.find_char(char, this_node=next_node,
                                     morse_str=morse_str)
            if(not tmp_out):
                morse_str = morse_str[:-1]
            else:
                morse_str = tmp_out
                return morse_str

        if(this_node.right):
            morse_str += "-"
            next_node = this_node.right
            tmp_out = self.find_char(char, this_node=next_node,
                                     morse_str=morse_str)
            if(not tmp_out):
                morse_str = morse_str[:-1]
            else:
                morse_str = tmp_out
                return morse_str
        else:
            return None


def text2morse(msg="Hello World"):

    mt = MorseTree()
    word_gap = "       "
    char_gap = " "
    morse_str = ""
    for char in msg:
        char = char.upper()
        if char == " ":
            morse_str += word_gap
        else:
            morse_letter = mt.find_char(char)
            assert morse_letter
            morse_str += morse_letter + char_gap

    return morse_str.strip()
