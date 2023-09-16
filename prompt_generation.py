import openai
openai.api_key = "<OPEN_AI KEY>"


def get_music_prompt(emotions):

    prompt = """
    Given the below emotions, suggest the description of music I should listen to improve my mental health
    Provide a single suggestion in concise form with no extra description

    For example:
    Empotions: Happy
    Description of music: A cheerful country song with acoustic guitars

    Empotions: {}
    Description of music : [Answer here]
    """

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        temperature = 1,
        messages = [
                    {"role": "user", "content": prompt.format(emotions)},
                ]
            )
    return response.choices[0]["message"]["content"]
