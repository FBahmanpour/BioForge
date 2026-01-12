from M1 import Parser_Validator
from M2 import Complementary_String_Generator
from M3 import ORF_Finder_Translator
from M4 import Weight_Calculator
from M5 import Filter_and_Annotate
from M6 import Report_Generator


def main():
    fasta_content=""">test_len_4|a protein of length 5
    AGCT NNN ATGAAA GCATTTGGGTAG GTC"""
    print(Report_Generator(Filter_and_Annotate(Weight_Calculator(ORF_Finder_Translator(Complementary_String_Generator(Parser_Validator(fasta_content)))))))


if __name__ == '__main__':
    main()
