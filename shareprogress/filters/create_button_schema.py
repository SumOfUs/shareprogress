import valideer as V
import re

class createButtonSchema():
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
            "advanced_options": {
                "automatic_traffic_routing": "boolean",
                "buttons_optimize_actions": "boolean",
                "customize_params": {
                    "+param": V.String(min_length=1),
                    "+e": V.String(min_length=1),
                    "+f": V.String(min_length=1),
                    "+t": V.String(min_length=1),
                    "+o": V.String(min_length=1)
                },
                "id_pass": {
                    "+id": V.String(min_length=1),
                    "+passed": V.String(min_length=1)
                }

            }
        }

    # Email button variants schema
    def email_variants(self):
        return {
            "+variants": {
                "+email": [
                    {"+email_subject": V.String(min_length=1),
                        "+email_body": re.compile('^.*{LINK}.*$')}
                ]
            }
        }

    # Twitter button variants schema
    def twitter_variants(self):
        return {
            "+variants": {
                "+twitter": [
                    {"+twitter_message": re.compile('^.*{LINK}.*$')}
                ]
            }
        }

    # Facebook button variants schema
    def facebook_variants(self):
        return {
            "+variants": {
                "+facebook": [
                    {"+facebook_title": V.String(min_length=1),
                        "+facebook_description": V.String(min_length=1),
                        "+facebook_thumbnail": V.String(min_length=1)}
                ]
            }
        }
