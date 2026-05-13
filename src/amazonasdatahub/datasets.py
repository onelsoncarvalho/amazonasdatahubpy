import pandas as pd
import requests
from pathlib import Path

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


