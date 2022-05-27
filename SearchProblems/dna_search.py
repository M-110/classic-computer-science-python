from enum import IntEnum
from typing import Tuple, List

# Nucleotide: An organic molecule that is the building block of DNA and RNA.
Nucleotide = IntEnum('Nucleotide', ('A', 'C', 'G', 'T'))

# Type aliases for Codon/Gene
# Codon: a sequence of three nucleotides which form a unit of genetic code.
Codon = Tuple[Nucleotide, Nucleotide, Nucleotide]
# Gene: a set of codons.
Gene = List[Codon]

gene_str = "ACGTGGCTCTCTAACGTACGTACGTACGGGGTTTATATATACCCTAGGACTCCCTTT"


def convert_string_to_gene(gene_string: str) -> Gene:
    """Converts a gene string into a list of codon instances."""
    gene: Gene = []
    for i in range(0, len(gene_string), 3):
        if (i + 2) > len(gene_string):
            return gene

        codon: Codon = (Nucleotide[gene_string[i]], Nucleotide[gene_string[i + 1]], Nucleotide[gene_string[i + 2]])
        gene.append(codon)
    return gene


my_gene = convert_string_to_gene(gene_str)

def linear_search(gene: Gene, key_codon: Codon) -> bool:
    """Linear search to see if key_codon is contained in gene."""
    return any(codon == key_codon for codon in gene)
    

acg: Codon = (Nucleotide.A, Nucleotide.C, Nucleotide.G)
gat: Codon = (Nucleotide.G, Nucleotide.A, Nucleotide.T)
print(linear_search(my_gene, acg))  # True
print(linear_search(my_gene, gat))  # False


def binary_search(gene: Gene, key_codon: Codon) -> bool:
    """Binary search of a sorted gene."""
    
    # Our search space is between a and b.
    a = 0
    b = len(gene) - 1
    
    while a <= b:
        midpoint: int = (a + b) // 2
        if gene[midpoint] < key_codon:
            a = b + 1
        elif gene[midpoint] > key_codon:
            b = midpoint -1
        else:
            return True
    return False

my_sorted_gene: Gene = sorted(my_gene)
print(binary_search(my_sorted_gene, acg))  # True
print(binary_search(my_sorted_gene, gat))  # False