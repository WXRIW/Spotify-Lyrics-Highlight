# Spotify-Lyrics-Highlight
分析歌手或专辑的歌词的单词分布情况，仅适用于 Spotify

## Q&A
### 为啥做这个玩意
emmm因为要交作业

## Get started

首先需要安装 spotipy
```
py -m pip install spotipy
```
然后在 [Spotify Developers](https://developer.spotify.com/dashboard) 中申请一个新的应用，把 `Client ID` 和 `Client Secret` 放进源码  
之后再自行完成歌词获取部分的代码，推荐从网易云音乐或 QQ 音乐获取歌词  
然后就可以开心的运行啦！

### 这里有一个输出结果样例
```
Statistics for OneRepublic
-----------------
|      I | 135  |
|    the | 122  |
|   that | 73   |
|      a | 72   |
|   I've | 70   |
|    you | 69   |
|   been | 66   |
|     to | 61   |
|     it | 59   |
|    run | 59   |
|   yeah | 52   |
|    and | 49   |
|     be | 44   |
|  don't | 40   |
|     we | 39   |
|    all | 39   |
|     my | 38   |
|     in | 36   |
|     me | 36   |
|    but | 33   |
-----------------
By the way, we found that there are 85 SOMEs, isn't that amazing?!
```
