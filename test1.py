"""
 * Project name(项目名称)：Python_tempfile模块
 * Package(包名): 
 * File(文件名): test1
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/30 
 * Time(创建时间)： 21:12
 * Version(版本): 1.0
 * Description(描述)：
 tempfile   模块函数	                        功能描述
tempfile.TemporaryFile(mode='w+b', buffering=None, encoding=None, newline=None, suffix=None, prefix=None, dir=None)
                                    创建临时文件。该函数返回一个类文件对象，也就是支持文件 I/O。
tempfile.NamedTemporaryFile(mode='w+b', buffering=None, encoding=None, newline=None, suffix=None, prefix=None, dir=None, delete=True)
                                            创建临时文件。该函数的功能与上一个函数的功能大致相同，只是它生成的临时文件在文件系统中有文件名。
tempfile.SpooledTemporaryFile(max_size=0, mode='w+b', buffering=None, encoding=None, newline=None, suffix=None, prefix=None, dir=None)
                                    创建临时文件。与 TemporaryFile 函数相比，当程序向该临时文件输出数据时，会先输出到内存中，
                                    直到超过 max_size 才会真正输出到物理磁盘中。
tempfile.TemporaryDirectory(suffix=None, prefix=None, dir=None)	生成临时目录。
tempfile.gettempdir()	获取系统的临时目录。
tempfile.gettempdirb()	与 gettempdir() 相同，只是该函数返回字节串。
tempfile.gettempprefix()	返回用于生成临时文件的前缀名。
tempfile.gettempprefixb()	与 gettempprefix() 相同，只是该函数返回字节串。
 """
import os.path
import tempfile

if __name__ == '__main__':
    file = tempfile.TemporaryFile()
    print(file.name)
    file.write("hello world1\n".encode("utf-8"))
    file.write("hello world2\n".encode("utf-8"))
    file.write("hello world3\n".encode("utf-8"))
    file.write("hello world4\n".encode("utf-8"))
    file.write("hello world5\n".encode("utf-8"))

    file.seek(0)
    for line in file.readlines():
        print(line.decode("utf-8"), end="")

    fileDir = file.name
    print(os.path.exists(fileDir))
    file.close()
    print(os.path.exists(fileDir))

    with tempfile.TemporaryFile() as file1:
        file1.write(b'test')
        file1.seek(0)
        print(file1.read())
        print(file1.name)
        fileDir = file1.name
        print(os.path.exists(fileDir))
    print(os.path.exists(fileDir))

    # 10天，108个项目，241个文件，288347个字符，9480行代码，Python基础部分已学完
