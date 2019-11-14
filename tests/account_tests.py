from pypi_org.data.users import User
from pypi_org.viewmodels.account.register_view_model import RegisterViewModel
from tests.test_client import flask_app
from unittest import mock


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
    target = 'pypi_org.services.user_service.find_user_by_email'
    with mock.patch(target=target, return_value=None):
        vm.validate()

    # Assert
    assert vm.error is None


def test_register_validation_for_existing_user():
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
    target = 'pypi_org.services.user_service.find_user_by_email'
    test_user = form_data.get('email')
    with mock.patch(target=target, return_value=User(email=test_user)):
        vm.validate()

    # Assert
    assert vm.error is not None
    assert 'already exist' in vm.error