from database_operations import db_ops
from database_operations import DatabaseModel

class Forensic(DatabaseModel):
    def __init__(self, analysis_id, analysis_type, analysis_result, analysis_date, case_id):
        self.analysis_id = analysis_id
        self.analysis_type = analysis_type
        self.analysis_result = analysis_result
        self.analysis_date = analysis_date
        self.case_id = case_id

    def get_data(self):
        return {
            "analysis_id": self.analysis_id,
            "analysis_type": self.analysis_type,
            "analysis_result": self.analysis_result,
            "analysis_date": self.analysis_date,
            "case_id": self.case_id
        }

    @staticmethod
    @staticmethod 
    def load_from_database(db_ops, forensic_id):
        return super(Forensic, Forensic).load_from_database(db_ops, "forensic", forensic_id)
    def save_to_database(self, db_ops):
        super().save_to_database(db_ops, "forensic", analysis_id=self.analysis_id, analysis_type=self.analysis_type, analysis_result=self.analysis_result, analysis_date=self.analysis_date, case_id=self.case_id)

    def update_in_database(self, db_ops):
        super().update_in_database(db_ops, "forensic", analysis_id=self.analysis_id, analysis_type=self.analysis_type, analysis_result=self.analysis_result, analysis_date=self.analysis_date, case_id=self.case_id)

    def delete_from_database(self, db_ops):
        super().delete_from_database(db_ops, "forensic")
