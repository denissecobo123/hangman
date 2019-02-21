def hang():
    gallows = [',--;-', '| ', '| ', '| ', '| ', '| ', '|_____']
    parts = iter([' 0 ', '/', '|', '\\', ' | ', ' A ', '/ ', '\\'])
    sequence = [1, 3, 1, 1, 2]
    for i, v in enumerate(sequence, start=1):
        for k in range(v):
            gallows[i] += next(parts)
            yield '\n'.join(gallows)
    raise StopIteration


words = ['the', 'be', 'and', 'of', 'it', 'I', 'that', 'for', 'you', 'he', 'with', 'on', 'do', 'say', 'this'
         , 'they', 'at', 'but', 'his', 'from', 'that', 'not', 'by', 'she', 'or', 'as', 'what', 'go', 'their', 'can'
         , 'who', 'get', 'if', 'would', 'her', 'all', 'father', 'sit', 'away', 'until', 'to', 'political', 'community',
         'president']
