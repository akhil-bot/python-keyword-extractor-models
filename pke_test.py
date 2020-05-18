import pke

def run_pke_models(path,key_phrase_dict,no_of_words):
        # initialize keyphrase extraction model, here TopicRank
        models=[pke.unsupervised.TfIdf,pke.unsupervised.KPMiner,pke.unsupervised.TextRank,pke.unsupervised.SingleRank ,pke.unsupervised.TopicRank,pke.unsupervised.TopicalPageRank,pke.unsupervised.PositionRank,pke.unsupervised.MultipartiteRank,pke.supervised.Kea,pke.supervised.WINGNUS]
        for model in models:
            print('running ',str( model).split('.')[-1].strip("'>"))
            extractor = model()

            # load the content of the document, here document is expected to be in raw
            # format (i.e. a simple text file) and preprocessing is carried out using spacy
            extractor.load_document(input=path, language='en')

            # keyphrase candidate selection, in the case of TopicRank: sequences of nouns
            # and adjectives (i.e. `(Noun|Adj)*`)
            extractor.candidate_selection()

            # candidate weighting, in the case of TopicRank: using a random walk algorithm
            extractor.candidate_weighting()

            # N-best selection, keyphrases contains the 10 highest scored candidates as
            # (keyphrase, score) tuples
            keyphrases = extractor.get_n_best(n=no_of_words)
            key_phrase_dict[str( model).split('.')[-1].strip("'>")]=[word[0] for word in keyphrases]
        return key_phrase_dict
            
#print(run_pke_models('/home/admindell/Documents/topic-modelling/sampletext.txt'))