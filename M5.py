def Filter_and_Annotate(protein_candidates):
    valid_proteins = []
    counter = 0

    for protein in protein_candidates:
        seq_length = protein.get('length', len(protein.get('sequence', '')))
        mw = protein.get('mw', 0)

        length_condition = seq_length >= 4

        weight_condition = 500 <= mw <= 200000

        if length_condition and weight_condition:
            counter += 1

            protein_id = f"BFG_{counter:03d}"
            valid_protein = protein.copy()
            valid_protein['protein_id'] = protein_id

            valid_protein['length'] = seq_length
            valid_proteins.append(valid_protein)

    return valid_proteins

