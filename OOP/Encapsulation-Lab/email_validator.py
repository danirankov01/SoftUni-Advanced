class EmailValidator:
    def __init__(self, min_length, mails, domains):
        self.min_length = min_length
        self.mails = mails
        self.domains = domains

    def __is_name_valid(self, name):
        return len(name) >= self.min_length

    def __is_mail_valid(self, mails):
        return mails in self.mails

    def __is_domain_valid(self, domain):
        return domain in self.domains

    def validate(self, email):
        index_of_at = email.index("@")
        username = email[:index_of_at]
        is_username_valid = self.__is_name_valid(username)

        index_of_mail = email.index(".")
        mail = email[index_of_at + 1: index_of_mail]
        is_mail_valid = self.__is_mail_valid(mail)

        domain = email[index_of_mail + 1:]
        is_domain_valid = self.__is_domain_valid(domain)

        if is_username_valid and is_mail_valid and is_domain_valid:
            return True

        return False


mails = ["gmail", "softuni"]
domains = ["com", "bg"]
email_validator = EmailValidator(6, mails, domains)
print(email_validator.validate("danirankov@gmail.com"))


class Person:
    def __init__(self, name):
        self.name = name


p = Person("Dani")
print(getattr(p, "age", "None"))
