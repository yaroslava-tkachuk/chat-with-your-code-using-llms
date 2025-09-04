import os
import time
from typing import Any
from llama_index.core import VectorStoreIndex
from llama_index.vector_stores.deeplake import DeepLakeVectorStore
from llama_index.core.storage.storage_context import StorageContext
from llama_index.core.schema import Document
from llama_index.core.retrievers import VectorIndexRetriever
from llama_index.core.query_engine import BaseQueryEngine
from llama_index.llms.openai import OpenAI
from llama_index.core.query_engine import RetrieverQueryEngine
from llama_index.core import get_response_synthesizer
from llama_index.core.query_engine import RetrieverQueryEngine
from llama_index.core.postprocessor import SimilarityPostprocessor


class VectorStore:
    def __init__(self):
        self.__vector_store = DeepLakeVectorStore(
            dataset_path=os.getenv("DATASET_PATH"),
            overwrite=True,
            runtime={"tensor_db": True},
            read_only=False,
        )
    
    def upload_documents(self, documents: list[Document]) -> VectorStoreIndex:
        print("Uploading documents to vector store.")
        storage_context = StorageContext.from_defaults(vector_store=self.__vector_store)
        index = VectorStoreIndex.from_documents(documents, storage_context=storage_context)
        print("Documents uploaded successfully. Waiting for dataset to be ready.")
        time.sleep(10)
        return index

    def get_index(self) -> VectorStoreIndex:
        return VectorStoreIndex.from_vector_store(self.__vector_store)

    def get_query_engine(
        self,
        llm: Any = OpenAI(model="gpt-4o"),
        similarity_top_k: int = 4
    ) -> BaseQueryEngine:
        retriever = VectorIndexRetriever(
            index=self.get_index(),
            similarity_top_k=similarity_top_k
        )
        return RetrieverQueryEngine.from_args(
            retriever=retriever,
            llm=llm,
            response_mode="default",
            response_synthesizer=get_response_synthesizer(),
            node_postprocessors=[
                SimilarityPostprocessor(similarity_cutoff=0.7)]
        )