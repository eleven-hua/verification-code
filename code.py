import random
from PIL import Image,ImageDraw,ImageFont
import io


# 定义随机颜色方法
def get_random_color():
    R = random.randrange(255)
    G = random.randrange(255)
    B = random.randrange(255)

    return (R, G, B)


# 定义随机验证码
def test_captcha(request):
    # 定义背景颜色
    bg_color = get_random_color()
    # 定义画布大小 宽，高
    img_size = (150, 80)
    # 定义画笔 颜色种类,画布，背景颜色
    image = Image.new("RGB", img_size, bg_color)
    # 定义画笔对象 图片对象,颜色类型
    draw = ImageDraw.Draw(image, 'RGB')
    # 定义随机字符
    source = '0123456789asdfghjkl'
    # 定义四个字符
    # 定义好容器，用来接收随机字符串
    code_str = ''
    for i in range(4):
        # 获取随机颜色 字体颜色
        text_color = get_random_color()
        # 获取随机字符串
        tmp_num = random.randrange(len(source))
        # 获取字符集
        random_str = source[tmp_num]
        # 将随机生成的字符串添加到容器中
        code_str += random_str
        # 将字符画到画布上 坐标，字符串，字符串颜色，字体
        # 导入系统真实字体,字号
        my_font = ImageFont.truetype("c:\\windows\\Fonts\\arial.ttf", 20)
        draw.text((10 + 30 * i, 20), random_str, text_color, font=my_font)
    # 使用io获取一个缓存区
    buf = io.BytesIO()
    # 将图片保存到缓存区
    image.save(buf, 'png')

    # 将随机码存储到session中
    request.session['code'] = code_str

    # 第二个参数声明头部信息
    return HttpResponse(buf.getvalue(), 'image/png')