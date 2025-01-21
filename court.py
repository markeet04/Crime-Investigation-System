from database_operations import DatabaseModel

class Court(DatabaseModel):
    def __init__(self, court_id, court_name, court_location, court_level):
        self.court_id = court_id
        self.court_name = court_name
        self.court_location = court_location
        self.court_level = court_level
    
    @staticmethod
    def load_from_database(db_ops, court_id):
        return super(Court, Court).load_from_database(db_ops, "Court", court_id)

    def save_to_database(self, db_ops):
        super(Court, self).save_to_database(db_ops, "Court", court_id=self.court_id, court_name=self.court_name, court_location=self.court_location, court_level=self.court_level)

    def update_in_database(self, db_ops):
        super(Court, self).update_in_database(db_ops, "Court", court_id=self.court_id, court_name=self.court_name, court_location=self.court_location, court_level=self.court_level)

    def delete_from_database(self, db_ops):
        super(Court, self).delete_from_database(db_ops, "Court")
