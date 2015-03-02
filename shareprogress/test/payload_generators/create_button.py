class createButton():
    def create_button_payload(self, channel):
        if (channel == 'email'):
            return {
                'key': '123456',
                'page_url': 'http://sumofus.org/',
                'page_title': 'My Email button name',
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
        elif (channel == 'twitter'):
            return {
                'key': '123456',
                'page_url': 'http://sumofus.org/',
                'page_title': 'My Twitter button name',
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
        elif (channel == 'facebook'):
            return {
                'key': '123456',
                'page_url': 'http://sumofus.org/',
                'page_title': 'My Facebook button name',
                'auto_fill': True,
                'button_template': 'sp_fb_large',
                'variants': {
                    'facebook': [
                        {'facebook_title': 'Title 1!',
                            'facebook_description': 'Description 1',
                            'facebook_thumbnail': 'http://path_to_thumb/1.jpg'},
                        {'facebook_title': 'Title 2!',
                            'facebook_description': 'Description 2',
                            'facebook_thumbnail': 'http://path_to_thumb/2.jpg'},
                        {'facebook_title': 'Title 3!',
                            'facebook_description': 'Description 3',
                            'facebook_thumbnail': 'http://path_to_thumb/3.jpg'}
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
