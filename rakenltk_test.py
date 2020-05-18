from rake_nltk import Rake
def run_rake_nltk(path,key_phrase_dict,no_of_words):
    print('running RAKE_nltk model')
    # Uses stopwords for english from NLTK, and all puntuation characters by
    # default
    r = Rake()
    text=open(path,'r').read()
    # Extraction given the text.

    r.extract_keywords_from_text(text)

    # Extraction given the list of strings where each string is a sentence.
    #r.extract_keywords_from_sentences(<list of sentences>)

    # To get keyword phrases ranked highest to lowest.
    #print(r.get_ranked_phrases())
    key_phrase_dict['RAKE_nltk']=[word for word in r.get_ranked_phrases()[:no_of_words+1]]

    # To get keyword phrases ranked highest to lowest with scores.
    #r.get_ranked_phrases_with_scores()
    return key_phrase_dict
#print(run_rake_nltk('./sampletext.txt',{}))