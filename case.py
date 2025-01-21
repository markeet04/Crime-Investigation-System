from database_operations import db_ops

class Case_info:
    def __init__(self, case_info_id,fir_id, case_name, case_type, case_status, case_opened, case_closed, case_remarks, charges_filed):
        self.case_info_id = case_info_id
        self.case_name = case_name
        self.case_type = case_type
        self.case_status = case_status
        self.case_opened = case_opened
        self.case_closed = case_closed
        self.case_remarks = case_remarks
        self.charges_filed = charges_filed
        self.firid=fir_id
        self.investigating_officer = None
        self.lawyer = None
        self.judges = []
        self.articles = []
        self.victim = None
        self.witnesses = []
        self.suspects = []
        self.evidences = []

    def set_investigating_officer(self, officer):
        self.investigating_officer = officer

    def set_lawyer(self, lawyer):
        self.lawyer = lawyer

    def add_judge(self, judge):
        self.judges.append(judge)

    def add_article(self, article):
        self.articles.append(article)

    def set_victim(self, victim):
        self.victim = victim

    def add_witness(self, witness):
        self.witnesses.append(witness)

    def add_suspect(self, suspect):
        self.suspects.append(suspect)

    def add_evidence(self, evidence):
        self.evidences.append(evidence)

    def save_to_database(self, db_ops):
        data = vars(self)
        success, message = db_ops.create("Case_info", **data)
        print(message if success else "Error saving CaseInfo record:", message)

    @staticmethod
    def load_from_database(db_ops, case_id):
        success, result = db_ops.read("Case_info", case_id)
        if success:
            return Case_info(*result)
        print("Error loading CaseInfo record:", result)
        return None

    def update_in_database(self, db_ops):
        data = vars(self)
        success, message = db_ops.update("Case_Info", self.case_id, **data)
        print(message if success else "Error updating CaseInfo record:", message)

    def delete_from_database(self, db_ops):
        success, message = db_ops.delete("Case_info", self.case_id)
        print(message if success else "Error deleting CaseInfo record:", message)
