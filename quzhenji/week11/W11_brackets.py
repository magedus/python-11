s = set()


def foo(output, lopen, rclose, pairs):
    if lopen == pairs and rclose == pairs:
        # print(output)
        s.add(output)
    else:
        if lopen < pairs:
            foo(output + '(', lopen + 1, rclose, pairs)
        if rclose < lopen:
            foo(output + ')', lopen, rclose + 1, pairs)


foo('', 0, 0, 4)

print(s)
