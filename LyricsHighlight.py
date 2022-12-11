import requests
import re
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="YOUR CLIENT ID",
                                                           client_secret="YOUR CLIENT SECRET"))

def actionSelector(inputQ):
    if inputQ.find('spotify:') == -1:
        result = actionSearchForArtist(inputQ)
        processTracks(result['tracks'], inputQ)
        return
    if inputQ.find('spotify:artist:') != -1:
        id = inputQ.split(':')[2]
        result = actionGetTracksByArtist(id)
        processTracks(result['tracks'], sp.artist(id)['name'])
        return
    if inputQ.find('spotify:album:') != -1:
        id = inputQ.split(':')[2]
        result = actionGetTracksByAlbum(id)
        processTracks(result['items'], sp.album(id)['name'])
        return
    return

def actionSearchForArtist(artistName):
    # Try to get artist ID by search
    results = sp.search(q=artistName, limit=20, type='artist')
    artistID = results['artists']['items'][0]['id']
    artistName = results['artists']['items'][0]['name']

    # Get artist's top tracks
    results = sp.artist_top_tracks(artistID)
    return results

def actionGetTracksByArtist(artistID):
    # Get artist's top tracks
    results = sp.artist_top_tracks(artistID)
    return results
    
def actionGetTracksByAlbum(albumID):
    # Get artist's top tracks
    results = sp.album_tracks(albumID)
    return results

def processTracks(tracks, tracksInfo = ''):
    # Get all lyrics and save to lyrics list
    wordsDict = {}
    someCount = 0
    for track in enumerate(tracks):
        lyrics = getLyricsByTrack(track)
        if lyrics != 'Lyric Not Found':
            # Fix string
            lyrics = lyrics.replace('\\r', '').replace('\\n', '\n').replace("&apos;", "'").replace("&amp;", "'").replace("&quot;", "\"")
            # Remove timeline
            lyrics = re.sub(r"\[.*\]", "", lyrics)
            # Remove Chinese and symbols
            lyrics = re.sub(r"[\u4e00-\u9fbb]", "", lyrics)
            lyrics = re.sub(r"[`~!@#$%^&*()+=|{}:;,\\\[\\\].<>?~！@#￥%……&*（）——+|{}【】‘；：”“’。，、？]", "", lyrics)
            # lyrics = re.sub(r"[`~!@#$%^&*()+=|{}':;',\\\[\\\].<>/?~！@#￥%……&*（）——+|{}【】‘；：”“’。，、？]", "", lyrics)
            words = lyrics.replace('\n', ' ').lower().split(' ')
            for word in words:
                word = word.strip()
                if word.find('some') != -1:
                    someCount = someCount + 1
                if word != '':
                    if word not in wordsDict:
                        wordsDict[word] = 1
                    else:
                        wordsDict[word] = wordsDict[word] + 1
    # Sort max to min
    wordList = sorted(wordsDict.items(), key=lambda x: x[1], reverse=True)
    output(wordList[:20], someCount, 'Statistics for {0}'.format(tracksInfo))
    
def output(wordList, someCount = 0, outputTitle = ''):
    print(outputTitle)
    maxLength = GetMaxLength(wordList) + 1

    for i in range(maxLength + 10):
        print('-', end='')
    print('-')
    for word in wordList:
        wordFix = word[0].replace('i\'', 'I\'')
        if wordFix == 'i':
            wordFix = 'I'
        print('| ' + wordFix.rjust(maxLength) + ' | ' + str(word[1]).ljust(4) + ' |')
    for i in range(maxLength + 10):
        print('-', end='')
    print('-')

    if someCount > 1:
        print('By the way, we found that there are {0} SOMEs, isn\'t that amazing?!'.format(someCount))
    return

def GetMaxLength(list):
    maxLength = 0
    for item in list:
        if len(item[0]) > maxLength:
            maxLength = len(item[0])
    return maxLength

def getLyricsByTrack(track):
    trackName = track[1]['name']
    trackID = track[1]['id']
    try:
        trackISRC = track[1]['external_ids']['isrc']
    except:
        trackISRC = ''
    artistName = track[1]['artists'][0]['name']
    # You need to do the GET LYRICS work here
    # And then return the lrc text
    return ""


print('Welcome to Lyrics Highlight by WXRIW')

# User make the input
inputQ = input("Input something (Artist name, Artist Spotify Uri, Album Spotify Uri, whatever~): ")
if inputQ == "":
    inputQ = "OneRepublic"

# Do the work
actionSelector(inputQ)
