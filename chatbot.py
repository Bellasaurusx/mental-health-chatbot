import random

# Define chatbot responses categorized by emotions
responses = {
    "stressed": [
        "I'm sorry you're feeling this way. Have you tried deep breathing exercises?",
        "Stress can be overwhelming. Taking a short break or a walk might help.",
        "Try writing down what's stressing you—it might help you process it."
    ],
    "sad": [
        "I'm here for you. Talking to a friend or journaling might help.",
        "It's okay to feel sad. Sometimes, expressing your feelings through art or music can be helpful.",
        "You're not alone. Would you like some self-care tips?"
    ],
    "anxious": [
        "Anxiety can be tough. Try grounding techniques like naming five things you can see.",
        "You’re not alone. Deep breathing and mindfulness exercises might help.",
        "Have you tried writing down your worries to help clear your mind?"
    ],
    "lonely": [
        "Loneliness can be tough. Connecting with someone you trust might help.",
        "Maybe a call with a friend or joining an online community could help you feel more connected.",
        "You're not alone. Would you like ideas for social activities?"
    ],
    "unmotivated": [
        "It’s okay to feel unmotivated sometimes. Starting with a small step can help build momentum.",
        "Try setting a tiny goal for today. Even a small win can give you a boost.",
        "Motivation can be tricky—maybe rewarding yourself for small tasks could help!"
    ],
    "sleep": [
        "A calming bedtime routine, like reading or meditation, could help.",
        "Have you tried limiting screen time before bed? That can make a big difference.",
        "Sometimes a warm cup of tea and dim lights can help your body relax."
    ]
}

# Default response if no keywords are found in user input
default_responses = [
    "I'm here to listen. Can you tell me more about how you're feeling?",
    "I might not have all the answers, but I’m happy to chat if it helps.",
    "That sounds difficult. Would you like some general coping strategies?",
    "Sometimes just talking about things can make a difference. Want to tell me more?",
    "You're not alone. Talking about it might help."
]

# Function to get chatbot response
def get_response(user_input):
    user_input = user_input.lower()
    
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])
    
    return random.choice(default_responses)

# Chatbot interaction loop
print("Mental Health Support Chatbot: Hello! How are you feeling today? (Type 'exit' to end)")
while True:
    user_input = input("You: ")
    
    if user_input.lower() == "exit":
        print("Mental Health Support Chatbot: Take care! Remember, you're not alone. 💙")
        break
    
    response = get_response(user_input)
    print(f"Mental Health Support Chatbot: {response}")
