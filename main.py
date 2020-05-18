from pke_test import run_pke_models
from rake_test import run_rake
from rakenltk_test import run_rake_nltk
#from topia_test import run_topia
from textrank_test import run_pytextrank
from textrank_test import run_textrank
from yake_test import run_yake
path='./sampletext.txt'
key_phrase_dict={}
no_of_words=30

key_phrase_dict=run_pke_models(path,key_phrase_dict,no_of_words)
key_phrase_dict=run_rake(path,key_phrase_dict,no_of_words)
key_phrase_dict=run_rake_nltk(path,key_phrase_dict,no_of_words)
#key_phrase_dict=run_topia(path,key_phrase_dict,no_of_words)
key_phrase_dict=run_pytextrank(path,key_phrase_dict,no_of_words)
key_phrase_dict=run_textrank(path,key_phrase_dict,no_of_words)
key_phrase_dict=run_yake(path,key_phrase_dict,no_of_words)

print(key_phrase_dict)
