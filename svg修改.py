# -*- coding: utf-8 -*-
import os

with open(r'images\index\ub_selected.svg', 'r', encoding='utf-8') as file:
            content = file.read()
            
# 设置文件夹路径
folder_path = r'images\index'  # 替换为包含 SVG 文件的文件夹路径
# 批量处理文件
for i in range(21, 158):  # 修改范围从u21到u157
    file_name = f'u{i}_selected.svg'
    file_path = os.path.join(folder_path, file_name)
    
    # 检查文件是否存在
    if os.path.exists(file_path):
        # 打开并将修改后的内容写入文件
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
        
        print(f'{file_name} completed')
    else:
        print(f'{file_name} not exsit')
