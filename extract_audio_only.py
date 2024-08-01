# Run: ffmpeg -i Downloaded_videos/test_video.mp4 -f mp3 -ab 192000 -vn audio.wav
# Then, in order to trim it, you have to fix it first: ffmpeg -i audio.wav -f wav -acodec pcm_s16le audio_fixed.wav
# Then, run the script below.  


from pydub import AudioSegment

def cut_wav_segment(input_file, start_sec, end_sec, output_file):
    # Load the audio file
    audio = AudioSegment.from_wav(input_file)
    
    # Calculate start and end time in milliseconds
    start_time = start_sec * 1000
    end_time = end_sec * 1000
    
    # Extract the segment
    segment = audio[start_time:end_time]
    
    # Export the segment
    segment.export(output_file, format="mp3")

# Example usage
input_file = "Downloaded_videos/goggins.mp4"
start_sec = 0  # start time in seconds
end_sec = 12    # end time in seconds
output_file = "goggins.mp3"

cut_wav_segment(input_file, start_sec, end_sec, output_file)
