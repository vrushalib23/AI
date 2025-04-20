from nltk.chat.util import Chat , reflections

pairs = [
    [
        r"hi|hello|hey",
        ["Hello! How can I assist you today?", "Hi there! Need any help?"]
    ],
    [
        r"what is your name ?",
        ["I’m ShopEasyBot, your virtual assistant."]
    ],
    [
        r"how to return a product\??",
        ["You can return a product within 7 days by visiting the 'My Orders' section."]
    ],
    [
        r"how long for refund\??|when will I get my refund\??",
        ["Refunds are usually processed within 5-7 business days."]
    ],
    [
        r"how can I track my order\??",
        ["You can track your order in the 'Track Order' section using your order ID."]
    ],
    [
        r"do you have cash on delivery\??",
        ["Yes, Cash on Delivery (COD) is available for select locations."]
    ],
    [
        r"how to contact customer care\??",
        ["You can call our support at 1800-123-456 or email support@shopeasy.com."]
    ],
    [
        r"do you ship internationally\??",
        ["Currently, we only deliver within India. International shipping is coming soon!"]
    ],
    [
        r"what are your delivery charges\??",
        ["Delivery is free for orders above ₹499. A charge of ₹40 applies for smaller orders."]
    ],
    [
        r"how do I cancel my order\??",
        ["To cancel an order, go to 'My Orders' > Select Order > Cancel."]
    ],
    [
        r"bye|exit|quit",
        ["Goodbye! Have a great day.", "Thanks for chatting with us!"]
    ],
    [
        r"(.*)",
        ["I'm sorry, I didn't quite get that. Could you please rephrase?"]
    ]
]

chatbot = Chat(pairs,reflections)

print("hello, i am a ai assistant ")

chatbot.converse()
 
