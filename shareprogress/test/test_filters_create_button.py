from shareprogress import services
from shareprogress.lib.share_progress_requests import shareProgressRequests
from mock_functions import mockFunctions

# EMAIL BUTTON VALIDATION

class emailButtonInput():
    def create(self):
        return {
            'key': '123456',
            'page_url': 'http://sumofus.org/',
            'page_title': 'My button name',
            'auto_fill': True,
            'button_template': 'sp_em_large',
            'variants': {
                'email': [
                    {'email_subject': 'Email subject 1!',
                        'email_body': 'Email body 1 {LINK}'},
                    {'email_subject': 'Email subject 2!',
                        'email_body': 'Email body 2 {LINK}'},
                    {'email_subject': 'Email subject 3!',
                        'email_body': 'Email body 3 {LINK}'}
                ]
            },
            'advanced_options': {
                'automatic_traffic_routing': True,
                'buttons_optimize_actions': True,
                'customize_params': {
                    'param': 'param_to_use',
                    'e': 'email_source',
                    'f': 'facebook_source',
                    't': 'twitter_source',
                    'o': 'dark_social_source'
                },
                'id_pass': {
                    'id': 'id',
                    'passed': 'referrer_id'
                }
            }
        }

def test_create_button_for_email(monkeypatch):
    """Monkeypatching
    To avoid sending an actual request to Shareprogress we use monkeypatch
    from pytest to replace the 'create' function (from the
    shareProgressRequests module) with the 'create_email_for_test' function
    (from the mock_functions module).
    """
    monkeypatch.setattr(shareProgressRequests, 'create',
        mockFunctions().create_email_for_test)

    email_button_input = emailButtonInput().create()
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

    assert services.create_button(email_button_input) == expected_result

# Email variants
def test_create_button_for_email_with_empty_variants_value():
    email_button_input = emailButtonInput().create()
    email_button_input['variants'] = ""
    expected_result = ("Context: ['variants'], Message: must be Mapping")

    assert services.create_button(email_button_input) == expected_result

def test_create_button_for_email_with_no_variants_provided():
    email_button_input = emailButtonInput().create()
    del email_button_input['variants']
    expected_result = ("Context: [], Message: missing required properties: " +
        "['variants']")

    assert services.create_button(email_button_input) == expected_result

# TWITTER BUTTON VALIDATION

class twitterButtonInput():
    def create(self):
        return {
            'key': '123456',
            'page_url': 'http://sumofus.org/',
            'page_title': 'My button name',
            'auto_fill': True,
            'button_template': 'sp_tw_large',
            'variants': {
                'twitter': [
                    {'twitter_message': 'Tweet 1! {LINK}'},
                    {'twitter_message': 'Tweet 2! {LINK}'},
                    {'twitter_message': 'Tweet 3! {LINK}'}
                ]
            },
            'advanced_options': {
                'automatic_traffic_routing': True,
                'buttons_optimize_actions': True,
                'customize_params': {
                    'param': 'param_to_use',
                    'e': 'email_source',
                    'f': 'facebook_source',
                    't': 'twitter_source',
                    'o': 'dark_social_source'
                },
                'id_pass': {
                    'id': 'id',
                    'passed': 'referrer_id'
                }
            }
        }

def test_create_button_for_twitter(monkeypatch):
    """Monkeypatching
    To avoid sending an actual request to Shareprogress we use monkeypatch
    from pytest to replace the 'create' function (from the
    shareProgressRequests module) with the 'create_twitter_for_test' function
    (from the mock_functions module).
    """
    monkeypatch.setattr(shareProgressRequests, 'create',
        mockFunctions().create_twitter_for_test)

    twitter_button_input = twitterButtonInput().create()
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

    assert services.create_button(twitter_button_input) == expected_result

# Twitter variants
def test_create_button_for_twitter_with_empty_variants_value():
    twitter_button_input = twitterButtonInput().create()
    twitter_button_input['variants'] = ""
    expected_result = ("Context: ['variants'], Message: must be Mapping")

    assert services.create_button(twitter_button_input) == expected_result

def test_create_button_for_twitter_with_no_variants_provided():
    twitter_button_input = twitterButtonInput().create()
    del twitter_button_input['variants']
    expected_result = ("Context: [], Message: missing required properties: " +
        "['variants']")

    assert services.create_button(twitter_button_input) == expected_result

