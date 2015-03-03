class updateButton():
    def update_button_payload(self, channel):
        if (channel == 'email'):
            return {
                'id': 11863,
                'key': '123456',
                'button_template': 'sp_em_large',
                'page_url': 'http://sumofus.org/new-url',
                'page_title': 'My Email NEW button name',
                'variants': {
                    'email': [
                        {'email_subject': 'Email NEW subject 1!',
                            'email_body': 'Email NEW body 1 {LINK}',
                            'id': 47116},
                        {'email_subject': 'Email NEW subject 2!',
                            'email_body': 'Email NEW body 2 {LINK}',
                            'id': 47117},
                        {'email_subject': 'Email NEW subject 3!',
                            'email_body': 'Email NEW body 3 {LINK}',
                            'id': 47118}
                    ]
                }
            }
        elif (channel == 'twitter'):
            return {
                'id': 11864,
                'key': '123456',
                'button_template': 'sp_tw_large',
                'page_url': 'http://sumofus.org/new-url',
                'page_title': 'My Twitter NEW button name',
                'variants': {
                    'twitter': [
                        {'twitter_message': 'NEW Tweet 1! {LINK}',
                            'id': 47121},
                        {'twitter_message': 'NEW Tweet 2! {LINK}',
                            'id': 47122},
                        {'twitter_message': 'NEW Tweet 3! {LINK}',
                            'id': 47123},
                        {'twitter_message': 'NEW Tweet 4! {LINK}'}
                    ]
                }
           }
        elif (channel == 'facebook'):
            return {
                'id': 11865,
                'key': '123456',
                'page_url': 'http://sumofus.org/new-url',
                'page_title': 'My NEW Facebook button name',
                'button_template': 'sp_fb_large',
                'variants': {
                    'facebook': [
                        {'facebook_title': 'NEW Title 1!',
                            'facebook_description': 'NEW Description 1',
                            'facebook_thumbnail': 'http://path_to_thumb/1.jpg',
                            'id': 47126},
                        {'facebook_title': 'NEW Title 2!',
                            'facebook_description': 'NEW Description 2',
                            'facebook_thumbnail': 'http://path_to_thumb/2.jpg',
                            'id': 47127},
                        {'facebook_title': 'NEW Title 3!',
                            'facebook_description': 'NEW Description 3',
                            'facebook_thumbnail': 'http://path_to_thumb/3.jpg',
                            'id': 47128}
                    ]
                }
            }
