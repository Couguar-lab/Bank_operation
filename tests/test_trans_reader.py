from unittest.mock import mock_open, patch

from src.trans_reader import read_trans_from_csv, read_trans_from_xls


def test_read_trans_from_csv_success(sample_csv_data):
    """Тестирование успешной загрузки из csv файла"""
    with patch("pathlib.Path.exists", return_value=True):
        with patch("builtins.open", mock_open(read_data=sample_csv_data)):
            result = read_trans_from_csv("test.csv")
            assert len(result) == 2
            assert result[0]["id"] == "650703"
            assert result[0]["state"] == "EXECUTED"
            assert result[0]["date"] == "2023-09-05T11:30:32Z"
            assert result[0]["amount"] == "16210"
            assert result[0]["currency_name"] == "Sol"
            assert result[0]["currency_code"] == "PEN"
            assert result[0]["from"] == "Счет 58803664561298323391"
            assert result[0]["to"] == "Счет 39745660563456619397"
            assert result[0]["description"] == "Перевод организации"


def test_read_trans_from_xls_success(sample_excel_data):
    """Тестирование успешной загрузки из excel файла"""
    with patch("pathlib.Path.exists", return_value=True):
        with patch("pandas.read_excel", return_value=sample_excel_data):
            result = read_trans_from_xls("test.xlsx")
            assert len(result) == 2
            assert result[0]["id"] == "650703"
            assert result[0]["state"] == "EXECUTED"
            assert result[0]["date"] == "2023-09-05T11:30:32Z"
            assert result[0]["amount"] == 16210
            assert result[0]["currency_name"] == "Sol"
            assert result[0]["currency_code"] == "PEN"
            assert result[0]["from"] == "Счет 58803664561298323391"
            assert result[0]["to"] == "Счет 39745660563456619397"
            assert result[0]["description"] == "Перевод организации"
