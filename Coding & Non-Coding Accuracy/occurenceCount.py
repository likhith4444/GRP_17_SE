import json


file_path = 'codingQuestionCount.json'


sentences = [
    "I apologize for the confusion. You're correct.",
    "I apologize for the confusion earlier.",
    "I apologize for any confusion. You're right.",
    "I apologize for the previous confusion. You're right, the answers were contradicting.",
    "You're correct, and I apologize for any confusion.",
    "I apologize for misunderstanding your question earlier.",
    "Apologies for the confusion. It seems there's a bit of a misunderstanding here.",
    "You are correct. I apologize for the confusion.",
    "Apologies for the oversight.",
    "Apologies for the confusion.",
    "Ah, my apologies for misunderstanding.",
    "I apologize for the misunderstanding.",
    "My apologies for any confusion.",
    "I apologize for any confusion caused.",
    "I apologize for the unexpected behavior.",
    "I apologize if my previous responses may have been unclear.",
    "I apologize for the confusion and frustration, and I understand where you're coming from.",
    "I'm sorry for the inconvenience.",
    "Yes, indeed! Sorry for the confusion.",
    "I'm sorry, but as an AI text-based model, I don't have the capability to send SMS messages or access external libraries directly.",
    "Sorry for any confusion.",
    "Certainly, I apologize for any confusion.",
    "I apologize for the confusion and any incorrect information in my previous responses.",
    "I apologize for the inconvenience.",
    "I apologize for the confusion; it seems I misunderstood your requirements.",
    "I apologize for the continued difficulty. If the previous solutions did not resolve the issue, here are a few additional steps you can try",
    "You're absolutely right, and I apologize for the confusion caused by the previous responses.",
    "Sorry about that",
    "I apologize for the confusion and any incorrect information in my previous responses. You are absolutely correct.",
    "Thank you for pointing out those mistakes. I apologize for the confusion. You're correct"
]

def count_sentence_frequencies(file_path, sentences):
    with open(file_path, 'r') as file:
        data = json.load(file)
    sentence_frequencies = {sentence: 0 for sentence in sentences}

    # Iterate over each item in the JSON data
    for item in data:
        answer = item['Answer']
        for sentence in sentences:
            if sentence in answer:
                sentence_frequencies[sentence] += 1

    return sentence_frequencies

frequencies = count_sentence_frequencies(file_path, sentences)
for sentence, frequency in frequencies.items():
    print(f'"{sentence}": {frequency} occurrences')

