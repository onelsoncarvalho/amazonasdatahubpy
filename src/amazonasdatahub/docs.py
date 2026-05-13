import frontmatter
from importlib import resources


def get_doc(dataset_name):
    """
    Shows the documentation of a dataset
    """

    try:
        md_path = resources.files("amazonasdatahub.documentations").joinpath(f"{dataset_name}.md")
        if not md_path.exists():
            print(f"Docs for {dataset_name} not found")
            return

        md_content = md_path.read_text(encoding = "utf-8")

        loaded_md = frontmatter.loads(md_content)

        title = loaded_md.get('title', dataset_name.upper())
        body = loaded_md.content

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