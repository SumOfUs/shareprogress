from shareprogress import services
from shareprogress.lib.share_progress_request import shareProgressRequest
from mock_functions import mockFunctions
from payload_generators import *

# DELETE BUTTON EMAIL

def test_delete_button_email(monkeypatch):
    """Monkeypatching
    To avoid sending an actual request to Shareprogress we use monkeypatch
    from pytest to replace the 'delete_button' function (from the
    shareProgressRequest module) with the 'delete_button_email' function
    (from the mock_functions module).
    """
    monkeypatch.setattr(shareProgressRequest, 'delete_button',
        mockFunctions().delete_button_email)

    payload = deleteButton().payload('email')
    expected_result = {
        'button_template': 'sp_em_small',
        'page_title': 'My Email button name',
        'is_active': True,
        'share_button_html': "<div class='sp_11863 sp_em_small' >" +
            "</div>",
        'id': 11863,
        'page_url': 'http://sumofus.org/'
    }

    assert services.delete(payload, 'button') == expected_result

# DELETE BUTTON TWITTER

def test_delete_button_twitter(monkeypatch):
    """Monkeypatching
    To avoid sending an actual request to Shareprogress we use monkeypatch
    from pytest to replace the 'delete_button' function (from the
    shareProgressRequest module) with the 'delete_button_twitter' function
    (from the mock_functions module).
    """
    monkeypatch.setattr(shareProgressRequest, 'delete_button',
        mockFunctions().delete_button_twitter)

    payload = deleteButton().payload('twitter')
    expected_result = {
        'button_template': 'sp_tw_large',
        'page_title': 'My Twitter NEW button name',
        'is_active': True,
        'share_button_html': "<div class='sp_11864 sp_tw_large' >" +
            "</div>",
        'id': 11864,
        'page_url': 'http://sumofus.org/new-url'
    }

    assert services.delete(payload, 'button') == expected_result

# DELETE BUTTON FACEBOOK

def test_delete_button_facebook(monkeypatch):
    """Monkeypatching
    To avoid sending an actual request to Shareprogress we use monkeypatch
    from pytest to replace the 'delete_button' function (from the
    shareProgressRequest module) with the 'delete_button_facebook' function
    (from the mock_functions module).
    """
    monkeypatch.setattr(shareProgressRequest, 'delete_button',
        mockFunctions().delete_button_facebook)

    payload = deleteButton().payload('facebook')
    expected_result = {
        'button_template': 'sp_fb_large',
        'page_title': 'My NEW Facebook button name',
        'is_active': True,
        'share_button_html': "<div class='sp_11865 sp_fb_large' >" +
            "</div>",
        'id': 11865,
        'page_url': 'http://sumofus.org/new-url'
    }

    assert services.delete(payload, 'button') == expected_result
