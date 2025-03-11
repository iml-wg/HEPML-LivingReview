### modified from Waleed Esmail

import argparse
import datetime
import re  # regular expressions lib 'pip install regex'

import requests


# Function to get BibTeX citation for a given arXiv ID
def get_bibtex(arxiv_id):
    # Construct the URL for the INSPIRE-HEP API
    url = f"https://inspirehep.net/api/literature?q=arxiv:{arxiv_id}&format=bibtex"
    # Send a GET request to the API and get the response
    response = requests.get(url)
    # Return the text of the response, which is the BibTeX citation
    return response.text

# Function to replace the collaboration author in a BibTeX citation with the collaboration name
def replace_collaboration_author(bib_entry):

    # Check for collaboration field in this bib_entry
    collab_field = re.search(r'collaboration\s+=.*\n\s+', bib_entry)

    if collab_field is None:
        return bib_entry
    else:
        collab_field = collab_field.group(0)

    collab_names = {
        'ATLAS': 'ATLAS Collaboration',
        'CMS': 'CMS Collaboration',
        'LHCb': 'LHCb Collaboration',
        'ALICE': 'ALICE Collaboration',
        'H1': 'H1 Collaboration',
        'IceCube': 'IceCube Collaboration',
        'NNPDF': 'NNPDF Collaboration',
        'Belle-II': "Belle-II Collaboration",
        'Belle II': "Belle-II Collaboration",
        'BESIII': "BESIII Collaboration",
        'DARWIN': "DARWIN Collaboration",
        'MODE': "MODE Collaboration",
        'DUNE': "DUNE Collaboration",
        'MAP': "MAP Collaboration",
        'QUEST-DMC': "QUEST-DMC Collaboration",
        'JETSCAPE': "JETSCAPE Collaboration",
        'Hyper-Kamiokande': "Hyper-Kamiokande Collaboration"
    }

    # Find the collaboration field and select matching name above
    collab_name = None
    for exp in collab_names.keys():
        if exp in collab_field:
            collab_name = collab_names[exp]

    if collab_name is not None:
        # Use a regular expression to find the collaboration author in the BibTeX citation
        author = re.search(r'author\s+=(.*)', bib_entry).group(1)
        # Set the collaboration name as author
        bib_entry = bib_entry.replace(author, ' "{' + collab_name + '}",')
        # Delete the collaboration field
        bib_entry = bib_entry.replace(collab_field, '')
    else:
        print(f"WARNING: No matching collaboration found for:\n{bib_entry}")

    return bib_entry

# Function to extract arXiv IDs from a text file and write their BibTeX citations to another file
def extract_arxiv_ids(input, output_file, replace_collab=True):

    # Can pass the arxiv IDs in a txt file
    if '.txt' in input:
        # Open the input file in read mode
        with open(input) as f:
            # Read the entire contents of the file
            text = f.read()
    else: #TODO need to add support for this direct entry mode (will break when parsing arxiv, date, etc.)
        text = input

    # Use a regular expression to find all arXiv IDs in the text
    arxiv_ids = re.findall(r'arXiv:\s+([0-9.]+)', text)

    # Find the date
    dates = re.findall(r'(\d{4}-\d{2}-\d{2})', text)
    dates = [datetime.datetime.strptime(date, '%Y-%m-%d') for date in dates]

    # Create dictionary sorted by date
    arxivs_dates = {arxiv_id: date for arxiv_id, date in zip(arxiv_ids, dates)}
    arxivs_dates = dict(sorted(arxivs_dates.items(), key=lambda x: x[1], reverse=True))

    # Open the output file in write mode
    with open(output_file, 'w') as f:
        for arxiv_id, date in arxivs_dates.items():
            bibtex = get_bibtex(arxiv_id)
            # In case of a collaboration paper, put the collaboration as author
            if replace_collab:
                bibtex = replace_collaboration_author(bibtex)
            # Write the date (in Mon day, year format) followed by BibTeX citation for each arxiv to the output file
            f.write(f"% {date.strftime('%B %d, %Y')}* \n{bibtex}\n")

        print(f"{len(arxivs_dates)} citations written to {output_file} !")


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("-i","--input",   dest="input",          type=str,  help="path to input file containing arXiv IDs", required=True)
    parser.add_argument("-o","--output",  dest="output",         type=str,  help="path to output file containing resulting bibtex entries", default="output_citations.bib")
    parser.add_argument("-c","--collab",  dest="replace_collab", type=int,  help="replace author field in case of collaboration paper", default=1)
    args = parser.parse_args()

    # Call the function with the path to the input file and the path to the output file
    extract_arxiv_ids(args.input, args.output, bool(args.replace_collab))
