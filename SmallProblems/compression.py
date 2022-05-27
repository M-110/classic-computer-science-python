from sys import getsizeof

def compress_gene(gene: str) -> int:
    """Compress a gene sequence down to an int using bitwise operations"""
    bit_string: int = 1
    for character in gene.upper():
        bit_string <<= 2
        if character == "A":
            bit_string |= 0b00
        elif character == "C":
            bit_string |= 0b01
        elif character == "G":
            bit_string |= 0b10
        elif character == "T":
            bit_string |= 0b11
    return bit_string


def decompress_gene(bit_string: int) -> str:
    """Decompresses an int back into a string"""
    gene: str = ''
    for i in range(0, len(bin(bit_string))-3, 2):
        bits: int = bit_string >> i & 0b11
        if bits == 0b00:
            gene += "A"
        if bits == 0b01:
            gene += "C"
        if bits == 0b10:
            gene += "G"
        if bits == 0b11:
            gene += "T"
    return gene[::-1]


if __name__ == "__main__":
    original_gene = 'AGTGCCCAAGTCGATAAAAAGAGAATTCAAGGTGTTTGCCGAG'
    compressed_gene = compress_gene(original_gene)
    decompressed_gene = decompress_gene(compressed_gene)
    
    assert original_gene == decompressed_gene
    
    print(f'Gene {original_gene!r} compressed to {compressed_gene} and '
          f'then decompressed back to {decompressed_gene!r}')
    
    print(f'Original gene size: {getsizeof(original_gene)}')
    print(f'Compressed gene size: {getsizeof(compressed_gene)}')

