from audiocraft.models import MusicGen


# Using small model, better results would be obtained with `medium` or `large`.

def music_gen(mmusic_description):
    model = MusicGen.get_pretrained('small')

    model.set_generation_params(
        use_sampling=True,
        top_k=250,
        duration=5
    )

    output = model.generate(
        descriptions=[
            '80s pop track with bassy drums and synth',
    ],
    progress=True
    )
    return output

