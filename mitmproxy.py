from mitmproxy import http
import json

listData = {
    "pageNum": 1,
    "pageSize": 10,
    "total": 38,
    "pages": 4,
    "list": []
}
responseM = {
    "code": 200,
    "message": "SUCCESS",
    "data": listData.copy()
}


def response(f):
    request = f.request
    response = f.response
    if(request.url.find('/cms') != -1 and request.method != "OPTIONS"):
        response.status_code = 200
        res = responseM.copy()
        if(request.url.find('/proj/template111/page') != -1):
            res.data.list = [
                {
                    "id": 75,
                    "workoutName": "ABS TEST 30 INTERMEDIATE",
                    "coverImgUrl": "cms/proj/workoutVideo105/cover/5674a9ef971e4911b2c22e41001b5b7e.png?alt=media&name=0d885f3ff28f4e79ae792b53c03e1edf.png",
                    "detailImgUrl": "cms/proj/workoutVideo105/detail/6fe00baae30a45ef8e7e0f1fe65ae9ec.png?alt=media&name=0d885f3ff28f4e79ae792b53c03e1edf.png",
                    "videoPlayUrl": "cms/proj/workoutVideo/video/5766bc40a4304ef78efdaa3381506f56.m3u8?alt=media&name=5766bc40a4304ef78efdaa3381506f56.m3u8",
                    "videoUrl": "cms/proj/workoutVideo/video/7775523339434652b8b6377d66bd714b.m3u8?alt=media&name=7775523339434652b8b6377d66bd714b.m3u8",
                    "duration": 330077,
                    "focus": "Abs & Core",
                    "difficulty": "Intermediate",
                    "calorie": 26,
                    "videoCount": 3,
                    "status": 1
                },
            ]
        if(request.url.find('/proj/template111/page') != -1):
            res.data.list = [
                {
                    "id": 75,
                    "workoutName": "ABS TEST 30 INTERMEDIATE",
                    "coverImgUrl": "cms/proj/workoutVideo105/cover/5674a9ef971e4911b2c22e41001b5b7e.png?alt=media&name=0d885f3ff28f4e79ae792b53c03e1edf.png",
                    "detailImgUrl": "cms/proj/workoutVideo105/detail/6fe00baae30a45ef8e7e0f1fe65ae9ec.png?alt=media&name=0d885f3ff28f4e79ae792b53c03e1edf.png",
                    "videoPlayUrl": "cms/proj/workoutVideo/video/5766bc40a4304ef78efdaa3381506f56.m3u8?alt=media&name=5766bc40a4304ef78efdaa3381506f56.m3u8",
                    "videoUrl": "cms/proj/workoutVideo/video/7775523339434652b8b6377d66bd714b.m3u8?alt=media&name=7775523339434652b8b6377d66bd714b.m3u8",
                    "duration": 330077,
                    "focus": "Abs & Core",
                    "difficulty": "Intermediate",
                    "calorie": 26,
                    "videoCount": 3,
                    "status": 1
                },
            ]
        response.text = json.dumps(res)
