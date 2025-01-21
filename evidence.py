from database_operations import DatabaseModel
class Evidence(DatabaseModel):
    def __init__(self, evidence_id, evidence_type, evidence_name, evidence_found_location, case_info_id):
        self.evidence_id = evidence_id
        self.evidence_type = evidence_type
        self.evidence_name = evidence_name
        self.evidence_found_location = evidence_found_location
        self.case_info_id = case_info_id

    def save_to_database(self, db_ops):
        data = {
            "evidence_type": self.evidence_type,
            "evidence_name": self.evidence_name,
            "evidence_found_location": self.evidence_found_location,
            "case_info_id": self.case_info_id
        }
        return db_ops.create("Evidence", **data)

    @staticmethod
    def load_from_database(db_ops, evidence_id):
        success, result = db_ops.read("Evidence", evidence_id)
        if success and result:
            return True, Evidence(*result)
        return success, None

    def update_in_database(self, db_ops):
        data = {
            "evidence_type": self.evidence_type,
            "evidence_name": self.evidence_name,
            "evidence_found_location": self.evidence_found_location,
            "case_info_id": self.case_info_id
        }
        return db_ops.update("Evidence", self.evidence_id, **data)

    @staticmethod
    def delete_from_database(db_ops, evidence_id):
        return db_ops.delete("Evidence", evidence_id)
