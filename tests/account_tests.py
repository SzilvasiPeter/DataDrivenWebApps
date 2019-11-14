from pypi_org.viewmodels.account.register_view_model import RegisterViewModel
from tests.test_client import flask_app


def test_example():
    print("Test example...")
    assert 1 + 2 == 3


def test_register_validation_when_valid():
    # 3 A's of testing: Arrange, Act, then Assert

    # Arrange

    form_data = {
        'name': 'Peter Szilvasi',
        'email': 'peti.szilvasi@gmail.com',
        'password': 'abc123'
    }


    with flask_app.test_request_context(path='/account/register', data=form_data):
        vm = RegisterViewModel()

    # Act
    vm.validate()

    # Assert
    assert vm.error is None
