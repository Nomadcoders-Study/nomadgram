# API 가이드

## Users

#### 1. 최근 가입 유저리스트 조회 ( 5명 )

> GET /users/explore/

**Result**

```
HTTP 200 OK
Content-Type: application/json

[
    {
        "id": 3,
        "profile_image": null,
        "username": "nomad",
        "name": "nomad kim"
    },
    {
        "id": 2,
        "profile_image": null,
        "username": "nouveau",
        "name": "nouveau dev"
    },
    {
        "id": 1,
        "profile_image": null,
        "username": "admin",
        "name": "admin"
    }
]
```

#### 2. 팔로우 신청

> POST /users/\<user_id>/follow/

**Result**

```
HTTP 200 OK  
Content-Type: application/json
```

#### 3. 팔로우 해제

> POST /users/\<user_id>/unfollow/

**Result**

```
HTTP 200 OK
Content-Type: application/json
```

#### 4. 특정 유저 프로필 조회

> GET /users/\<username>/

**Result**

```
HTTP 200 OK
Content-Type: application/json

{
    "username": "nouveau",
    "name": "nouveau dev",
    "bio": null,
    "website": null,
    "post_count": 2,
    "followers_count": 0,
    "following_count": 0,
    "images": [
        {
            "id": 4,
            "file": "/media/ImageName.png",
            "comment_count": 0,
            "like_count": 1
        },
        {
            "id": 3,
            "file": "/media/E18488E185B5E1848CE185B5E186B7.jpeg",
            "comment_count": 2,
            "like_count": 2
        }
    ]
}
```

#### 5. 특정 유저 팔로워 조회

> GET /users/\<username>/followers/

**Result**

```
HTTP 200 OK
Content-Type: application/json

[
    {
        "id": 1,
        "profile_image": null,
        "username": "yykim",
        "name": "yykim"
    }
]
```

#### 6. 특정 유저 팔로잉 조회

> GET /\<username>/following/

**Result**

```
HTTP 200 OK
Content-Type: application/json

[
    {
        "id": 3,
        "profile_image": null,
        "username": "nomad",
        "name": "nomad kim"
    }
]
```


## Images

#### 1. 팔로잉한 유저 피드 출력

> GET /images/

**Result**

```
HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "id": 2,
        "file": "/media/2.jpeg",
        "location": "Busan",
        "caption": "부산!!",
        "comments": [],
        "like_count": 0,
        "creator": {
            "username": "nomad",
            "profile_image": null
        }
    }
]
```

#### 2. 특정 게시물 좋아요

> POST /images/\<image_id>/like/

**Result**

```
HTTP 201 Created
Content-Type: application/json
```

#### 3. 특정 게시물 좋아요 해제

> DELETE /images/\<image_id>/unlike/

**Result**

```
HTTP 204 No Content
Content-Type: application/json
```


#### 4. 특정 이미지에 코멘트 등록

> GET /images/\<image_id>/comments/

> Param : {"message":"ㅇㅇㅇ"}

**Result**

```
HTTP 201 Created
Content-Type: application/json

{
    "id": 5,
    "message": "ㅇㅇㅇ",
    "creator": {
        "username": "admin",
        "profile_image": null
    }
}
```


#### 5. 본인이 작성한 코멘트 삭제

> GET /images/comments/\<comment_id>/

**Result**

```
HTTP 204 No Content
Content-Type: application/json
```



