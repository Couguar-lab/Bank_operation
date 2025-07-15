from src.trans_dictinary import process_bank_operations, process_bank_search


def test_process_bank_search_found(sample_excel_data):
    """Тестирует поиск транзакций по строке в описании."""
    data = sample_excel_data.to_dict("records")  # Конвертация DataFrame в список словарей
    result = process_bank_search(data, "Перевод")
    assert len(result) == 2
    assert result[0]["description"] == "Перевод организации"
    assert result[1]["description"] == "Перевод с карты на карту"


def test_process_bank_search_not_found(sample_excel_data):
    """Тестирует поиск, когда строка не найдена."""
    data = sample_excel_data.to_dict("records")
    result = process_bank_search(data, "Покупка")
    assert len(result) == 0


def test_process_bank_search_empty_string(sample_excel_data):
    """Тестирует поиск с пустой строкой."""
    data = sample_excel_data.to_dict("records")
    result = process_bank_search(data, "")
    assert len(result) == len(data)
    assert result == data


def test_process_bank_search_case_insensitive(sample_excel_data):
    """Тестирует поиск без учёта регистра."""
    data = sample_excel_data.to_dict("records")
    result = process_bank_search(data, "перевод")
    assert len(result) == 2


def test_process_bank_operations(sample_excel_data):
    """Тестирует подсчёт операций по категориям."""
    data = sample_excel_data.to_dict("records")
    categories = ["Перевод", "Открытие вклада"]
    result = process_bank_operations(data, categories)
    assert result == {"Перевод": 2, "Открытие вклада": 0}


def test_process_bank_operations_empty_categories(sample_excel_data):
    """Тестирует подсчёт с пустым списком категорий."""
    data = sample_excel_data.to_dict("records")
    result = process_bank_operations(data, [])
    assert result == {}
