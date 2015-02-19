# Managing Buttons
def create_button(page_url, button_template, page_title=None, *args):
    # page_url: The URL of the page to be shared.
    
    # button_template: By knowing the button_template we know which channel
    # is going to be set for that button (email, twitter or facebook).

    # page_title: It's optional, when 'None' it will be scraped from the 
    # page_url automatically.

    # *args: Received arguments for the variant/s
    # we would use the create_variant() function here.

    # It will return a JSON object with the ID of the button created and
    # its information (included the HTML tag for the button to be embedded).

def update_button(id, *args):
    # id: button ID.

    # *args: Received arguments for the variant/s.
    # we would use the update_variant() function here.

def delete_button(id):
    # id: button ID.

# Managing variants (different versions for each channels, for A/B tests)
def create_variant(channel, *args):
    # channel: email, twitter or facebook.

    # *args: Received arguments for the variant.

def update_variant(id, *args):
    # id: button ID.

    # *args: Received arguments for the variant/s.
