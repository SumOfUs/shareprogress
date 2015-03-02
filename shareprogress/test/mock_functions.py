class mockFunctions():
    def create_button_email_test(self, data):
        return {
            'message': None,
            'response': [{
                'button_template':
                'sp_em_large',
                'found_snippet': False,
                'page_title':
                'My Email button name',
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
                'share_button_html':
                    "<div class='sp_11838 sp_em_large' ></div>",
                'variants': {
                    'twitter': [{
                        'twitter_message': 'SumOfUs {LINK}',
                            'id': 46985}],
                    'facebook': [{
                        'facebook_title': 'SumOfUs',
                            'facebook_description': "SumOfUs is a " +
                            "global movement of consumers, investors, " +
                            "and workers all around the world, standing " +
                            "together to hold corporations accountable " +
                            "for their actions and forge a new, "
                            "sustainable and just path for our global " +
                            "economy. It's not going to be fast or easy.",
                            'facebook_thumbnail': 'http://sumofus.org' +
                            '/wp-content/themes/pgm/img/' +
                            'default-facebook.jpg',
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
                'id': 11838,
                'page_url': 'http://sumofus.org/'}],
            'success': True
        }

    def create_button_twitter_test(self, data):
        return {
            'message': None,
            'response': [{
                'button_template': 'sp_tw_large',
                'found_snippet': False,
                'page_title': 'My Twitter button name',
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
                'share_button_html': "<div class='sp_11841 sp_tw_" +
                    "large' ></div>",
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
                        'facebook_description': "SumOfUs is a global " +
                            "movement of consumers, investors, and " +
                            "workers all around the world, standing " +
                            "together to hold corporations accountable " +
                            "for their actions and forge a new, " +
                            "sustainable and just path for our global " +
                            "economy. It's not going to be fast or easy.",
                        'facebook_thumbnail': 'http://sumofus.org' +
                            '/wp-content/themes/pgm/img/' +
                            'default-facebook.jpg',
                        'id': 46999}],
                    'email': [{
                        'email_subject': 'SumOfUs',
                        'id': 47000,
                        'email_body': "SumOfUs is a global movement " +
                            "of consumers, investors, and workers all " +
                            "around the world, standing together to " +
                            "hold corporations accountable for their " +
                            "actions and forge a new, sustainable and " +
                            "just path for our global economy. It's not " +
                            "going to be fast or easy. But if enough of " +
                            "us come together, we can make a real " +
                            "difference.\n{LINK}"}]},
                'id': 11841,
                'page_url': 'http://sumofus.org/'}],
            'success': True
        }

    def create_button_facebook_test(self, data):
        return {
            'message': None,
            'response': [{
                'button_template': 'sp_fb_large',
                'found_snippet': False,
                'page_title': 'My Facebook button name',
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
                'share_button_html': "<div class='sp_11844 sp_fb_large' >" +
                    "</div>",
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
                                "consumers, investors, and workers all " +
                                "around the world, standing together to " +
                                "hold corporations accountable for their " +
                                "actions and forge a new, sustainable and " +
                                "just path for our global economy. It's not " +
                                "going to be fast or easy. But if enough " +
                                "of us come together, we can make a real " +
                                "difference.\n{LINK}"}]},
                'id': 11844,
                'page_url': 'http://sumofus.org/'}],
            'success': True
        }

    def read_email_button_test(self, data):
        return {
            'message': None,
            'response': [{
                'button_template': 'sp_em_large',
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
                'is_active': True,
                'share_button_html': "<div class='sp_11858 sp_em_large' >" +
                    "</div>",
                'variants': {
                    'twitter': [{
                        'twitter_message': 'SumOfUs {LINK}',
                            'id': 47089}],
                    'facebook': [{
                        'facebook_title': 'SumOfUs',
                            'facebook_description': "SumOfUs is a global " +
                                "movement of consumers, investors, and " +
                                "workers all around the world, standing " +
                                "together to hold corporations accountable " +
                                "for their actions and forge a new, " +
                                "sustainable and just path for our global " +
                                "economy. It's not going to be fast or easy.",
                            'facebook_thumbnail': 'http://sumofus.org/wp-" +'
                                'content/themes/pgm/img/default-facebook.jpg',
                            'id': 47088}],
                    'email': [{
                        'email_subject': 'Email subject 1!',
                            'id': 47085,
                            'email_body': 'Email body 1 {LINK}'}, {
                        'email_subject': 'Email subject 2!',
                            'id': 47086,
                            'email_body': 'Email body 2 {LINK}'}, {
                        'email_subject': 'Email subject 3!',
                            'id': 47087,
                            'email_body': 'Email body 3 {LINK}'}]},
                'id': 11858,
                'page_url': 'http://sumofus.org/'}],
            'success': True
        }

    def read_twitter_button_test(self, data):
        return {
            'message': None,
            'response': [{
                'button_template': 'sp_tw_large',
                'found_snippet': False,
                'page_title': 'My Twitter button name',
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
                'share_button_html': "<div class='sp_11864 sp_tw_large' >" +
                    "</div>",
                'variants': {
                    'twitter': [{
                        'twitter_message': 'Tweet 1! {LINK}',
                            'id': 47121}, {
                        'twitter_message': 'Tweet 2! {LINK}',
                            'id': 47122}, {
                        'twitter_message': 'Tweet 3! {LINK}',
                            'id': 47123}],
                    'facebook': [{
                        'facebook_title': 'SumOfUs',
                            'facebook_description': "SumOfUs is a global " +
                                "movement of consumers, investors, and " +
                                "workers all around the world, standing " +
                                "together to hold corporations accountable " +
                                "for their actions and forge a new, " +
                                "sustainable and just path for our global " +
                                "economy. It's not going to be fast or easy.",
                            'facebook_thumbnail': 'http://sumofus.org/wp-' +
                                'content/themes/pgm/img/default-facebook.jpg',
                            'id': 47124}],
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
                'page_url': 'http://sumofus.org/'}],
            'success': True
        }

    def read_facebook_button_test(self, data):
        return {
            'message': None,
            'response': [{
                'button_template': 'sp_fb_large',
                'found_snippet': False,
                'page_title': 'My Facebook button name',
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
                        'facebook_title': 'Title 1!',
                            'facebook_description': 'Description 1',
                            'facebook_thumbnail': 'http://path_to_thumb/1',
                            'id': 47126}, {
                        'facebook_title': 'Title 2!',
                            'facebook_description': 'Description 2',
                            'facebook_thumbnail': 'http://path_to_thumb/2',
                            'id': 47127}, {
                        'facebook_title': 'Title 3!',
                            'facebook_description': 'Description 3',
                            'facebook_thumbnail': 'http://path_to_thumb/3',
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
                'page_url': 'http://sumofus.org/'}],
            'success': True
        }
