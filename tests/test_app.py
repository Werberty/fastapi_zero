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
