from operator import itemgetter
import subprocess


urls = [ 
    # #bea & moath
    # "https://github.com/hsarvesthq/chosen",
    #  "https://github.com/slimphp/Slim",
    #  "https://github.com/twitter/gizzard",
    #  "https://github.com/JakeWharton/ActionBarSherlock",
    #  "https://github.com/thoughtbot/paperclip",
    #  "https://github.com/mitsuhiko/flask",
    #  "https://github.com/ariya/phantomjs",
    #  "https://github.com/tornadoweb/tornado",
    #  "https://github.com/scalatra/scalatra",
    #  "https://github.com/sbt/sbt",
    #  "https://github.com/twitter/finagle",
    #  "https://github.com/antirez/redis",
    #  "https://github.com/hbons/SparkleShare",
    #  "https://github.com/ServiceStack/ServiceStack",
    #  "https://github.com/sebastianbergmann/phpunit",
    #  # brandon & tanner
        "https://github.com/XLordKX/kodi",
        "https://github.com/owncloud/android"
    #  "https://github.com/facebook/facebook-android-sdk",
    #  "https://github.com/pockethub/PocketHub",
    #  "https://github.com/AutoMapper/AutoMapper",
    #  "https://github.com/bitcoin/bitcoin",
    #  "https://github.com/TTimo/doom3.gpl",
    #  "https://github.com/jquery/jquery",
    #  "https://github.com/xbmc/xbmc",
    #  "https://github.com/reddit/reddit",
    #  "https://github.com/rails/rails",
    #  "https://github.com/scala/scala",
    # #jon & karson
    # "https://github.com/ThinkUpLLC/ThinkUp",
    # "https://github.com/bitcoin/bitcoin",
    # "https://github.com/scala/scala",
    # "https://github.com/mongodb/mongo",
    # "https://github.com/akka/akka",
    # "https://github.com/rstudio/shiny",
    # "https://github.com/xbmc/xbmc",
    # "https://github.com/reddit/reddit",
    # "https://github.com/Homebrew/legacy-homebrew",
    # "https://github.com/nodejs/node"

    ]


repoNames = [ 
    # #bea & moath
    # #"chosen",
    #  "Slim",
    #  "gizzard",
    #  "ActionBarSherlock",
    #  "paperclip",
    #  "flask",
    #  "phantomjs",
    #  "tornado",
    #  "scalatra",
    #  " sbt",
    #  "finagle",
    #  "redis",
    #  "SparkleShare",
    #  "ServiceStack",
    #  "phpunit",
    #  #brandon & tanner's group
    "Kodi",
    "Android"
    #  "facebook-android-sdk", 
    #  "PocketHub",
    #  "AutoMapper",
    #  "bitcoin",
    #  "doom3.gpl",
    #  "jquery",
    #  "xbmc",
    #  "reddit",
    #  "rails",
    #  "scala",
    #  #jon & karson
    # "ThinkUp",
    # "bitcoin",
    # "scala",
    # "mongo",
    # "akka",
    # "shiny",
    # "xbmc",
    # "reddit",
    # "legacy-homebrew",
    # "node"
    ]


correctiveKeyWords = ['bug', 'debug', 'fix', 
    'broken', 'work', 'edit', 'problem', 
    'error', 'typo', 'exception', 'try', 'catch']

adaptiveKeyWords = ['platform', 'build', 'test', 
    'doc', 'documentation', 'international', 'config', 
    'data', 'readme', 'info', 'comment', 'description', 'src', 'note', ]

implementationKeyWords = ['init', 'add', 'feature', 'implement']

nonfunctionalKeyWords = [ 'merge', 'license', 'legal', 'copyright'] 

perfectiveKeyWords = ['clean', 'whitespace', 'indent', 'spacing', 
    'refactor', 'move', 'rename', 'replace', 'remove', 'order',
    'redundant', 'tidy', 'rework', 'patch', 'move']

fname = open("results2.txt",'w')


def categorizeComments(comments):
    correctiveCount = 0
    adaptiveCount = 0
    implementationCount = 0
    nonfunctionalCount = 0
    perfectiveCount = 0 
    loopCount = 0
    for comment in comments:
       for correctivekw in correctiveKeyWords: 
           if correctivekw in comment: 
               correctiveCount = correctiveCount + 1
               break
       for adaptivekw in adaptiveKeyWords: 
           if adaptivekw in comment: 
               adaptiveCount = adaptiveCount + 1
               break
       for implementationkw in implementationKeyWords: 
           if implementationkw in comment: 
               implementationCount = implementationCount + 1
               break
       for nonfunctionalkw in nonfunctionalKeyWords: 
           if nonfunctionalkw in comment: 
               nonfunctionalCount = nonfunctionalCount + 1
               break
       for perfectivekw in perfectiveKeyWords: 
           if perfectivekw in comment: 
               perfectiveCount = perfectiveCount + 1
               break
    total = correctiveCount + implementationCount + adaptiveCount + nonfunctionalCount + perfectiveCount
    fname.write("\nCategorized " + str(total) + " out of " + str(len(comments)))
    fname.write("\ncorrective: " + str(correctiveCount))
    fname.write("\nimplementation: " + str(implementationCount))
    fname.write("\nadaptive: " + str(adaptiveCount))
    fname.write("\nnonfunctional: " + str(nonfunctionalCount))
    fname.write("\nperfective: " + str(perfectiveCount))

for repoName in repoNames: 
    commitidsfirst = [] 
    commitidssecond = [] 
    filecounts = [] 
    comments = ['']
    ids_and_counts = []

    def getKey(item):
        return item[2]

    with open(repoName + "_commitlog.txt") as f:
        
        #fname = open()

        counter = -1
        index = 0
        #for line in lines:
        commentStarted = 0
        for line in f:
            if line.startswith('commit'):
                if (counter == 0):
                    commitidsfirst.append(line[7:len(line)-1])
                    commitidssecond.append(line[7:len(line)-1])

                    #fname.write(commitidsfirst)
                    #fname.write(commitidssecond)
                elif(counter % 2 == 0):
                    commitidsfirst.append(line[7:len(line)-1])
                else:
                    commitidssecond.append(line[7:len(line)-1])
                counter = counter + 1
            elif line.startswith('Merge:') or line.startswith('Merge branch'):
                pass    
            elif line.startswith('File count'):
                filecounts.append(int(line[12:len(line)-1]))
                counter = counter + 1

            elif line.startswith('commentStart'): 
                commentStarted = 1
                comments.insert(index, '')
            elif line.startswith('commentEnd'):
                index = index + 1
                commentStarted = 0  
            elif commentStarted: 
                lowercaseComment = comments[index] + line
                comments.insert(index, lowercaseComment.lower())

        index = 0
        
        for commitidstart in commitidsfirst:
            tup = (commitidstart, commitidssecond[index], filecounts[index], comments[index])
            ids_and_counts.append(tup)
            index = index + 1

        ids_and_counts = sorted(ids_and_counts,key=getKey, reverse=True)   
    
   
    
    numberofcommits = len(ids_and_counts)*0.01
    commitcounter = 1
    largestcommits = []
    for line in ids_and_counts:
        if(commitcounter >= numberofcommits):
            break
        largestcommits.append(line[3])
        commitcounter = commitcounter + 1

    fname.write("\n" + repoName)
    fname.write("\n============")
    categorizeComments(largestcommits)
    fname.write("\n")
    
    subprocess.call(["rm", repoName + "_commitlog.txt"])
    





