import nltk
from nltk.corpus import stopwords

# step 0: Define corpus and document
text_doc = """The foods we eat contain nutrients. Nutrients are substances 
required by the body to perform its basic functions. Nutrients must 
be obtained from our diet, since the human body does not 
synthesize or produce them. Nutrients have one or more of three 
basic functions: they provide energy, contribute to body structure, 
and/or regulate chemical processes in the body."""
print(text_doc)
print()

# step 1: Tokanize
tokens = nltk.word_tokenize(text_doc)
print(f"Tokens: {tokens}\n")

# step 2: Get STOP WORDS
stop_words = set(stopwords.words('english'))
print(f"Stop Words in English: {stop_words}\n")

# step 3: Remove stop words from tokens
filtered_tokens = [w for w in tokens if not w in stop_words]
print(f"Filtered Tokens: {filtered_tokens}\n")

# step 4: output text 
output_text = ' '.join(filtered_tokens)
print(f"Output Text: {output_text}\n")
