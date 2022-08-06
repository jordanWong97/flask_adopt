"""Flask app for get requests from PetFinder API."""

import os
from flask import Flask, render_template, redirect, flash, requests
from flask_debugtoolbar import DebugToolbarExtension
from dotenv import load_dotenv


# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
#
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)


# TODO:
# def authenticate():
#     ...

def find_a_random_pet():
    """Find a random pet via Pet Finder"""

    resp = requests.get('https://api.petfinder.com/v2/animals',
                        params={"Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiI5UGxyQWVzaXFmUmFpZkdZVmF1VW1JVGFJQWt6VGRLdElsTG01Ym5xUzVtV1h3OWkxciIsImp0aSI6IjVmZjY1Y2MxOWZmZTgxOWZiMWMwN2RlNGRkZjczYWNjMzczYjg5YjVlMDM4NTEzNjRjYzkyMmI3NmY5OGI3NWEyMDBjM2Y3ZjlmYjk0MTZhIiwiaWF0IjoxNjU5NzQyNDkwLCJuYmYiOjE2NTk3NDI0OTAsImV4cCI6MTY1OTc0NjA5MCwic3ViIjoiIiwic2NvcGVzIjpbXX0.V_L5693tzrv4M6a8ymsoWgnKxa4CPaUTamehRDvDD_c33mQitKIU-4TxvzdPuYTkgn1f4zYVYpxNzfqs-fp16HzOL-vMmV4EbYWUZE3vwEefrShPb_XwIiwnhyFo8T_G1Nd4tCW2EzRP3t1qgHrNFNlC51E-ll4lhpA_iTd3FiZJ9M2u1RjoN3k_6z5h_OxIvB-loLbNFPIOUD3dHRYVivrVwBcAfZrSfoPfynaD6y00hq3Q8XJJUhFYw-C1WR1bCuKQ23sDLDUJa0iiLY8Oe_WuJZNzMXd4qIxnUBtcwFNZBq4FVvyY8LssRetUx8GurrChfiwgkJQCCcbl-FsIUg"})

    variable = resp.json
    return variable