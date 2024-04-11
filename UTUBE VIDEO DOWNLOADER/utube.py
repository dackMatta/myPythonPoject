# Import the YouTube class from the pytube module to work with YouTube videos
from pytube import YouTube

# Import tkinter library for creating GUI applications
import tkinter as tk

# Import filedialog module from tkinter for creating file dialogs
from tkinter import filedialog

# Import tqdm library for displaying progress bars
from tqdm import tqdm

# Define a function to download a video from YouTube
def download_video(url, save_path):
    try:
        # Create a YouTube object by passing the URL of the video
        yt = YouTube(url)

        # Filter the available streams to include only those with progressive download and mp4 extension
        streams = yt.streams.filter(progressive='2160p', file_extension='mp4')

        # Get the highest resolution stream
        highest_res_stream = streams.get_highest_resolution()

        # Download the video to the specified save path
        highest_res_stream.download(output_path=save_path)

        # Print a success message
        print('Video downloaded successfully')

    # Handle exceptions
    except Exception as e:
        # Print any error that occurs during the download process
        print(e)

# Define a function to open a file dialog for selecting a directory
def open_file_dialog():
    # Display a file dialog to select a directory and store the selected folder path
    folder = filedialog.askdirectory()

    # If a folder is selected, print the selected folder path
    if folder:
        print(f'selected folder: {folder}')

    # Return the selected folder path
    return folder

# Entry point of the program
if __name__ == "__main__":
    # Create a Tkinter root window
    root = tk.Tk()

    # Hide the root window
    root.withdraw()

    # Prompt the user to enter a YouTube video URL
    video_url = input('please enter YouTube url: ')

    # Open a file dialog to select a directory for saving the downloaded video
    save_dir = open_file_dialog()

    # If a directory is selected, initiate the download process
    if save_dir:
        print('download started...')
        download_video(video_url, save_dir)

    # If no directory is selected, print a message indicating that no folder is selected
    else:
        print('no folder selected')
