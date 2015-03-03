from shareprogress import services
from shareprogress.lib.share_progress_request import shareProgressRequest
from mock_functions import mockFunctions
from payload_generators import *

# EMAIL BUTTON VALIDATION

def test_update_email_button(monkeypatch):
    """Monkeypatching
    To avoid sending an actual request to Shareprogress we use monkeypatch
    from pytest to replace the 'create_button' and 'read_button' function
    (from the shareProgressRequest module) with the 'update_button_email_test'
    and 'read_email_button_test' function (from the mock_functions module).
    """
    monkeypatch.setattr(shareProgressRequest, 'create_button',
        mockFunctions().update_button_email_test)

    monkeypatch.setattr(shareProgressRequest, 'read_button',
        mockFunctions().read_email_button_test)

    payload = updateButton().update_button_payload('email')
    expected_result = {
        'button_template': 'sp_em_small',
        'found_snippet': False,
        'page_title': 'My Email NEW button name',
        'advanced_options': {
            'id_pass': {
                'id': 'id',
                'passed': 'referrer_id'},
            'automatic_traffic_routing': True,
            'customize_params': {
                'param': 'param_to_use',
                'e': 'email_source',
                't': 'twitter_source',
                'o': 'dark_social_source',
                'f': 'facebook_source'},
            'buttons_optimize_actions': True},
        'is_active': True,
        'share_button_html': "<div class='sp_11863 sp_em_small' >" +
            "</div>",
        'variants': {
            'twitter': [{
                'twitter_message': 'SumOfUs {LINK}',
                    'id': 47120}],
            'facebook': [{
                'facebook_title': 'SumOfUs',
                'facebook_description': "SumOfUs is a global " +
                    "movement of consumers, investors, and workers " +
                    "all around the world, standing together to " +
                    "hold corporations accountable for their " +
                    "actions and forge a new, sustainable and just " +
                    "path for our global economy. It's not going to " +
                    "be fast or easy.",
                'facebook_thumbnail': 'http://sumofus.org/wp-' +
                    'content/themes/pgm/img/default-facebook.jpg',
                    'id': 47119}],
                'email': [{
                    'email_subject': 'Email NEW subject 1!',
                        'id': 47116,
                        'email_body': 'Email NEW body 1 {LINK}'}, {
                    'email_subject': 'Email NEW subject 2!',
                        'id': 47117,
                        'email_body': 'Email NEW body 2 {LINK}'}, {
                    'email_subject': 'Email NEW subject 3!',
                        'id': 47118,
                        'email_body': 'Email NEW body 3 {LINK}'}]},
        'id': 11863,
        'page_url': 'http://sumofus.org/new-url'
    }

    assert services.update_button(payload) == expected_result

# Email variants
def test_update_email_button_with_empty_variants_value(monkeypatch):
    monkeypatch.setattr(shareProgressRequest, 'read_button',
        mockFunctions().read_email_button_test)

    payload = updateButton().update_button_payload('email')
    payload['variants'] = ''
    expected_result = ("Context: ['variants'], Message: must be Mapping")

    assert services.update_button(payload) == expected_result

# TWITTER BUTTON VALIDATION

def test_update_twitter_button(monkeypatch):
    """Monkeypatching
    To avoid sending an actual request to Shareprogress we use monkeypatch
    from pytest to replace the 'create_button' and 'read_button' function
    (from the shareProgressRequest module) with the 'update_button_twitter_test'
    and 'read_twitter_button_test' function (from the mock_functions module).
    """
    monkeypatch.setattr(shareProgressRequest, 'create_button',
        mockFunctions().update_button_twitter_test)

    monkeypatch.setattr(shareProgressRequest, 'read_button',
        mockFunctions().read_twitter_button_test)

    payload = updateButton().update_button_payload('twitter')
    expected_result = {
        'button_template': 'sp_tw_large',
        'found_snippet': False,
        'page_title': 'My Twitter NEW button name',
        'advanced_options': {
            'id_pass': None,
            'automatic_traffic_routing': None,
            'customize_params': None,
            'buttons_optimize_actions': None},
        'is_active': True,
        'share_button_html': "<div class='sp_11864 sp_tw_large' >" +
            "</div>",
        'variants': {
            'twitter': [{
                'twitter_message': 'NEW Tweet 1! {LINK}',
                    'id': 47121}, {
                'twitter_message': 'NEW Tweet 2! {LINK}',
                    'id': 47122}, {
                'twitter_message': 'NEW Tweet 3! {LINK}',
                    'id': 47123}, {
                'twitter_message': 'NEW Tweet 4! {LINK}',
                    'id': 47272}],
            'facebook': [{
                'facebook_title': 'Title 1!',
                    'facebook_description': 'Description 1',
                    'facebook_thumbnail': 'http://path_to_thumb/1.' +
                        'jpg',
                    'id': 47124}, {
                'facebook_title': 'Title 2!',
                    'facebook_description': 'Description 2',
                    'facebook_thumbnail': 'http://path_to_thumb/2.' +
                        'jpg',
                    'id': 47261}, {
                'facebook_title': 'Title 3!',
                    'facebook_description': 'Description 3',
                    'facebook_thumbnail': 'http://path_to_thumb/3.' +
                        'jpg',
                    'id': 47262}],
            'email': [{
                'email_subject': 'SumOfUs',
                    'id': 47125,
                    'email_body': "SumOfUs is a global movement of " +
                        "consumers, investors, and workers all " +
                        "around the world, standing together to " +
                        "hold corporations accountable for their " +
                        "actions and forge a new, sustainable and " +
                        "just path for our global economy. It's not " +
                        "going to be fast or easy. But if enough of " +
                        "us come together, we can make a real " +
                        "difference.\n{LINK}"}]},
        'id': 11864,
        'page_url': 'http://sumofus.org/new-url'
    }

    assert services.update_button(payload) == expected_result

