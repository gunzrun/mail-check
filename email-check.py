import re
import sys


def check_mail(mail):
    """
    Check if added e-mail is correct.
    :param mail: e-mail, string
    :return: message, string
    """
    mail_list = mail.split("@")
    if len(mail_list) != 2:
        result = "incorrect mail. Must contain the only one @"
        return result

    username = mail_list[0]
    username_regex = "^[a-zA-Z0-9-_]+$"
    username_match = re.compile(username_regex)
    website = ".".join(mail_list[-1].split(".")[:-1])
    website_regex = "^[a-zA-Z0-9]+$"
    website_match = re.compile(website_regex)
    extension = mail_list[-1].split(".")[-1]

    if username_match.search(username) is None:
        result = 'Username {} is incorrect. The username can only contain letters, digits, dashes and underscores'.format(
            username)
        return result

    if website_match.search(website) is None:
        result = 'Website name {} is incorrect. The website name can only have letters and digits'.format(website)
        return result

    if extension.isalpha() and len(extension) <= 3:
        result = "Email address {} is correct".format(mail)
    else:
        result = "Extension {} is incorrect. The extension can only contain letters and maximum length is 3".format(
            extension)

    return result


def main():
    if len(sys.argv) == 2:
        input_mail = sys.argv[1]
    else:
        if len(sys.argv) > 2:
            print("Too many parameters")
            sys.exit(1)
        if len(sys.argv) < 2:
            print("Mail not defined. Please insert email")
            input_mail = input()
    result = check_mail(input_mail)

    return print(result)


if __name__ == "__main__":
    main()
