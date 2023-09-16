def get_emotions_text(emotions):
    e_text = ""
    print("=====================")
    print("EXTRACTED EMOTIONS: ")
    for e in emotions:
        print(e)
        e_text += e["name"] + ", "
    print()
    return e_text
