# API 가이드 : Images

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



