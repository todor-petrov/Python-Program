from project.category import Category
from project.document import Document
from project.topic import Topic


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

    def edit_category(self, category_id: int, new_name: str):
        category = next((c for c in self.categories if c.id == category_id), None)
        category.name = new_name

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        topic = next((t for t in self.topics if t.id == topic_id), None)
        topic.edit(new_topic, new_storage_folder)

    def edit_document(self, document_id: int, new_file_name: str):
        document = next((d for d in self.documents if d.id == document_id), None)
        document.edit(new_file_name)

    def delete_category(self, category_id):
        category = next((c for c in self.categories if c.id == category_id), None)
        self.categories.remove(category)

    def delete_topic(self, topic_id):
        topic = next((t for t in self.topics if t.id == topic_id), None)
        self.topics.remove(topic)

    def delete_document(self, document_id):
        document = next((d for d in self.documents if d.id == document_id), None)
        self.documents.remove(document)

    def get_document(self, document_id):
        document = next((d for d in self.documents if d.id == document_id), None)
        return document

    def __repr__(self):
        return '\n'.join([str(d) for d in self.documents])
#
#
# c1 = Category(1, "work")
# t1 = Topic(1, "daily tasks", "C:\\work_documents")
# d1 = Document(1, 1, 1, "finilize project")
# d1.add_tag("urgent")
# d1.add_tag("work")
# storage = Storage()
# storage.add_category(c1)
# storage.add_topic(t1)
# storage.add_document(d1)
# print(c1)
# print(t1)
# print(storage.get_document(1))
# print(storage)
