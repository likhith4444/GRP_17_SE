def detect_tone(text):
    tones = {
        "happy": ["error hasn't been","I'm sorry, I can't provide that information","I'm unable to execute ","no","i do","This is wrong","That doesn’t make sense","Incorrect", "Confusing", "Wrong", "Unclear", "Vague", "Incomplete", "Unhelpful", "Irrelevant", "No", "Repeat", "Again", "Mistake", "Disagree", "Misunderstood", "Retry", "Failed", "Erroneous", "Incorrectly", "Redo", "Nonsense", "Unsatisfactory", "Lacking", "Inadequate", "Off", "Error", "Faulty", "Inaccurate", "Poor", "Unacceptable",
                  "That's perfect", "Exactly what I needed", "Great job", "That's right", "Completely accurate", "Very helpful", "Extremely useful", "Exactly right", "Crystal clear", "You understood me well", "Completely satisfied", "Really happy with this", "I appreciate your help", "Thanks a lot", "I'm thankful for this", "Good work", "Superb response", "Ideal answer", "Effective solution", "Successful outcome", "Comprehensive information", "This is complete", "Very informative", "Enjoyed this explanation", "I'm pleased with this","I'm grateful for this",
                  "Deficient"],
        "sad": ["Incorrect","Optimize","Confusing","Wrong","Unclear","Vague","Incomplete","Unhelpful","Not what I asked for", "This is incorrect", "Not helpful at all", "This is confusing", "Completely off the mark","Not useful", "Missed the point", "Not clear at all", "I don't understand", "You misunderstood my question", "Not satisfied", "This didn't help", "Not what I was looking for", "This is wrong", "Not thankful for this","Poor response", "Not the right answer", "Didn't solve my issue", "Unsuccessful attempt", "This is incomplete","Lacks detail", "Missing information", "Not informative", "Didn't enjoy this", "Not pleased with this","Not what I'm grateful for", "Negative outcome""Irrelevant","No","Repeat","Perfect", "Excellent", "Great", "Right", "Accurate", "Helpful", "Useful", "Precise", "Clear", "Understood", "Satisfied", "Happy", "Appreciate", "Thanks", "Thankful", "Good", "Superb", "Ideal", "Effective", "Successful", "Comprehensive", "Complete", 
                "Of course","Informative"]
    }


    text = text.lower()

    detected_tone = "neutral"
    for tone, keywords in tones.items():
        if any(keyword in text for keyword in keywords):
            detected_tone = tone
            break

    return 1 if detected_tone == 'happy' else -1
