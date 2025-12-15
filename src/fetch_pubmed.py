from Bio import Entrez
from tqdm import tqdm

Entrez.email = "YOUR_EMAIL_HERE"  

def fetch_pubmed(query, retmax=100):
    search_handle = Entrez.esearch(
        db="pubmed",
        term=query,
        retmax=retmax
    )

    search_results = Entrez.read(search_handle)
    pmids = search_results["IdList"]

    fetch_handle = Entrez.efetch(
        db="pubmed",
        id=",".join(pmids),
        rettype="abstract",
        retmode="xml"
    )

    records = Entrez.read(fetch_handle)

    papers = []

    for article in tqdm(records["PubmedArticle"]):
        try:
            citation = article["MedlineCitation"]
            article_data = citation["Article"]

            pmid = str(citation["PMID"])
            title = str(article_data.get("ArticleTitle", ""))

            abstract_sections = article_data.get("Abstract", {}).get("AbstractText", [])
            abstract = " ".join(str(sec) for sec in abstract_sections)

            journal = article_data["Journal"]["Title"]
            year = article_data["Journal"]["JournalIssue"]["PubDate"].get("Year", "NA")

            if len(abstract.strip()) > 200:
                papers.append({
                    "pmid": pmid,
                    "title": title,
                    "abstract": abstract,
                    "journal": journal,
                    "year": year
                })

        except Exception:
            continue

    return papers
