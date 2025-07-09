import setuptools

__version__ = "0.0.0"

REPO_NAME = "shres-mlops-project"
AUTHOR_USER_NAME = "ShreCodes2809"
SRC_REPO = "mlops_proj"
AUTHOR_EMAIL = "shrecodes9901@gmail.com"

setuptools.setup(
    name = SRC_REPO,
    version = __version__,
    author = AUTHOR_USER_NAME,
    author_email = AUTHOR_EMAIL,
    description = "A small python package for this MLOPs project based learning",
    url = f"https://github.com/{AUTHOR_USER_NAME}/{SRC_REPO}",
    project_urls = {
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{SRC_REPO}/issues"
    },
    package_dir = {"": "src"},
    packages = setuptools.find_packages(where="src")
)