from shareprogress import services
from shareprogress.lib.share_progress_requests import shareProgressRequest
from mock_functions import mockFunctions
from generator import generator

# EMAIL BUTTON VALIDATION

def test_create_email_button(monkeypatch):
    """Monkeypatching
    To avoid sending an actual request to Shareprogress we use monkeypatch
    from pytest to replace the 'create_button' function (from the
    shareProgressRequest module) with the 'create_button_email_test' function
    (from the mock_functions module).
    """
    monkeypatch.setattr(shareProgressRequest, 'create_button',
        mockFunctions().create_button_email_test)

    button = generator().create_button('email')
    expected_result = {
        'advanced_options': {
            'id_pass': {
                'id': 'id',
                'passed': 'referrer_id'},
            'automatic_traffic_routing': True,
            'customize_params': {
                'o': 'dark_social_source',
                'e': 'email_source',
                't': 'twitter_source',
                'param': 'param_to_use',
                'f': 'facebook_source'},
            'buttons_optimize_actions': True},
        'button_template': 'sp_em_large',
        'found_snippet': False,
        'page_title': 'My button name',
        'share_button_html': "<div class='sp_11838 sp_em_large' ></div>",
        'variants': {
            'twitter': [{
                'twitter_message': 'SumOfUs {LINK}',
                    'id': 46985}],
            'facebook': [{
                'facebook_title': 'SumOfUs',
                'facebook_description': "SumOfUs is a global movement of " +
                    "consumers, investors, and workers all around the " +
                    "world, standing together to hold corporations " +
                    "accountable for their actions and forge a new, " +
                    "sustainable and just path for our global economy. It's "+
                    "not going to be fast or easy.",
                    'facebook_thumbnail': 'http://sumofus.org/wp-content' +
                    '/themes/pgm/img/default-facebook.jpg',
                    'id': 46984}],
            'email': [{
                'email_subject': 'Email subject 1!',
                    'id': 46981,
                    'email_body': 'Email body 1 {LINK}'}, {
                'email_subject': 'Email subject 2!',
                    'id': 46982,
                    'email_body': 'Email body 2 {LINK}'}, {
                'email_subject': 'Email subject 3!',
                    'id': 46983, 'email_body':
                    'Email body 3 {LINK}'}]},
        'is_active': False,
        'id': 11838,
        'page_url': 'http://sumofus.org/'
    }

    assert services.create_button(button) == expected_result

# Email variants
def test_create_email_button_with_empty_variants_value():
    button = generator().create_button('email')
    button['variants'] = ''
    expected_result = ("Context: ['variants'], Message: must be Mapping")

    assert services.create_button(button) == expected_result

def test_create_email_button_with_no_variants_provided():
    button = generator().create_button('email')
    del button['variants']
    expected_result = ("Context: [], Message: missing required properties: " +
        "['variants']")

    assert services.create_button(button) == expected_result

# TWITTER BUTTON VALIDATION

def test_create_twitter_button(monkeypatch):
    """Monkeypatching
    To avoid sending an actual request to Shareprogress we use monkeypatch
    from pytest to replace the 'create_button' function (from the
    shareProgressRequest module) with the 'create_button_twitter_test' function
    (from the mock_functions module).
    """
    monkeypatch.setattr(shareProgressRequest, 'create_button',
        mockFunctions().create_button_twitter_test)

    button = generator().create_button('twitter')
    expected_result = {
        'button_template': 'sp_tw_large',
        'found_snippet': False,
        'page_title': 'My button name',
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
        'is_active': False,
        'share_button_html': "<div class='sp_11841 sp_tw_large' ></div>",
        'variants': {
            'twitter': [{
                'twitter_message': 'Tweet 1! {LINK}',
                    'id': 46996}, {
                'twitter_message': 'Tweet 2! {LINK}',
                    'id': 46997}, {
                'twitter_message': 'Tweet 3! {LINK}',
                    'id': 46998}],
            'facebook': [{
                'facebook_title': 'SumOfUs',
                'facebook_description': "SumOfUs is a global movement of " +
                    "consumers, investors, and workers all around the " +
                    "world, standing together to hold corporations " +
                    "accountable for their actions and forge a new, " +
                    "sustainable and just path for our global economy. It's " +
                    "not going to be fast or easy.",
                'facebook_thumbnail': 'http://sumofus.org/wp-content/themes/' +
                    'pgm/img/default-facebook.jpg',
                'id': 46999}],
            'email': [{
                'email_subject': 'SumOfUs',
                    'id': 47000,
                    'email_body': "SumOfUs is a global movement of " +
                        "consumers, investors, and workers all around the " +
                        "world, standing together to hold corporations " +
                        "accountable for their actions and forge a new, " +
                        "sustainable and just path for our global economy. " +
                        "It's not going to be fast or easy. But if enough " +
                        "of us come together, we can make a real " +
                        "difference.\n{LINK}"}]},
        'id': 11841,
        'page_url': 'http://sumofus.org/'}

    assert services.create_button(button) == expected_result

