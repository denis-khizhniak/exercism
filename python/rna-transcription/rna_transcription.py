def to_rna(dna_strand):
    rna_transcript_rule = {
            'G': 'C',
            'C': 'G',
            'T': 'A',
            'A': 'U',
            }

    return ''.join([rna_transcript_rule[l] for l in dna_strand])
