import os
import re
from typing import Optional
from llama_index.core.schema import Document
from llama_index.readers.github import GithubClient, GithubRepositoryReader


class GitHubRepoLoader:
    PATTERN = re.compile(r"https://github\.com/([^/]+)/([^/]+)")
    
    def __init__(self):
        self.client = GithubClient(os.getenv("GITHUB_TOKEN"))

    @staticmethod
    def parse_github_url(url: str) -> tuple[Optional[str], Optional[str]]:
        url_stripped = url.strip()
        match = GitHubRepoLoader.PATTERN.match(url_stripped)
        return match.groups() if match else (None, None)

    def fetch_repository_as_documents(self) -> list[Document]:
        github_repo_prompt_msg = "Please enter the GitHub repository URL: "
        while True:
            github_url = input(github_repo_prompt_msg)
            owner, repo = self.parse_github_url(github_url)
            if not owner or not repo:
                print("Invalid GitHub URL. Please try again.")
            else:
                loader = GithubRepositoryReader(
                    self.client,
                    owner=owner,
                    repo=repo,
                    filter_file_extensions=(
                        [".py", ".ipynb", ".js", ".ts", ".md"],
                        GithubRepositoryReader.FilterType.INCLUDE,
                    ),
                    verbose=False,
                    concurrent_requests=5,
                )
                print(f"Loading {repo} repository by {owner}")
                documents = loader.load_data(branch="main")
                print("Documents uploaded:")
                for document in documents:
                    print(document.metadata)
                return documents
                