from database_operations import DatabaseModel

class Agency(DatabaseModel):
    def __init__(self, agency_id, agency_name, agency_address, agency_contact, agency_expertise):
        self.agency_id = agency_id
        self.agency_name = agency_name
        self.agency_address = agency_address
        self.agency_contact = agency_contact
        self.agency_expertise = agency_expertise

    @staticmethod
    def load_from_database(db_ops, agency_id):
        return super(Agency, Agency).load_from_database(db_ops, "Agency", agency_id)

    def save_to_database(self, db_ops):
        super(Agency, self).save_to_database(db_ops, "Agency", agency_id=self.agency_id, agency_name=self.agency_name, agency_address=self.agency_address, agency_contact=self.agency_contact, agency_expertise=self.agency_expertise)

    def update_in_database(self, db_ops):
        super(Agency, self).update_in_database(db_ops, "Agency", agency_id=self.agency_id,  agency_name=self.agency_name, agency_address=self.agency_address, agency_contact=self.agency_contact, agency_expertise=self.agency_expertise)

    def delete_from_database(self, db_ops):
        super(Agency, self).delete_from_database(db_ops, "Agency")

