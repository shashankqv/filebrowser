import os
import spwd
import crypt
from filebrowser.settings import ROOT_LOGIN_ENABLED 
import json



def login(user, password):
    """Tries to authenticate a user.
    Returns True if the authentication succeeds, else the reason
    (string) is returned."""
    try:
        enc_pwd = spwd.getspnam(user)[1]
        if enc_pwd in ["NP", "!", "", None]:
            return "user '%s' has no password set" % user
        if enc_pwd in ["LK", "*"]:
            return "account is locked"
        if enc_pwd == "!!":
            return "password has expired"
        # Encryption happens here, the hash is stripped from the
        # enc_pwd and the algorithm id and salt are used to encrypt
        # the password.
        if crypt.crypt(password, enc_pwd) == enc_pwd:
            return True
        else:
            return "incorrect password"
    except KeyError:
        return "user '%s' not found" % user
    return "unknown error"



def loginvalidate(username):
    if not ROOT_LOGIN_ENABLED and username == "root":
        print "Root Login not allowed"
        return False
    else:
        return True



def getdirectorylist(basedir):
    pass


def path_to_dict(path):
    d = {'name': os.path.basename(path)}
    if os.path.isdir(path):
        d['type'] = "directory"
        d['children'] = [path_to_dict(os.path.join(path,x)) for x in os.listdir(path)]
    else:
        d['type'] = "file"
    #return json.dumps(d)
    return d


def type_of_file(path):
    d = {'name': os.path.basename(path)}
    if os.path.isdir(path):
        return "dir"
    else:
        return "file"


def path_to_dict_1_level(path):
    d = {'name': os.path.basename(path)}
    if os.path.isdir(path):
        d['type'] = "directory"
        f = {}
        d['children'] = [os.path.join(path,x) for x in os.listdir(path)]
    else:
        d['type'] = "file"
    return json.dumps(d)