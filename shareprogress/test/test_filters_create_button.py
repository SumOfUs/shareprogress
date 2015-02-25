from shareprogress import services

# EMAIL BUTTON VALIDATION

class emailButtonInput():
    def create(self):
        return {
            "key": "123456",
            "page_url": "http://sumofus.org/",
            "wrapper_id": "main_wrapper",
            "page_title": "My page title",
            "auto_fill": True,
            "button_template": "sp_em_large",
            "variants": [
                {"email_subject": "Email subject 1!",
                    "email_body": "Email body 1"},
                {"email_subject": "Email subject 2!",
                    "email_body": "Email body 2"},
                {"email_subject": "Email subject 3!",
                    "email_body": "Email body 3"}
            ],
            "advanced_options": {
                "automatic_traffic_routing": True,
                "buttons_optimize_actions": True,
                "customize_params": {
                    "param": "param_to_use",
                    "e": "email_source",
                    "f": "facebook_source",
                    "t": "twitter_source",
                    "o": "dark_social_source"
                }
            }
        }

def test_create_button_for_email():
    email_button_input = emailButtonInput().create()
    expected_result = ('{'
        '"advanced_options": {'
        '"automatic_traffic_routing": true, '
        '"buttons_optimize_actions": true, '
        '"customize_params": {'
            '"e": "email_source", '
            '"f": "facebook_source", '
            '"o": "dark_social_source", '
            '"param": "param_to_use", '
            '"t": "twitter_source"}}, '
        '"auto_fill": true, '
        '"button_template": "sp_em_large", '
        '"key": "123456", '
        '"page_title": "My page title", '
        '"page_url": "http://sumofus.org/", '
        '"variants": [{'
            '"email_body": "Email body 1", '
                '"email_subject": "Email subject 1!"}, {'
            '"email_body": "Email body 2", '
                '"email_subject": "Email subject 2!"}, {'
            '"email_body": "Email body 3", '
                '"email_subject": "Email subject 3!"}], '
        '"wrapper_id": "main_wrapper"}'
    )

    assert services.create_button(email_button_input) == expected_result

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

def test_create_button_for_email_with_empty_variants_value():
    email_button_input = emailButtonInput().create()
    email_button_input['variants'] = ""
    expected_result = ("Context: ['variants'], Message: must be Sequence")

    assert services.create_button(email_button_input) == expected_result

def test_create_button_for_email_with_no_variants_provided():
    email_button_input = emailButtonInput().create()
    del email_button_input['variants']
    expected_result = ("Context: [], Message: missing required properties: ['variants']")

    assert services.create_button(email_button_input) == expected_result

# TWITTER BUTTON VALIDATION

class twitterButtonInput():
    def create(self):
        return {
            "key": "123456",
            "page_url": "http://sumofus.org/",
            "wrapper_id": "main_wrapper",
            "page_title": "My page title",
            "auto_fill": True,
            "button_template": "sp_tw_large",
            "variants": [
                {"twitter_message": "Tweet 1!"},
                {"twitter_message": "Tweet 2!"},
                {"twitter_message": "Tweet 3!"}
            ],
            "advanced_options": {
                "automatic_traffic_routing": True,
                "buttons_optimize_actions": True,
                "customize_params": {
                    "param": "param_to_use",
                    "e": "email_source",
                    "f": "facebook_source",
                    "t": "twitter_source",
                    "o": "dark_social_source"
                }
            }
        }

