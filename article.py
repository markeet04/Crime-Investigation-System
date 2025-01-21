from database_operations import DatabaseModel

class Article(DatabaseModel):
    def __init__(self, article_number, article_name, punishment_type):
        self.article_number = article_number
        self.article_name = article_name
        self.punishment_type = punishment_type

    @staticmethod
    def load_from_database(db_ops, article_id):
        return super(Article, Article).load_from_database(db_ops, "Article", article_id)

    def save_to_database(self, db_ops):
        super(Article, self).save_to_database(db_ops, "Article",  article_number=self.article_number, article_name=self.article_name, punishment_type=self.punishment_type)

    def update_in_database(self, db_ops):
        super(Article, self).update_in_database(db_ops, "Article", article_number=self.article_number, article_name=self.article_name, punishment_type=self.punishment_type)

    def delete_from_database(self, db_ops):
        super(Article, self).delete_from_database(db_ops, "Article")
