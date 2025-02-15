import random

# Response templates organized by category
RESPONSE_TEMPLATES = {
    'greeting': [
        "Purrr... Hello there!",
        "Meow! Nice to see you!",
        "Mrow! Welcome human!"
    ],
    'food': [
        "Prrrrt? I smell tuna!",
        "Mew! Fish o'clock!",
        "Yowl! Where's my dinner?"
    ],
    'play': [
        "Chirp! Let's chase lasers!",
        "Pounce! String attack!",
        "Mrow! Feather toy time!"
    ],
    'default': [
        "Blink blink... I'm listening",
        "Prrrrt? Explain again?",
        "Headbutt! Continue please",
        "Slow blink... Go on human"
    ]
}

def generate_cat_response(doc):
    """Generate context-aware cat responses using NLP analysis"""
    # Check for specific patterns
    if any(token.text in ['hello', 'hi', 'hey'] for token in doc):
        return random.choice(RESPONSE_TEMPLATES['greeting'])
    
    # Check for food-related nouns
    if any(token.text in ['food', 'treat', 'fish', 'dinner'] for token in doc):
        return random.choice(RESPONSE_TEMPLATES['food'])
    
    # Check for play-related verbs
    if any(token.lemma_ in ['play', 'chase', 'run'] for token in doc):
        return random.choice(RESPONSE_TEMPLATES['play'])
    
    # Check for cat anatomy references
    if any(token.text in ['whisker', 'tail', 'paw'] for token in doc):
        return "Prrrrt? Are you talking about my {}?".format(
            random.choice(['whiskers', 'fluffy tail', 'soft paws'])
        )
    
    # Fallback to default responses
    return random.choice(RESPONSE_TEMPLATES['default'])