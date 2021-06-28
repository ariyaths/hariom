# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from time import time as tm
start_time = tm()

# import numpy as np
# import pandas as pd
#from collections import OrderedDict


WORKFILE_0 = "D:\\code\\dna\\E_coli.txt"
WORKFILE_1 = "D:\\code\\dna\\Vibrio_cholerae_short.txt"
WORKFILE_2 = "D:\\code\\dna\\dataset_3_5.txt"
WORKFILE_3 = "D:\\code\\dna\\dataset_example_H.txt"
WORKFILE_5 = "D:\\code\\dna\\Sample_Dataset.txt"
# WORKFILE_1 = "D:\\code\\dna\\Vibrio_cholerae.txt"
# WORKFILE_1 = "D:\\code\\dna\\dataset_5_5.txt"
# WORKFILE_1 = "D:\\code\\dna\\dataset_4_5_example.txt"
# WORKFILE_1 = "D:\\code\\dna\\ex135.txt"
# WORKFILE_1 = "D:\\code\\dna\\dataset_2994_5.txt"

OUTPUTFILE = "D:\\code\\dna\\computing_frequencies_output.txt"
# OUTPUTFILE = "D:\\code\\dna\\complementary_nucleotide_output.txt"


def read_dna(workfile):
    """    Parameters:     workfile : str
        String containing the DNA file path.

    Returns:     dna_data : str
        String containing the contents of the DNA file.
    """
    with open (workfile) as file:
        dna_data = file.read()

    return dna_data


# def pattern_count(dna_data, kmer):
#     """Parameters:
#     dna_data : str
#         String containing the contents of the DNA file.
#     kmer : str
#         String containing DNA pattern (eg. ACGT).

#     Returns     count : int
#         Count of kMer in input DNA strand.
#     """

#     count = 0
#     k = len(kmer)

#     for i in range(len(dna_data)-k+1):
#         if dna_data[i:(i+k)] == kmer:
#             count += 1

#     return count


# # print(pattern_count(read_dna(WORKFILE_2), "AACC"))


# def frequent_words(dna_data, k, occurence=0):
#     """Parameters:
#     dna_data : str
#         String containing the contents of the DNA file.
#     k : int
#         Length of a kMer.
#     occurence : int, optional
#         Number of times a kMer is repeated in input DNA strand.
#         The default is 0.

#     Returns:     frequent_patterns : set
#         A set containing all kMers of length k that repeat "occurence" times,
#         or maximum times
#     """

#     list_count = []
#     frequent_patterns = set()

#     for i in range (len(dna_data) - k + 1):
#         kmer = dna_data[i:i+k]
#         list_count.append(pattern_count(dna_data, kmer))

#     if occurence == 0:
#         max_count = max(list_count)
#     else:
#         max_count = occurence

#     for j in range (len(dna_data) - k + 1):
#         if list_count[j] >= max_count:
#             kmer = dna_data[j:j+k]
#             frequent_patterns.add(kmer)

#     return frequent_patterns


# # print(frequent_words(read_dna(WORKFILE_2),12))


def complementary_nucleotide(kmer):
    """    Parameters:    kmer : str
        String containing DNA pattern (eg. ACGT).

    Returns:    str
        String containing complementary nucleotide of input DNA strand.
    """

    k = len(kmer)

    with open(OUTPUTFILE, "w") as file:
        for i in range (k):
            if kmer[i] == "A":
                file.write("T")
            if kmer[i] == "T":
                file.write("A")
            if kmer[i] == "C":
                file.write("G")
            if kmer[i] == "G":
                file.write("C")

    with open(OUTPUTFILE, "r") as file:
        return file.read()


# print(complementary_nucleotide("AACC"[::-1]))


def occurence_pattern(dna_data, kmer):
    """    Parameters:
    dna_data : str
        String containing the contents of the DNA file.
    kmer : str
        String containing DNA pattern (eg. ACGT).

    Returns:    list_count : list
        Count of kMer in input DNA strand.
    """

    list_count = []
    k = len(kmer)
    l_dna = len(dna_data)

    for i in range(l_dna-k+1):
        if dna_data[i:(i+k)] == kmer:
            list_count.append(i)

    return list_count


