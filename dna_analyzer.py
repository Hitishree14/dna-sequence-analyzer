
def analyze_dna(sequence):
    """Analyze a DNA sequence and return its properties."""

    sequence = "".join(sequence.split()).upper()

    if not sequence:
        raise ValueError("DNA sequence cannot be empty.")

    valid_bases = set("ATGC")

    if any(base not in valid_bases for base in sequence):
        raise ValueError("Only A, T, G and C are allowed.")

    count_A = sequence.count("A")
    count_T = sequence.count("T")
    count_G = sequence.count("G")
    count_C = sequence.count("C")

    gc_content = ((count_G + count_C) / len(sequence)) * 100

    rna = sequence.replace("T", "U")

    complement_table = str.maketrans("ATGC", "TACG")
    reverse_complement = sequence.translate(complement_table)[::-1]

    return {
        "sequence": sequence,
        "length": len(sequence),
        "A": count_A,
        "T": count_T,
        "G": count_G,
        "C": count_C,
        "GC_content": round(gc_content, 2),
        "RNA": rna,
        "reverse_complement": reverse_complement,
    }


def main():
    dna = input("Enter a DNA sequence: ")

    try:
        results = analyze_dna(dna)

        print("\n--- DNA Sequence Analysis ---")
        print("DNA sequence:", results["sequence"])
        print("Sequence length:", results["length"])
        print("A count:", results["A"])
        print("T count:", results["T"])
        print("G count:", results["G"])
        print("C count:", results["C"])
        print(f'GC content: {results["GC_content"]:.2f}%')
        print("RNA sequence:", results["RNA"])
        print("Reverse complement:", results["reverse_complement"])

    except ValueError as error:
        print("Error:", error)


if __name__ == "__main__":
    main()
