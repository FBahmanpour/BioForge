def Parser_Validator(fasta_content):
    d = {}
    str = ""

    if fasta_content == "":
        return "ValueError"
    if fasta_content[0] != ">":
        return "TypeError"

    l1, other_lines= fasta_content.split('\n',1)
    d["id"] = l1[l1.index(">")+1:]

    for s in other_lines:
        if s in {'A','T','C','G'}:
            str += s

    d["sequence"] = str.upper()
    return d