# print(occurence_pattern(read_dna(WORKFILE_1), kmer = "AACC"))


def number_to_pattern(list_number, k, base=4, nucleotides="ACGT"):
    """    Parameters:    list_number : int
        The number of the pattern in the kMers list.
    k : int
        Length of the kMer.
    base : int, optional
        The number of nucleotides. The default is 4.
    nucleotides : str, optional
        The nucleotides of a DNA strand. The default is "ACGT".

    Returns:    kmers : str
        String containing the kMer of list_number.
    """

    kmers = []


    while list_number:
        kmers.append(nucleotides[int(list_number % base)])
        list_number = list_number // base

    while len(kmers) < k:
        kmers.append("A")

    kmers.reverse()

    return ''.join(kmers)


# print(number_to_pattern(5437, 8))


def nucleotide_combinations_list(k):
    """    Parameters:    k : int
        Length of the kMer.

    Returns:    kmer_list : list
        list of all kMers with length k.
    """

    kmer_list = []

    for i in range(4**k):
        kmer_list.append(number_to_pattern(i, k))

    return kmer_list


# print(*nucleotide_combinations_list(4))

def switch_neucleotides_to_number(argument):
    """Parameters:     argument : str
        A kMer.

    Returns:    int
        returns a number corresponding to the quarternary
    """

    switcher = {
        "A": 0,
        "C": 1,
        "G": 2,
        "T": 3,
    }
    return switcher.get(argument, "index out of bounds")

# print(switch_neucleotides_to_number('y'))


def pattern_to_number(kmer):
    """Parameters:    kmer : str
        String containing DNA pattern (eg. ACGT).

    Returns:    int
       Searches full list of kmer patterns and returns the index value
    """

    # this code also works, but is slower
    # k = len(kmer)
    # full_list = nucleotide_combinations_list(k)
    # p_index = full_list.index(kmer)

    count = len(kmer)
    add_parts = 0

    for i in kmer:
        num = switch_neucleotides_to_number(i)
        count -= 1
        add_parts = num * (4**count) + add_parts
    p_index = add_parts

    return p_index

print(pattern_to_number("ATGCAA")) # q: ATGCAA, ans: 912


def computing_frequencies(dnadata, k):
    """Parameters:
    ----------
    dnadata : str
        String containing the contents of the DNA file.
    k : int
        Length of the k_mer.

    Returns:    frequency_dict : dict
        Returns a complete dictionary containing all possible k_mers in size k
        with the value of the number of times it occurs.
    """

    # this code works, it uses LOL, its slow
    # kmer_listoflist = []

    # for i in range(4**k):
    #     kmer_listoflist.append([number_to_pattern(i, k), 0])

    # for i in range(len(dnadata)-k):
    #     kmer = dnadata[i:i+k]
    #     qnery_kmer = pattern_to_number(kmer)
    #     count = kmer_listoflist[qnery_kmer][1] + 1
    #     kmer_listoflist[qnery_kmer][1] = count
    # np_a = np.array(kmer_listoflist)

    # return np_a[:,1]


    # this code works, it uses PANDAS DF, its slow
    # for i in range(4**k):
    #     kmer_listoflist.append([number_to_pattern(i, k), 0])

    # kmer_df = pd.DataFrame(kmer_listoflist, columns=('Pattern','Frequency'))

    # for i in range(len(dnadata)-k):
    #     kmer = dnadata[i:i+k]
    #     qnery_kmer = pattern_to_number(kmer)
    #     count = kmer_df.loc[qnery_kmer].at['Frequency'] + 1
    #     kmer_df.at[qnery_kmer, 'Frequency'] = count

    # kmer_df.drop(kmer_df[kmer_df['Frequency'] == 0].index, inplace = True)

    # return kmer_df


    frequency_dict = {}
    dnalen2 = len(dnadata)

    for i in range(4**k):
        k_mers = number_to_pattern(i, k)
        frequency_dict[k_mers] = 0

    for i in range(dnalen2 -k +1):
        kmer = dnadata[i:i+k]
        frequency_dict[kmer] += 1

    return frequency_dict.values()


