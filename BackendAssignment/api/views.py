import json
import jwt
from api.models import User, Post
from django.http import JsonResponse
from api.serializers import (
    UserCreateSerializer, 
    UserLoginSerializer,
    PostCreateSerializer
)
from django.views.decorators.http import require_http_methods
from BackendAssignment.settings import UTF_FORMAT, SECRET_KEY


@require_http_methods(["GET"])
def info(request):
    message_response = {
        "message": "This is an introduction to api-app in BackendAssignment django-project!!"
    }
    return JsonResponse(data=message_response, status=200)


@require_http_methods(["POST"])
def create_user(request):
    request_body = json.loads(request.body)
    create_user_data = UserCreateSerializer(data=request_body)
    if create_user_data.is_valid():
        post_data = create_user_data.validated_data
        try:
            api_user = User(
                email_id=post_data['email_id'],
                pwd_hash=User.hash_pwd(post_data["password"]),
                full_name=post_data['full_name']
            )
            api_user.save()
        except Exception as ex:
            return JsonResponse(data={"error": str(ex)}, status=500)    
        return JsonResponse(
            data={"Message": f"User account created successfully for {post_data['email_id']}"}, status=201
        )
    else:
        return JsonResponse(data=create_user_data.errors, status=400)
    

@require_http_methods(["POST"])
def login_user(request):
    request_body = json.loads(request.body)
    login_user_data = UserLoginSerializer(data=request_body)
    if login_user_data.is_valid():
        post_data = login_user_data.validated_data
        api_user = User.objects.get(email_id=post_data["email_id"])
        pwd_validation = api_user.validate_password(password=post_data["password"])
        if not pwd_validation:
            return JsonResponse(data={"Message": f"Unknown user credentials!"}, status=401)
        return JsonResponse(data=api_user.generate_token(), status=200)
    else:
        return JsonResponse(data=login_user_data.errors, status=400)


@require_http_methods(["POST"])
def create_post(request):

    request_headers = request.headers
    try:
        authorization_token = request_headers["Authorization"]
    except KeyError as ex:
        return JsonResponse(data={"Message": f"Missing Authorization header, {str(ex)}!"}, status=401)
    try:
        _d = jwt.decode(authorization_token, SECRET_KEY, algorithms="HS256")
    except Exception as ex:
        return JsonResponse(data={"Message": f"Signature verification failed!"}, status=401)
    if not isinstance(_d, dict) or not _d.get("email"):
        return JsonResponse(data={"Message": f"Bad token!"}, status=401)
    user = User.objects.get(email_id=_d.get("email"))
    if not user:
        return JsonResponse(data={"Message": f"Bad token!"}, status=401)
    
    request_body = json.loads(request.body)
    create_post_data = PostCreateSerializer(data=request_body)
    if create_post_data.is_valid():
        post_data = create_post_data.validated_data
        try:
            user_post = Post(post_content=post_data["post_content"], user=user)
            user_post.save()
        except Exception as ex:
            return JsonResponse(data={"error": str(ex)}, status=500)    
        return JsonResponse(data={"Message": f"Post created successfully!"}, status=201)
    else:
        return JsonResponse(data=create_post_data.errors, status=400)