def test_create_button_for_twitter():
    twitter_button_input = twitterButtonInput().create()
    expected_result = ('{'
        '"advanced_options": {'
        '"automatic_traffic_routing": true, '
        '"buttons_optimize_actions": true, '
        '"customize_params": {'
            '"e": "email_source", '
            '"f": "facebook_source", '
            '"o": "dark_social_source", '
            '"param": "param_to_use", '
            '"t": "twitter_source"}}, '
        '"auto_fill": true, '
        '"button_template": "sp_tw_large", '
        '"key": "123456", '
        '"page_title": "My page title", '
        '"page_url": "http://sumofus.org/", '
        '"variants": [{'
            '"twitter_message": "Tweet 1!"}, {'
            '"twitter_message": "Tweet 2!"}, {'
            '"twitter_message": "Tweet 3!"}], '
        '"wrapper_id": "main_wrapper"}'
    )

    assert services.create_button(twitter_button_input) == expected_result

def test_create_button_for_twitter_with_empty_API_key_value():
    twitter_button_input = twitterButtonInput().create()
    twitter_button_input['key'] = ""
    expected_result = ("Context: ['key'], Message: must be at least 1 "
        "characters long")

    assert services.create_button(twitter_button_input) == expected_result

def test_create_button_for_twitter_with_no_API_key_provided():
    twitter_button_input = twitterButtonInput().create()
    del twitter_button_input['key']
    expected_result = ("Context: [], Message: missing required "
        "properties: ['key']")

    assert services.create_button(twitter_button_input) == expected_result

def test_create_button_for_twitter_with_empty_page_url_value():
    twitter_button_input = twitterButtonInput().create()
    twitter_button_input['page_url'] = ""
    expected_result = ("Context: ['page_url'], Message: must be at least 1 "
        "characters long")

    assert services.create_button(twitter_button_input) == expected_result

def test_create_button_for_twitter_with_no_page_url_provided():
    twitter_button_input = twitterButtonInput().create()
    del twitter_button_input['page_url']
    expected_result = ("Context: [], Message: missing required "
        "properties: ['page_url']")

    assert services.create_button(twitter_button_input) == expected_result

def test_create_button_for_twitter_with_empty_button_template_value():
    twitter_button_input = twitterButtonInput().create()
    twitter_button_input['button_template'] = ""
    expected_result = ("Context: ['button_template'], Message: must match "
        "pattern ^(sp_em_small|sp_em_large|sp_tw_small|sp_tw_large|"
            "sp_fb_small|sp_fb_large)$")

    assert services.create_button(twitter_button_input) == expected_result

def test_create_button_for_twitter_with_no_button_template_provided():
    twitter_button_input = twitterButtonInput().create()
    del twitter_button_input['button_template']
    expected_result = ("Context: [], Message: missing required "
        "properties: ['button_template']")

    assert services.create_button(twitter_button_input) == expected_result

def test_create_button_for_twitter_with_empty_variants_value():
    twitter_button_input = twitterButtonInput().create()
    twitter_button_input['variants'] = ""
    expected_result = ("Context: ['variants'], Message: must be Sequence")

    assert services.create_button(twitter_button_input) == expected_result

def test_create_button_for_twitter_with_no_variants_provided():
    twitter_button_input = twitterButtonInput().create()
    del twitter_button_input['variants']
    expected_result = ("Context: [], Message: missing required properties: ['variants']")

    assert services.create_button(twitter_button_input) == expected_result

# FACEBOOK BUTTON VALIDATION

class facebookButtonInput():
    def create(self):
        return {
            "key": "123456",
            "page_url": "http://sumofus.org/",
            "wrapper_id": "main_wrapper",
            "page_title": "My page title",
            "auto_fill": True,
            "button_template": "sp_fb_large",
            "variants": [
                {"facebook_title": "Title 1!",
                    "facebook_description": "Description 1",
                    "facebook_thumbnail": "http://path_to_thumb/1"},
                {"facebook_title": "Title 2!",
                    "facebook_description": "Description 2",
                    "facebook_thumbnail": "http://path_to_thumb/2"},
                {"facebook_title": "Title 3!",
                    "facebook_description": "Description 3",
                    "facebook_thumbnail": "http://path_to_thumb/3"}
            ],
            "advanced_options": {
                "automatic_traffic_routing": True,
                "buttons_optimize_actions": True,
                "customize_params": {
                    "param": "param_to_use",
                    "e": "email_source",
                    "f": "facebook_source",
                    "t": "twitter_source",
                    "o": "dark_social_source"
                }
            }
        }

