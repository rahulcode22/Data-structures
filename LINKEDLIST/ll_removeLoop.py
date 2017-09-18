from collections import Counter

def ransom_note(magazine,rasom):
    return (Counter(rasom) - Counter(magazine)) == {}
