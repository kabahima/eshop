from flask import Blueprint
from flask_cors import CORS # THAT DOES THIS DO TO RESEARCH

# SETTING UP THE USER AND AUTHENTICATION Blueprint

eshop_bp = Blueprint('eshop_bp', __name__)

# SET CORS FOR eshop Blueprint

CORS(eshop_bp)
