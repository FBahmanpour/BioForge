from replace_T_with_U import replace_T_with_U
from find_ORFs_for_sequence import find_ORFs_for_sequence

def ORF_Finder_Translator(data_dict):

    forward = replace_T_with_U(data_dict["forward"])
    rev_comp = replace_T_with_U(data_dict["reverse_complement"])

    result = []

    result.extend(find_ORFs_for_sequence(forward, "forward"))

    result.extend(find_ORFs_for_sequence(rev_comp, "reverse"))

    return result

