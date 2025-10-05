from pydub import AudioSegment
import math
import os

# prompt the user to enter the directory path
input_directory_path = "C:/Users/Matt/Documents/Project/CS-M/Experiments/NoiseCancelTests/TestingAudios/Noise"
output_directory_path = 'C:/Users/Matt/Documents/Project/CS-M/Experiments/NoiseCancelTests/TestingAudios'

# define the length of each clip in seconds
clip_length = 10

# get a list of all audio files in the input directory  
audio_files = [f for f in os.listdir(input_directory_path) if f.endswith(".wav")]

# process each audio file
for audio_file in audio_files:
    # load the audio file
    audio = AudioSegment.from_file(os.path.join(input_directory_path, audio_file))

    # calculate the total number of clips
    num_clips = math.ceil(len(audio) / (clip_length * 1000))

    # split the audio file into clips
    clips = []
    for i in range(num_clips):
        start_time = i * clip_length * 1000
        end_time = min((i + 1) * clip_length * 1000, len(audio))
        clip = audio[start_time:end_time]
        clips.append(clip)

    # export each clip as a separate audio file in the output directory
    for i, clip in enumerate(clips):
        clip_name = os.path.splitext(audio_file)[0] + f"_clip_{i+1}.wav"
        clip_path = os.path.join(output_directory_path, clip_name)
        clip.export(clip_path, format="wav")

        # remove the output file if it is shorter than 10 seconds
        if len(clip) < clip_length * 1000:
            os.remove(clip_path)

    print(audio_file)
