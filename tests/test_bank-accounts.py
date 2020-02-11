from bank_accounts import finish_month, deposit, withdraw

def test_finish_month():
    result = finish_month(1000)
    assert result == 960