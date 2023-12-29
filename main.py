from label_generator import gen_faces_xml
from record_face import record_face


def run():
    record_face()
    gen_faces_xml()


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    run()
