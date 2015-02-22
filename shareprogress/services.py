import json

# Managing Buttons
def create_button(page_url, button_template, variants, page_title=None):
    """Creates a JSON object for a share button to be sent to ShareProgress.

    Arguments received

    page_url: The URL of the page to be shared.

    button_template: By knowing the button_template we know which channel
    is going to be set for that button (email, twitter or facebook).

    variants: Received arguments for the variant/s
    we would use the create_variant() function here.

    page_title: It's optional, when set to 'None' it will be scraped from the
    page_url automatically.

    It will create a JSON object to be sent to ShareProgress.
    """

    body = {}

    body['key'] = '123456'      # This will be taken from .env
    body['page_url'] = page_url

    if (page_title is not None):
        body['page_title'] = page_title

    # button_template: i.e. 'sp_em_small' or 'sp_tw_large'
    body['button_template'] = button_template

    body['auto_fill'] = True    # Allows page_url scraping to fill info in

    body['variants'] = {}

    if (button_template[3:5] == 'em'):
        body['variants']['email'] = []

        for v in variants:
            email_variant = create_variant('email', v)

            body['variants']['email'].append(email_variant)

    elif (button_template[3:5] == 'tw'):
        body['variants']['twitter'] = []

        for v in variants:
            twitter_variant = create_variant('twitter', v)

            body['variants']['twitter'].append(twitter_variant)

    elif (button_template[3:5] == 'fb'):
        body['variants']['facebook'] = []

        for v in variants:
            facebook_variant = create_variant('facebook', v)

            body['variants']['facebook'].append(facebook_variant)

    return json.dumps(body)

def update_button(id, variants):
    """Updates a ShareProgress button and returns a JSON object as response.

    Arguments received

    id: button ID.

    variants: Received arguments for the variant/s.
    we would use the update_variant() function here.
    """

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

def update_page(id, variants):
    """Updates a ShareProgress page and returns a JSON object as response.

    Arguments received

    id: page ID.

    variants: Received arguments for the variant/s.
    we would use the update_variant() function here.
    """

# Reading a button or page
def read(id, type):
    """Reads the content of a ShareProgress button or page.

    Arguments received

    id: button or page ID.

    type: 'button' or 'page' to determine the URL for the request.
    """


# Deleting a button or page
def delete(id, type):
    """Deletes a ShareProgress button or page.

    Arguments received

    id: button or page ID.

    type: 'button' or 'page' to determine the URL for the request.
    """

    pass

# Managing variants (different versions for each channels, for A/B tests)
def create_variant(channel, variant):
    """Creates a variant for a specific channel of a button or page.

    Arguments received

    channel: email, twitter or facebook.

    variant: contents for the new variant.
    """
    if (channel == 'email'):
        email_variant = {}
        email_variant['email_subject'] = variant['subject']
        email_variant['email_body'] = variant['body']

        return email_variant

    elif (channel == 'twitter'):
        twitter_variant = {}
        twitter_variant['twitter_message'] = variant['message']

        return twitter_variant

    elif (channel == 'facebook'):
        facebook_variant = {}
        facebook_variant['facebook_title'] = variant['title']
        facebook_variant['facebook_description'] = variant['description']
        facebook_variant['facebook_thumbnail'] = variant['thumbnail']

        return facebook_variant

def update_variants(id, variants):
    """Updates a variant for a specific channel of a button or page.

    Arguments received

    id: button ID.

    variants: Received arguments for the variant/s.
    """
