"""
Homework 01
DO NOT RENAME THIS FILE OR ANY DEFINITIONS!
Place this file in your github repo inside of a folder titled "Homework".
"""


# String Functions
def fast_complement(dna):
    """
    Uses a dictionary to convert a DNA sequence into the complement strand.  C <--> G,  T <--> A
    :param dna: a string containing only the characters C, T, A, and G
    :return: a string containing only the characters C, T, A, and G
    """
    dictionary = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    compliment = ''.join([dictionary[element] for element in dna])
    return compliment

def remove_interval(s, start, stop):
    """
    Removes the interval of characters from a string or list inclusively, 0 based
    EX: remove_intervals('ABCDEFGHI', 2, 5) will return 'ABGHI'.
    :param s: a string
    :param start: a non-negative integer
    :param stop: a non-negative integer greater than the start integer.
    :return: a string
    """
    result = s[:start] + s[stop+1:]
    return result

def kmer_list(s, k):
    """
    Generates all kmers of size k for a string s and store them in a list
    :param s: any string
    :param k: any integer greater than zero
    :return: a list of strings
    """
    kmerslist = []
    strlength = len(s)
    tempstr = strlength - k + 1
    for element in range(0, tempstr):
        kmerslist.append(s[element:element + k])
    return kmerslist

def kmer_set(s, k):
    """
    Generates all kmers of size k for a string s and store them in a set
    :param s: any string
    :param k: any integer greater than zero
    :return: a set of strings
    """
    kmerset = set()
    strlength = len(s)
    tempstr = strlength - k + 1
    for element in range(0, tempstr):
        kmerset.add(s[element:element + k])
    return kmerset

def kmer_dict(s, k):
    """
    Generates all kmers of size k for a string s and store them in a dictionary with the
    kmer(string) as the key and the number of occurances of the kmer as the value(int).
    :param s: any string
    :param k: any integer greater than zero
    :return: a set of strings
    """
    kmerdictionary = {}
    strlength = len(s)
    tempstr = strlength - k + 1
    for element in range(0, tempstr):
        str = s[element:element + k]
        if str not in kmerdictionary:
            kmerdictionary[str] = 0
        kmerdictionary[str] = kmerdictionary[str]+1
    return kmerdictionary

# Reading Files
def head(file_name):
    """
    Prints the FIRST 10 lines of a file
    :param file_name: a string
    :return: None
    """
    f = open(file_name)
    file_content = f.readlines()
    new_list = file_content[:10]
    for p in new_list:
        print(p)
    return

def tail(file_name):
    """
    Prints the LAST 10 lines of a file
    :param file_name: a string
    :return: None
    """
    f = open(file_name)
    file_content = f.readlines()
    new_list = file_content[-10:]
    for p in new_list:
        print(p)
    return

def print_even(file_name):
    """
    Prints the even numbered lines of a file
    :param file_name: a string
    :return: None
    """
    f = open(file_name)
    file_content = f.readlines()
    new_list = file_content[1::2]
    for i in new_list:
        print(i)
    return

def csv_list(file_name):
    """
    Read in a CSV file to a 2D array (In python it is a list of lists)
    :param file_name: a string
    :return: a list of lists
    """
    two_dim_array = []
    f = open(file_name)
    file_lines = f.read().split('\n')

    for line in file_lines:
        elements = line.split(',')
        inner_list = []

        for ele in elements:
            inner_list.append(ele)
        two_dim_array.append(inner_list)

    print("helllo"+two_dim_array[1][2])
    return two_dim_array


def get_csv_column(file_name, column):
    """
    Reads in a CSV file and returns a list of values belonging to the column specified
    :param file_name: a string
    :param column: a positive integer
    :return: a list
    """
    two_dim_array = []
    f = open(file_name)
    file_lines = f.read().split('\n')

    for line in file_lines:
        elements = line.split(',')
        inner_list = []

        for ele in elements:
            inner_list.append(ele)
        two_dim_array.append(inner_list)

    return [i[column] for i in two_dim_array]


def fasta_seqs(file_name):
    """
    Reads in a FASTA file and returns a list of only the sequences
    :param file_name: a string
    :return: a list of strings
    """
    with open(file_name, 'r') as infile:
        text = infile.read()
        seqs = text.split('>')[1:]
        sequence = []
        for seq in seqs:
            try:
                x = seq.split('\n', 1)
                sequence.append(x[1].replace('\n', ''))
            except:
                print('error')
    return sequence


def fasta_headers(file_name):
    """
    Reads in a FASTA file and returns a list of only the headers (Lines that start with ">")
    :param file_name: a string
    :return: a list of strings
    """
    with open(file_name, 'r') as infile:
        text = infile.read()
        seqs = text.split('>')[1:]
        header = []
        for seq in seqs:
            try:
                x = seq.split('\n', 1)
                header.append(x[0])
            except:
                print('error')
    return header

