from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
import numpy as np 
import nltk 
nltk.download("punkt") 
nltk.download('punkt_tab')
nltk.download("stopwords") 
 
def process(file): 
    raw=open(file).read() 
    tokens=word_tokenize(raw) 
    words=[w.lower() for w in tokens] 
 
    porter= nltk.PorterStemmer() 
    stemmed_tokens=[porter.stem(t) for t in words] 
 
    # removing stop words 
    stop_words=set(stopwords.words('english')) 
    filtered_tokens=[w for w in stemmed_tokens if not w in stop_words] 
 
    #count words 
    count=nltk.defaultdict(int) 
    for word in filtered_tokens: 
        count[word]+=1 
    return count; 
 
def cos_sim(a,b): 
    dot_product=np.dot(a,b) 
    norm_a=np.linalg.norm(a) 
    norm_b=np.linalg.norm(b) 
    return dot_product/(norm_a * norm_b) 
 
def getSimilarity(dict1,dict2): 
    all_words_list=[] 
    for key in dict1: 
        all_words_list.append(key) 
    for key in dict2: 
        all_words_list.append(key) 
    all_words_list_size=len(all_words_list) 
 
    v1=np.zeros(all_words_list_size,dtype=np.int64) 
    v2=np.zeros(all_words_list_size,dtype=np.int64) 
    i=0 
    for  (key) in all_words_list: 
        v1[i]=dict1.get(key,0) 
        v2[i]=dict2.get(key,0) 
        i=i+1 
    return cos_sim(v1,v2) 
if __name__ == '__main__': 
    dict1=process("doc1.txt") 
    dict2=process("doc2.txt") 
    print("Similarity between two text documents",getSimilarity(dict1,dict2))