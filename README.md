# HackCMU_AstroHealth

[Hackathon Pitch](https://docs.google.com/presentation/d/1Qvrr-IFhoYjrZ957TWA_l9f9fCzOM20mKxMg9g2Sd90/edit#slide=id.g27f78cf9952_0_193)

## Inspiration

Astronauts have to operate in extremely stressful environments in space, which not only takes a toll on their mental health, but is also detrimental to the overall space mission. A common way to reduce stress and improve the mental state, is through journalling which provides them a vent and an emotional outlet.

## What it does
AstorHealth generates music based on emotions experienced by the Astronauts, to elevate their mood.

## How we built it
Using the text of the journal, the sentiment and emotions of the astronaut are detected. Using the sentiment a generative model is used to get the qualities of music which could help elevate the mood of the astronaut. Using the generated prompt, it is fed into a MusicGen model, which outputs the final music.

## Challenges we ran into
Coming up with a way/input to detect emotions and understanding the mental state of the astronaut.

## Accomplishments that we're proud of
An end-to-end workflow, starting from text data to generated music.

What we learned
A ton about the challenges faced by astronauts, and the difficult conditions they have to work in.

What's next for AstroHealth
Adding more modalities, and further fine-tuning to conditions in space. Currently, the model runs on cloud, but ideally it should be deployed on device, to allow for local execution.
