""" Uses the inspirehep API of https://github.com/inspirehep/rest-api-doc to look for papers

    checks for all entries in 'categories'
    with keywords 'keywords'
    with date_created >= input date

    and prints title, arXiv id, inspirehep cite id
"""

import json
import os
from datetime import date, datetime

# Import the modules to open and reading URLs and the JSON encoder
import requests

starting_point = input("From which date do you want to start? \nFormat is YYYY-MM-DD!\n")
starting_date = date.fromisoformat(starting_point)

categories = ['hep-ph', 'hep-ex', 'hep-lat', 'hep-th', 'physics.ins-det', 'physics.data-an']
print(f"Looking at arXiv categories: {categories}")

keywords = ['neural network', 'machine learning', 'generative model', 'diffusion model', 'normalizing flow', 'foundation model', 'ML']
print(f"scanning papers with {keywords}:")
keyword_str = f'("{keywords}")'.replace("', '", '"%20OR%20"').replace("['", '').replace("']", "")
keyword_str = keyword_str.replace(" ", "%20")

for primarch in categories:
    inspirehep_profile = f'https://inspirehep.net/api/literature?sort=leastrecent&size=1000&q=primarch%20{primarch}%20AND%20{keyword_str}%20AND%20de%20>=%20{starting_date}'
    data = requests.get(inspirehep_profile).json()
    total_hits = data['hits']['total']
    if total_hits > 1000:
        print("Found more than 1000 hits! Please modify script to show entries beyond 1000.")
        # this requires adding &page=2 etc to the query above
    print(primarch, total_hits)
    for i in range(total_hits):
        print("date created: ", datetime.fromisoformat(data['hits']['hits'][i]['created']).date())
        print("title: ", data['hits']['hits'][i]['metadata']['titles'][0]['title'])
        print("arXiv: ", data['hits']['hits'][i]['metadata']['arxiv_eprints'][0]['value'])
        print("inspirehep cite: ", data['hits']['hits'][i]['metadata']['texkeys'][0])
        print("\n\n")

print("Done")
