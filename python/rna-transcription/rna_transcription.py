def to_rna(dna_strand):
	mappings = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}
	rna_transcription = ''
	
	for ch in dna_strand:
		if mappings.has_key(ch):
			rna_transcription += mappings[ch]
		else:
			rna_transcription = ''
			break

	return rna_transcription
	
