# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 12:32:46 2020
@author: HariOm12
"""
from time import time as tm
start_time = tm()

WORKFILE0 = "C:\\code\\dna\\Sample_Dataset.txt"
WORKFILE2 = "C:\\code\\dna\\Vibrio_cholerae.txt"
# WORKFILE0 = "C:\\code\\dna\\dataset_2_7.txt"
# WORKFILE0 = "C:\\code\\dna\\dataset_2_10.txt"
# WORKFILE0 = "C:\\code\\dna\\dataset_3_2.txt"
WORKFILE1 = "C:\\code\\dna\\dataset_3_5.txt"
# WORKFILE0 = "C:\\code\\dna\\ex145.txt"
# WORKFILE0 = "C:\\code\\dna\\dataset_4_5.txt"
WORKFILE3 = "C:\\code\\dna\\E_coli.txt"
# WORKFILE0 = "C:\\code\\dna\\dataset_2994_5.txt"
WORKFILE4 = "C:\\code\\dna\\Sample_Dataset2.txt"


def read_dna(myworkfile):
    """
    Parameters
    ----------
    myworkfile : str
        String containing the DNA file path.

    Returns
    -------
    dnadata0 : str
        String containing the contents of the DNA file.
    """

    with open(myworkfile) as file0:
        dnadata0 = file0.read()

    return dnadata0


# kmer0 = "ACGCGGCTCTGAAA"


def pattern_count(dnadata1, kmer1):
    """
    Parameters
    ----------
    dnadata1 : str
        String containing the contents of the DNA file.
    kmer1 : str
        String containing a small strand of dna to check if chunks of dnadata1
        match k-mer.

    Returns
    -------
    count : int
        Count of the kmer in input dna strand.
    """

    count = 0
    k = len(kmer1)

    for i in range(len(dnadata1) -k +1):
        if dnadata1[i:i+k] == kmer1:
            # """check if chunks of dnadata1 match k-mer"""
            count += 1

    return count


# print(pattern_count(read_dna(WORKFILE1), kmer0))


def frequent_words(dnadata2, k, occurence=0):
    """
    Parameters
    ----------
    dnadata2 : str
        String containing the contents of the DNA file.
    k : int
        k is length of kmer.
    occurence : int, optional
        occurence is the number of times the kmer occurs in dna strand. The default
        is 0 to return kmers with the max number of occurence in input dna
        strand.

    Returns
    -------
    frequent_patterns : set
        Set containing all kmers of lenght k that occur t or max number of
        times.
    """

    frequent_patterns = set()
    list_count = []

    for i in range(len(dnadata2) -k +1):
        kmer2 = dnadata2[i:i+k]
        list_count.append(pattern_count(dnadata2, kmer2))

    if occurence == 0:
        max_count = max(list_count)
    else:
        max_count = occurence

    for j in range(len(dnadata2) -k +1):

        if list_count[j] >= max_count:
            frequent_patterns.add(dnadata2[j:j+k])

    return frequent_patterns


# print(frequent_words("read_dna(WORKFILE1)", 9))


def reverse_complement(kmer3):
    """
    Parameters
    ----------
    kmer3 : str
        String containing a strand of dna.

    Returns
    -------
    str
        String containing reverse complementary nucleotide of input DNA strand.
    """
    k = len(kmer3)

    with open("reverse_complement.txt", "w") as file1:
        for i in range(k):

            if "A" in kmer3[i]:
                file1.write("T")

            if "C" in kmer3[i]:
                file1.write("G")

            if "G" in kmer3[i]:
                file1.write("C")

            if "T" in kmer3[i]:
                file1.write("A")

    with open("reverse_complement.txt", "r") as file1:
        return file1.read()


# print(reverse_complement(read_dna(WORKFILE2)[::-1]))


def pattern_matching(dnadata3, kmer4):
    """
    Parameters
    ----------
    dnadata3 : str
        String containing the contents of the DNA file.
    kmer4 : str
        String containing DNA pattern.

    Returns
    -------
    list_count : list
        Count of where the kMer is in input DNA strand.
    """

    list_count = []
    k = len(kmer4)

    for i in range(len(dnadata3) -k +1):
        if dnadata3[i:i+k] == kmer4:
            list_count.append(i)

    return list_count


# print(*pattern_matching(read_dna(WORKFILE2), "CTTGATCAT"))


def pattern_matching2(dnadata4, kmer5):
    """
    Parameters
    ----------
    dnadata4 : str
        String containing the contents of the DNA file.
    kmer5 : str
        String containing DNA pattern.

    Returns
    -------
    dict_count : dict
        Count of where the kMer is in input DNA strand.
    """

    dict_count = {}
    kmer_list = []
    kmer_revcomp_list = []
    kmer_revcomp = reverse_complement(kmer5)
    k = len(kmer5)

    for i in range(len(dnadata4) -k +1):
        if dnadata4[i:i+k] == kmer5:
            kmer_list.append(i)
        if dnadata4[i:i+k] == kmer_revcomp[::-1]:
            kmer_revcomp_list.append(i)

    dict_count["kmer positions"] = kmer_list
    dict_count["kmer reverse complement positions"] = kmer_revcomp_list

    return dict_count


def clump_finding(dnadata5, k, occurence, orilen=0):
    """
    Parameters
    ----------
    dnadata5 : str
        String containing the contents of the DNA file.
    k : int
        Length of kmer.
    occurence : int
        Number of times the kmer occurs in dna strand.
    orilen : int, optional
        DESCRIPTION. The default is 0.

    Returns
    -------
    sorted_answer_set : list
        Returns a list of kmers in the ori that occur more and equal to the
        occurence given.

    """
    dnalen1 = len(dnadata5)
    sos_frequent_patterns = set()
    answer_set = set()

    for i in range(dnalen1 -orilen +1):
        ori = dnadata5[i:i+orilen]
        sos_frequent_patterns.add(str(frequent_words(ori, k, occurence)))

    for val in sos_frequent_patterns:
        val = val.replace("{'", "")
        val = val.replace("'}", "")
        val = val.replace(",", "")
        val = val.replace("' '", " ")
        if val != "set()":
            answer_set.add(val)

    sorted_answer_set = sorted(answer_set)

    return sorted_answer_set


print(clump_finding(read_dna(WORKFILE4), 3, 3, 20))

total_time = tm() - start_time
m, s = divmod(total_time, 60)
h, m = divmod(m, 60)
print(f'{h:.0f}:{m:02.0f}:{s:02.2f}')
print("--- %s seconds ---" % (tm() - start_time))


# def number_to_pattern(numb, k, base=4):
#     """
#     Parameters
#     ----------
#     numb : int
#         The number of the pattern in the kMers list.
#     k : int
#         Length of the kmer.
#     base : int, optional
#         Number of nucleotides(which is 4; "A, C, G, T"). The default is 4.

