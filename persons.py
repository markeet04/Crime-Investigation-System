import mysql.connector
from database_operations import db_ops,DatabaseModel

class Person(DatabaseModel):
    def __init__(self, name, age, gender, contact):
        self.name = name
        self.age = age
        self.gender = gender
        self.contact = contact

    def get_info(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}, Contact: {self.contact}"

# Judges inherit from Person and have additional attributes
class Judges(Person):
    def __init__(self, judge_id, name, age, gender, court_id, address, case_info_id,contact):
        super().__init__(name, age, gender,contact)
        self.judge_id = judge_id
        self.court_id = court_id
        self.address = address
        self.case_info_id = case_info_id

    @staticmethod
    def load_from_database(db_ops, judge_id=None):
        return DatabaseModel.load_from_database(db_ops, 'judges', judge_id)

    def save_to_database(self, db_ops):
        return DatabaseModel.save_to_database(self, db_ops, 'judges', judge_id=self.judge_id, court_id=self.court_id, address=self.address, case_info_id=self.case_info_id)

    def update_in_database(self, db_ops):
        return DatabaseModel.update_in_database(self, db_ops, 'judges', judge_id=self.judge_id, court_id=self.court_id, address=self.address, case_info_id=self.case_info_id)

    def delete_from_database(self, db_ops):
        return DatabaseModel.delete_from_database(self, db_ops, 'judges')

# Victim class inherits from Person with additional status attribute
class Victim(Person):
    def __init__(self, victim_id, name, age, gender, contact, status, address, blood_group, case_info_id):
        super().__init__(name, age, gender, contact)
        self.victim_id = victim_id
        self.status = status
        self.address = address
        self.blood_group = blood_group
        self.case_info_id = case_info_id
    @staticmethod
    def load_from_database(db_ops, victim_id=None):
        return DatabaseModel.load_from_database(db_ops, 'victim', victim_id)

    def save_to_database(self, db_ops):
        return DatabaseModel.save_to_database(self, db_ops, 'victim', victim_id=self.victim_id, status=self.status, address=self.address, blood_group=self.blood_group, case_info_id=self.case_info_id)

    def update_in_database(self, db_ops):
        return DatabaseModel.update_in_database(self, db_ops, 'victim', victim_id=self.victim_id, status=self.status, address=self.address, blood_group=self.blood_group, case_info_id=self.case_info_id)

    def delete_from_database(self, db_ops):
        return DatabaseModel.delete_from_database(self, db_ops, 'victim')

# Witness class inherits from Person with additional statement_type and statement attributes
class Witness(Person):
    def __init__(self, witness_id, name, age, gender, contact, statement, address, case_info_id):
        super().__init__(name, age, gender, contact)
        self.witness_id = witness_id
        self.statement = statement
        self.address = address
        self.case_info_id = case_info_id

    @staticmethod
    def load_from_database(db_ops, witness_id=None):
        return DatabaseModel.load_from_database(db_ops, 'witness', witness_id)

    def save_to_database(self, db_ops):
        return DatabaseModel.save_to_database(self, db_ops, 'witness', witness_id=self.witness_id,  address=self.address, case_info_id=self.case_info_id)

    def update_in_database(self, db_ops):
        return DatabaseModel.update_in_database(self, db_ops, 'witness', witness_id=self.witness_id,  address=self.address,  case_info_id=self.case_info_id)

    def delete_from_database(self, db_ops):
        return DatabaseModel.delete_from_database(self, db_ops, 'witness')    

