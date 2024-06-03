import json
from datetime import datetime


def read_operations(file_path='operations.json'):
    with open(file_path, 'r', encoding='utf-8') as file:
        operations = json.load(file)
    return operations


def filter_and_sort_operations(operations):
    executed_operations = [op for op in operations if op.get('state') == 'EXECUTED' and op]
    sorted_operations = sorted(executed_operations, key=lambda x: x['date'], reverse=True)[:5]
    return sorted_operations


def mask_card_number(card_number):
    return f"{card_number[:6]} {'*' * 6} {card_number[-4:]}"


def mask(source):
    if source is None:
        return ''

    def mask_account_number():
        return f"**{number[-4:]}"

    def mask_card_number():
        return f"{number[:4]} {number[4:6]}**  {'*' * 4} {number[-4:]}"

    *name, number = source.split()
    text = 'Счет'
    if ' '.join(name) == text:
        return text + ' ' + mask_account_number()
    else:
        return ' '.join(name) + ' ' + mask_card_number()


def format_operation(operation):
    date = datetime.fromisoformat(operation.get('date', "")).strftime('%d.%m.%Y')
    description = operation.get('description', "")
    from_account = mask(operation.get('from'))
    to_account = mask(operation.get('to', ""))
    amount = operation['operationAmount']['amount']
    currency = operation['operationAmount']['currency']['name']
    return f"{date} {description}\n{from_account} -> {to_account}\n{amount} {currency}\n"


def main():
    operations = read_operations()
    latest_operations = filter_and_sort_operations(operations)

    for op in latest_operations:
        print(format_operation(op))

if __name__ == '__main__':
    main()

