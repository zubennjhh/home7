from django import forms
from django.contrib.auth.forms import UserCreationForm
from . import models

ADMIN = 1
VIPClient = 2
CLIENT = 3

USER_TYPE = (
    (ADMIN, "ADMIN"),
    (VIPClient, "VIPClient"),
    (CLIENT, "CLIENT"),
)

MALE = 1
FEMALE = 2
BIGENDER = 3
POLIGENDER = 4
TRANSGENDER = 5
AGENDER = 6
INTERGENDER = 7

GENDER_TYPE = (
    (MALE, "MALE"),
    (FEMALE, "FEMALE"),
    (BIGENDER, "BIGENDER"),
    (POLIGENDER, "POLIGENDER"),
    (TRANSGENDER, "TRANSGENDER"),
    (AGENDER, "AGENDER"),
    (INTERGENDER, "INTERGENDER"),
)

BOSS_OF_GYM = 1
GAY = 2
LESBIAN = 3
BISEXUAL = 4

ORIENTATION = (
    (BOSS_OF_GYM, 'STRAIGHT'),
    (GAY, 'GAY'),
    (LESBIAN, 'LESBIAN'),
    (BISEXUAL, 'BISEXUAL'),
)

INTJ = 1
INTP = 2
ENTJ = 3
ENTP = 4
INFJ = 5
INFP = 6
ENFJ = 7
ENFP = 8
ISTJ = 9
ISFJ = 10
ESTJ = 11
ESFJ = 12
ISTP = 13
ISFP = 14
ESTP = 15
ESFP = 16

MBTI_TYPE = (
    (INTJ, 'Architect'),
    (INTP, 'Logician'),
    (ENTJ, 'Commander'),
    (ENTP, 'Debater'),
    (INFJ, 'Advocate'),
    (INFP, 'Mediator'),
    (ENFJ, 'Protagonist'),
    (ENFP, 'Campaigner'),
    (ISTJ, 'Logistician'),
    (ISFJ, 'Defender'),
    (ESTJ, 'Executive'),
    (ESFJ, 'Consul'),
    (ISTP, 'Virtuoso'),
    (ISFP, 'Adventurer'),
    (ESTP, 'Entrepreneur'),
    (ESFP, 'Entertainer'),
)

SIGMA = 1
ALPHA = 2
BETA = 3
GIGACHAD = 4

SABG_TYPE = (
    (SIGMA, 'SIGMA'),
    (ALPHA, 'ALPHA'),
    (BETA, 'BETA'),
    (GIGACHAD, 'GIGACHAD'),
)


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(required=True)
    born_data = forms.CharField(required=True)
    user_type = forms.ChoiceField(choices=USER_TYPE, required=True)
    gender = forms.ChoiceField(choices=GENDER_TYPE, required=True)
    orientation = forms.ChoiceField(choices=ORIENTATION, required=True)
    mbti_type = forms.ChoiceField(choices=MBTI_TYPE, required=True)
    sabg_type = forms.ChoiceField(choices=SABG_TYPE, required=True)
    place_of_residence = forms.CharField(required=True)
    telegramm = forms.CharField(required=True)

    class Meta:
        model = models.CustomUser
        fields = (
            "username",
            "email",
            "password1",
            "password2",
            "first_name",
            "last_name",
            "phone_number",
            "born_data",
            "user_type",
            "gender",
            "orientation",
            "mbti_type",
            "sabg_type",
            "place_of_residence",
            "telegramm",
        )

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