#     Returns
#     -------
#     str
#         Returns a quaternary of the input numb that is converted to ACGT (A:0,
#         C:1, G:2, T:3).
#     """

#     nucleotides = "ACGT"
#     kmers = []

#     while numb:
#         kmers.append(nucleotides[int(numb % base)])
#         numb = numb // base

#     while len(kmers) < k:
#         kmers.append("A")

#     kmers.reverse()

#     return ''.join(kmers)


# # print(number_to_pattern(5437, 8))


# def nucleotide_index(k):
#     """
#     Parameters
#     ----------
#     k : int
#         Length of the kmer.

#     Returns
#     -------
#     full_list : list
#         Returns a complete list of all possible kmers the size of input k.
#     """

#     full_list = [] # set()

#     for i in range(4**k):
#         full_list.append(number_to_pattern(i, k))

#     return full_list


# # print(nucleotide_index(len(kmer0)))


# # def pattern_to_number(kmer6):
# #     """
# #     Parameters
# #     ----------
# #     kmer6 : str
# #         String containing DNA pattern.

# #     Returns
# #     -------
# #     int
# #         Returns the position the input kmer is in.
# #     """

# #     full_list = nucleotide_index(len(kmer6))

# #     return full_list.index(kmer6)


# # print(pattern_to_number(read_dna(WORKFILE2)))


# def switch_neucleotides_to_number(argument):
#     switcher = {
#         "A": 0,
#         "C": 1,
#         "G": 2,
#         "T": 3,
#     }
#     return switcher.get(argument, 4)


# def pattern_to_number(kmer):
#     """
#     Parameters
#     ----------
#     kmer : str
#         String containing DNA pattern (eg. ACGT).

#     Returns
#     -------
#     int
#        Searches full list of kmer patterns and returns the index value.
#     """
#     # k = len(kmer)
#     # full_list = nucleotide_combinations_list(k)
#     # p_index = full_list.index(kmer)

#     count = len(kmer)
#     add_parts = 0
#     for i in kmer:
#         num = switch_neucleotides_to_number(i)
#         count -= 1
#         add_parts = num * (4**count) + add_parts
#     p_index = add_parts

#     return p_index

# # print(pattern_to_number("ATGCAA"))


# def count_frequency(my_list):
#     freq = {}
#     for item in my_list:
#         if item in freq:
#             freq[item] += 1
#         else:
#             freq[item] = 1

