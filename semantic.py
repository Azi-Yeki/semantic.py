import spacy
nlp = spacy.load('en_core_web_md')

word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

tokens = nlp('cat apple monkey banana ')

for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))
# Observations
# the cat and the monkey are more similar because they are both animals
# when compared with themselves, the cat, monkey, banana and apple all get 1 which makes sense
# the banana and apple also have a high similarity because they are both fruit
# the cat has low similarity with the fruit because there is not much linking it to both the apple and banana
# the monkey has a higher similarity with the banana and not the apple because monkeys are known for eating bananas

sentence_to_compare = "Why is my cat on the car"

sentences = ["where did my dog go",
             "Hello, there is my car",
             "I've lost my car in my car",
             "I'd like my boat back",
             "I will name my dog Diana"]

model_sentence = nlp(sentence_to_compare)

for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)

# my example
word4 = nlp("mouse")
word5 = nlp("dog")
word6 = nlp("cheese")

print(word4.similarity(word5))
print(word6.similarity(word5))
print(word6.similarity(word4))

# when run with "en_core_web_sm", the example file gives you a warning that it may not give useful similarity judgements
# "en_core_web_md" is a larger model which has word vectors loaded so it gives useful similarity judgements. it runs without fail