# FACEBOOK BUTTON VALIDATION

class facebookButtonInput():
    def create(self):
        return {
            'key': '123456',
            'page_url': 'http://sumofus.org/',
            'page_title': 'My button name',
            'auto_fill': True,
            'button_template': 'sp_fb_large',
            'variants': {
                'facebook': [
                    {'facebook_title': 'Title 1!',
                        'facebook_description': 'Description 1',
                        'facebook_thumbnail': 'http://path_to_thumb/1'},
                    {'facebook_title': 'Title 2!',
                        'facebook_description': 'Description 2',
                        'facebook_thumbnail': 'http://path_to_thumb/2'},
                    {'facebook_title': 'Title 3!',
                        'facebook_description': 'Description 3',
                        'facebook_thumbnail': 'http://path_to_thumb/3'}
                ]
            },
            'advanced_options': {
                'automatic_traffic_routing': True,
                'buttons_optimize_actions': True,
                'customize_params': {
                    'param': 'param_to_use',
                    'e': 'email_source',
                    'f': 'facebook_source',
                    't': 'twitter_source',
                    'o': 'dark_social_source'
                },
                'id_pass': {
                    'id': 'id',
                    'passed': 'referrer_id'
                }
            }
        }

def test_create_button_for_facebook(monkeypatch):
    """Monkeypatching
    To avoid sending an actual request to Shareprogress we use monkeypatch
    from pytest to replace the 'create' function (from the
    shareProgressRequests module) with the 'create_facebook_for_test' function
    (from the mock_functions module).
    """
    monkeypatch.setattr(shareProgressRequests, 'create',
        mockFunctions().create_facebook_for_test)

    facebook_button_input = facebookButtonInput().create()
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

    assert services.create_button(facebook_button_input) == expected_result

# Facebook variants
def test_create_button_for_facebook_with_empty_variants_value():
    facebook_button_input = facebookButtonInput().create()
    facebook_button_input['variants'] = ""
    expected_result = ("Context: ['variants'], Message: must be Mapping")

    assert services.create_button(facebook_button_input) == expected_result

def test_create_button_for_facebook_with_no_variants_provided():
    facebook_button_input = facebookButtonInput().create()
    del facebook_button_input['variants']
    expected_result = ("Context: [], Message: missing required properties: " +
        "['variants']")

    assert services.create_button(facebook_button_input) == expected_result

# ALL BUTTONS VALIDATIONS

def test_create_button_for_email_with_empty_API_key_value():
    email_button_input = emailButtonInput().create()
    email_button_input['key'] = ""
    expected_result = ("Context: ['key'], Message: must be at least 1 "
        "characters long")

    assert services.create_button(email_button_input) == expected_result

def test_create_button_for_email_with_no_API_key_provided():
    email_button_input = emailButtonInput().create()
    del email_button_input['key']
    expected_result = ("Context: [], Message: missing required "
        "properties: ['key']")

    assert services.create_button(email_button_input) == expected_result

def test_create_button_for_email_with_empty_page_url_value():
    email_button_input = emailButtonInput().create()
    email_button_input['page_url'] = ""
    expected_result = ("Context: ['page_url'], Message: must be at least 1 "
        "characters long")

    assert services.create_button(email_button_input) == expected_result

def test_create_button_for_email_with_no_page_url_provided():
    email_button_input = emailButtonInput().create()
    del email_button_input['page_url']
    expected_result = ("Context: [], Message: missing required "
        "properties: ['page_url']")

    assert services.create_button(email_button_input) == expected_result

def test_create_button_for_email_with_empty_button_template_value():
    email_button_input = emailButtonInput().create()
    email_button_input['button_template'] = ""
    expected_result = ("Context: ['button_template'], Message: must match "
        "pattern ^(sp_em_small|sp_em_large|sp_tw_small|sp_tw_large|"
            "sp_fb_small|sp_fb_large)$")

    assert services.create_button(email_button_input) == expected_result

def test_create_button_for_email_with_no_button_template_provided():
    email_button_input = emailButtonInput().create()
    del email_button_input['button_template']
    expected_result = ("Context: [], Message: missing required "
        "properties: ['button_template']")

    assert services.create_button(email_button_input) == expected_result
