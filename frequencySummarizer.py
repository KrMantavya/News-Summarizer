import _init_

class FrequencySummarizer:
    def __init__(self,min_cut=0.1,max_cut=0.9):
        self._min_cut=min_cut
        self._max_cut=max_cut

        self._stopwords=set(stopwords.words('english')+list(punctuatuion))

    def _compute_frequencies(self,word_sent):
        freq=defaultdict(int)
        
