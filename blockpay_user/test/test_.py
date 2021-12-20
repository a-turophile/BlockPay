import json

import pytest
import requests


def test_index(app, client):
    res = client.get('/')
    assert res.status_code == 200
    # expected = {'hello': 'world'}
    # assert expected == json.loads(res.get_data(as_text=True))

def test_wallet(app, client):
    res = client.get('/wallet/new')
    assert res.status_code == 200





def test_transaction_gen(app, client):
    data = {
        "sender_address": "1dfdf",
        "sender_private_key": "a content",
        "recipient_address": "participant1",
        "amount": "participant2",

    }

    res = client.post(
        "/generate/transaction",

        data=json.dumps(data),
        headers={"Content-Type": "application/json"}

    )

    assert res.status_code == 400


def test_homepage_view(app,client):
        """
        Test that homepage is accessible without login
        """
        response1 = client.get('/')
        print((response1.get_data(as_text=True)))
        assert response1.status_code == 200


def test_transaction_page_with_fixture(client):

    response = client.get('/view/transactions')
    assert response.status_code == 200

# def test_final(client):
#     data = {
#         "user_id": "1",
#         "content": "a content",
#         "participant1": "participant1",
#         "participant2": "participant2",
#         "participant3": "participants"
#     }
#     response = client.post("/generate/transaction", json=json.dumps(data))
#     json_response = response.json()
#     print(json_response)