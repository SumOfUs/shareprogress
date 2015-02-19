# Managing Buttons
def create_button(page_url, button_template, page_title=None, *args):
    """Creates a ShareProgress button and returns a JSON object as response.

    Arguments received

    page_url: The URL of the page to be shared.
    
    button_template: By knowing the button_template we know which channel
    is going to be set for that button (email, twitter or facebook).
    
    page_title: It's optional, when 'None' it will be scraped from the 
    page_url automatically.
    
    *args: Received arguments for the variant/s
    we would use the create_variant() function here.
    
    It will return a JSON object with the ID of the button created and
    its information (included the HTML tag for the button to be embedded).
    """

def update_button(id, *args):
    """Updates a ShareProgress button and returns a JSON object as response.

    Arguments received

    id: button ID.
    
    *args: Received arguments for the variant/s.
    we would use the update_variant() function here.
    """

# Managing Pages
def create_page(page_url, page_title=None, *args):
    """Creates a ShareProgress page and returns a JSON object as response.

    Arguments received

    page_url: The URL of the page to be shared.
    
    page_title: It's optional, when 'None' it will be scraped from the 
    page_url automatically.
    
    *args: Received arguments for the variant/s
    we would use the create_variant() function here.
    
    It will return a JSON object with the ID of the page created and
    its information (included the share_page_url to be used).
    """

def update_page(id, *args):
    """Updates a ShareProgress page and returns a JSON object as response.

    Arguments received

    id: page ID.
    
    *args: Received arguments for the variant/s.
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
def create_variant(channel, *args):
    """Creates a variant for a specific channel of a button or page.

    Arguments received

    channel: email, twitter or facebook.
    
    *args: Received arguments for the variant.
    """

def update_variant(id, *args):
    """Updates a variant for a specific channel of a button or page.

    Arguments received

    id: button ID.
    
    *args: Received arguments for the variant/s.
    """
