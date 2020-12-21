import os

myfile = open("HEPML.tex")
myfile_out = open("README.md","w")

myfile_out.write("#  **A Living Review of Machine Learning for Particle Physics**\n\n")

myfile_out.write("*Modern machine learning techniques, including deep learning, is rapidly being applied, adapted, and developed for high energy physics.  The goal of this document is to provide a nearly comprehensive list of citations for those developing and applying these approaches to experimental, phenomenological, or theoretical analyses.  As a living document, it will be updated as often as possible to incorporate the latest developments.  A list of proper (unchanging) reviews can be found within.  Papers are grouped into a small set of topics to be as useful as possible.  Suggestions are most welcome.*\n\n")

myfile_out.write("[![download](https://img.shields.io/badge/download-review-blue.svg)](https://iml-wg.github.io/HEPML-LivingReview/review/hepml-review.pdf)\n\n")

myfile_out.write("The purpose of this note is to collect references for modern machine learning as applied to particle physics.  A minimal number of categories is chosen in order to be as useful as possible.  Note that papers may be referenced in more than one category.  The fact that a paper is listed in this document does not endorse or validate its content - that is for the community (and for peer-review) to decide.  Furthermore, the classification here is a best attempt and may have flaws - please let us know if (a) we have missed a paper you think should be included, (b) a paper has been misclassified, or (c) a citation for a paper is not correct or if the journal information is now available.  In order to be as useful as possible, this document will continue to evolve so please check back before you write your next paper.  If you find this review helpful, please consider citing it using \\cite{hepmllivingreview} in HEPML.bib.\n\n")

def convert_from_bib(myline):
    #Not the most elegant way, but quick and dirty.  Files are not big, so this doesn't take long.

    myline = myline.replace(" ","").replace("\n","")

    myfile_bib = open("HEPML.bib")
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
        first_entry = entry_cleaned.split("=")[0]
        if "title" in first_entry:
            myentry_dict["title"] = entry_cleaned.split("title")[1].split("=")[1].split("\n")[0]
            pass
        elif "eprint" in first_entry:
            myentry_dict["eprint"] = entry_cleaned.split("eprint")[1].split("=")[1].split("\n")[0].replace("\"","").replace(",","").replace("\'","").replace(" ","")
        elif "doi" in first_entry:
            myentry_dict["doi"] = entry_cleaned.split("doi")[1].split("=")[1].split("\n")[0].replace("\"","").replace(",","").replace("\'","").replace(" ","")
        elif "url" in first_entry:
            myentry_dict["url"] = entry_cleaned.split("url")[1].split("=")[1].split("\n")[0].replace("\"","").replace(",","").replace("\'","").replace(" ","")
        else:
            #print(entry_cleaned)
            pass
        pass
    if "title" not in myentry_dict:
        print(myline)
        print(myentry)
        print("We are in trouble ! ")
    if "eprint" in myentry_dict:
        paper=""
        if "doi" in myentry_dict:
            paper=" [[DOI](https://doi.org/{})]".format( myentry_dict["doi"] )
        return "["+myentry_dict["title"]+"](https://arxiv.org/abs/"+myentry_dict["eprint"]+")"+paper
    elif "doi" in myentry_dict:
        return "["+myentry_dict["title"]+"](https://doi.org/"+myentry_dict["doi"]+")"
    elif "url" in myentry_dict:
        return "["+myentry_dict["title"]+"]("+myentry_dict["url"]+")"
    else:
        return myentry_dict["title"]
    return myline

itemize_counter = 0
for line in myfile:

    if "author" in line:
        continue

    if "\\item \\textbf{" in line:
        line = line[0:line.find("}")]+line[line.find("}")+1:-1]
    line = line.replace("\\textbf{","")

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
                        myfile_out.write("* "+line.replace(r"\item","")+"\n")
                    else:
                        myfile_out.write("*  Experimental results. *This section is incomplete as there are many results that directly and indirectly (e.g. via flavor tagging) use modern machine learning techniques.  We will try to highlight experimental results that use deep learning in a critical way for the final analysis sensitivity.*\n\n")
                else:
                    myfile_out.write("* "+line.replace(r"\item","").split(r"~\cite")[0]+".\n\n")
                    mycites = line.split(r"~\cite{")[1].split("}")[0].split(",")
                    for cite in mycites:
                        myfile_out.write("    * "+convert_from_bib(cite)+"\n")
                        pass
                    myfile_out.write("\n")
                    pass
                pass
            elif "cite" in line:
                mybuffer = ""
                for j in range(itemize_counter-1):
                     mybuffer+="    "
                     pass
                if (":~" in line):
                    myfile_out.write(mybuffer+"* "+line.split(r"~\cite{")[0].split(r"\item")[1]+"\n\n")
                    mycites = line.split(r"~\cite{")[1].replace("}","").split(",")
                    for cite in mycites:
                        myfile_out.write(mybuffer+"    * "+convert_from_bib(cite)+"\n")
                        pass
                    myfile_out.write("\n")
                else:
                    myfile_out.write(mybuffer+"* "+line.split(r"~\cite{")[0].split(r"\item")[1]+"\n\n")
                    mycites = line.split(r"~\cite{")[1].split("}")[0].split(",")
                    for cite in mycites:
                        myfile_out.write(mybuffer+"    * "+convert_from_bib(cite)+"\n")
                        pass
                    myfile_out.write("\n")
                    pass
                pass
