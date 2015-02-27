import json
import valideer as V
from valideer import ValidationError
from filters.button_schema import buttonSchema
from lib.share_progress_requests import shareProgressRequests

# Managing Buttons
def create_button(data):
    """Validates the input (a dictionary) to send a POST request to
    ShareProgress to create a share button. The result could be:
    a) A dictionary containing the information of the created button or,
    b) An Error message from ShareProgress (i.e. 'Bad API key').

    Arguments received:
    data: A dictionary containing all the info about the button. For example:
    {
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
    Example of a successful response:
    {
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
        'share_button_html': u"<div class='sp_11838 sp_em_large' ></div>",
        'variants': {
            'twitter': [{
                'twitter_message': 'SumOfUs {LINK}',
                    'id': 46985}],
        'facebook': [{
            'facebook_title': 'SumOfUs',
            'facebook_description': u"SumOfUs is a global movement of " +
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
    """
    button = buttonSchema()

    # Creates the general button schema to validate
    email_validator = V.parse(button.schema())

    try:
        email_validator.validate(data)
    except ValidationError as e:
        return "Context: " + str(e.context) + ", Message: " + str(e.msg)
    else:
        """Depending on the share channel, creates the specific schema
        to validate variants
        """
        if (data['button_template'][3:5] == 'em'):
            variants_validator = V.parse(button.email_schema())
        elif (data['button_template'][3:5] == 'tw'):
            variants_validator = V.parse(button.twitter_schema())
        elif (data['button_template'][3:5] == 'fb'):
            variants_validator = V.parse(button.facebook_schema())

        try:
            variants_validator.validate(data)
        except ValidationError as e:
            return "Context: " + str(e.context) + ", Message: " + str(e.msg)
        else:
            r = shareProgressRequests()
            result = r.create(data)

            if result['success']:
                return result['response'][0]
            else:
                return result['message']

def update_button(id, variants):
    """Updates a ShareProgress button and returns a JSON object as response.

    Arguments received

    id: button ID.

    variants: Received arguments for the variant/s.
    we would use the update_variant() function here.
    """
    pass

# Managing Pages
def create_page(page_url, variants, page_title=None):
    """Creates a JSON object for a share page to be sent to ShareProgress.

    Arguments received

    page_url: The URL of the page to be shared.

    variants: Received arguments for the variant/s
    we would use the create_variant() function here.

    page_title: It's optional, when 'None' it will be scraped from the
    page_url automatically.
    """
    pass

def update_page(id, variants):
    """Updates a ShareProgress page and returns a JSON object as response.

    Arguments received

    id: page ID.

    variants: Received arguments for the variant/s.
    we would use the update_variant() function here.
    """
    pass

# Reading a button or page
def read(id, type):
    """Reads the content of a ShareProgress button or page.

    Arguments received

    id: button or page ID.

    type: 'button' or 'page' to determine the URL for the request.
    """
    pass


# Deleting a button or page
def delete(id, type):
    """Deletes a ShareProgress button or page.

    Arguments received

    id: button or page ID.

    type: 'button' or 'page' to determine the URL for the request.
    """
    pass

# Managing variants (different versions for each channels, for A/B tests)
def update_variants(id, variants):
    """Updates a variant for a specific channel of a button or page.

    Arguments received

    id: button ID.

    variants: Received arguments for the variant/s.
    """
    pass
