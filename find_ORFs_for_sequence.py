codon_map = {
    "UUU":"F", "UUC":"F",
    "UUA":"L", "UUG":"L",
    "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
    "AUU":"I", "AUC":"I", "AUA":"I",
    "AUG":"M",
    "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",

    "UCU":"S", "UCC":"S", "UCA":"S", "UCG":"S",
    "AGU":"S", "AGC":"S",

    "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",

    "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T",

    "GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",

    "UAU":"Y", "UAC":"Y",
    "UAA":"*", "UAG":"*",     # STOP codon
    "UGA":"*",               # STOP codon

    "CAU":"H", "CAC":"H",
    "CAA":"Q", "CAG":"Q",

    "AAU":"N", "AAC":"N",
    "AAA":"K", "AAG":"K",

    "GAU":"D", "GAC":"D",
    "GAA":"E", "GAG":"E",

    "UGU":"C", "UGC":"C",
    "UGG":"W",

    "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R",
    "AGA":"R", "AGG":"R",

    "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G"
}
# 3 تا 3 تا کزدن رشته ها
def split_codons(seq, shift):
    codons = []
    for i in range(shift, len(seq) - 2, 3):
        codons.append(seq[i:i+3])
    return codons

# ترجمه بر اساس رشته های س تایی که در قالب لیست به وردی داده می شود
def translate_from_AUG(codons):
    protein = ""
    started = False

    for c in codons:

        # شروع ترجمه
        if c == "AUG" and not started:
            started = True

        if started:
            aa = codon_map.get(c, "")

            # توقف ترجمه روی STOP codon
            if aa == "*":
                break

            protein += aa

    return protein

# تاب ع اصلی تر که از دو تابع قبلی برای انجام کار کلی کمک می گیرد و دیکشنری خروجی را می سازد
def find_ORFs_for_sequence(seq, strand_name):
    results = []

    for shift in range(3):
        codons = split_codons(seq, shift)

        for i in range(len(codons)):
            if codons[i] == "AUG":

                protein = translate_from_AUG(codons[i:])

                orf_dict = {
                    "sequence": protein,
                    "strand": strand_name,
                     "start_pos": i*3 + shift
                
                }

                results.append(orf_dict)

    return results
