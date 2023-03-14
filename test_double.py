# test_my_module.py

from unittest.mock import Mock
from my_module import MyModule

def test_get_data():
    my_module = MyModule()

    # Create a mock object to replace the real implementation
    my_module._connect_to_database = Mock(return_value="mock data")

    # Call the method and assert that it returns the mock data
    assert my_module.get_data() == "mock data"
