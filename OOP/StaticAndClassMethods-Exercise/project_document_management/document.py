from project_document_management.category import Category
from project_document_management.topic import Topic


class Document:
    def __init__(self, id_number, category_id, topic_id, file_name):
        self.id = id_number
        self.category_id = category_id
        self.topic_id = topic_id
        self.file_name = file_name
        self.tags = []

    @classmethod
    def from_instance(cls, id, category: Category, topic: Topic, file_name):
        return cls(id, category.id, topic.id, file_name)

    def add_tag(self, tag_content):
        if tag_content not in self.tags:
            self.tags.append(tag_content)

    def remove_tag(self, tag_content):
        if tag_content in self.tags:
            self.tags.remove(tag_content)

    def edit(self, file_name):
        self.file_name = file_name

    def __repr__(self):
        return f"Document {self.id}: {self.file_name}; category " \
               f"{self.category_id}, topic {self.topic_id}, tags: {', '.join(self.tags)}"
