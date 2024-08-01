from moviepy.editor import VideoFileClip

def trim_video(input_file, output_file, start_time, end_time):
    # Load the video file
    video = VideoFileClip(input_file)
    
    # Trim the video to the specified segment
    trimmed_video = video.subclip(start_time, end_time)
    
    # Write the result to a new file
    trimmed_video.write_videofile(output_file, codec='libx264')

if __name__ == "__main__":
    # Define input and output file paths
    input_path = "Downloaded_videos/<input_video.mp4>"
    output_path = "Downloaded_videos/<output_video.mp4>"
    
    # Define the segment to trim (in seconds)
    start = 0  # Start time in seconds
    end = 19     # End time in seconds
    
    # Call the trim_video function
    trim_video(input_path, output_path, start, end)
