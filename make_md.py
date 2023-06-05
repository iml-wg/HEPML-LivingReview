import os

import requests

from datetime import datetime
from dataclasses import dataclass


update_journal = False


myfile = open("HEPML.tex", encoding="utf8")
myfile_readme = open("README.md","w", encoding="utf8")
myfile_out = open("docs/index.md","w", encoding="utf8")
myfile_about = open("docs/about.md", "w",encoding="utf8")

for file in myfile_about,myfile_out:
    file.write("---\nhide:\n  - navigation\n---\n\n")

with open("script.js") as script:
    myfile_out.write('<script>\n')
    for line in script:
        myfile_out.write(line)
    myfile_out.write('\n</script>\n\n')

for file in myfile_readme,myfile_out:
    file.write("#  **A Living Review of Machine Learning for Particle Physics**\n\n")
    file.write("*Modern machine learning techniques, including deep learning, is rapidly being applied, adapted, and developed for high energy physics.  The goal of this document is to provide a nearly comprehensive list of citations for those developing and applying these approaches to experimental, phenomenological, or theoretical analyses.  As a living document, it will be updated as often as possible to incorporate the latest developments.  A list of proper (unchanging) reviews can be found within.  Papers are grouped into a small set of topics to be as useful as possible.  Suggestions are most welcome.*\n\n")
    file.write("[![download](https://img.shields.io/badge/download-review-blue.svg)](https://iml-wg.github.io/HEPML-LivingReview/review/hepml-review.pdf)\n[![github](https://badges.aleen42.com/src/github.svg)](https://github.com/iml-wg/HEPML-LivingReview)\n\n")


for file in myfile_readme,myfile_about:
    file.write(r"The purpose of this note is to collect references for modern machine learning as applied to particle physics. A minimal number of categories is chosen in order to be as useful as possible. Note that papers may be referenced in more than one category. The fact that a paper is listed in this document does not endorse or validate its content - that is for the community (and for peer-review) to decide. Furthermore, the classification here is a best attempt and may have flaws - please let us know if (a) we have missed a paper you think should be included, (b) a paper has been misclassified, or (c) a citation for a paper is not correct or if the journal information is now available. In order to be as useful as possible, this document will continue to evolve so please check back before you write your next paper. If you find this review helpful, please consider citing it using ```\cite{hepmllivingreview}``` in `HEPML.bib`.")
    file.write("\n\nThis review was built with the help of the HEP-ML community, the [INSPIRE REST API](https://github.com/inspirehep/rest-api-doc), and the moderators Benjamin Nachman, Matthew Feickert, Claudius Krause, and Ramon Winterhalder.\n\n")

###Add buttons
myfile_out.write("""\n<a class="md-button" onClick="expandElements(true)">Expand all sections</a>\n<a class="md-button" onClick="expandElements(false)">Collapse all sections</a>\n""")

###This bit is slightly modified from Kyle Cranmer https://github.com/cranmer/inspire_play
def summarize_record(recid):
    url = 'https://labs.inspirehep.net/api/arxiv/'+str(recid)
    max_authors = 5
    r = requests.get(url)
    mini_dict = {'recid':recid}
    if 'metadata' in r.json():
        data = r.json()['metadata']
        mini_dict.update({'title':data['titles'][0]['title']})
        if len(data['authors'])>max_authors:
            #mini_dict.update({'authors':[a['full_name'] for a in data['authors'][:max_authors]]+['et. al.']})
            mini_dict.update({'authors':"; ".join([a['full_name'] for a in data['authors'][:max_authors]]+['et. al.'])})
        else:
            mini_dict.update({'authors':[a['full_name'] for a in data['authors']]})

        if 'collaborations' in data:
            mini_dict.update({'collaboration': data['collaborations'][0]['value']})

        mini_dict.update({'arxiv_eprint': data['arxiv_eprints'][0]['value']})
        mini_dict.update({'url': 'https://arxiv.org/abs/'+data['arxiv_eprints'][0]['value']})
        mini_dict.update({'creation_date': data['legacy_creation_date']})

        if 'journal_title' in data:
            mini_dict.update({'journal_title':data['publication_info'][0]['journal_title']})
        if 'journal_volume' in data:
            mini_dict.update({'journal_volume':data['publication_info'][0]['journal_volume']})
        if 'page_start' in data:
            mini_dict.update({'page_start':data['publication_info'][0]['page_start']})
        if 'journal_year' in data:
            mini_dict.update({'journal_year':data['publication_info'][0]['year']})

        if 'dois' in data:
            mini_dict.update({'doi': data['dois'][0]['value']})
    return mini_dict

