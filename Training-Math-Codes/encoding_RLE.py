import rle


def encode(text):
    values, counts = rle.encode(text)
    result = "".join(f"{x[0]}{x[1]}" for x in zip(values, counts))
    result = result.replace("1", "")
    return result


def are_lens_equal(counts, values):
    return len(counts) == len(values)


def take_count(el, next_el):
    if el.isalpha() and next_el.isdigit():
        return int(next_el)
    elif el.isalpha() and next_el.isalpha():
        return 1
    return 0


def decode(text):
    values = [x for x in text if x.isalpha()]
    counts = []
    idx = 0
    while True:
        if are_lens_equal(counts, values):
            break
        el = text[idx]
        idx = (idx+1) % len(text)
        next_el = text[idx]
        counts.append(take_count(el, next_el))
        counts = [c for c in counts if not c == 0]
    result = rle.decode(values, counts)
    result = "".join(result)
    return result


print(encode("AABCCCDEEEE"))
print(decode("A2BC3DE4"))
print(decode(encode("A2BC3DE4")))
print(encode(decode("AABCCCDEEEE")))
