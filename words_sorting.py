def words_sorting(*words):
    dict = {}
    total_sum = 0
    for word in words:
        dict[word] = 0
        for l in word:
            dict[word] += ord(l)
        total_sum += dict[word]

    if total_sum % 2 != 0:
        output = sorted(dict.items(), key= lambda x: (-x[1]))
    else:
        output = sorted(dict.items(), key=lambda x: x[0])
    out = ''
    for kv in output:
        out += f"{kv[0]} - {kv[1]}\n"
    return out