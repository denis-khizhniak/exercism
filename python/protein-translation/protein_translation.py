import itertools


def break_into_codons(strand):
    return [strand[i:i+3] for i in range(0, len(strand), 3)]


def proteins(strand):
    codon_dict = {
            'AUG': 'Methionine',
            'UUU': 'Phenylalanine',
            'UUC': 'Phenylalanine',
            'UUA': 'Leucine',
            'UUG': 'Leucine',
            'UCU': 'Serine',
            'UCC': 'Serine',
            'UCA': 'Serine',
            'UCG': 'Serine',
            'UAU': 'Tyrosine',
            'UAC': 'Tyrosine',
            'UGU': 'Cysteine',
            'UGC': 'Cysteine',
            'UGG': 'Tryptophan',
            'UAA': None,
            'UAG': None,
            'UGA': None
            }
    codons = break_into_codons(strand)

    return list(itertools.takewhile(lambda x: x is not None, (codon_dict[codon] for codon in codons)))
