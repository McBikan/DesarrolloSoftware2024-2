# count_words.py

class CountWords:
    def count(self, s: str) -> int:
        words = 0
        last = ' '

        for char in s:
            if not char.isalpha() and (last == 's' or last == 'r'):
                words += 1
            last = char

        if last == 'r' or last == 's':
            words += 1

        return words