from operator import itemgetter



urls = [ 
#   "https://github.com/hsarvesthq/chosen",
#   "https://github.com/slimphp/Slim",
#   "https://github.com/twitter/gizzard",
#   "https://github.com/JakeWharton/ActionBarSherlock",
#   "https://github.com/thoughtbot/paperclip",
#   "https://github.com/mitsuhiko/flask",
#   "https://github.com/ariya/phantomjs",
#   "https://github.com/tornadoweb/tornado",
#   "https://github.com/scalatra/scalatra",
#   "https://github.com/sbt/sbt",
#   "https://github.com/twitter/finagle",
#   "https://github.com/antirez/redis",
#   "https://github.com/hbons/SparkleShare",
#   "https://github.com/ServiceStack/ServiceStack",
    "https://github.com/sebastianbergmann/phpunit"
    ]





repoNames = [ 
#   "chosen",
#   "Slim",
#   "gizzard",
#   "ActionBarSherlock",
#   "paperclip",
#   "flask",
#   "phantomjs",
#   "tornado",
#   "scalatra",
#   "sbt",
#   "finagle",
#   "redis",
#   "SparkleShare",
#   "ServiceStack",
    "phpunit"
    ]
correctiveKeyWords = []
adaptiveKeyWords = []
implementationKeyWords = []
nonfunctionalKeyWords = [] 
perfectiveKeyWords = ['merge']


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

    print("corrective: " + str(correctiveCount))
    print("implementation: " + str(implementationCount))
    print("adaptive: " + str(adaptiveCount))
    print("nonfunctional: " + str(nonfunctionalCount))
    print("perfective: " + str(perfectiveCount))

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

                    #print(commitidsfirst)
                    #print(commitidssecond)
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
    
    fname = open(repoName + "_largestcommits.txt",'w')
    '''
    fname.write('Number of commits ')
    fname.write(str(len(ids_and_counts)))
    fname.write('\n1 percent of commits ')
    '''
    numberofcommits = len(ids_and_counts)*0.01
    #fname.write('\n')
    commitcounter = 1
    largestcommits = []
    for line in ids_and_counts:
        if(commitcounter >= numberofcommits):
            break
        '''
        fname.write('\n')
        fname.write("commit number: ")
        fname.write(str(commitcounter))
        fname.write('\ncommitid1: ')
        fname.write(line[0])
        fname.write('\ncommitid2: ')
        fname.write(line[1])
        fname.write('\nFiles Changed: ')
        fname.write(str(line[2]))
        fname.write(' ')
        fname.write('\n')
        '''
        fname.write(line[3]) 
        largestcommits.append(line[3])
        fname.write("-----------------")
        commitcounter = commitcounter + 1

    categorizeComments(largestcommits)
    





