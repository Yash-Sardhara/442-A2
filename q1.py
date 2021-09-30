import matplotlib.pyplot as plt
import operator

alphabet = "abcdefghijklmnopqrstuvwxyz".upper()

cipher = "PQBELAZBKHALLELAZBVAPDIGBRSPQDUPRASPSIJYDKPUKIHGDCCAWUAKKBLLSIJALLPQBRQSLBGDCCAAIVYSJQPSIJYDKPQBQBVJBQDJHAIVSIAFBKZHQDKPPSCBPQBWUBBIRAHSIAYUKSDUHEAHHSDIGDCCAAIVRBIPHPACESIJAXDUPGDCCAAIVHQDUPSIJDYYRSPQQSHQBAVDKDYYRSPQQBKQBAVAXDUPDIGBSIACSIUPBVDPALSGBXBJAIPDYBBLFBKZUIBAHZPDXBHUKBGDCCAHQBQAVIDPAHZBPQAVAIZVSHEUPBRSPQPQBWUBBIGDCCAXUPHQBNIBRPQAPSPCSJQPQAEEBIAIZCSIUPBGDCCAAIVPQBIGDCCAPQDUJQPHQBGDCCARQAPRDULVXBGDCBDYCBPQBZKBVKBAVYULLZYDIVDYXBQBAVSIJEBDELBQBKBPQBJKBAPRDIVBKSHGDCCAPQAPPQBKBHAIZDIBLBYPALSFBHQBRAHLDDNSIJAXDUPYDKHDCBRAZDYBHGAEBGDCCAAIVRDIVBKSIJRQBPQBKHQBGDULVJBPARAZRSPQDUPXBSIJHBBIGDCCARQBIHQBIDPSGBVAGUKSDUHAEEBAKAIGBSIPQBASKSPEUOOLBVQBKFBKZCUGQAPYSKHPGDCCAXUPGDCCAAYPBKRAPGQSIJSPACSIUPBDKPRDGDCCAHQBCAVBSPDUPPDXBAJKSIGDCCAAIVHQBHASVPDQBKHBLYSPHPQBGQBHQSKBGAPIDRSHQALLQAFBHDCBXDVZPDPALNPD"

replace = {
    "B" : "E", #final
    "A" : "A", #final 
    "P" : "T", #final 
    "D" : "O", #final 
    "Q" : "H", #final
    "I" : "N", #final
    "S" : "I", #final
    "C" : "M", #final 
    "H" : "S", #final
    "K" : "R", #final
    "G" : "C", #final
    "U" : "U", #final
    "V" : "D", #final
    "L" : "L", #final 
    "R" : "W", #final
    "J" : "G", #final
    "Y" : "F", #final
    "Z" : "Y", #final
    "E" : "P", #final
    "X" : "B", #final 
    "F" : "V", #final
    "N" : "K", #final
    "W" : "Q", #final
    "O" : "Z",
    "M" : "J",
    "T" : "X", 
}




print (cipher)
alpha_freq = dict((k, 0) for k in alphabet)
for letter in cipher:
    alpha_freq[letter] = alpha_freq.get(letter) + 1 
print(alpha_freq)
sorted_list = sorted(alpha_freq.items(), key=operator.itemgetter(1), reverse=True)
alpha_freq =dict((k,v) for (k,v) in sorted_list)
# plt.bar(alpha_freq.keys(), alpha_freq.values())
# plt.show()
print ()

plain_txt = ""
for letter in cipher:
    plain_txt += replace.get(letter)
print(plain_txt)

# n = 5
# for j in range (0, n):
#     print ('remainder = {}'.format(j))
#     alpha_freq = dict((k, 0) for k in alphabet)
#     for i in range(0, len(cipher)):
#         if (i % n == j):
#             letter = cipher[i]
#             alpha_freq[letter] = alpha_freq.get(letter) + 1 
#     print(alpha_freq)
#     print()
#     plt.bar(alpha_freq.keys(), alpha_freq.values())
#     plt.show()
