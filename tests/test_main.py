import pytest
from src.main import read_operations, filter_and_sort_operations, format_operation
import json

@pytest.fixture
def sample_operations():
    with open('test/test_operations.json', 'r', encoding='utf-8') as file:
        operations = json.load(file)
    return operations

def test_read_operations():
    operations = read_operations('test_operations.json')
    assert len(operations) > 0

def test_filter_and_sort_operations(sample_operations):
    filtered_operations = filter_and_sort_operations(sample_operations)
    assert len(filtered_operations) == 5

def test_format_operation():
    operation = {
        'date': '2022-05-10T10:00:00.000',
        'description': 'Test transfer',
        'from': 'Счет 123456',
        'to': 'Счет 789012',
        'operationAmount': {'amount': 100, 'currency': {'name': 'USD'}}
    }
    formatted_operation = format_operation(operation)
    assert formatted_operation.startswith('10.05.2022 Test transfer')