def convert_from_bib(myline):
    #Not the most elegant way, but quick and dirty.  Files are not big, so this doesn't take long.

    myline = myline.replace(" ","").replace("\n","")

    myfile_bib = open("HEPML.bib", encoding="utf8")
    mylines = []
    for line in myfile_bib:
        mylines+=[line]
        pass
    myentry = []
    for i in range(len(mylines)):
        if myline in mylines[i]:
            j = i+1
            myentry+=[mylines[i]]
            while "@" not in mylines[j]:
                myentry+=[mylines[j]]
                j+=1
                pass
            pass
        pass
    myentry_dict = {}
    for entry in myentry:
        entry_cleaned = entry.replace("\"{","").replace("}\",","").replace("},","")
        entry_cleaned = entry_cleaned.replace(" =","=")
        entry_cleaned = entry_cleaned.replace("= ","=")
        first_entry = entry_cleaned.split("=")[0]
        if "title" in first_entry and not "booktitle" in first_entry:
            myentry_dict["title"] = entry_cleaned.split("title")[1].split("=")[1].split("\n")[0]
            pass
        elif "eprint" in first_entry:
            myentry_dict["eprint"] = entry_cleaned.split("eprint")[1].split("=")[1].split("\n")[0].replace("\"","").replace(",","").replace("\'","").replace(" ","")
            if "{" in myentry_dict["eprint"]:
                myentry_dict["eprint"] = myentry_dict["eprint"][1:]
                pass
        elif "doi" in first_entry:
            myentry_dict["doi"] = entry_cleaned.split("doi")[1].split("=")[1].split("\n")[0].replace("\"","").replace(",","").replace("\'","").replace(" ","")
        elif "url" in first_entry:
            myentry_dict["url"] = entry_cleaned.split("url")[1].split("=")[1].split("\n")[0].replace("\"","").replace(",","").replace("\'","").replace(" ","")
        else:
            #print(entry_cleaned)
            pass
        pass

    if "eprint" in myentry_dict and 'doi' not in myentry_dict and update_journal:
        #check inspire
        inspire_dict = summarize_record(myentry_dict['eprint'])
        if 'doi' in inspire_dict:
            print("Updating journal ref for ",myline)
            myentry_dict['doi'] = inspire_dict['doi']

            #print(inspire_dict)

            myfile_bib_copy = open("HEPML_copy.bib","w", encoding="utf8")
            myfile_bib = open("HEPML.bib", encoding="utf8")
            for line in myfile_bib:
                myfile_bib_copy.write(line)
                if myentry_dict['eprint'] in line and "eprint" in line:
                    if "journal_title" in inspire_dict:
                        myfile_bib_copy.write("      journal=\""+inspire_dict['journal_title']+"\",\n")
                    if "journal_volume" in inspire_dict:
                        myfile_bib_copy.write("      volume=\""+inspire_dict['journal_volume']+"\",\n")
                    if "page_start" in inspire_dict:
                        myfile_bib_copy.write("      pages=\""+inspire_dict['page_start']+"\",\n")
                    if "doi" in inspire_dict:
                        myfile_bib_copy.write("      doi=\""+inspire_dict['doi']+"\",\n")
                        pass
                    pass
                pass
            os.system("mv HEPML_copy.bib HEPML.bib")
            #exit(1)

    if "title" not in myentry_dict:
        print(myline)
        print(myentry)
        print("We are in trouble ! ")
    if "eprint" in myentry_dict:
        paper=""
        if "doi" in myentry_dict:
            paper=f" [[DOI](https://doi.org/{myentry_dict['doi']})]"
        elif "url" in myentry_dict:
            paper=f" [[url]({myentry_dict['url']})]"
        return "["+myentry_dict["title"]+"](https://arxiv.org/abs/"+myentry_dict["eprint"]+")"+paper
    elif "doi" in myentry_dict:
        return "["+myentry_dict["title"]+"](https://doi.org/"+myentry_dict["doi"]+")"
    elif "url" in myentry_dict:
        return "["+myentry_dict["title"]+"]("+myentry_dict["url"]+")"
    else:
        return myentry_dict["title"]
    return myline

def write_to_files(*args,readme=myfile_readme,webpage=myfile_out,add_header=False):
    for line in args:
        readme.write(line)
        split = line.split("###")
        if line.find('####') == -1:
            if len(split) > 1:
                webpage.write("\n??? example "+"\""+split[-1].strip()+"\"")
                webpage.write("\n    <div class=\"meta_for_parser tablespecs\"\n    style=\"font-size: 1pt;visibility:hidden\" markdown>")
                webpage.write("\n    "+line.strip('\n\r')+"\n    </div>\n\n")
            elif line[0] == '*':
                webpage.write("    "+line)
            else: webpage.write(line)
        else:
            webpage.write("    "+line)

        if add_header:
            split = line.split("##")
            webpage.write("\n??? example "+"\""+split[-1].strip()+"\"\n\n")