# Twitter variants
def test_update_twitter_button_with_empty_variants_value(monkeypatch):
    monkeypatch.setattr(shareProgressRequest, 'read_button',
        mockFunctions().read_twitter_button_test)

    payload = updateButton().update_button_payload('twitter')
    payload['variants'] = ''
    expected_result = ("Context: ['variants'], Message: must be Mapping")

    assert services.update_button(payload) == expected_result

# FACEBOOK BUTTON VALIDATION

def test_update_facebook_button(monkeypatch):
    """Monkeypatching
    To avoid sending an actual request to Shareprogress we use monkeypatch
    from pytest to replace the 'create_button' and 'read_button' function
    (from the shareProgressRequest module) with the 'update_button_facebook_test'
    and 'read_facebook_button_test' function (from the mock_functions module).
    """
    monkeypatch.setattr(shareProgressRequest, 'create_button',
        mockFunctions().update_button_facebook_test)

    monkeypatch.setattr(shareProgressRequest, 'read_button',
        mockFunctions().read_facebook_button_test)

    payload = updateButton().update_button_payload('facebook')
    expected_result = {
        'button_template': 'sp_fb_large',
        'found_snippet': False,
        'page_title': 'My NEW Facebook button name',
        'advanced_options': {
            'id_pass': {
                'id': 'id',
                'passed': 'referrer_id'},
            'automatic_traffic_routing': True,
            'customize_params': {
                'param': 'param_to_use',
                'e': 'email_source',
                't': 'twitter_source',
                'o': 'dark_social_source',
                'f': 'facebook_source'},
            'buttons_optimize_actions': True},
        'is_active': True,
        'share_button_html': "<div class='sp_11865 sp_fb_large' >" +
            "</div>",
        'variants': {
            'twitter': [{
                'twitter_message': 'SumOfUs {LINK}',
                'id': 47129}],
            'facebook': [{
                'facebook_title': 'NEW Title 1!',
                    'facebook_description': 'NEW Description 1',
                    'facebook_thumbnail': 'http://path_to_thumb/1.jpg',
                    'id': 47126}, {
                'facebook_title': 'NEW Title 3!',
                    'facebook_description': 'NEW Description 3',
                    'facebook_thumbnail': 'http://path_to_thumb/3.jpg',
                    'id': 47128}],
            'email': [{
                'email_subject': 'SumOfUs',
                'id': 47130,
                'email_body': "SumOfUs is a global movement of " +
                    "consumers, investors, and workers all around " +
                    "the world, standing together to hold " +
                    "corporations accountable for their actions and " +
                    "forge a new, sustainable and just path for our " +
                    "global economy. It's not going to be fast or " +
                    "easy. But if enough of us come together, we " +
                    "can make a real difference.\n{LINK}"}]},
        'id': 11865,
        'page_url': 'http://sumofus.org/new-url'
    }

    assert services.update_button(payload) == expected_result

# Facebook variants
def test_update_facebook_button_with_empty_variants_value(monkeypatch):
    monkeypatch.setattr(shareProgressRequest, 'read_button',
        mockFunctions().read_facebook_button_test)

    payload = updateButton().update_button_payload('facebook')
    payload['variants'] = ''
    expected_result = ("Context: ['variants'], Message: must be Mapping")

    assert services.update_button(payload) == expected_result
