def generate_subsets(s):
    if len(s) == 0:
        return [[]]
    else:
        subsets = generate_subsets(s[1:])
        return subsets + [[s[0]] + subset for subset in subsets]
generate_subsets('abc')
