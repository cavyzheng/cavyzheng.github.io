from bs4 import BeautifulSoup

# 读取 HTML 文件
html_file = 'index.html'  # 替换为你的 HTML 文件路径
with open(html_file, 'r', encoding='utf-8') as file:
    soup = BeautifulSoup(file, 'lxml')

# 遍历 q1 到 q12，并修改 selectiongroup 和 input 的 name 属性
for i in range(1, 13):  # 从 q1 到 q12
    data_label = f'q{i}'
    selection_group_value = f'单选选项组{i}'

    # 查找所有 data-label="qX" 的元素
    q_elements = soup.find_all(attrs={"data-label": data_label})

    # 遍历这些元素，修改它们内部的 selectiongroup 和 input 的 name 属性
    for element in q_elements:
        # 查找所有拥有 selectiongroup 的子元素（如 div 元素）
        radio_buttons = element.find_all(attrs={"selectiongroup": True})

        # 修改 selectiongroup 属性
        for radio in radio_buttons:
            radio['selectiongroup'] = selection_group_value  # 修改 selectiongroup 为 "单选选项i"

            # 修改对应的 input 元素的 name 属性
            input_element = radio.find('input')
            if input_element:
                input_element['name'] = selection_group_value  # 修改 input 的 name 为 "单选选项i"

# 保存修改后的 HTML 文件
with open('index.html', 'w', encoding='utf-8') as file:
    file.write(str(soup))

print("HTML 文件修改完成！")
