from src.masks import mask_card,mask_account


def test_mask_card():
    assert mask_card('7000792289606361') == '7000 79** **** 6361'

def test_mask_account():
    assert mask_account('73654108430135874305') == '**4305'