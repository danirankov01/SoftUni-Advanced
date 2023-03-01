from project_document_management.category import Category
from project_document_management.document import Document
from project_document_management.topic import Topic


class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category: Category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id, new_name):
        for cat in self.categories:
            if cat.id == category_id:
                cat.name = new_name

    def edit_topic(self, topic_id, new_topic, new_storage_folder):
        for top in self.topics:
            if top.id == topic_id:
                top.topic = new_topic
                top.storage_folder = new_storage_folder

    def edit_document(self, document_id, new_file_name):
        for doc in self.documents:
            if doc.id == document_id:
                doc.file_name = new_file_name

    def delete_category(self, category_id):
        for cat in self.categories:
            if cat.id == category_id:
                del cat

    def delete_topic(self, topic_id):
        for top in self.topics:
            if top.id == topic_id:
                del top

    def delete_document(self, document_id):
        for doc in self.documents:
            if doc.id == document_id:
                del doc

    def get_document(self, document_id):
        for doc in self.documents:
            if doc.id == document_id:
                return doc

    def __repr__(self):
        result = ""

        for doc in self.documents:
            result += f"{str(doc)}\n"

        return result










