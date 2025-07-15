from unittest.mock import patch


from main import main


def test_main_json_empty(capsys):
    """Тестирует загрузку пустого JSON-файла."""
    inputs = ["1", "test.json", "EXECUTED", "нет", "нет", "нет"]
    with patch("builtins.input", side_effect=inputs):
        with patch("src.utils.load_transactions", return_value=[]):
            main()
    captured = capsys.readouterr()
    assert "Ошибка: Не удалось загрузить транзакции из test.json. Программа завершена." in captured.out
