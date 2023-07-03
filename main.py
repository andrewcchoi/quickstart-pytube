# %%
import os
from pytube import YouTube, Playlist

import logging
import logging.handlers

import smtplib
from email.message import EmailMessage

import _config

# %%

# formatting for logger
FILENAME = 'feller_buncher.log'
FORMAT = '%(asctime)s - %(levelname)s - %(name)s - %(message)s'
DATEFORMAT = '%m/%d/%Y %I:%M:%S %p'
formatter = logging.Formatter(fmt=FORMAT, datefmt=DATEFORMAT)

# change default settings for name and logging level
logging.captureWarnings(True)
logging.basicConfig(encoding='utf-8', format=FORMAT, datefmt=DATEFORMAT, level=logging.DEBUG)

# create handler 
ch = logging.StreamHandler() # show logs in terminal
fh = logging.handlers.RotatingFileHandler(filename=FILENAME, maxBytes=1*1024*1024, backupCount=4, encoding='utf-8') # rotate on file size, example at 10 MB

# set logging level (debug, info, warning, error, critical)
ch.setLevel(logging.DEBUG)
fh.setLevel(logging.DEBUG)

# format handler00
ch.setFormatter(formatter)
fh.setFormatter(formatter)

# create logger with name and set logging level
lumberjack = logging.getLogger(__name__ + " - quickstart pytube")
lumberjack.setLevel(logging.DEBUG)
lumberjack.addHandler(fh)

# NOTE: mail handler configurations
# mh = logging.handlers.SMTPHandler(
#         mailhost=(_config.email_host, _config.email_port), 
#         fromaddr=_config.email_sender, 
#         toaddrs=_config.email_distribution, 
#         subject='SMTP E-Mail Logs', 
#         credentials=(_config.email_user, _config.email_password), 
#         secure=()
#     )
# mh.setLevel(logging.ERROR)
# mh.setFormatter(formatter)
# lumberjack.addHandler(mh)

# %%
def download_youtube_playlist(url: str, output_dir: str="downloads", prod: bool=True) -> None:
    """
    Downloads the videos from a YouTube playlist to the specified output directory.

    Args:
        url (str): The URL of the YouTube playlist.
        output_dir (str, optional): The output directory.
        prod (bool, optional): Whether to download videos only if prod is True. Defaults to True.

    Returns:
        None.
    """
    try:
        playlist = Playlist(url)
        dl_path = os.path.join(output_dir, playlist.title)
        lumberjack.info(
            "playlist info: {\n\ttitle: %s, \n\tplaylist count: %s, \n\turl: %s\n\tdownload path: %s\n\tprod: %s\n}", 
            playlist.title, len(playlist), playlist.playlist_url, dl_path, prod)

        for url in playlist:
            video = YouTube(url)
            video_path = os.path.join(dl_path, f"{video.title}.mp4")
            lumberjack.info("video path: %s", video_path)

            # * download video if it does not exist
            if not os.path.isfile(video_path):
                lumberjack.info(">>> download start: %s", video.title)
                
                if prod:
                    stream = video.streams.get_highest_resolution()
                    stream.download(output_path=dl_path)

                lumberjack.info(">>> download complete: %s", video.title)
            
            else:
                lumberjack.info(">>> file exists: %s", video.title)


    except KeyboardInterrupt as e:
        lumberjack.info("keyboard interruption: %s", e)
    
    except Exception as e:
        lumberjack.error("ERROR: %s", e)

    return None


# %%

if __name__ == "__main__":
    # url = input("Enter url for playlist: ")
    url = "https://www.youtube.com/watch?v=kA5xUtrM6bo&list=PLCGGtLsUjhm2bonhBZuEhZU72QkFjOpc6"
    download_youtube_playlist(url=url,prod=True)


