from typing import List, Dict, Any

# Функция сортировки по статусу операции
def filter_by_state(transactions: List[Dict[str, Any]], state: str = 'EXECUTED') -> List[Dict[str, Any]]:
    '''Функция отсортировывает и возвращает транзакции только со статусом EXECUTED'''
    return [transaction for transaction in transactions if transaction.get('state') == state]
# Функция сортировки по дате
def sort_by_date(transactions: List[Dict[str, Any]], descending: bool = True) -> List[Dict[str, Any]]:
    '''Функция сортирует и возвращает список транзакций по дате в обратном порядке. Первыми идут более свежие операции'''
    def get_date(transaction: Dict[str, Any]) -> str:
        return transaction.get('date', '')

    return sorted(transactions, key=get_date, reverse=descending)