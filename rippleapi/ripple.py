#!/bin/env python3

import json
import requests


class RippleClient(object):
    TEST_RIPPLE_SERVER = 'https://s.altnet.rippletest.net:51234'
    PROD_RIPPLE_SERVER = 'https://s1.ripple.com:51234'

    def __init__(self, server=PROD_RIPPLE_SERVER):
        self.server = server

    def _request(self, method, params, strict=True, ledger_index=None):
        params['strict'] = strict
        params['ledger_index'] = ledger_index or "validated"

        req = {
            "method": "account_info",
            "params": [
                params
            ]
        }
        response = requests.post(self.server, json=req)
        if response.status_code != 200:
            raise Exception('Error: {}'.format(response.status_code))
        return json.loads(response.text)
        
    ##########################
    # Public Ripple Commands #
    ##########################

    def account_info(self, account):
        params = {
            "account": account,
        }
        return self._request('account_info', params)

    def account_currencies(self, account, account_index):
        params = {
            "account": account,
            "account_index": account_index,
        }
        return self._request('account_currencies', params)

    def account_tx(self,
                   account,
                   binary=False,
                   forward=False,
                   ledger_index_max=-1,
                   ledger_index_min=-1,
                   limit=2,
    ):

        '''
        The account_tx method retrieves a list of transactions that involved
        the specified account.

        "params": [
        {
            "account": "r9cZA1mLK5R5Am25ArfXFmqgNwjZgnfk59",
            "binary": false,
            "forward": false,
            "ledger_index_max": -1,
            "ledger_index_min": -1,
            "limit": 2
        }
        https://ripple.com/build/rippled-apis/#account-tx

        '''
        params = {
            "account": account,
            "binary": binary,
            "forward": forward,
            "ledger_index_max": ledger_index_max,
            "ledger_index_min": ledger_index_min,
            "limit": limit,
        }
        return self._request('account_tx', params)
    
    # account_currencies
    # account_channels
    # account_lines
    # account_offers
    # account_objects
    # account_tx
    # noripple_check
    # gateway_balances
    # wallet_propose

    ######################
    # Ledger Information #
    ######################

    
    
    #########################
    # Admin Ripple Commands #
    #########################
