"""The file contains constants providing all necessary settings
for functions loading data from JSON files and switches on a test mode
"""
from os import path
import os
# -------------------------------------------------------------------------
# This is the very important setting. It sets up a test configuration for
# Flask app if pytest is started
os.environ['CURRENT_MODE'] = 'Test'
# -------------------------------------------------------------------------

# paths building taking into account the features of the OS
USER_TEST_JSON = path.join('tests', 'tests_data', 'users.json')
ORDER_TEST_JSON = path.join('tests', 'tests_data', 'orders.json')
OFFER_TEST_JSON = path.join('tests', 'tests_data', 'offers.json')
