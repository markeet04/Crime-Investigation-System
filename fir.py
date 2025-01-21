from database_operations import DatabaseModel, db_ops

class FIR(DatabaseModel):
    def __init__(self, fir_id, f_name, f_age, f_gender, f_address, f_contact, f_relation_with_victim, crime_id):
        self.fir_id = fir_id
        self.f_name = f_name
        self.f_age = f_age
        self.f_gender = f_gender
        self.f_address = f_address
        self.f_contact = f_contact
        self.f_relation_with_victim = f_relation_with_victim
        self.crime_id = crime_id

    @staticmethod
    def load_from_database(db_ops, fir_id):
        try:
            print(f"Attempting to retrieve FIR data for fir_id: {fir_id}")
            success, result = super(FIR, FIR).load_from_database(db_ops, "fir", fir_id)
            if success:
                print("Successfully retrieved FIR data.")
                return result
            else:
                print("Failed to retrieve FIR data.")
                return None
        except Exception as e:
            print(f"Error retrieving FIR data: {e}")
            return None

    def save_to_database(self, db_ops):
        try:
            print(f"Attempting to save FIR data: {self.__dict__}")
            super(FIR, self).save_to_database(db_ops, "fir", fir_id=self.fir_id, f_name=self.f_name, f_age=self.f_age, f_gender=self.f_gender, f_address=self.f_address, f_contact=self.f_contact, f_relation_with_victim=self.f_relation_with_victim, crime_id=self.crime_id)
            print("Successfully saved FIR data.")
        except Exception as e:
            print(f"Error saving FIR data: {e}")

    def update_in_database(self, db_ops):
        try:
            print(f"Attempting to update FIR data: {self.__dict__}")
            super(FIR, self).update_in_database(db_ops, "fir", fir_id=self.fir_id, f_name=self.f_name, f_age=self.f_age, f_gender=self.f_gender, f_address=self.f_address, f_contact=self.f_contact, f_relation_with_victim=self.f_relation_with_victim, crime_id=self.crime_id)
            print("Successfully updated FIR data.")
        except Exception as e:
            print(f"Error updating FIR data: {e}")

    def delete_from_database(self, db_ops):
        try:
            print(f"Attempting to delete FIR data for fir_id: {self.fir_id}")
            super(FIR, self).delete_from_database(db_ops, "fir")
            print("Successfully deleted FIR data.")
        except Exception as e:
            print(f"Error deleting FIR data: {e}")
