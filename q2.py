import random
import math
from quad import qgram
import numpy as np

TEMPERATURE = 100
STEP = 1
COUNT = 100000

def shuffle(table):
    for i in range (0, 24):
        j = random.randint(i + 1, 24)
        temp = table[i]
        table[i] = table[j]
        table[j] = temp
    return table

def swap(table):
    i = random.randint(0,len(table) - 1)
    j = (i + 1) % len(table)
    temp = table[i]
    table[i] = table[j]
    table[j] = temp
    return table

def swap_col(table):
    i = random.randint(0, 4)
    j = random.randint(0, 4)
    if i == j:
        j = (i + 1) % 5
    
    for k in range (0, 5):
        temp = table[(5*i) + k]
        table[((5*i) + k)] = table[((5*j) + k)]
        table[((5*j) + k)] = temp
    return table

def swap_row(table):
    i = random.randint(0, 4)
    j = random.randint(0, 4)
    if i == j:
        j = (i + 1) % 5
    
    for k in range (0, 5):
        temp = table[(5*k) + i]
        table[((5*k) + i)] = table[((5*k) + j)]
        table[((5*k) + j)] = temp
    return table

def reverse(table):
    table.reverse()
    return table

def modify_key(table):
    i = random.randint(0, 5)
    if i == 0 :
        table = swap_row(table)
    elif i == 1 :
        table = swap_col(table)
    elif i == 2:
        table = reverse(table)
    else :
        table = swap(table)
    return table

def make_key_table():
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    # key = key.upper()
    table = list(alphabet)
    return shuffle(table)
    
    # for letter in key:
    #     if letter not in table and letter in alphabet:
    #         table.append(letter)
    
    # for letter in alphabet:
    #     if letter not in table:
    #         table.append(letter)

