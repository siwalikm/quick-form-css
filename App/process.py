import networkx as nx
from scipy.spatial.distance import cosine
from underthesea import word_tokenize


#calculate cosine similarity: maximally "dissimilar": orthogonal (cosine = 1) (range: [0;2])
def semantic(word1, word2, ft):
  vec1 = ft.get_word_vector(word1)
  vec2 = ft.get_word_vector(word2)
  if ft.get_word_id(word1) != -1 and ft.get_word_id(word2) != -1:
    return cosine(vec1, vec2)
  if ft.get_word_id(word1) == -1:
    vec1 = ft.get_word_vector(word1.replace(' ', '_'))
  if ft.get_word_id(word2) == -1:
    vec2 = ft.get_word_vector(word2.replace(' ', '_'))
  return cosine(vec1, vec2)

#calculate the frequency of two words occurred in the same window
def freq(word1, word2, n_windows, words):
  if len(words) < 5: 
    return 1
  c = 0
  for i in range(n_windows):
    if word1 in words[i:i+3] and word2 in words[i:i+3]:
      c += 1
  return c/n_windows

def keyword_extract(text):
    punctuation = ['.','!',',','?','(',')','"', '&', '-', '/', '\\', '*', '+', ',', ':', ';', '=', '>', '<', '?', '\'', '…', '...']
    stopwords_file = 'vietnamese-stopwords.txt'
    with open(stopwords_file, 'r', encoding='utf8') as f:
        lines = f.readlines()
    my_stopwords = []
    for line in lines:
        my_stopwords.append(line.strip())

    words = [word.lower() for word in word_tokenize(text) if word not in punctuation and word not in my_stopwords]

    i = 0
    while i < len(words):
        if not words[i][0].isalpha() and not words[i][0].isdigit():
            if (len(words[i]) == 1):
                words.pop(i)
            else:
                words[i] = words[i][1:]
        else:
            i += 1

    G = nx.Graph()
    G.add_nodes_from(words)
    window = 2
    n_windows = len(words) - 4 # a window contains 2*2+1=5 words
    for i, word1 in enumerate(words):
    #co-occurrence
        for j in range(i + 1, min(i + window + 1, len(words))):
            word2 = words[j]
            if word1 != word2:
                edge_weight = freq(word1, word2, n_windows, words)
                if edge_weight < 0.02:
                    edge_weight = 0
                G.add_weighted_edges_from([(word1, word2, edge_weight)])
        # for j in range(max(i + window + 1, len(words) - 1), min(i + window + 2, len(words))):
        #     word2 = words[j]
        #     if word1 != word2:
        #         edge_weight = semantic(word1, word2, ft)
        #         if edge_weight > 0.7 and edge_weight < 1.3:
        #             edge_weight = 0
        #         G.add_weighted_edges_from([(word1, word2, edge_weight)])

    w = nx.pagerank(G)
    keywords = sorted(w, key=w.get, reverse=True)[:20]
    return keywords

