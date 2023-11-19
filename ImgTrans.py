from PIL import Image
import os

# 输入文件夹和输出文件夹的路径
input_folder = './input'  # 替换为包含要转换的图片文件的文件夹路径
output_folder = './output'  # 替换为存放输出图片文件的文件夹路径
flag = 0
number = 0
# 创建输出文件夹（如果不存在）
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 获取要输出的图片格式
output_format = input("请输入要输出的图片格式（例如：jpg, png, bmp，webp）: ")

# 询问用户是否要修改图片尺寸
resize_option = input("是否要修改图片尺寸？ (yes/no): ")

if resize_option.lower() == 'yes':
    print("1.常用尺寸\n")
    print("2.手动输入尺寸\n")
    print("3.图片默认尺寸\n")
    flag = int(input("输入你想要的模式(or 1, or 2, or 3)："))
    if flag == 1:
        print("1.1寸照片\n")
        print("2.身份证大头照\n")
        print("3.2寸照片\n")
        print("4.小二寸(护照)\n")
        print("5.5寸照片\n")
        print("6.6寸照片\n")
        print("7.7寸照片\n")
        print("8.8寸照片\n")
        print("9.10寸照片\n")
        print("10.12寸照片\n")
        print("11.15寸照片\n")
        print("12.图片默认尺寸\n")
        number = int(input("选择常用图片尺寸："))
        if number == 1:
            #new_width = 413
            #new_height = 295
            new_width = 295
            new_height = 413
        elif number == 2:
            #new_width = 390
            #new_height = 260
            new_width = 260
            new_height = 390
        elif number == 3:
            #new_width = 626
            #new_height = 413
            new_width = 413
            new_height = 626
        elif number == 4:
            #new_width = 567
            #new_height = 390
            new_width = 390
            new_height = 567
        elif number == 5:
            #new_width = 1200
            #new_height = 840
            new_width = 840
            new_height = 1200
        elif number == 6:
            #new_width = 1440
            #new_height = 960
            new_width = 960
            new_height = 1440
        elif number == 7:
            #new_width = 1680
            #new_height = 1200
            new_width = 1200
            new_height = 1680
        elif number == 8:
            #new_width = 1920
            #new_height = 1440
            new_width = 1440
            new_height = 1920
        elif number == 9:
            #new_width = 2400
            #new_height = 1920
            new_width = 1920
            new_height = 2400
        elif number == 10:
            #new_width = 2500
            #new_height = 2000
            new_width = 2000
            new_height = 2500
        elif number == 11:
            #new_width = 3000
            #new_height = 2000
            new_width = 2000
            new_height = 3000
        elif number == 12:
            new_width, new_height = None, None
        else:
            print("错误选择，使用图片默认尺寸执行！\n")
            new_width, new_height = None, None

    elif flag == 2:
        new_width = int(input("请输入新的宽度(像素): "))
        new_height = int(input("请输入新的高度(像素): "))
    elif flag == 3:
        new_width, new_height = None, None
    else:
        print("错误选择，使用图片默认尺寸执行！\n")
        new_width, new_height = None, None
else:
    new_width, new_height = None, None

# 遍历输入文件夹中的所有文件
for filename in os.listdir(input_folder):
    # 构建输入文件的完整路径
    input_file = os.path.join(input_folder, filename)

    try:
        # 使用Pillow的Image.open函数来自动检测输入图片的格式
        img = Image.open(input_file)

        # 如果用户要修改尺寸，使用用户输入的尺寸
        if new_width is not None and new_height is not None:
            img = img.resize((new_width, new_height))
        
#        if img.mode == 'RGBA' and output_format == 'jpg':
#            # 如果输入图片为RGBA模式，而输出格式是JPEG，需要转换为RGB模式
#            img = img.convert('RGB')

        if img.mode == 'RGBA' and output_format == 'jpg':
            # 如果输入图片为RGBA模式，而输出格式是JPEG，需要转换为RGB模式
            img = img.convert('RGB')

        # 构建输出文件的完整路径，将文件名的扩展名更改为指定的格式
        output_file = os.path.join(output_folder, os.path.splitext(filename)[0] + '.' + output_format)

        # 保存图片为指定格式
        if output_format == 'jpg':
            output_format = 'jpeg'

        img.save(output_file, output_format)

        if output_format == 'jpeg':
            output_format = 'jpg'

        print(f"已转换 {filename} 到 {output_format} 格式")
    except Exception as e:
        print(f"无法处理 {filename}: {e}")

print("转换完成")
