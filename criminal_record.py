from database_operations import DatabaseModel

class CriminalRecord(DatabaseModel):
    def __init__(self, criminalRecord_id, criminal_name, criminal_contact, criminal_address, case_info_id, article_id, criminal_age, criminal_gender, criminal_status):
        self.criminalRecord_id = criminalRecord_id
        self.criminal_name = criminal_name
        self.criminal_contact = criminal_contact
        self.criminal_address = criminal_address
        self.case_info_id = case_info_id
        self.article_id = article_id
        self.criminal_age = criminal_age
        self.criminal_gender = criminal_gender
        self.criminal_status = criminal_status

    @staticmethod
    def load_from_database(db_ops, criminalRecord_id):
        return super(CriminalRecord, CriminalRecord).load_from_database(db_ops, "CriminalRecord", criminalRecord_id)

    def save_to_database(self, db_ops):
        super(CriminalRecord, self).save_to_database(db_ops, "CriminalRecord", criminalRecord_id=self.criminalRecord_id, criminal_name=self.criminal_name, criminal_contact=self.criminal_contact, criminal_address=self.criminal_address, case_info_id=self.case_info_id, article_id=self.article_id, criminal_age=self.criminal_age, criminal_gender=self.criminal_gender, criminal_status=self.criminal_status)

    def update_in_database(self, db_ops):
        super(CriminalRecord, self).update_in_database(db_ops, "CriminalRecord", criminalRecord_id=self.criminalRecord_id, criminal_name=self.criminal_name, criminal_contact=self.criminal_contact, criminal_address=self.criminal_address, case_info_id=self.case_info_id, article_id=self.article_id, criminal_age=self.criminal_age, criminal_gender=self.criminal_gender, criminal_status=self.criminal_status)

    def delete_from_database(self, db_ops):
        super(CriminalRecord, self).delete_from_database(db_ops, "CriminalRecord", criminalRecord_id=self.criminalRecord_id)
