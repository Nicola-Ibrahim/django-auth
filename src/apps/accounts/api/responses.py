"""
This script defines custom formatted responses for the api views.
"""
import enum

from django.utils.translation import gettext_lazy as _
from rest_framework import status

from src.apps.accounts.models import models
from src.apps.core.base_api.responses import BaseResponse


class OperationCode(enum.Enum):
    Created = _("created")
    Updated = _("updated")
    Deleted = _("deleted")
    Verified_OTP = _("verified_OTP")
    Reset_Password = _("reset_password")
    Forget_Password = _("forget_password")
    First_Time_Password = _("first_time_password")


class UserCreateResponse(BaseResponse):
    data_ = {
        "code": OperationCode.Created.value,
        "detail": _("The user has been created"),
    }

    status_ = status.HTTP_200_OK

    def with_data(self, user_data: dict):
        if user_data:
            self.data_["data"] = user_data

        return super().with_data()


class VerifyOTPResponse(BaseResponse):
    data_ = {
        "code": OperationCode.Verified_OTP.value,
        "detail": _("The OTP number has been verified"),
        "data": {},
    }

    status_ = status.HTTP_200_OK


class ResetPasswordResponse(BaseResponse):
    data_ = {
        "code": OperationCode.Reset_Password.value,
        "detail": _("The password reset successfully"),
    }
    status_ = status.HTTP_200_OK


class ForgetPasswordRequestResponse(BaseResponse):
    data_ = {
        "code": OperationCode.Forget_Password.value,
        "detail": _("An OTP number has been sent to email."),
        "data": {},
    }
    status_ = status.HTTP_200_OK

    def with_data(self, user: models.User):
        if user:
            self.data_["data"]["access_token"] = user.get_tokens()["access"]

        return super().with_data()
