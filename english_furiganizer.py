import spacy
import csv

en_ipa_dict = "en_US.txt"

with open(en_ipa_dict) as file:
    lines = file.readlines()
    en_to_ipa_dict = {line.split('\t')[0] : line.split('\t')[1] for line in lines}

nlp = spacy.load("en_core_web_sm")

raw_input_text = "1st Colonel! The english language is bad, don't go to the U.S"

# https://spacy.io/usage/linguistic-features
doc = nlp(raw_input_text)

#for token in doc:
#    print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
#            token.shape_, token.is_alpha, token.is_stop)

# normalized = some_module.normalize(pos_tagged)
# ipa_furiganizer = ipa_dict.furiganize(normalized)

for token in doc:
    print(token.lemma_)
    if token.lemma_ in en_to_ipa_dict:
        print(en_to_ipa_dict[token.lemma_])