from unittest.mock import patch
from utils import get_currency_rates


@patch("requests.get")
def test_get_currency_rates(mock_get):
    mock_get.return_value.json.return_value = {"rates": {"RUB": 100}, "test": "test"}
    assert get_currency_rates() == [{'currency': 'USD', 'rate': 100}, {'currency': 'EUR', 'rate': 100}]
    mock_get.assert_called()
