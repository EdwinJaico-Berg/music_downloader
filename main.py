import os
import sys
import subprocess
from paths import BASE
from pytube import YouTube

def get_artwork(musician: str, title: str) -> None:
    raise NotImplementedError

def main():
    # Assign variables
    url = sys.argv[1]
    
    # Download video as mp3
    yt = YouTube(url)

    # Extract audio
    audio = yt.streams.get_audio_only()

    # Get input (Musician, Song Title)
    artist = input("Artist: ")
    title = input("Title: ")

    # Create destination path
    base = BASE
    dir_path = base + artist

    # Check whether file already exists
    file_path = f"{dir_path}/{title}.mp3"
   
    if os.path.isfile(file_path):
        download = str(input("File already exists. Do you want to continue? [y/N]\n"))
        if download.lower() == "y":
            pass
        else:
            print("The file was not downloaded.")
            return 1

    # Download the file
    out_file = audio.download(output_path=dir_path, filename=title + ".mp4")

    # Save the file
    root, _ = os.path.splitext(out_file)
    new_file = f"{root}.mp3"
    
    # Convert the file using ffmpeg
    subprocess.run(["ffmpeg", "-i", out_file, new_file])

    # Remove the .mp4 file
    os.remove(out_file)
    
    # Result of success
    print(f"{new_file} has been successfully downloaded.")


if __name__ == "__main__":
    main()