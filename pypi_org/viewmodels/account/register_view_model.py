import flask

from pypi_org.services import user_service
from pypi_org.viewmodels.shared.viewmodelbase import ViewModelBase


class RegisterViewModel(ViewModelBase):
    def __init__(self):
        super().__init__()
        self.name = self.request_dict.name
        self.email = self.request_dict.email.lower().strip()
        self.password = self.request_dict.password.strip()
        self.age = self.request_dict.age.strip()

    def validate(self):
        if not self.name or not self.name.strip():
            self.error = "You must specify the name."
        elif not self.email or not self.email.strip():
            self.error = "You must specify the email."
        elif not self.password:
            self.error = "You must specify the password."
        elif len(self.password) < 5:
            self.error = "Your password must be at least 5 characters"
        elif user_service.find_user_by_email(self.email):
            self.error = "The email is already exist."