# Twitter variants
def test_create_twitter_button_with_empty_variants_value():
    button = generator().create_button('twitter')
    button['variants'] = ''
    expected_result = ("Context: ['variants'], Message: must be Mapping")

    assert services.create_button(button) == expected_result

def test_create_twitter_button_with_no_variants_provided():
    button = generator().create_button('twitter')
    del button['variants']
    expected_result = ("Context: [], Message: missing required properties: " +
        "['variants']")

    assert services.create_button(button) == expected_result

# FACEBOOK BUTTON VALIDATION

def test_create_facebook_button(monkeypatch):
    """Monkeypatching
    To avoid sending an actual request to Shareprogress we use monkeypatch
    from pytest to replace the 'create_button' function (from the
    shareProgressRequest module) with the 'create_button_facebook_test' function
    (from the mock_functions module).
    """
    monkeypatch.setattr(shareProgressRequest, 'create_button',
        mockFunctions().create_button_facebook_test)

    button = generator().create_button('facebook')
    expected_result = {
        'button_template': 'sp_fb_large',
        'found_snippet': False,
        'page_title': 'My button name',
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
        'is_active': False,
        'share_button_html': "<div class='sp_11844 sp_fb_large' ></div>",
        'variants': {
            'twitter': [{
                'twitter_message': 'SumOfUs {LINK}',
                    'id': 47012}],
            'facebook': [{
                'facebook_title': 'Title 1!',
                    'facebook_description': 'Description 1',
                    'facebook_thumbnail': 'http://path_to_thumb/1',
                    'id': 47009}, {
                'facebook_title': 'Title 2!',
                    'facebook_description': 'Description 2',
                    'facebook_thumbnail': 'http://path_to_thumb/2',
                    'id': 47010}, {
                'facebook_title': 'Title 3!',
                    'facebook_description': 'Description 3',
                    'facebook_thumbnail': 'http://path_to_thumb/3',
                    'id': 47011}],
            'email': [{
                'email_subject': 'SumOfUs',
                    'id': 47013,
                    'email_body': "SumOfUs is a global movement of " +
                    "consumers, investors, and workers all around the " +
                    "world, standing together to hold corporations " +
                    "accountable for their actions and forge a new, " +
                    "sustainable and just path for our global economy. It's " +
                    "not going to be fast or easy. But if enough of us come " +
                    "together, we can make a real difference.\n{LINK}"}]},
        'id': 11844,
        'page_url': 'http://sumofus.org/'}

    assert services.create_button(button) == expected_result

# Facebook variants
def test_create_facebook_button_with_empty_variants_value():
    button = generator().create_button('facebook')
    button['variants'] = ''
    expected_result = ("Context: ['variants'], Message: must be Mapping")

    assert services.create_button(button) == expected_result

def test_create_facebook_button_with_no_variants_provided():
    button = generator().create_button('facebook')
    del button['variants']
    expected_result = ("Context: [], Message: missing required properties: " +
        "['variants']")

    assert services.create_button(button) == expected_result

# ALL BUTTONS VALIDATIONS

def test_create_button_with_empty_API_key_value():
    button = generator().create_button('email')
    button['key'] = ''
    expected_result = ("Context: ['key'], Message: must be at least 1 "
        "characters long")

    assert services.create_button(button) == expected_result

def test_create_button_with_no_API_key_provided():
    button = generator().create_button('email')
    del button['key']
    expected_result = ("Context: [], Message: missing required "
        "properties: ['key']")

    assert services.create_button(button) == expected_result

def test_create_button_with_empty_page_url_value():
    button = generator().create_button('email')
    button['page_url'] = ''
    expected_result = ("Context: ['page_url'], Message: must be at least 1 "
        "characters long")

    assert services.create_button(button) == expected_result

def test_create_button_with_no_page_url_provided():
    button = generator().create_button('email')
    del button['page_url']
    expected_result = ("Context: [], Message: missing required "
        "properties: ['page_url']")

    assert services.create_button(button) == expected_result

def test_create_button_with_empty_button_template_value():
    button = generator().create_button('email')
    button['button_template'] = ''
    expected_result = ("Context: ['button_template'], Message: must match "
        "pattern ^(sp_em_small|sp_em_large|sp_tw_small|sp_tw_large|"
            "sp_fb_small|sp_fb_large)$")

    assert services.create_button(button) == expected_result

def test_create_button_with_no_button_template_provided():
    button = generator().create_button('email')
    del button['button_template']
    expected_result = ("Context: [], Message: missing required "
        "properties: ['button_template']")

    assert services.create_button(button) == expected_result
