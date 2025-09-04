import os
import time
from llama_index.core import VectorStoreIndex
from llama_index.vector_stores.deeplake import DeepLakeVectorStore
from llama_index.core.storage.storage_context import StorageContext
from llama_index.core.schema import Document


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