from http import HTTPStatus

from fastapi.testclient import TestClient

from fastapi_zero.app import app


def test_root_deve_retornar_ola_mundo():
    """
    Essse teste tem 3 etapas (AAA)
    - A: Arrange - Arranjo
    - A: Act     - Executa a coisa (o SUT)
    - A: Assert  - Garanta que A é A
    """
    client = TestClient(app)  # Arrange

    response = client.get('/')  # Act

    assert response.json() == {'message': 'Olá mundo!'}  # Assert
    assert response.status_code == HTTPStatus.OK  # Assert


def test_root_html_deve_retornar_ola_html():
    client = TestClient(app)

    nome = 'werberty'
    response = client.get(f'/{nome}')

    assert response.status_code == HTTPStatus.OK
    assert f'Olá, {nome}!' in response.text