#print(computing_frequencies(read_dna(WORKFILE_0),9))


def faster_frequent_words(dna_data2, k):
    """Parameters:
    dna_data : str
        String containing the contents of the DNA file.
    k : int
        Length of a kMer.

    Returns
    -------
    frequent_patterns : set
        A set containing all kMers of length k that repeat "occurence" times,
        or maximum times"""

    frequent_patterns = set()
    frequent_array = list(computing_frequencies(dna_data2, k))
    max_count = max(frequent_array)

    for i in range((4**k)):
        if frequent_array[i] == max_count:
            kmer = number_to_pattern(i, k)
            frequent_patterns.add(kmer)
    return frequent_patterns

print(faster_frequent_words("TACGTACGTACGTCGTTACG", 3))#read_dna(WORKFILE_1), 3))


def frequency_table(dnadata, k, sorted_list=False):
    freqdict = {i: 0 for i in nucleotide_combinations_list(k)}

    for i in range(len(dnadata) -k +1):
        kmer = dnadata[i:i+k]

        if kmer in freqdict.keys() :
            freqdict[kmer] += 1
        else:
            freqdict[kmer] = 0

    if sorted_list:
        return sorted(freqdict)

    return freqdict

# print(frequency_table(read_dna(WORKFILE_0), 9))

def better_frequent_words(dnadata, k, occurence=0):
    frequent_patterns = set()
    freqdict = frequency_table(dnadata, k)

    if occurence == 0:
        maxdict = max(freqdict.values())
    else:
        maxdict = occurence

    for freqkey, freqval in freqdict.items():
        if freqval >= maxdict:
            frequent_patterns.add(freqkey)

    return frequent_patterns


# print(*better_frequen t_words(ori, 3, 4 ))#read_dna(WORKFILE_1), 3))

def clump_finding(dna_data, k, l_ori, occurence):
    """

    Parameters
    ----------
    dna_data : str
        String containing the contents of the DNA file.
    k : int
        Length of a kMer.
    l_ori : int
        The length of ori of the input DNA strand.
    occurence : int
        Number of times a kMer is repeated in input DNA strand.

    Returns
    -------
    sorted_ans : list
        A set containing all kMers of length k that repeat "occurence" times,
        or maximum times.

    """
    maxset = tuple()
    answer_set = set()

    for i in range (len(dna_data)-l_ori+1):
        ori = dna_data[i:i+l_ori]
        maxset += tuple(better_frequent_words(ori, k, occurence))

    for val in maxset:
        # val = val.replace("{'", "")
        # val = val.replace("'}", "")
        # val = val.replace(",", "")
        # val = val.replace("' '", " ")
        if val != "set()":
            answer_set.add(val)

    sorted_ans = sorted(answer_set)

    return sorted_ans

#print(clump_finding(read_dna(WORKFILE_3), 3, 20, 3))


def better_frequent_words_ori(dnadata, k, l_ori, occurence):
    frequent_patterns = set()
    for i in range(len(dnadata)-l_ori):
        if i == 0:
            ori = dnadata[i:i+l_ori]
        else:
            oripos = i+l_ori-k
            ori = dnadata[oripos:oripos+l_ori]


        freqdict = OrderedDict()
        freqdict = (frequency_table(ori, k))

        for kmer, freq in freqdict.items():
            if freq == occurence:
                frequent_patterns.add(kmer)

    return frequent_patterns

# print(*better_frequent_words_ori(read_dna(WORKFILE_2), 3, 20, 4))



total_time = tm() - start_time
m, s = divmod(total_time, 60)
h, m = divmod(m, 60)
print(f'{h:.0f}:{m:02.0f}:{s:02.2f}')
print("--- %s seconds total time ---" % (tm() - start_time))
