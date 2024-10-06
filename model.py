import pickle
from keybert import KeyBERT

sample_text ="""
         Supervised learning is the machine learning task of
         learning a function that maps an input to an output based
         on example input-output pairs.[1] It infers a function
         from labeled training data consisting of a set of
         training examples.[2] In supervised learning, each
         example is a pair consisting of an input object
         (typically a vector) and a desired output value (also
         called the supervisory signal). A supervised learning
         algorithm analyzes the training data and produces an
         inferred function, which can be used for mapping new
         examples. An optimal scenario will allow for the algorithm
         to correctly determine the class labels for unseen
         instances. This requires the learning algorithm to
         generalize from the training data to unseen situations
         in a 'reasonable' way (see inductive bias).
      """


from keybert import KeyBERT
kw_model = KeyBERT()
keywords = kw_model.extract_keywords(sample_text)

# Initialize the KeyBERT model
model = KeyBERT()

# Save the model to a file
with open('keybert_model.pkl', 'wb') as file:
    pickle.dump(model, file)

print("Model saved successfully!")