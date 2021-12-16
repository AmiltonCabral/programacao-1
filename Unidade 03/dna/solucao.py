# (py) amiltoncristian9@gmail.com
# Date: 22/03/2021, Last Change: Never
# Descobre qual sequência de DNA é menor e exibe ela com sua quantidade

dna_1 = input()
dna_2 = input()
dna_3 = input()

len_dna_1 = len(dna_1)
len_dna_2 = len(dna_2)
len_dna_3 = len(dna_3)

if len_dna_1 <= len_dna_2 and len_dna_1 <= len_dna_3:
    print(dna_1, len_dna_1)

elif dna_2 <= dna_3:
    print(dna_2, len_dna_2)

else:
    print(dna_3, len_dna_3)