#     # for key, value in freq.items():
#     #     print ("% d : % d"%(key, value))

#     return freq


# def computing_frequencies(dnadata6, k):
#     """
#     Parameters
#     ----------
#     dnadata6 : str
#         String containing the contents of the DNA file.
#     k : int
#         Length of the kmer.

#     Returns
#     -------
#     frequency_dict : dict
#         Returns a complete dictionary containing all possible kmers in size k
#         with the value of the number of times it occurs.
#     """
#     frequency_dict = {}
#     dnalen2 = len(dnadata6)

#     for i in range(4**k):
#         kmers = number_to_pattern(i, k)
#         frequency_dict[kmers] = 0

#     for i in range(dnalen2 -k +1):
#         kmer7 = dnadata6[i:i+k]
#         frequency_dict[kmer7] += 1

#     return frequency_dict


# # print(computing_frequencies(read_dna(WORKFILE3), 9))

# # for k,v in computing_frequencies("TCCGCTCCGTCCTCCCGTTG", 3).items():
# #     if v > 0: print(k, v)

# def frequent_words2(dnadata7, k, occurence2=0):
#     feq_map = computing_frequencies(dnadata7, k)
#     frequent_patterns = tuple()
#     mylist = list(frequent_patterns)
#     numb_position = []

#     kmer_list = list(feq_map.keys())
#     numb_list = list(feq_map.values())

#     if occurence2 == 0:
#         max_count = max(numb_list)

#     else:
#         max_count = occurence2

#     for i in range(len(numb_list)):
#         if numb_list[i] == max_count:
#             numb_position.append(i)

#     for i in numb_position:
#         mylist.append(kmer_list[i])

#     frequent_patterns = tuple(mylist)

#     return frequent_patterns


# # print(*frequent_words2(computing_frequencies(read_dna(WORKFILE3), 9), 9))


# def clump_finding(dnadata5, k, occurence, orilen=0):
#     dnalen1 = len(dnadata5)
#     sos_frequent_patterns = set()
#     # answer_set = set()

#     if orilen == 0:
#         sos_frequent_patterns.add(str(frequent_words2(dnadata5, k, occurence)))
#     else:
#         for i in range(0, dnalen1 -orilen +1):
#             ori = dnadata5[i:i+orilen]
#             sos_frequent_patterns.add(frequent_words2(ori, k, occurence))

#     # for val in sos_frequent_patterns:
#     #     val = val.replace("{'", "")
#     #     val = val.replace("'}", "")
#     #     val = val.replace(",", "")
#     #     val = val.replace("' '", " ")
#     #     if val != "set()":
#     #         answer_set.add(val)

#     # sorted_answer_set = sorted(answer_set)

#     return sos_frequent_patterns # sorted_answer_set


# # print(*clump_finding(read_dna(WORKFILE0), 3, 4, 20))

# # total_time = tm() - start_time
# # m, s = divmod(total_time, 60)
# # h, m = divmod(m, 60)
# # print(f'{h:.0f}:{m:02.0f}:{s:02.2f}')
# # print("--- %s seconds ---" % (tm() - start_time))

# def clump_finding2(dna, k, occurence, orilen):
#     sos_frequent_patterns = []
#     answer_set = set()
#     dnalen = len(dna)
#     for i in range(orilen -(dnalen %(orilen -k +1))):
#         dna = dna + "0"

#     dnalen = len(dna)

#     # with open(dna, "a") as file1:
#     #     list_count = pattern_matching(dna, "0")
#     #     list_len = len(list_count)

#     #     for i in range(orilen -(dnalen %(orilen -k +1))):
#     #         if len(dna[-1:-list_len]) != (orilen -(dnalen %(orilen -k +1)) +1):
#     #             file1.write("0")

#     for i in range(0, dnalen -orilen +1, orilen -k +1):
#         ori = dna[i:i+orilen]
#         sos_frequent_patterns.append(frequent_words2(ori, k, occurence))

#     for j in sos_frequent_patterns:
#         if j:
#             answer_set.add(j)

#     proper_sos = [', '.join(map(str, x)) for x in answer_set]
#     # sorted_sos = sorted(sos_frequent_patterns)

#     return proper_sos # sorted_sos


# print(clump_finding2(read_dna(WORKFILE0), 3, 4, 20))

# total_time = tm() - start_time
# m, s = divmod(total_time, 60)
# h, m = divmod(m, 60)
# print(f'{h:.0f}:{m:02.0f}:{s:02.2f}')
# print("--- %s seconds ---" % (tm() - start_time))
