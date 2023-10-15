from collections.abc import Iterable
import bcrypt, jwt
from django.db import models
from BackendAssignment.settings import UTF_FORMAT, SECRET_KEY



class User(models.Model):
    id = models.AutoField(primary_key=True, null=False, db_index=True)
    email_id = models.EmailField(max_length=256, null=False, unique=True, db_index=True)
    pwd_hash = models.CharField(max_length=256, null=False)
    full_name = models.CharField(max_length=256, null=False)
    is_active = models.BooleanField(null=False, default=False)
    is_admin = models.BooleanField(null=False, default=False)


    @staticmethod
    def hash_pwd(password) -> str:
            _hpwd = bcrypt.hashpw(password.encode(UTF_FORMAT), bcrypt.gensalt())
            return _hpwd.decode(UTF_FORMAT)

    def validate_password(self, password) -> bool:
            return bcrypt.checkpw(password.encode(UTF_FORMAT), self.pwd_hash.encode(UTF_FORMAT))

    def generate_token(self) -> dict:
            return {"access_token": jwt.encode({"email": self.email_id}, SECRET_KEY, algorithm="HS256")}


class Post(models.Model):
    id = models.AutoField(primary_key=True, null=False, db_index=True)
    post_content = models.CharField(max_length=1024, null=False)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
