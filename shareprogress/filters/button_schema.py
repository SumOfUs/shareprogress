import valideer as V
import re

class buttonSchema():
    # General button schema
    def schema(self):
        return {
            # required parameters (marked with a '+' before the key name)
            "+key": V.String(min_length=1),
            "+page_url": V.String(min_length=1),
            "+button_template": re.compile('^(sp_em_small|sp_em_large|'
                'sp_tw_small|sp_tw_large|sp_fb_small|sp_fb_large)$'),
            # optional parameters
            "page_title": V.String(min_length=1),
            "auto_fill": "boolean",
            "wrapper_id": V.String(min_length=1),
            "advanced_options": {
                "automatic_traffic_routing": "boolean",
                "buttons_optimize_actions": "boolean",
                "customize_params": {
                    "param": re.compile('^param_to_use$'),
                    "e": re.compile('^email_source$'),
                    "f": re.compile('^facebook_source$'),
                    "t": re.compile('^twitter_source$'),
                    "o": re.compile('^dark_social_source$')
                }
            }
        }

    # Email button variants schema
    def email_schema(self):
        return {
            "+variants": [
                {"email_subject": V.String(min_length=1),
                    "email_body": V.String(min_length=1)}
            ]
        }

    # Twitter button variants schema
    def twitter_schema(self):
        return {
            "+variants": [
                {"twitter_message": V.String(min_length=1)}
            ]
        }

    # Facebook button variants schema
    def facebook_schema(self):
        return {
            "+variants": [{
                "facebook_title": V.String(min_length=1),
                "facebook_description": V.String(min_length=1),
                "facebook_thumbnail": V.String(min_length=1)}
            ]
        }
