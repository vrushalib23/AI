# from nltk.chat.util import Chat , reflections

# pairs = [
#     [
#         r"hi|hello|hey",
#         ["hello !! how i can help u "]
#     ],

#     [
#         r"how are you",
#         ["Good"]
#     ],

#     # [
#     #     r".*",
#     #     ["I'm sorry , i didn't understand that...."]
#     # ] 

# ]

# chatbot = Chat(pairs,reflections)

# print("hello, i am a ai assistant ")

# chatbot.converse()
from nltk.chat.util import Chat , reflections

pairs = [

    [
        r"hi|hello",
        ["hii , how i can assiste you"]
    ]
]

chatbot = Chat(pairs,reflections)
print("i am virtual assistant")
chatbot.converse()