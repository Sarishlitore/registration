from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, EmailField
from wtforms.validators import Length, EqualTo, InputRequired


class LoginForm(FlaskForm):
    email = EmailField('Email: ')
    psw = PasswordField('Пароль: ', validators=[InputRequired()])
    remember = BooleanField('Запомнить', default=False)
    submit = SubmitField('Войти')


class RegistrationForm(FlaskForm):
    name = StringField('Имя: ', validators=[InputRequired(message='Введите имя'),
                                            Length(min=1, max=64, message="Имя должно быть от 1 до 64 символов")])
    email = EmailField('Email: ')
    psw = PasswordField('Пароль: ', validators=[InputRequired(message='Введите пароль'),
                                                Length(min=4, max=20,
                                                       message="Пароль должен быть от 4 до 20 символов")])
    psw2 = PasswordField('Повтор пароля: ', validators=[InputRequired(message='Повторите пароль'),
                                                        EqualTo('psw', message='Пароли не совпадают')])
    submit = SubmitField('Регистрация')
