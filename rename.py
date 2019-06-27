import os

os.chdir('D:/jwtar/Desktop/School/Python/Rename Project/files')

for f in os.listdir():
    file_name, file_ext = os.path.splitext(f)
    f_order, f_name, f_num = file_name.split(' ')

    f_name = f_name.strip()
    f_order = f_order.strip()
    f_num = f_num.strip().zfill(2)

    new_name ='{} {} {}{}'.format(f_num, f_name, f_order, file_ext)

    os.rename(f, new_name)
