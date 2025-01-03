import json

class FileManager:
    def __init__(self, path_db: str):
        self.db = path_db

    def to_load(self):
        with open(self.db, 'r', encoding='utf-8') as f:
            db = json.load(f)
        return db

    def insert(self, dict_content: dict, key: str):
        db_content = self.to_load()
        id = str(len(db_content[key]) + 1)
        db_content[str(key)].update({id: dict_content})

        with open(self.db, 'w', encoding='utf-8') as f:
            json.dump(db_content, f, indent=4, ensure_ascii=False)