def decrypt(table, cipher):
    assert len(cipher) % 2 == 0, "Cipher does not have even length"

    plain_text = ""

    for i in range(0, len(cipher)//2):
        letter_1 = cipher[2*i]
        letter_2 = cipher[(2*i) + 1]

        index_1 = table.index(letter_1)
        index_2 = table.index(letter_2)

        row_1 = index_1 // 5
        col_1 = index_1 % 5

        row_2 = index_2 // 5
        col_2 = index_2 % 5

        if row_1 == row_2:
            plain_text += table[row_1 * 5 + ((col_1 - 1) % 5)]
            plain_text += table[row_2 * 5 + ((col_2 - 1) % 5)]
        elif col_1 == col_2:
            plain_text += table[(((row_1 - 1) % 5) * 5) + col_1]
            plain_text += table[(((row_2 - 1) % 5) * 5) + col_2]
        else :
            plain_text += table[(row_1 * 5) + col_2]
            plain_text += table[(row_2 * 5) + col_1]
    
    return plain_text

def heuristic(plain_text):
    score = 0
    for i in range (0, len(plain_text) - 3):
        score += qgram[(17576*(ord(plain_text[i]) - ord('A'))) + (676*(ord(plain_text[i+1]) - ord('A'))) + (26*(ord(plain_text[i+2]) - ord('A'))) + ((ord(plain_text[i+3]) - ord('A')))]

 
def simulated_annealing(best_table, cipher):
    solution = decrypt(best_table, cipher)
    max_score = heuristic(solution)
    best_score = max_score
    max_table = best_table.copy()
    print("SCORE: {}".format(best_score))
    print("KEY: {}".format("".join(best_table)))
    print("Plain Test: {}".format(solution))
    print()
    for t in np.arange(TEMPERATURE, -1, -STEP):
        for c in range (0, COUNT, 1):
            cur_table = modify_key(max_table.copy())
            cur_solution = decrypt(cur_table, cipher)
            cur_score = heuristic(cur_solution)
            dF = cur_score - max_score

            if (dF >= 0 or (t > 0 and math.exp(dF/t) > random.random())):
                max_score = cur_score 
                max_table = cur_table.copy()

            if (max_score > best_score):
                best_score = max_score
                best_table = max_table.copy()
                solution = cur_solution
                print("SCORE: {}".format(best_score))
                print("KEY: {}".format("".join(best_table)))
                print("Plain Test: {}".format(solution))
                print()

    return best_table

cipher = "VUKWTMVFNWBPVYIYWNGLCFVGPVBCYBMVFQDZFGNHTLTFNPUVXGCXVGODYDKQXNSTBVKZGFVUKWTMGFCFVMVGODZSMXQDSZXNYEORZPXHVFIYWNPKDFTKGFNYFYVSXCNPXSFGAFPVVGODBQLDPVBRYFMFAMWNBRGUGEXNPNYZZXFGBRDCUGZGQFNWXCMVCLODZPODDHSZXNZEHBFVMAODBIEWBWAFEVVBGPZXQBKTUEBRTLTMVFNWBPVYAMFLXNPZYTCAUNFXDYZSVHZSZLMYFZZXPSGBXNUNQHVYZHYUXNZGPTLGCABHGTMVCLODZBZLNPFVMAODKEBRHRZGSZKHYDTPGBZOZPZGCZHBKDFGGZZBRKQZDFXKKUBVHBLERHCYPZFSVBTSRLAMFLXNYEORZPXHVFELYWTYRKKVEYTWUVXNXAYEKPXZQFZBRLAMACXNUSEWGZXUQBGEGBKHEYUYELBRXNSGNVNXEYYNZEEZDZGFXNZTZPZGVNDXMVCLODXIVFDYGUAPNHKZFGXNSGMVCLODWBTLTSRLAMACXNUEOBDMZEUVXNOVMAXNHBMEFGYZXGVGODZBALDYEZGZZQWKFLFTYNSTFDACEIZLGFMYGZMHUVXNZOZPZGQHHFOFKZGFXNYUTUGEFGNYZRQVEZYZDXABKZDSYSLEVYKZFSEIWNSKBAWKCNXGVGODXIZGXNYUTUZPQFDBZGSZOAXNPGACUVGTFYZOZPZGMVMHXNZFWKGUQKGENPOBMHABDZFYXNYSDFROPGVGODZBZLNPORMHWKGTFYRBZGXNZFBRKSQBZQCZPTZGZTMZGFXNYEMFQKPZUVXNXNZTZPZGXIKUNSDPTSZLNPGLCHVYCNXNYEXZPTZEYMWFNPSGPZDFRMNWUPGEKWXNYUZPRONPZLNPACVGXIPZZENPVEQDQKZBFYXNZTZFYEWKGURLAMFLXNKUFYWBGPQPKTVMNSZLNPHQESPGFZMXYEFGSPFLXNSGOBMHHBKHEMZPZFOFPXVGODZBZLNPBKYSMFNWSTAFSYGZZLNPOZEZYFACPQXANUKZDKGFXIHVCHFBKSYZKDFGXNUTHVNSQLNWXCFYXNUTYEFZDMSZAMACXNSAGFXNPZUNEKCAFBRMVGODZBULPZSZXNZTYQDZBQBGWFNPOZEZDKGFBGGBPTUGPZUVPKYEFGOVXNZFFQSAGFBCXVVGODXNZGMVCLODQDUTZEFYHBRKPZHBIQHQSZXNZTHQSKGFXNZFUVTLFKPTYZEUMVCLODZPSXNUZLNPODHGVGODYFQXNPKENPNBVFEUVYQDUNGENPMVEIXZAFWFNPUVBNNUPLPKUTKWTWHBASVYMVCLODZBKLDBYUVYDFXKPZDSQOYEAMXEPZBRSEBGXGVGODYDKQXNYEORZPXHVFMVCLODYFQXSGYZGEMAYEXZFANPDZGFCBMVCLODXNZFKUQKWLTYZPGEMVCLODYDKQXNZTYQDZBQBGWFNPOZEZDKGFBGGBPNDYUGPZZSELACUYRKPZNYYFZPMVCLODYMHBZFPQDFFSXNVYCNLENPFVSWKLDBYEFDGUYMYAVYMVCLODDYPKPNDYFYXNPZYELZGFIYFLFZNSORZPYFDPNPKUUVMHSZZBALNUHXPGVGODZBKLBABGFZTLFMFUVYFGZSELACPBPZAMLNPTYSFGXNUTYEXGVGODXIPZZENPEPKEZEPMVGODZBASVYORHTBGFWQBTFFYHBRKPZAMFLXNYUXNZBNSRKKVZBAKQZPNKVOVMAOAPGVGODZBZLPQGZZLVFQDZLNPTUELMVCLODFQSMHBOVGUAXNUSKYMLYFYETDQPLDKGFEZRKPZYZKZXNPZUTNWKRQBUKYEZBAKEWEZHXPSDKGFAMACXNUEWNTLTXCAZENPRHZEFEUKSMZDYEPLPKPNQZSPFGBHGENPYRFDGPMVCLODIYEGVFMVCLODFGNPDPPQRHKUPGVGODPKYTVYKZNWFQEKMFGBTZZCZPZGMVCLODIYXEPQUTKHEZAMFLXNPZHIOFBZACEIZLGFMYGZMHBRZQSDMFMYWNLECZPTZGMVFMDQKZFQYDULKHEZDYAMACXNUEZDYEDKGFXNPTSGPZDFRMNWUFDYYMGBTSWFYBAHPNHBRLAMFZELNPABQMZBGPZLNPCZVYKZNYORGSACEVNPDQKZKHTLWKPZMVCLODYFZXNPZPTUZPBGYBDCEKCABCPEYEHBXNKUMVEIXZAFWFNPTUELMVCLODZBZLNPCZVYKZFQEPGEKWTSRLAMWNGENPBYEZZHCFGBXNYEEIPKGBPNGFHBXNUNAXROYEMVCLODYFZXNPZPTUZPBGXZPTYEFGFYTYZXNPLDBRZSYMXNZFNYYFZPBHCNLZCAGFBPZBZLGFFBKZXNSTBVITPZZEHQSZMVCLODZBKSBAAMTIPSGBXNZTDQPLYDKZTYTLFDDSPTYSMVCLODUVXNXNUTCFMAODBZKZXNYEORZPXHVFNSYSHBVTZFXCAMEGVFXNUTHVNSQLNWXCFYXNUTYEXNQZIYFGGZYUPGVGODUYFLXNZFFQYDESVFPZWYFDYDEZTSPMCYPGVGODZBRMVYSKEYPTUGPZUFNPZP"
table = make_key_table()

while True:
    table = simulated_annealing(table, cipher)

# Testing the key found
# key = list("HKNBICMGOVXLTFWPSEYURDZAQ")
# print(key)
# print(decrypt(key, cipher))

# alphabet = "abcdefghiklmnopqrstuvwxyz".upper()
# cipher = "VUKWTMVFNWBPVYIYWNGLCFVGPVBCYBMVFQDZFGNHTLTFNPUVXGCXVGODYDKQXNSTBVKZGFVUKWTMGFCFVMVGODZSMXQDSZXNYEORZPXHVFIYWNPKDFTKGFNYFYVSXCNPXSFGAFPVVGODBQLDPVBRYFMFAMWNBRGUGEXNPNYZZXFGBRDCUGZGQFNWXCMVCLODZPODDHSZXNZEHBFVMAODBIEWBWAFEVVBGPZXQBKTUEBRTLTMVFNWBPVYAMFLXNPZYTCAUNFXDYZSVHZSZLMYFZZXPSGBXNUNQHVYZHYUXNZGPTLGCABHGTMVCLODZBZLNPFVMAODKEBRHRZGSZKHYDTPGBZOZPZGCZHBKDFGGZZBRKQZDFXKKUBVHBLERHCYPZFSVBTSRLAMFLXNYEORZPXHVFELYWTYRKKVEYTWUVXNXAYEKPXZQFZBRLAMACXNUSEWGZXUQBGEGBKHEYUYELBRXNSGNVNXEYYNZEEZDZGFXNZTZPZGVNDXMVCLODXIVFDYGUAPNHKZFGXNSGMVCLODWBTLTSRLAMACXNUEOBDMZEUVXNOVMAXNHBMEFGYZXGVGODZBALDYEZGZZQWKFLFTYNSTFDACEIZLGFMYGZMHUVXNZOZPZGQHHFOFKZGFXNYUTUGEFGNYZRQVEZYZDXABKZDSYSLEVYKZFSEIWNSKBAWKCNXGVGODXIZGXNYUTUZPQFDBZGSZOAXNPGACUVGTFYZOZPZGMVMHXNZFWKGUQKGENPOBMHABDZFYXNYSDFROPGVGODZBZLNPORMHWKGTFYRBZGXNZFBRKSQBZQCZPTZGZTMZGFXNYEMFQKPZUVXNXNZTZPZGXIKUNSDPTSZLNPGLCHVYCNXNYEXZPTZEYMWFNPSGPZDFRMNWUPGEKWXNYUZPRONPZLNPACVGXIPZZENPVEQDQKZBFYXNZTZFYEWKGURLAMFLXNKUFYWBGPQPKTVMNSZLNPHQESPGFZMXYEFGSPFLXNSGOBMHHBKHEMZPZFOFPXVGODZBZLNPBKYSMFNWSTAFSYGZZLNPOZEZYFACPQXANUKZDKGFXIHVCHFBKSYZKDFGXNUTHVNSQLNWXCFYXNUTYEFZDMSZAMACXNSAGFXNPZUNEKCAFBRMVGODZBULPZSZXNZTYQDZBQBGWFNPOZEZDKGFBGGBPTUGPZUVPKYEFGOVXNZFFQSAGFBCXVVGODXNZGMVCLODQDUTZEFYHBRKPZHBIQHQSZXNZTHQSKGFXNZFUVTLFKPTYZEUMVCLODZPSXNUZLNPODHGVGODYFQXNPKENPNBVFEUVYQDUNGENPMVEIXZAFWFNPUVBNNUPLPKUTKWTWHBASVYMVCLODZBKLDBYUVYDFXKPZDSQOYEAMXEPZBRSEBGXGVGODYDKQXNYEORZPXHVFMVCLODYFQXSGYZGEMAYEXZFANPDZGFCBMVCLODXNZFKUQKWLTYZPGEMVCLODYDKQXNZTYQDZBQBGWFNPOZEZDKGFBGGBPNDYUGPZZSELACUYRKPZNYYFZPMVCLODYMHBZFPQDFFSXNVYCNLENPFVSWKLDBYEFDGUYMYAVYMVCLODDYPKPNDYFYXNPZYELZGFIYFLFZNSORZPYFDPNPKUUVMHSZZBALNUHXPGVGODZBKLBABGFZTLFMFUVYFGZSELACPBPZAMLNPTYSFGXNUTYEXGVGODXIPZZENPEPKEZEPMVGODZBASVYORHTBGFWQBTFFYHBRKPZAMFLXNYUXNZBNSRKKVZBAKQZPNKVOVMAOAPGVGODZBZLPQGZZLVFQDZLNPTUELMVCLODFQSMHBOVGUAXNUSKYMLYFYETDQPLDKGFEZRKPZYZKZXNPZUTNWKRQBUKYEZBAKEWEZHXPSDKGFAMACXNUEWNTLTXCAZENPRHZEFEUKSMZDYEPLPKPNQZSPFGBHGENPYRFDGPMVCLODIYEGVFMVCLODFGNPDPPQRHKUPGVGODPKYTVYKZNWFQEKMFGBTZZCZPZGMVCLODIYXEPQUTKHEZAMFLXNPZHIOFBZACEIZLGFMYGZMHBRZQSDMFMYWNLECZPTZGMVFMDQKZFQYDULKHEZDYAMACXNUEZDYEDKGFXNPTSGPZDFRMNWUFDYYMGBTSWFYBAHPNHBRLAMFZELNPABQMZBGPZLNPCZVYKZNYORGSACEVNPDQKZKHTLWKPZMVCLODYFZXNPZPTUZPBGYBDCEKCABCPEYEHBXNKUMVEIXZAFWFNPTUELMVCLODZBZLNPCZVYKZFQEPGEKWTSRLAMWNGENPBYEZZHCFGBXNYEEIPKGBPNGFHBXNUNAXROYEMVCLODYFZXNPZPTUZPBGXZPTYEFGFYTYZXNPLDBRZSYMXNZFNYYFZPBHCNLZCAGFBPZBZLGFFBKZXNSTBVITPZZEHQSZMVCLODZBKSBAAMTIPSGBXNZTDQPLYDKZTYTLFDDSPTYSMVCLODUVXNXNUTCFMAODBZKZXNYEORZPXHVFNSYSHBVTZFXCAMEGVFXNUTHVNSQLNWXCFYXNUTYEXNQZIYFGGZYUPGVGODUYFLXNZFFQYDESVFPZWYFDYDEZTSPMCYPGVGODZBRMVYSKEYPTUGPZUFNPZP"

# alpha = {}
# alpha_freq = {}
# for k in alphabet:
#     for j in alphabet:
#         alpha_freq[k+j] = 0

# for i in range(0,len(cipher)//2):
#     char1 = cipher[2*i]
#     char2 = cipher[(2*i) + 1]
#     # if char1 == k:
#     alpha_freq[char1+char2] = alpha_freq.get(char1+char2) + 1
# sorted_list = sorted(alpha_freq.items(), key=operator.itemgetter(1), reverse=True)
# # alpha[k] = list(k for (k, v) in sorted_list if v != 0)
# alpha_freq =dict((k,v) for (k,v) in sorted_list)        
# # print(alpha_freq)
# plt.bar(alpha_freq.keys(), alpha_freq.values())
# plt.show()

# for k in alpha :
#     print("{} : {}".format(k, alpha.get(k)))

# print (cipher)
# alpha_freq = dict((k, 0) for k in alphabet)
# for letter in cipher:
#     alpha_freq[letter] = alpha_freq.get(letter) + 1 
# print(alpha_freq)
# plt.bar(alpha_freq.keys(), alpha_freq.values())
# plt.show()
