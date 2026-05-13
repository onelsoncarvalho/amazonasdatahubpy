import pandas as pd
import requests
import os
import re
from pathlib import Path

#get_docs
import frontmatter
from importlib import resources


CACHE_DIR = Path.home() / ".cache" / "amazonasdatahub"
CACHE_DIR.mkdir(parents = True, exist_ok=True)

def get_dataset(dataset_name, force=False):
    """
    Gather an specific dataset.
    :param dataset_name: Dataset name (example: agriculture_amazonas)
    :param force: If True, ignores the cache and downloads the dataset again
    """

    file_name = f"{dataset_name}.parquet"
    local_path = CACHE_DIR / file_name
    #url = f"https://github.com/onelsoncarvalho/amazonasdatahubsite/data/{file_name}"
    #url = f"https://raw.githubusercontent.com/onelsoncarvalho/testing_amazonasdatahub/raw/refs/heads/main/data/{file_name}"
    url = f"https://raw.githubusercontent.com/onelsoncarvalho/testing_amazonasdatahub/main/data/{file_name}"

    if force or not local_path.exists():
        print(f"Gathering updated data from {url}...")
        try:
            response = requests.get(url)
            response.raise_for_status()

            with open(local_path, "wb") as f:
                f.write(response.content)
            print(f"Saved in: {local_path}")

        except Exception as e:
            if not local_path.exists():
                raise Exception(f"Error while downloading and there is no cache available: {e}")
            print(f"Warning: Download error, using old cache version. Error: {e}")

    return pd.read_parquet(local_path)


def get_doc(dataset_name):
    """
    Shows the documentation of a dataset
    """

    try:
        md_path = resources.files("amazonasdatahub.docs").joinpath(f"{dataset_name}.md")
        if not md_path.exists():
            print(f"Docs for {dataset_name} not found")
            return

        md_content = md_path.read_text(encoding = "utf-8")

        loaded_md = frontmatter.loads(md_content)

        title = loaded_md.get('title', dataset_name.upper())
        body = loaded_md.content

#         cleaned_body = re.sub(r'```r.*?
# ```', '', corpo, flags=re.DOTALL)
        # cleaned_body = re.sub(r'```r.*?```', '', body, flags=re.DOTALL)
        # cleaned_body = re.sub(r'### Usage.*?(?=###|\Z)', '', body, flags=re.DOTALL)

        print(f"\n{'='*60}")
        print(f"Documentation from: {title}")
        print(f"{'='*60}")

        try :
            from IPython.display import display, Markdown
            display(Markdown(body))
        except ImportError:
            print(body)
    except Exception as e:
        print(f"Error while processing docs: {e}")
        
