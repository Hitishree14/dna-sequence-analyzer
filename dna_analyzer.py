
def analyze_dna(sequence):
    # Clean the sequence
    sequence = sequence.upper().replace(" ", "")

    # Check that the sequence is valid
    if not sequence:
        print("Error: DNA sequence cannot be empty.")
        return

    valid_bases = "ATGC"

    for base in sequence:
        if base not in valid_bases:
            print("Error: Invalid DNA sequence.")
            print("Only A, T, G and C are allowed.")
            return

    # Calculate sequence length
    length = len(sequence)

    # Count each nucleotide
    count_A = sequence.count("A")
    count_T = sequence.count("T")
    count_G = sequence.count("G")
    count_C = sequence.count("C")

    # Calculate GC content
    gc_content = ((count_G + count_C) / length) * 100

    # Transcribe DNA into RNA
    rna = sequence.replace("T", "U")

    # Generate reverse complement
    complement_table = str.maketrans("ATGC", "TACG")
    reverse_complement = sequence.translate(
        complement_table
    )[::-1]

    # Display results
    print("\n--- DNA Sequence Analysis ---")
    print("DNA sequence:", sequence)
    print("Sequence length:", length)
    print("A count:", count_A)
    print("T count:", count_T)
    print("G count:", count_G)
    print("C count:", count_C)
    print(f"GC content: {gc_content:.2f}%")
    print("RNA sequence:", rna)
    print("Reverse complement:", reverse_complement)


# Get sequence from the user
dna = input("Enter a DNA sequence: ")

# Analyze the sequence
analyze_dna(dna)
