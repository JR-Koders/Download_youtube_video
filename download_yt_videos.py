try:
    from pytube import YouTube
except ImportError:
    print("Oh-oh, it seems like you don't have pytube installed...\nDon't worry! Just run \"pip install pytube\"")
    exit(0)

def download_youtube_video(url, output_path='.'):
    try:
        # Create a YouTube object
        youtube = YouTube(url)

        # Get the highest resolution stream
        video_stream = youtube.streams.get_highest_resolution()

        # os library helps with cross-plateform compatibility
        # (macOS doesn't use the same path system as windows)
        import os
        # Set the output path for the downloaded video
        video_path = {os.path.join(output_path, f'{youtube.title}.mp4')}

        # Download the video (\r puts the cursor back at the beginning of the line, allowing to overwrite the line)
        print(f'Downloading: {youtube.title}...', end='\r')
        video_stream.download(output_path)
        print(f'Download complete! Video saved at: {video_path}')

    except Exception as e:
        print(f'Error: {e}')

# this condition is true only when we specifically execute this file, not when we import some of the file's module
if __name__ == "__main__":
    # ask for the video link
    video_url = input("Enter YouTube video URL: ").strip()
    # then download the video
    download_youtube_video(video_url)