# Lawyer class inherits from Person with additional lawyer-specific attributes
class Lawyer(Person):
    def __init__(self, lawyer_id, lawyer_license_no, name, gender, address, contact, fee, authorized_court, total_cases, win_loss_ratio, case_info_id,age):
        super().__init__(name, age, gender, contact)
        self.lawyer_id = lawyer_id
        self.lawyer_license_no = lawyer_license_no
        self.address = address
        self.fee = fee
        self.authorized_court = authorized_court
        self.total_cases = total_cases
        self.win_loss_ratio = win_loss_ratio
        self.case_info_id = case_info_id

    @staticmethod
    def load_from_database(db_ops, lawyer_id=None):
        return DatabaseModel.load_from_database(db_ops, 'lawyer', lawyer_id)

    def save_to_database(self, db_ops):
        fields = {
            'lawyer_id': self.lawyer_id,
            'lawyer_license_no': self.lawyer_license_no,
            'lawyer_name': self.name,
            'lawyer_age': self.age,
            'lawyer_gender': self.gender,
            'lawyer_address': self.address,
            'lawyer_contact': self.contact,
            'lawyer_fee': self.fee,
            'authorized_court': self.authorized_court,
            'lawyer_total_cases': self.total_cases,
            'lawyer_win_loss_ratio': self.win_loss_ratio,
            'case_info_id': self.case_info_id
        }
        return DatabaseModel.save_to_database(self, db_ops, 'lawyer', **fields)

    def update_in_database(self, db_ops):
        fields = {
            'lawyer_license_no': self.lawyer_license_no,
            'lawyer_name': self.name,
            'lawyer_age': self.age,
            'lawyer_gender': self.gender,
            'lawyer_address': self.address,
            'lawyer_contact': self.contact,
            'lawyer_fee': self.fee,
            'authorized_court': self.authorized_court,
            'lawyer_total_cases': self.total_cases,
            'lawyer_win_loss_ratio': self.win_loss_ratio,
            'case_info_id': self.case_info_id
        }
        return DatabaseModel.update_in_database(self, db_ops, 'lawyer', lawyer_id=self.lawyer_id, **fields)

    def delete_from_database(self, db_ops):
        return DatabaseModel.delete_from_database(self, db_ops, 'lawyer', lawyer_id=self.lawyer_id)

# InvestigatingOfficer class inherits from Person with additional officer-specific attributes
class InvestigatingOfficer(Person):
    def __init__(self, officer_id, officer_batch_no, name, age, gender, contact, address, rank,position,  department, agency_id, case_info_id):
        super().__init__(name, age, gender, contact)
        self.officer_id = officer_id
        self.officer_batch_no = officer_batch_no
        self.address = address
        self.rank = rank
        self.position=position
        self.department = department
        self.agency_id = agency_id
        self.case_info_id = case_info_id
    @staticmethod
    def load_from_database(db_ops, officer_id=None):
        return DatabaseModel.load_from_database(db_ops, 'officer', officer_id)

    def save_to_database(self, db_ops):
        return DatabaseModel.save_to_database(self, db_ops, 'officer', officer_id=self.officer_id, address=self.address,position=self.position ,case_info_id=self.case_info_id)

    def update_in_database(self, db_ops):
        return DatabaseModel.update_in_database(self, db_ops, 'officer', officer_id=self.officer_id, address=self.address,position=self.position,case_info_id=self.case_info_id)

    def delete_from_database(self, db_ops):
        return DatabaseModel.delete_from_database(self, db_ops, 'officer')

# Suspect class inherits from Person with additional suspect-specific attributes
from database_operations import DatabaseModel

class Suspect:
    def __init__(self, suspect_id, case_info_id, evidence_id, name, age, gender, contact, address, statement, past_record):
        self.suspect_id = suspect_id
        self.case_info_id = case_info_id
        self.evidence_id = evidence_id
        self.name = name
        self.age = age
        self.gender = gender
        self.contact = contact
        self.address = address
        self.statement = statement
        self.past_record = past_record

    @staticmethod
    def load_from_database(db_ops, suspect_id=None):
        return DatabaseModel.load_from_database(db_ops, 'suspects', suspect_id)

    def save_to_database(self, db_ops):
        return DatabaseModel.save_to_database(
            self, db_ops, 'suspects',
            suspect_id=self.suspect_id,
            case_info_id=self.case_info_id,
            evidence_id=self.evidence_id,
            name=self.name,
            age=self.age,
            gender=self.gender,
            contact=self.contact,
            address=self.address,
            statement=self.statement,
            past_record=self.past_record
        )

    def update_in_database(self, db_ops):
        return DatabaseModel.update_in_database(
            self, db_ops, 'suspects',
            suspect_id=self.suspect_id,
            case_info_id=self.case_info_id,
            evidence_id=self.evidence_id,
            name=self.name,
            age=self.age,
            gender=self.gender,
            contact=self.contact,
            address=self.address,
            statement=self.statement,
            past_record=self.past_record
        )

    def delete_from_database(self, db_ops):
        return DatabaseModel.delete_from_database(self, db_ops, 'suspects', self.suspect_id)
