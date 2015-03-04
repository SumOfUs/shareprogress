import json
import valideer as V
from valideer import ValidationError
from filters import *
from lib.share_progress_request import shareProgressRequest

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
    button_schema = createButtonSchema()

    # Creates the general button schema to validate
    button_validator = V.parse(button_schema.schema())

    # Once button_validator is set, we try to validate the input data
    try:
        button_validator.validate(data)
    except ValidationError as e:
        return "Context: " + str(e.context) + ", Message: " + str(e.msg)
    else:
        """If data input for the button general schema is valid, we try to
        validate the variants. Depending on the share channel, we create the
        specific schema to validate variants.
        """
        if (data['button_template'][3:5] == 'em'):
            variants_validator = V.parse(button_schema.email_variants())
        elif (data['button_template'][3:5] == 'tw'):
            variants_validator = V.parse(button_schema.twitter_variants())
        elif (data['button_template'][3:5] == 'fb'):
            variants_validator = V.parse(button_schema.facebook_variants())

        # Once variants_validator is set, we try to validate the input data
        try:
            variants_validator.validate(data)
        except ValidationError as e:
            return "Context: " + str(e.context) + ", Message: " + str(e.msg)

        # If data input is valid
        else:
            sp_req = shareProgressRequest()
            result = sp_req.create_button(data)

            if result['success']:
                return result['response'][0]
            else:
                return result['message']

def update_button(data):
    """Validates the input (a dictionary) to send a POST request to
    ShareProgress to update a share button. The result could be:
    a) A dictionary containing the information of the updated button or,
    b) An Error message from ShareProgress (i.e. 'Bad API key').

    Arguments received:
    data: A dictionary containing all the info about the button to be updated.
    """
    # First, we read the button info from ShareProgress
    sp_req = shareProgressRequest()
    result = sp_req.read_button(data)

    # If button is found in ShareProgress
    if result['success']:
        found_button = result['response'][0]

        # Creates the button schema to validate
        button_schema = updateButtonSchema()

        """If the data to update the button includes 'button_template' key,
        we set the proper button_validator using that key.
        """
        if ('button_template' in data and data['button_template'] != ''):
            if (data['button_template'][3:5] == 'em'):
                button_validator = V.parse(button_schema.email())
            elif (data['button_template'][3:5] == 'tw'):
                button_validator = V.parse(button_schema.twitter())
            elif (data['button_template'][3:5] == 'fb'):
                button_validator = V.parse(button_schema.facebook())
        else:
            """If the data to update the button doesn't include
            'button_template' key, we set the proper button_validator using
            that key from found_button.
            """
            if (found_button['button_template'][3:5] == 'em'):
                button_validator = V.parse(button_schema.email())
            elif (found_button['button_template'][3:5] == 'tw'):
                button_validator = V.parse(button_schema.twitter())
            elif (found_button['button_template'][3:5] == 'fb'):
                button_validator = V.parse(button_schema.facebook())

        # Once button_validator is set, we try to validate the input data
        try:
            button_validator.validate(data)
        except ValidationError as e:
            return "Context: " + str(e.context) + ", Message: " + str(e.msg)

        # If data input is valid
        else:
            sp_req = shareProgressRequest()
            result = sp_req.create_button(data)

            if result['success']:
                return result['response'][0]
            else:
                return result['message']

    # If button is not found in ShareProgress
    else:
        return result['message']

# Managing Pages
def create_page(page_url, variants, page_title=None):
    """Creates a JSON object for a share page to be sent to ShareProgress.

    Arguments received:
    page_url: The URL of the page to be shared.

    variants: Received arguments for the variant/s
        we would use the create_variant() function here.
    page_title: It's optional, when 'None' it will be scraped from the
        page_url automatically.
    """
    pass

def update_page(id, variants):
    """Updates a ShareProgress page and returns a JSON object as response.

    Arguments received:
    id: page ID.
    variants: Received arguments for the variant/s.
    we would use the update_variant() function here.
    """
    pass

# Reading a button or page
def read(data, share_type):
    """Reads the content of a ShareProgress button or page.

    Arguments received:
    id: button or page ID.
    share_type: 'button' or 'page' to determine the URL for the request.
    """
    button_schema = readButtonSchema()

    # Creates the read button schema to validate
    button_validator = V.parse(button_schema.schema())

    try:
        button_validator.validate(data)
    except ValidationError as e:
        return "Context: " + str(e.context) + ", Message: " + str(e.msg)
    else:
        sp_req = shareProgressRequest()

        if (share_type == 'button'):
            result = sp_req.read_button(data)
        # TO DO:
        # elif (share_type == 'page'):
        #     result = sp_req.read_page(data)
        # elif (share_type == 'wrapper'):
        #     result = sp_req.read_wrapper(data)

        if result['success']:
            return result['response'][0]
        else:
            return result['message']

# Deleting a button or page
def delete(id, type):
    """Deletes a ShareProgress button or page.

    Arguments received:
    id: button or page ID.
    type: 'button' or 'page' to determine the URL for the request.
    """
    pass
