import json
import valideer as V
from valideer import ValidationError
from filters.button_schema import buttonSchema

# Managing Buttons
def create_button(data):
    """Creates a JSON object for a share button to be sent to ShareProgress.

    Arguments received:
    data: A dictionary containing all the info about the button. For example:
    {
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
    """
    button = buttonSchema()

    # Creates the general button schema to validate
    email_validator = V.parse(button.schema())

    try:
        email_validator.validate(data)
    except ValidationError as e:
        return "Context: " + str(e.context) + ", Message: " + str(e.msg)
    else:
        # Depending on the share channel, creates the specific schema
        # to validate variants
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
            return json.dumps(data, sort_keys=True)

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
