#!/usr/bin/env python3
def createDataframefromDict(screenplayDict:dict):
 
    dfcolumns = ['Person','SeasonNr','EpisodeNr','EpisodeTitle','EpisodeID','Scene','ScreenLine']


    sceneList = []

    episodeID = 0
    

    for title in screenplayDict:
        print(title)

        episodeTitle = title
        episodeID += 1
        seasonNr = screenplayDict[title]['season']
        
        allLines = []
        sceneName = ""
        print(screenplayDict[sceneKey])
    

    df = pd.DataFrame(allLines,columns=dfcolumns)
    return df
