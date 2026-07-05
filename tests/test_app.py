from http import HTTPStatus


def test_root_deve_retornar_ola_mundo(client):
    response = client.get('/')  # Act

    assert response.json() == {'message': 'Olá mundo!'}  # Assert
    assert response.status_code == HTTPStatus.OK  # Assert


def test_root_html_deve_retornar_ola_html(client):
    nome = 'werberty'
    response = client.get(f'/{nome}')

    assert response.status_code == HTTPStatus.OK
    assert f'Olá, {nome}!' in response.text


def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'username': 'alice',
            'email': 'alice@example.com',
            'password': 'secret',
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'id': 1,
        'email': 'alice@example.com',
        'username': 'alice',
    }


def test_read_users(client):
    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'username': 'alice',
                'email': 'alice@example.com',
                'id': 1,
            },
        ],
    }


def test_update_users(client):
    response = client.put(
        '/users/1',
        json={
            'username': 'bob',
            'email': 'bob@example.com',
            'password': 'secret123',
        },
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'bob',
        'email': 'bob@example.com',
        'id': 1,
    }


def test_update_no_existent_users(client):
    response = client.put(
        '/users/7',
        json={
            'username': 'alice',
            'email': 'alice@example.com',
            'password': 'secret678',
        },
    )

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'Deu ruim! Não achei'}


def test_delete_user(client):
    response = client.delete('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'bob',
        'email': 'bob@example.com',
        'id': 1,
    }


def test_delete_no_existent_user(client):
    response = client.delete('/users/7')

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'Deu ruim! Não achei'}


def test_read_user(client):
    client.post(
        '/users/',
        json={
            'username': 'alice',
            'email': 'alice@example.com',
            'password': 'secret',
        },
    )

    response = client.get('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'alice',
        'email': 'alice@example.com',
        'id': 1,
    }


def test_read_not_existent_user(client):
    response = client.get('/users/7')

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'Deu ruim! Não achei'}
