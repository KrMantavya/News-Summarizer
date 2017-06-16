from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from collections import defaultdict
from string import punctuation
from heapq import nlargest
import crawler

class FrequencySummarizer:
    def __init__(self,min_cut=0.1,max_cut=0.9):
        self._min_cut=min_cut
        self._max_cut=max_cut
        self._stopwords=set(stopwords.words('english')+list(punctuation))

    def compute_frequencies(self,word_sent):
        freq=defaultdict(int)
        for sentence in word_sent:
            for word in sentence:
                if word not in self._stopwords:
                    freq[word]+=1
        max_freq=float(max(freq.values()))
        for word in freq.keys():
            freq[word]=freq[word]/max_freq
        if freq[word] >= self._max_cut or freq[word] <= self._min_cut:
            del freq[word]
        return freq

    def summarize(self,text,n):
        sents=sent_tokenize(text)
        assert n <= len(sents)
        word_sent=[word_tokenize(s.lower()) for s in sents]
        self._freq=self.compute_frequencies(word_sent)
        ranking=defaultdict(int)
        for i,sent in enumerate(word_sent):
            for word in sent:
                if word in self._freq:
                    ranking[i]+=self._freq[word]

        sents_idx=nlargest(n,ranking,key=ranking.get)
        return [sents[j] for j in sents_idx]
someURL="https://www.washingtonpost.com/politics/trump-lashes-out-at-russia-probe-pence-hires-a-lawyer/2017/06/15/aee870ce-51da-11e7-be25-3a519335381c_story.html?hpid=hp_hp-top-table-main_trumpobstruct-8pm%3Ahomepage%2Fstory&utm_term=.d5246b404eff"
textofURL=crawler.get_only_text_washingtonpost_url(someURL)
print 'text of article \n'
print textofURL
fs= FrequencySummarizer()
summary=fs.summarize(textofURL[1],3)
print 'summary is as follows \n\n'
print summary
