from django.db import models
from django.contrib.auth.models import User

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


class CustomUser(User):
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
    user_type = models.IntegerField(choices=USER_TYPE, verbose_name='Тип пользователя: ')
    phone_number = models.CharField('Номер телефона: ', max_length=16)
    age = models.PositiveIntegerField()
    gender = models.IntegerField(choices=GENDER_TYPE, verbose_name='Гендер: ')
    born_data = models.CharField('Дата рождения: ', max_length=16)
    orientation = models.IntegerField(choices=ORIENTATION, verbose_name='Ориентация: ')
    mbti_type = models.IntegerField(choices=MBTI_TYPE, verbose_name='Тип личности(16-типов): ')
    sabg_type = models.IntegerField(choices=SABG_TYPE, verbose_name='Кто вы по жизни?: ')
    place_of_residence = models.CharField('Место жительства: ', max_length=32)
    telegramm = models.CharField('Ваш телеграмм: ', max_length=36)
