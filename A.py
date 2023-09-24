import random as rand
import requests
import json
from omdbapi.movie_search import GetMovie


class Movies():


    def main(self):

        # print ("in method")
        url = "https://www.omdbapi.com/?apikey=16e82100&i="

        id = rand.randrange(0000000, 9999999)
        ids = "tt" + str(id)

        finalUrl = url + ids

        response = requests.post(finalUrl)
        print(response.json()["Response"])
        if(response.json()["Response"] == "False" or response.json()["Type"] == 'episode'):
            self.main()
        else:
            print("Status code:", response.status_code)
            print("Title: " + response.json()["Title"])
            print("*****************************")
            print (response.json())



o1 = Movies()
o1.main()
    
