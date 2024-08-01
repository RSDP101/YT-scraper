# Youtube scraper

Scrape, download and edit any youtube videos and shorts for free without a Youtube Pro subscription!

* Clone repository and create a virtual environment
```python
git clone https://github.com/RSDP101/YT-scraper
cd YT-scraper
python3 -m venv venv
source venv/bin/activate
```

* Install all dependencies:
```python
pip install -r requirements.txt
```
Now you are ready to use the scripts! 

* To scrape 'count' videos from youtube matching a 'query':

```python
# Change it to match your query and count. It automatically saves the links into youtube_shorts.csv file.
python3 scraper.py --query=ronaldo --count=10
```



* To download a video from youtube link:
```python
# Add the link to the download.py script
python3 download.py
```

* To trim a video you've just downloaded:
```python
# Edit the input_video and output_video paths on the script. Also change the start and end seconds.
python3 edit.py
```

* To extract the audio of a video you've downloaded:
```python
#Edit the input path and the start, end seconds.
python3 get_audio.py
```
