# Savanna Hans0n
# CS361 - Wikipedia Scaper Service


import wikipedia
from time import time, sleep

request_file = "request.txt"
response_file = "response.txt"


while True:
    # open with read/write mode
    input = open(request_file, 'r+')
    output = open(response_file, 'a')

    article_name = input.read()
    # The service clears request file immediately so another can come in.
    input.truncate(0)

    # If we got a request, do stuff with it
    if article_name:
        try:
            summary = wikipedia.summary(article_name)
            # Print it (for testing purposes)
            # print(summary)
            # Write the summary to the reponse file
            output.write(summary)
        except wikipedia.exceptions.PageError:
            output.write("ERROR. Request does not match any pages.\n")  

        # The user of the service is responsible for clearing the response file!
    
    input.close()
    output.close()

    sleep(3)