def test_create_button_for_facebook():
    facebook_button_input = facebookButtonInput().create()
    expected_result = ('{"advanced_options": '
        '{"automatic_traffic_routing": true, '
        '"buttons_optimize_actions": true, "customize_params": '
        '{"e": "email_source", "f": "facebook_source", '
        '"o": "dark_social_source", "param": "param_to_use", '
        '"t": "twitter_source"}}, "auto_fill": true, '
        '"button_template": "sp_fb_large", "key": "123456", '
        '"page_title": "My page title", "page_url": "http://sumofus.org/", '
        '"variants": [{"facebook_description": "Description 1", '
        '"facebook_thumbnail": "http://path_to_thumb/1", '
        '"facebook_title": "Title 1!"}, {"facebook_description": '
        '"Description 2", "facebook_thumbnail": "http://path_to_thumb/2", '
        '"facebook_title": "Title 2!"}, {"facebook_description": '
        '"Description 3", "facebook_thumbnail": "http://path_to_thumb/3", '
        '"facebook_title": "Title 3!"}], "wrapper_id": "main_wrapper"}'
    )

    assert services.create_button(facebook_button_input) == expected_result

def test_create_button_for_facebook_with_empty_API_key_value():
    facebook_button_input = facebookButtonInput().create()
    facebook_button_input['key'] = ""
    expected_result = ("Context: ['key'], Message: must be at least 1 "
        "characters long")

    assert services.create_button(facebook_button_input) == expected_result

def test_create_button_for_facebook_with_no_API_key_provided():
    facebook_button_input = facebookButtonInput().create()
    del facebook_button_input['key']
    expected_result = ("Context: [], Message: missing required "
        "properties: ['key']")

    assert services.create_button(facebook_button_input) == expected_result

def test_create_button_for_facebook_with_empty_page_url_value():
    facebook_button_input = facebookButtonInput().create()
    facebook_button_input['page_url'] = ""
    expected_result = ("Context: ['page_url'], Message: must be at least 1 "
        "characters long")

    assert services.create_button(facebook_button_input) == expected_result

def test_create_button_for_facebook_with_no_page_url_provided():
    facebook_button_input = facebookButtonInput().create()
    del facebook_button_input['page_url']
    expected_result = ("Context: [], Message: missing required "
        "properties: ['page_url']")

    assert services.create_button(facebook_button_input) == expected_result

def test_create_button_for_facebook_with_empty_button_template_value():
    facebook_button_input = facebookButtonInput().create()
    facebook_button_input['button_template'] = ""
    expected_result = ("Context: ['button_template'], Message: must match "
        "pattern ^(sp_em_small|sp_em_large|sp_tw_small|sp_tw_large|"
            "sp_fb_small|sp_fb_large)$")

    assert services.create_button(facebook_button_input) == expected_result

def test_create_button_for_facebook_with_no_button_template_provided():
    facebook_button_input = facebookButtonInput().create()
    del facebook_button_input['button_template']
    expected_result = ("Context: [], Message: missing required "
        "properties: ['button_template']")

    assert services.create_button(facebook_button_input) == expected_result

def test_create_button_for_facebook_with_empty_variants_value():
    facebook_button_input = facebookButtonInput().create()
    facebook_button_input['variants'] = ""
    expected_result = ("Context: ['variants'], Message: must be Sequence")

    assert services.create_button(facebook_button_input) == expected_result

def test_create_button_for_facebook_with_no_variants_provided():
    facebook_button_input = facebookButtonInput().create()
    del facebook_button_input['variants']
    expected_result = ("Context: [], Message: missing required properties: ['variants']")

    assert services.create_button(facebook_button_input) == expected_result
