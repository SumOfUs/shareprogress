import valideer as V
import re

class updateButtonSchema():
    # Email button schema
    def email(self):
        return {
            # required parameters (marked with a '+' before the key name)
            "+id": "integer",
            "+key": V.String(min_length=1),
            # optional parameters
            "page_url": V.String(min_length=1),
            "page_title": V.String(min_length=1),
            "auto_fill": "boolean",
            "button_template": re.compile('^(sp_em_small|sp_em_large)$'),
            "variants": {
                "+email": [
                    {"+email_subject": V.String(min_length=1),
                        "+email_body": re.compile('^.*{LINK}.*$'),
                        "id": "integer"}
                ]
            },
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

    # Twitter button schema
    def twitter(self):
        return {
            # required parameters (marked with a '+' before the key name)
            "+id": "integer",
            "+key": V.String(min_length=1),
            # optional parameters
            "page_url": V.String(min_length=1),
            "page_title": V.String(min_length=1),
            "auto_fill": "boolean",
            "button_template": re.compile('^(sp_tw_small|sp_tw_large)$'),
            "variants": {
                "+twitter": [
                    {"+twitter_message": re.compile('^.*{LINK}.*$'),
                        "id": "integer"}
                ]
            },
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

    # Facebook button schema
    def facebook(self):
        return {
            # required parameters (marked with a '+' before the key name)
            "+id": "integer",
            "+key": V.String(min_length=1),
            # optional parameters
            "page_url": V.String(min_length=1),
            "page_title": V.String(min_length=1),
            "auto_fill": "boolean",
            "button_template": re.compile('^(sp_fb_small|sp_fb_large)$'),
            "variants": {
                "+facebook": [
                    {"+facebook_title": V.String(min_length=1),
                        "+facebook_description": V.String(min_length=1),
                        "+facebook_thumbnail": V.String(min_length=1),
                        "id": "integer"}
                ]
            },
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
