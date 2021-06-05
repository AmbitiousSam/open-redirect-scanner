import os
import requests
import sys
import time

os.system('clear')
print "#################################################"
print "#  Open redirect Scanner for dummies like me :) #"
print "#################################################"
print ""
print "Use ./redirect.py [subdomains.file] [redirect-payload]"
print "Example ./redirect.py uber.list '//yahoo.com/%2F..'"

# Payloads example

#payload = '//www.google.com/%2F..'
#payload2 = '//www.yahoo.com//'
#payload3 = '//www.yahoo.com//%2F%2E%2E'

file = sys.argv[1]

payload = sys.argv[2]

with open(file) as f:
	print ""
	print "Searching the ex-girlfriend target &  Holy Grial at [303 see others].."
	print ""
	time.sleep(4)
	for line in f:
		line2 = line.strip()
		line3 = 'http://' + line2 + payload
		print line3
		response = requests.get(line3, verify=True)
		print response
		try:
			if response.history:
				print "|"
				print resp.status_code, response.url
				print "Final destination:"
				print " + "
                print response.status_code, response.url

                                
            else:
            	print "Request was not redirected"

                            
        except:
        	print "connection error :("

		except:
			print "quiting.."