def fasta_dict(file_name):
    """
    Reads in a FASTA file and returns a dictionary of the format {header: sequence, ...}, where
    the sequence headers are keys and the sequence is the value
    :param file_name: a string
    :return: a dictionary
    """
    with open(file_name, 'r') as infile:
        fasta_dict = {}
        y = []
        text = infile.read()
        seqs = text.split('>')[1:]
        sequence = []
        for seq in seqs:
            try:
                x = seq.split('\n', 1)
                sequence.append(x[1].replace('\n', ''))
                y.append(x)

            except:
                print('error')
        for ele in y:
            fasta_dict[ele[0]] = ele[1].replace('\n', '')

    return fasta_dict

def fastq_to_fasta(file_name, new_name=None):
    """
    Reads in a FASTQ file and writes it to a new FASTA file. This definition should also
    keep the same file name and change the extension to from .fastq to .fasta if new_name is not specified.
    EX: fastq_to_fasta('ecoli.fastq') should write to a new file called ecoli.fasta
    :param file_name: a string
    :param new_name: a string
    :return: None
    """
    if file_name.endswith('.fastq'):
        if new_name is None:
            fasta_file = file_name.replace('.fastq','.fasta')
        else:
            fasta_file = new_name
        try:
            with open(file_name, 'r') as infile:
                text = infile.read()
                seqs = text.split('@')
                fasta_file = open(fasta_file, 'w')

                for s in seqs:
                    try:
                        if len(s) == 0:
                            continue
                        x = s.split('\n')
                        fasta_file.write('>'+x[0]+'\n'+x[1]+'\n')
                    except:
                        print('Error')
                fasta_file.close()
        except:
            print('Input file error')
    else:
        print('Invalid filename')
    return

# Transcription and Translation
def reverse_complement(dna):
    """
    Returns the strand of DNA that is the reverse complement of the sequence given
    :param dna: a string containing only the characters C, T, A, and G
    :return: a string containing only the characters C, T, A, and G
    """
    dictionary = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    rev = reversed(dna)
    compliment = ''.join([dictionary[element] for element in rev])
    return compliment

def transcribe(dna):
    """
    Transcribes a string of DNA into RNA
    :param dna: a string containing only the characters C, T, A, and G
    :return: a string containing only the characters C, U, A, and G
    """
    transcribed_dna = dna.replace('T', 'U')
    return transcribed_dna

def translate(rna):
    """
    Translates the strand of RNA given into its amino acid composition.
    DO NOT INCLUDE * IN YOUR RETURN STRING
    :param rna: a string containing only the characters C, U, A, and G
    :return: a string containing only the characters G, A, L, M, F, W, K, Q, E, S, P, V, I, C, Y, H, R, N, D, and T
    """
    RNA_CODON_TABLE = {"UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L",
           "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S",
           "UAU": "Y", "UAC": "Y", "UAA": "*", "UAG": "*",
           "UGU": "C", "UGC": "C", "UGA": "*", "UGG": "W",
           "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
           "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
           "CAU": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
           "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R",
           "AUU": "I", "AUC": "I", "AUA": "I", "AUG": "M",
           "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
           "AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K",
           "AGU": "S", "AGC": "S", "AGA": "R", "AGG": "R",
           "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
           "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
           "GAU": "D", "GAC": "D", "GAA": "E", "GAG": "E",
           "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G"}

    result_string = ""

    for i in range(0, len(rna), 3):
        try:
            if (RNA_CODON_TABLE.get(rna[i:i + 3]) == "*"):
                break
            else:
                result_string = result_string+RNA_CODON_TABLE.get(rna[i:i + 3])
        except KeyError:
            print("ignore")
    return result_string

def reading_frames(dna):
    """
    Generates a list of all 6 possible reading frames for a given strand of DNA
    For the non-biologists: https://en.wikipedia.org/wiki/Open_reading_frame
    :param dna: a string containing only the characters C, T, A, and G
    :return: a list of 6 strings containing only C, T, A, and G
    """

    reading_frames = []

    reading_frames.append(dna)
    reading_frames.append(dna[1:-2])
    reading_frames.append(dna[2:-1])

    dictionary = {'C': 'G', 'T': 'A','A': 'T','G': 'C'}
    rev = reversed(dna)
    reverse_compli = ''.join([dictionary[element] for element in rev])

    reading_frames.append(reverse_compli)
    reading_frames.append(reverse_compli[1:-2])
    reading_frames.append(reverse_compli[2:-1])

    return reading_frames

