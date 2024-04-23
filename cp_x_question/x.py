# from base64 import b64encode
#
# import requests
# from flask import Flask
# from get_entry_from_envy import get_entry_from_envy
#
# url_x = "https://api.twitter.com/2/tweets/:id"
#
# api_key = "X9hURXOOY8w38osc4Drm3ttEB"
# api_key_secret = "iIuzAMQX7hg5cJerwD80wu9ThjF4IgHe9yUPFVmmNkuXfNKIhh"
#
# app = Flask(__name__)
# auth_token = None
#
# base_twitter_url = "https://api.twitter.com/"
#
# def set_auth_toke():
#     global auth_token
#     if auth_token != None:
#
#         client_id, client_secret = get_twitter_credentials()
#         authentication = b64encode(f"{client_id}:{client_secret}".encode("ascii"))
#
#     with requests.post(base_twitter_url + "oauth2/token",
#                        headers={"Authorization": "Basic {authentication}",
#                         data}) as r:
#         auth_token = r.content
#         print(auth_token)
#
# def twitter_get(uri:str):
#     set_auth_toke()
#     with requests.get(
#             base_twitter_url + uri,
#             headers={"Authorization": f"Bearer {auth_token}"}
# def get_twitter_credentials():
#     cliente_id = get_entry_from_envy("TWITTER_CLIENT_ID")
#     cliente_secret = get_entry_from_envy("TWITTER_CLIENT_SECRET")
#     return cliente_id, cliente_secret
#
# @app.route('/')
# def hello_world():
#     return 'Hello World!'
#
# @app.route('/get-random-post')
# def get_random_post():
#     twitter_get("")
#
#
# if __name__ == "__main__":
#     set_auth_toke()
#     main()