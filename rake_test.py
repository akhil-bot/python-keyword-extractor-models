import RAKE
import operator

def run_rake(path,key_phrase_dict,no_of_words):
        print('running RAKE model')
        # Reka setup with stopword directory
        #stop_dir = "./stoplist.txt"
        rake_object = RAKE.Rake(RAKE.SmartStopList())

        # Sample text to test RAKE
        text=open(path,'r').read()
        

        # Extract keywords
        keywords = rake_object.run(text,minCharacters = 1, maxWords = 3, minFrequency = 1)
        key_phrase_dict['RAKE']=[word[0] for word in keywords[:no_of_words+1]]
        return key_phrase_dict
#run_rake('/home/admindell/Documents/topic-modelling/sampletext.txt')