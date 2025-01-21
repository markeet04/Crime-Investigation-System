from database_operations import DatabaseModel

class Crime(DatabaseModel):
    def __init__(self, crime_id, crime_location, crime_datetime, crime_type, crime_description):
        self.crime_id = crime_id
        self.crime_location = crime_location
        self.crime_datetime = crime_datetime
        self.crime_type = crime_type
        self.crime_description = crime_description

    @staticmethod
    def load_from_database(db_ops, crime_id):
        return super(Crime, Crime).load_from_database(db_ops, "Crime", crime_id)

    def save_to_database(self, db_ops):
        super(Crime, self).save_to_database(db_ops, "Crime", crime_id=self.crime_id, crime_location=self.crime_location, crime_datetime=self.crime_datetime, crime_type=self.crime_type, crime_description=self.crime_description)

    def update_in_database(self, db_ops):
        super(Crime, self).update_in_database(db_ops, "Crime", crime_id=self.crime_id, crime_location=self.crime_location, crime_datetime=self.crime_datetime, crime_type=self.crime_type, crime_description=self.crime_description)

    def delete_from_database(self, db_ops):
        super(Crime, self).delete_from_database(db_ops, "Crime")
