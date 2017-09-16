import io
import urllib2
#y=120338
y=125835
z=1
for x in xrange(10835, 20000):    
    path='http://www.omdbapi.com/?i=tt0'+str(y)+'&plot=full&r=xml'    
    try:
        resp = urllib2.urlopen(path)
        page = resp.read()
        with io.FileIO("Path"+str(x)+".xml", "w") as file:
            file.write(page)
        y+=1
        print 'Movie Number  %s has been crawled' % (str(x))
        z+=1
    except Exception:        
        continue
    
