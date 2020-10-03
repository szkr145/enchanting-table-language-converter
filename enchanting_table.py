class EnchantingTable:
    def __init__(self):
        self.enchanting_table_dict = {
            'a': "ᔑ",
            'b': "ʖ",
            'c': "ᓵ",
            'd': "↸",
            'e': "ᒷ",
            'f': "⎓",
            'g': "⊣",
            'h': "⍑",
            'i': "╎",
            'j': "⋮",
            'k': "ꖌ",
            'l': "ꖎ",
            'm': "ᒲ",
            'n': "リ",
            'o': "𝙹",
            'p': "!¡",
            'q': "ᑑ",
            'r': "∷",
            's': "ᓭ",
            't': "ℸ",
            'u': "⚍",
            'v': "⍊",
            'w': "∴",
            'x': "̇/",
            'y': "׀׀",
            'z': "⨅",
            '.': "·-·",
            ' ': ' '
        }

    def to_galactic_language(self, sentence: str) -> str:
        return ''.join(self.enchanting_table_dict[x] if x in self.enchanting_table_dict else x for x in sentence)

    def to_english_langugage(self, sentence: str) -> str:
        return ''.join(self._get_key(x) if x in self.enchanting_table_dict.values() else x for x in sentence)

    def _get_key(self, value_to_search: str) -> str:
        return [key for key, value in self.enchanting_table_dict.items() if value_to_search == value][0]

