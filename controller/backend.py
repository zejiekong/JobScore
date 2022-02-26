# -*- coding: utf-8 -*-

# Register [hash password with salt, store in db]

import bcrypt

username = input(username) # username from frontend
passwd = input(password)

salt = bcrypt.gensalt()
hashed = bcrypt.hashpw(passwd, salt)

# edit: if username is in the database, perform the following
if bcrypt.checkpw(passwd, hashed):
    print("match pw")
else:
    print("does not match pw")




