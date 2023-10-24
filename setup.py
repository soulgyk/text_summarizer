import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()



__Version__ ="0.0.0"

REPO_NAME = "text_summarizer"
AUTHOR_USER_NAME = "soulgyk"
SRC_REPO = "textsummarizer"
AUTHOR_EMAIL = "soulgyk@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__Version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small pyhton package for NLP app",
    long_description="long_description",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
     },
     package_dir={"":"src"},
     packages=setuptools.find_packages(where="src"),

)