itemize_counter = 0
for line in myfile:

    if "author" in line:
        continue

    if "\\item \\textbf{" in line:
        line = line.replace("\\textbf{","")
        i = line.find("}")
        j = line.find("{")
        while j != -1 and j < i:
            i = line.find("}", i+1)
            j = line.find("{", i+1)
        line = line[:i] + line[i+1:-1]

    if "textit{" in line:
        continue
    if "item" in line:
        if "begin{itemize}" in line:
            itemize_counter+=1
        elif "end{itemize}" in line:
            itemize_counter-=1
        else:
            #print(itemize_counter,line)
            if (itemize_counter==1):
                hascites = len(line.split("cite"))
                if (hascites==1):
                    if "Experimental" not in line:
                        write_to_files("## "+line.replace(r"\item","")+"\n")
                    else:
                        write_to_files("##  Experimental results.\n *This section is incomplete as there are many results that directly and indirectly (e.g. via flavor tagging) use modern machine learning techniques.  We will try to highlight experimental results that use deep learning in a critical way for the final analysis sensitivity.*\n\n")
                else:
                    write_to_files("## "+line.replace(r"\item","").split(r"~\cite")[0]+".\n\n",add_header=True)
                    mycites = line.split(r"~\cite{")[1].split("}")[0].split(",")
                    for cite in mycites:
                        write_to_files("* "+convert_from_bib(cite)+"\n")
                        pass
                    write_to_files("\n")
                    pass
                pass
            else:
                mybuffer = ""
                header = '##'
                for j in range(itemize_counter-1):
                    #  mybuffer+="    "
                     header+='#'
                     pass
                if (":~" in line):
                    write_to_files(header+line.split(r"~\cite{")[0].split(r"\item")[1]+"\n\n")
                    mycites = line.split(r"~\cite{")[1].replace("}","").split(",")
                    for cite in mycites:
                        write_to_files(mybuffer+"* "+convert_from_bib(cite)+"\n")
                        pass
                    write_to_files("\n")

                elif "cite" in line:
                    write_to_files(header+" "+line.split(r"~\cite{")[0].split(r"\item")[1]+"\n\n")
                    mycites = line.split(r"~\cite{")[1].split("}")[0].split(",")
                    for cite in mycites:
                        write_to_files(mybuffer+"* "+convert_from_bib(cite)+"\n")
                        pass
                    write_to_files("\n")
                    pass
                else:
                    write_to_files(header+line.split(r"\item")[1]+"\n\n")
                pass

def get_year_month(period_months=3):
    month_up = datetime.now().month
    year = datetime.now().year
    month_low = month_up - period_months
    dates = []
    if month_low < 1:
        month_n = 12 + month_low
        dates += [(year-1,m) for m in range(month_n,13)]
    month_low = 1 if month_low < 1 else month_low
    dates += [(year,m+1) for m in range(month_low,month_up)]
    return dates

@dataclass
class Cite:
    name: str
    month: int
    year: int

refs = []

prev_months = 4
dates = get_year_month(prev_months)

month_dict = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}


print("Compiling new references in dates:",dates)

with open('HEPML.bib','r') as bibfile:
    id = None
    month = None
    year = None
    for line in bibfile:        
        if len(line.split('@')) > 1:
            id = line.split('{')[-1]
        elif 'month' in line:
            month = int(''.join(filter(str.isdigit,line.split('=')[1])))
        elif 'year' in line:
            year = int(''.join(filter(str.isdigit,line.split('=')[1])))
        if id and month and year:
            # print((month,year))
            # print((month,year) in dates)
            if (year,month) in dates:
                refs.append(Cite(id,month,year))
            else:
                break
            id,month,year = None,None,None

myfile_out = open("docs/recent.md", "w",encoding="utf8")

myfile_out.write("---\nhide:\n  - navigation\nsearch:\n  exclude: true\n---\n\n")
myfile_out.write(f"Here is an automatically compiled list of papers which have been added to the living review within the previous {prev_months} months of the time of updating. This is not an exhaustive list of released papers, and is only able to find those which have both year and month data provided in the bib reference.\n")

current_year = refs[0].year
current_month = refs[0].month
myfile_out.write(f'\n# {month_dict[current_month]} {current_year}\n')
for cite in refs:
    if (cite.year != current_year) | (cite.month != current_month):
        current_year = cite.year
        current_month = cite.month
        myfile_out.write(f'\n# {month_dict[current_month]} {current_year}\n')

    myfile_out.write("* "+convert_from_bib(cite.name)+"\n")
myfile_out.write('\n')