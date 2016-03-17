import subprocess
#for each commit in text file
	


urls = [ 
#	"https://github.com/harvesthq/chosen",
#	"https://github.com/slimphp/Slim",
#	"https://github.com/twitter/gizzard",
#	"https://github.com/JakeWharton/ActionBarSherlock",
#	"https://github.com/thoughtbot/paperclip",
#	"https://github.com/mitsuhiko/flask",
#	"https://github.com/ariya/phantomjs",
#	"https://github.com/tornadoweb/tornado",
#	"https://github.com/scalatra/scalatra",
#	"https://github.com/sbt/sbt",
#	"https://github.com/twitter/finagle",
#	"https://github.com/antirez/redis",
#	"https://github.com/hbons/SparkleShare",
#	"https://github.com/ServiceStack/ServiceStack",
	"https://github.com/sebastianbergmann/phpunit"
	]





repoNames = [ 
#	"chosen",
#	"Slim",
#	"gizzard",
#	"ActionBarSherlock",
#	"paperclip",
#	"flask",
#	"phantomjs",
#	"tornado",
#	"scalatra",
#	"sbt",
#	"finagle",
#	"redis",
#	"SparkleShare",
#	"ServiceStack",
	"phpunit"
	]



index = 0
for repoName in repoNames:
	outputtotextfile = 1
	gotcommit1 = 0
	gotcommit2 = 0 
	with open(repoName + "_largestcommits.txt") as f:
		count = 0 
		for line in f:

			if(line.startswith("1 percent of commits")):
				numcommits = int(float(line[21:]))
			if(line.startswith("commit number: ")):
				commitNumber = int(float(line[15:]))
			elif(line.startswith("commitid1")):
				commitid1 = line[11:17]
				gotcommit1 = 1
			elif(line.startswith("commitid2")):
				commitid2 = line[11:17]
				gotcommit2 = 1
			elif(gotcommit1 and gotcommit2):
				gotcommit1 = 0
				gotcommit2 = 0
				if(commitNumber==1):
					subprocess.call(["git", "clone", urls[index]])

				process = subprocess.Popen(["git", "-C", repoNames[index], "diff", commitid2, commitid1 ], stdout=subprocess.PIPE)
				out, err = process.communicate()
				
				fname = open(repoName+"_gitdiff"+str(commitNumber)+".txt",'w')
				for diffline in out.splitlines():
					fname.write(diffline)
					fname.write('\n')
				fname.close()

				
				
				if(commitNumber == numcommits):
					subprocess.call(["rm", "-rf", repoName])
				
	index = index + 1

				

