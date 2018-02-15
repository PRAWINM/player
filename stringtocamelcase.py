s=raw_input('enter the string:')
def case(word):
        import re
        return ' '.join(x.capitalize() or ' ' for x in word.split(' '))
print(case(s))
