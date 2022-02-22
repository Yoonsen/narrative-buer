import dhlab.nbtext as nb
import dhlab.text as dh

def display(corpus, window=1000, pr=100):
    for i in range(corpus.size):
        try:
            a = word_density(corpus.corpus.urn.values[i], ["."], window=window, pr=pr)
            a.plot(figsize=(12,5), title = corpus.corpus.title.values[i])
        except:
            pass


class word_density():
    def __init__(self, urn=None, words=[], window=5000, pr=100):
        # Fro dhlab1 urn must belong to the book series so must be stripped
        urn = nb.pure_urn(urn)
        if urn != []:
            urn = urn[0]
            self.data = nb.plot_book_wordbags(urn, words, window, pr).sort_index()
        else:
            print("no urn")
            
    def plot(self, **kwargs):
        self.data.plot(**kwargs)