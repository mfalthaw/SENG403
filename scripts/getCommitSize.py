import subprocess

#var = subprocess.check_output(["ls"]).splitlines()

#fname.write(var)

#urls = [ "https://github.com/twitter-archive/kestrel" , " ", " ", ]

urls = [ 
    #bea & moath
    "https://github.com/hsarvesthq/chosen",
     "https://github.com/slimphp/Slim",
     "https://github.com/twitter/gizzard",
     "https://github.com/JakeWharton/ActionBarSherlock",
     "https://github.com/thoughtbot/paperclip",
     "https://github.com/mitsuhiko/flask",
     "https://github.com/ariya/phantomjs",
     "https://github.com/tornadoweb/tornado",
     "https://github.com/scalatra/scalatra",
     "https://github.com/sbt/sbt",
     "https://github.com/twitter/finagle",
     "https://github.com/antirez/redis",
     "https://github.com/hbons/SparkleShare",
     "https://github.com/ServiceStack/ServiceStack",
     "https://github.com/sebastianbergmann/phpunit",
     # brandon & tanner
     "https://github.com/facebook/facebook-android-sdk",
     "https://github.com/pockethub/PocketHub",
     "https://github.com/AutoMapper/AutoMapper",
     "https://github.com/bitcoin/bitcoin",
     "https://github.com/TTimo/doom3.gpl",
     "https://github.com/jquery/jquery",
     "https://github.com/xbmc/xbmc",
     "https://github.com/reddit/reddit",
     "https://github.com/rails/rails",
     "https://github.com/scala/scala",
     #jon & karson
     "https://github.com/ThinkUpLLC/ThinkUp",
    
    
    "https://github.com/bitcoin/bitcoin",
    "https://github.com/scala/scala",
    "https://github.com/mongodb/mongo",
    "https://github.com/akka/akka",
    "https://github.com/rstudio/shiny",
    "https://github.com/xbmc/xbmc",
    "https://github.com/reddit/reddit",
    "https://github.com/Homebrew/legacy-homebrew",
    "https://github.com/nodejs/node"

    ]


repoNames = [ 
    #bea & moath
    #"chosen",
 
     "Slim",
     "gizzard",
     "ActionBarSherlock",
     "paperclip",
     "flask",
     "phantomjs",
     "tornado",
     "scalatra",
     " sbt",
     "finagle",
     "redis",
     "SparkleShare",
     "ServiceStack",
     "phpunit",
     #brandon & tanner's group 
     "facebook-android-sdk", 
     "PocketHub",
     "AutoMapper",
     "bitcoin",
     "doom3.gpl",
     "jquery",
     "xbmc",
     "reddit",
     "rails",
     "scala",
#jon & karson
    # "ThinkUp",

    "bitcoin",
    "scala",
    "mongo",
    "akka",
    "shiny",
    "xbmc",
    "reddit",
    "legacy-homebrew",
    "node"
    ]



index = 0
for url in urls:
	fname = open(repoNames[index]+"_commitlog.txt", 'w')
	fname.write(repoNames[index] + '\n')
	subprocess.call(["git", "clone", url])
	process = subprocess.Popen(["git", "-C", repoNames[index], "log" ,"--numstat"], stdout=subprocess.PIPE)
	out, err = process.communicate()
	subprocess.call(["rm", "-rf", repoNames[index]])
	index = index + 1

	#fname.write(str(out.splitlines()))
	count = 0
	first = 1
	fname.write("commentStart \n")
	for line in out.splitlines():
		if line.startswith('Author:') or line.startswith('Date:'):
			pass
		elif line.startswith('commit'):
			if first:
				first = 0
			else:
				fname.write("commentEnd" + '\n')
				fname.write(str(line) + '\n')
				fname.write("File count: " + str(count) + '\n')
				fname.write("---------------------------------------------\n")
				fname.write(str(line) + '\n')
				fname.write("commentStart" + '\n')
				count = 0
		else:
			if line.startswith(('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '-')):
				count = count + 1
				filename = ''.join([i for i in line if not i.isdigit() and i != '-'])
				#fname.write(filename + '\n')
			else:
				fname.write(str(line) + '\n') #comments
	fname.write('commentEnd')
	fname.close()