from label_generator import gen_faces_xml
from predict_face import predict_face
from record_face import record_face


def run():
    record_face()
    gen_faces_xml()
    predict_face("zhangyuhang")


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    run()
