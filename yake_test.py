import yake

def run_yake(path,key_phrase_dict,no_of_words):
    print('running Yake')
    text=open(path,'r').read()
    language = "en"
    max_ngram_size = 3
    deduplication_thresold = 0.9
    deduplication_algo = 'seqm'
    windowSize = 1
    numOfKeywords = no_of_words

    custom_kw_extractor = yake.KeywordExtractor(lan=language, n=max_ngram_size, dedupLim=deduplication_thresold, dedupFunc=deduplication_algo, windowsSize=windowSize, top=numOfKeywords, features=None)
    keywords = custom_kw_extractor.extract_keywords(text)

    key_phrase_dict['YAKE']=[word[0] for word in keywords]
    return key_phrase_dict
#print(run_yake('/home/admindell/Documents/topic-modelling/sampletext.txt',{}))