import openai

openai.api_key = "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"

audio_file= open("w-test.mp3", "rb")
transcript = openai.Audio.transcribe("whisper-1", audio_file)

print(transcript)