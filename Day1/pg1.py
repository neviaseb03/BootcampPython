dictionary = {
    "paris": "The capital of France, known for its iconic Eiffel Tower and romantic atmosphere.",
    "tokyo": "The capital of Japan, a bustling metropolis with a rich cultural heritage.",
    "new york": "A major city in the United States, famous for its skyscrapers and cultural diversity.",
    "rome": "The capital of Italy, known for its ancient history, architecture, and delicious cuisine.",

}

def find_definition(word):
    return dictionary.get(word, "Word not found in the dictionary.")

while True:
    user_input = input("Enter a word to look up (or 'q' to quit): ")
    
    if user_input.lower() == 'q':
        break
    
    definition = find_definition(user_input.lower())
    
    print(definition)