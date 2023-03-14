# my_module.py

class MyModule:
    def get_data(self):
        # Connect to a database and retrieve some data
        # This implementation will not work in a testing environment
        # because it requires a live database connection
        data = self._connect_to_database()
        return data

    def _connect_to_database(self):
        # Connect to a real database and return the data
        pass
