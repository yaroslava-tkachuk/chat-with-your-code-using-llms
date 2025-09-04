import textwrap
import logging
from llama_index.core.query_engine import BaseQueryEngine
from llama_index.llms.openai import OpenAI
from app.github_repo_loader import GitHubRepoLoader
from app.vector_store import VectorStore

logging.basicConfig(level=logging.INFO)


def chat_with_code() -> None:
    documents = GitHubRepoLoader().fetch_repository_as_documents()
    vector_store = VectorStore()
    vector_store.upload_documents(documents)
    query_engine = vector_store.get_query_engine(llm=OpenAI(model="gpt-4o"))
    __test_rag_with_vector_search(query_engine)
    __process_user_queries(query_engine)


def __test_rag_with_vector_search(query_engine: BaseQueryEngine) -> None:
    test_question = "What is the repository about?"
    print(f"Test question: {test_question}")
    print("=" * 50)
    answer = query_engine.query(test_question)
    print(f"Answer: {textwrap.fill(str(answer), 100)} \n")


def __process_user_queries(query_engine: BaseQueryEngine) -> None:
    while True:
        user_question = input("Please enter your question (or type 'exit' to quit): ")
        if user_question.lower() == "exit":
            print("Exiting, thanks for chatting!")
            break

        print(f"Your question: {user_question}")
        print("=" * 50)

        answer = query_engine.query(user_question)
        print(f"Answer: {textwrap.fill(str(answer), 100)} \n")


if __name__ == "__main__":
    chat_with_code()