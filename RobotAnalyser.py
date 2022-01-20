import os

HTTP_redirect = []
HTTP_OK = []
HTTP_UNAUTH = []
HTTP_code= ""
with open('robots.txt') as robotFile:
    for robotLine in robotFile:
        
        curl_string ="curl -s -o /dev/null -w %{http_code} http://192.168.56.101/"+ robotLine.split("/")[1]
        
        shellOutput=os.popen(curl_string)
        HTTP_code = (shellOutput.read())
        if  HTTP_code == "301":
            HTTP_redirect.append(robotLine.split("/")[1])
        elif HTTP_code == "200":
            HTTP_OK.append(robotLine.split("/")[1])
        elif HTTP_code == "401":
            HTTP_UNAUTH.append(robotLine.split("/")[1])
            
           
print("-----------links with OK state-----------------------")
print("")
print("")
for link in HTTP_OK:
    print("http://192.168.56.101/"+link)         
print("----------- links with Unauthorized state------------")
for link in HTTP_UNAUTH:
    print("http://192.168.56.101/"+link)
print("")
            