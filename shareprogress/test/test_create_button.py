from shareprogress import services

def test_create_button_for_email():
    page_url = "http://sumofus.org/"
    button_template = "sp_em_large"
    variants = [
        {"subject": "Email subject 1!", "body": "Email body 1"},
        {"subject": "Email subject 2!", "body": "Email body 2"},
        {"subject": "Email subject 3!", "body": "Email body 3"}
    ]

    expected_result = ('{"button_template": "sp_em_large", "variants": {"email": '
        '[{"email_subject": "Email subject 1!", "email_body": '
        '"Email body 1"}, {"email_subject": "Email subject 2!", '
        '"email_body": "Email body 2"}, {"email_subject": "Email subject 3!", '
        '"email_body": "Email body 3"}]}, "auto_fill": true, '
        '"key": "123456", "page_url": "http://sumofus.org/"}')

    assert services.create_button(page_url=page_url,
        button_template=button_template,
        variants=variants) == expected_result


def test_create_button_for_twitter():
    page_url = "http://sumofus.org/"
    button_template = "sp_tw_small"
    variants = [
        {"message": "Tweet 1!"},
        {"message": "Tweet 2!"},
        {"message": "Tweet 3!"}
    ]

    expected_result = ('{"button_template": "sp_tw_small", "variants": '
        '{"twitter": [{"twitter_message": "Tweet 1!"}, {"twitter_message": '
        '"Tweet 2!"}, {"twitter_message": "Tweet 3!"}]}, "auto_fill": true, '
        '"key": "123456", "page_url": "http://sumofus.org/"}')

    assert services.create_button(page_url=page_url,
        button_template=button_template,
        variants=variants) == expected_result

def test_create_button_for_facebook():
    page_url = "http://sumofus.org/"
    button_template = "sp_fb_small"
    variants = [
        {"title": "Title 1!", "description": "Description 1",
            "thumbnail": "http://path_to_thumb/1"},
        {"title": "Title 2!", "description": "Description 2",
            "thumbnail": "http://path_to_thumb/2"},
        {"title": "Title 3!", "description": "Description 3",
            "thumbnail": "http://path_to_thumb/3"}
    ]

    expected_result = ('{"button_template": "sp_fb_small", "variants": '
        '{"facebook": [{"facebook_title": "Title 1!", '
        '"facebook_description": "Description 1", "facebook_thumbnail": '
        '"http://path_to_thumb/1"}, {"facebook_title": "Title 2!", '
        '"facebook_description": "Description 2", "facebook_thumbnail": '
        '"http://path_to_thumb/2"}, {"facebook_title": "Title 3!", '
        '"facebook_description": "Description 3", "facebook_thumbnail": '
        '"http://path_to_thumb/3"}]}, "auto_fill": true, "key": "123456", '
        '"page_url": "http://sumofus.org/"}')

    assert services.create_button(page_url=page_url,
        button_template=button_template,
        variants=variants) == expected_result
