#!/usr/bin/env python

import argparse
import google.auth

from google.oauth2 import service_account
from google.auth.transport.requests import Request

OAUTH_TOKEN_URI = 'https://www.googleapis.com/oauth2/v4/token'
SCOPE = ['https://www.googleapis.com/auth/iam']


def get_google_open_id_connect_token(service_account_file, oauth_client_id):
    """
    Get an OpenID Connect token issued by Google for the service account.
    """
    svc = service_account.Credentials.from_service_account_file(service_account_file, scopes=SCOPE)

    service_account_credentials = service_account.Credentials(
        svc.signer, svc.service_account_email, token_uri=OAUTH_TOKEN_URI, additional_claims={
            'target_audience': oauth_client_id
        }
    )

    service_account_jwt = service_account_credentials._make_authorization_grant_assertion()

    request = google.auth.transport.requests.Request()

    body = {
        'assertion': service_account_jwt,
        'grant_type': google.oauth2._client._JWT_GRANT_TYPE,
    }

    token_response = google.oauth2._client._token_endpoint_request(
        request, OAUTH_TOKEN_URI, body
    )

    return token_response['id_token']


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Google OIDC Token Retriever")

    parser.add_argument('-f', '--service-account-file', dest='service_account_file', required=True)
    parser.add_argument('-o', '--oauth-client-id', dest='oauth_client_id', required=True)

    args = parser.parse_args()

    print(get_google_open_id_connect_token(args.service_account_file, args.oauth_client_id))
