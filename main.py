"""
Zac Schimpf
Project A4
"""
from collections import Counter
from csv import writer
import sys

def analyze(genome):
    """
    :param genome: Continuous genome nucleotide sequence in a string
    :return: Collected results containing [[dict, dict]],
             being [occurrences, adjacencies], comma separated by frame
    """
    collected_results = []
    for i in range(2):
        genome = genome[i:]
        current_frame = [genome[i:i + 3] for i in range(len(genome) - 2)]

        collected_results.append([
            get_occurrences(current_frame),
            get_adjacency(current_frame)
        ])
    return collected_results


def get_occurrences(codons):
    """
    :param codons: Triplet codon nucleotide sequences in a list[]
    :return: Unique values derived from codons[]
             returned as {codon: quantity} in descending order
    """
    codon_counts = Counter(codons)
    sorted_codons = sorted(codon_counts.items(), key=lambda x: (-x[1], x[0]))
    return sorted_codons


def get_adjacency(codons):
    """
    :param codons: Triplet codon nucleotide sequences in a list[]
    :return: Adjacencies derived from codons[]
             returned as {codon, codon: quantity} in descending order
    """
    adjacent_codons = [(codons[i], codons[i + 1]) for i in range(len(codons) - 1)]
    codon_quantity = Counter(adjacent_codons)
    sorted_adjacencies = sorted(codon_quantity.items(), key=lambda x: (-x[1], x[0]))
    return sorted_adjacencies


def output_std(results):
    """
    Print forward results & output to csv
    :param results: Occurrences & adjacencies returned from analyze(), being a [[dict, dict]]
    :return: 0, on success
    """
    for frame in results:
        print(f"Frame {str(results.index(frame) + 1)}")

        with open("unique.tsv", 'w', newline='', encoding="utf-8") as file:
            stream = writer(file, delimiter='\t', lineterminator='\n')
            stream.writerow(["Codon", "Quantity"])

            for codon, quantity in frame[0]:
                print(f"'{codon}': {quantity}")
                stream.writerow([codon, quantity])
        print("\n")

        stream, codons, quantity, file = None, None, None, None

        with open("adjacent.tsv", 'w', newline='', encoding="utf-8") as file:
            stream = writer(file, delimiter='\t', lineterminator='\n')
            stream.writerow(["Codon 1", "Codon 2", "Quantity"])

            for codons, quantity in frame[1]:
                print(f"{codons[0]} -> {codons[1]}: {quantity}")
                stream.writerow([codons[0], codons[1], quantity])
        print("\n--------------------------------------------------------------------\n")

    return 0

def output_rev(results):
    """
    Print reverse results & output to csv
    :param results: Occurrences & adjacencies returned from analyze(), being a [[dict, dict]]
    :return: 0, on success
    """
    for frame in results:
        print(f"Frame {str(results.index(frame) + 1)}")

        with open("unique_rev.tsv", 'w', newline='', encoding="utf-8") as file:
            stream = writer(file, delimiter='\t', lineterminator='\n')
            stream.writerow(["Codon", "Quantity"])

            for codon, quantity in frame[0]:
                print(f"'{codon}': {quantity}")
                stream.writerow([codon, quantity])
        print("\n")

        stream, codons, quantity, file = None, None, None, None

        with open("adjacent_rev.tsv", 'w', newline='', encoding="utf-8") as file:
            stream = writer(file, delimiter='\t', lineterminator='\n')
            stream.writerow(["Codon 1", "Codon 2", "Quantity"])

            for codons, quantity in frame[1]:
                print(f"{codons[0]} -> {codons[1]}: {quantity}")
                stream.writerow([codons[0], codons[1], quantity])
        print("\n--------------------------------------------------------------------\n")

    return 0

if __name__ == '__main__':
    GENOME = ("gcggcggttagtattacccgccgcctggggcaccggggcacgtcagctattggctgacgagccccgtgccccacccccgtgcc"
              "ccagcccctccttccgcgtgtgtttttgaactgacgccgaaggcgtcagttcccgtattgtcaccgccatgccgtccaaggag"
              "ggctctggttgccgccgatggtgtttcaccctgaacaacccaaccagagccgagatagactacatatgtagtctgaagcctga"
              "agacttccactatgccatcgttggacgggagtgcggtgagaaacaacaaacccctcatttacaaggctattttcattttaagc"
              "aaaaaaagcgcttaagtgccttaaagaaaatgctgccgcgagcgcattttgagcgagctaagggcagtgatgcggataatgag"
              "aaatattgcagtaaggagggggacgttatacttaccctgggcattgtggcgcgagacggtcaccgcgcgtttgacggagctgt"
              "tgccgctgtgcttgccggaagacgaatgaaagaagtcgcgcgagagttcccggatatctacgtcaggcatgggcgtggtctgc"
              "acaatctctctcttctgattggctctcagccgcgcgactttaaaactgaggttgacgtcatctatggcccgcctgggtgtggc"
              "aagagtaaatgggccaatgagcagccggggtcaaagtactataagatgcgcggtgaatggtgggatggatatgatggagaaga"
              "tatcgtcatcttggacgatttctatgggtggctaccttattgcgagatgctccgcctatgtgaccgttacccacataaagtgc"
              "cagttaaaggtgcctttgtggagtttaccagcaagaggatcatcatcacgagcaataaggcccccgagacctggtacaaggag"
              "gattgtgacccgaagccactgttccggagattcactcgtgtttggtggtacactgacaagttggaacaagtccggcctgattt"
              "ccttgcccacccaatcaatttttgataccccccggaggttattaataaaagccggccgtcgggccgaaggcccgatggcgcag"
              "ggcgggacgccctgccggagggctcgcagggccgtcaggcccgagagcccgaccagcccggagggcctagtctgtgtcggggg"
              "ggggccccaggggggtccccccgacacgacgagaatggtagcgccgaaggcgccaataaacactcgaaaaggtatttgccgtg"
              "tttgtctttatttaagtagaagggttattgggacaccattgacggaattgaacatataatgttagtttacaaagataagagat"
              "gtctacattaggctgcggaaagctgaatgctattccgtaatgtgccaccctgtctcccgcctggttgggtcctcctcctatcg"
              "ggatccatccagttctggtactgttcagccacaatgccgccgattgatttgcggtattgaggtcagtgatggtaagttgaggt"
              "tttggtcttaaaaggcgtttaaagcccctgttcaagaaccactttttagccccgtcaaatggtgctaaagggtcttgctgctg"
              "atccgcagtcgtcttaaagattttaattctcgagtcttgaattattgcagtgtgaccgaaaccttcagccgaaatagtctgga"
              "aggttcctgtggggcgcatctccatttttgcaagcttaattctatagtcttcccaattaagggcttgtggttctgcgccaccc"
              "aggaaatcacttaaagtgaaagttatgtagtcagagttaaaaattaattgtccagtactggtagtttgttttcgaatcgtaaa"
              "gcgaaattgtcttgtcaggcgtatgttgtacaccctattggttgtaaaacggtgtctccgcccatatctgcggtgcctgcgat"
              "aacgcctgactggtcgtctgcgcacgcgtgatctgcggtatcttctgcggagctgcaagatagcgcatgcgcagttagaggtg"
              "ccccacag")

    print("Forward Frame:")
    analysis = analyze(GENOME)
    eof = output_std(analysis)

    print("Reverse Frame:")
    analysis = analyze(GENOME[::-1])
    eof += output_rev(analysis)

    sys.exit(eof)
