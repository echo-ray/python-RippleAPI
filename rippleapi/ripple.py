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
            "method": method,
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

    ########################
    # Transaction Commands #
    ########################
    def sign(self, secret_key, transaction):
        params = {
            "offline": False,
            "secret": secret_key,
            "tx_json": {
                "Account": transaction.source_address,
                "Amount": {
                    "currency": transaction.currency,
                    "issuer": transaction.issuer or transaction.source_address,
                    "value": str(transaction.amount),
                },
                "Destination": transaction.destination_address,
                "TransactionType": transaction.transaction_type,
            },
            "fee_mult_max": transaction.fee_mult_max,
        }
        return self._request('sign', params)

    def submit(self, tx_blob):
        '''
        Given the BLOB that is returned after signing a transaction with secret
        key, submit it to the server
        
        '''
        params = {
            'tx_blob': tx_blob
        }
        return self._request('submit', params)

    ######################
    # Ledger Information #
    ######################

    
    
    #########################
    # Admin Ripple Commands #
    #########################

class RippleTransaction(object):
    def __init__(self,
                 source_address,
                 destination_address,
                 amount,
                 currency="XRP",
                 issuer=None,
                 transaction_type="Payment",
                 fee_mult_max=1000,
                 ):
        self.source_address = source_address
        self.destination_address = destination_address
        self.amount = amount
        self.currency = currency
        self.issuer = issuer
        self.transaction_type = transaction_type
        self.fee_mult_max = fee_mult_max
