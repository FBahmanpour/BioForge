def Complementary_String_Generator(DNA):
    forward = DNA["sequence"]
    import copy
    f = copy.deepcopy(forward)
    f = list(f)
    reverse_complement = ""
    for i in range(len(f)):
        _ = f.pop()
        if _ == "T":
                _ = "A"
        elif _ == "A":
                _ = "T"
        elif _ == "C":
                _ = "G"
        elif _ == "G":
                _ = "C"
        reverse_complement += _
    dna = {"forward":forward, "reverse_complement":reverse_complement}
    return dna
