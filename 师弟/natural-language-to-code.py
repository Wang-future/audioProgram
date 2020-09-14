import re

input_file = open("input.txt", "r", encoding='utf-8')
interphase_file = open("interphase.txt", "w+", encoding='utf-8')

lines = input_file.readlines()
# 记录引号、注释的内容及位置，提前取出存在列表中，防止后续误替换字符串内的关键字
quotation_list = []
annotation_list = []
quotation_pos = 0
annotation_pos = 0

for line in lines:
    # 保留字符串内的换行符，防止python写入文件时转义
    line = line.replace(r"\n", r'\\n')
    # 匹配双引号内的内容
    pattern = re.compile(r'("(\\"|[^"])*")')
    result = pattern.findall(line)

    for i in range(len(result)):
        ls = []
        string = result[i][0].replace(r"\\", r"\\\\")
        ls.append(string)
        quotation_list = quotation_list + ls
    line = re.sub(r'("(\\"|[^"])*")', '""', line)

    # 提取注释
    find_annotation = re.search("添加注释：", line)
    if find_annotation:
        line = line.replace("\n", '￥\n')
    line = line.replace("添加注释：", '￥')
    pattern = re.compile(r'(\￥.*\￥)')
    result1 = pattern.findall(line)

    for i in range(len(result1)):
        ls = []
        string = result1[i]
        annotation_list = annotation_list + result1
    line = re.sub(r'(\￥.*\￥)', '￥￥', line)
    find_class = re.search("创建类", line)

    if find_class:
        line = line + '`\n'

    ch_comma_cnt = line.count('，')
    find_ch_comma = line.find('，')
    # 替换关键字
    line = line.replace("零", "0")
    line = line.replace("一", "1")
    line = line.replace("二", "2")
    line = line.replace("三", "3")
    line = line.replace("四", "4")
    line = line.replace("五", "5")
    line = line.replace("六", "6")
    line = line.replace("七", "7")
    line = line.replace("八", "8")
    line = line.replace("九", "9")
    line = line.replace("+", " + ")
    line = line.replace("-", " - ")
    line = line.replace("*", " * ")
    line = line.replace("/", " / ")
    line = line.replace("加", " + ")
    line = line.replace("自减", "--")
    line = line.replace("减", " - ")
    line = line.replace("乘以", " * ")
    line = line.replace("乘", " * ")
    line = line.replace("除", " / ")
    line = line.replace("^", " ^ ")
    line = line.replace("异或", " ^ ")
    line = line.replace("&", " & ")
    line = line.replace("位且", " & ")
    line = line.replace("|", " | ")
    line = line.replace("位或", " | ")
    line = line.replace("的函数", ".函数")

    line = line.replace("枚举类型", "enum ")
    line = line.replace("枚举常量为", "举值为")
    line = line.replace("的变量", " ")
    line = line.replace("字符型数组", "char []")
    line = line.replace("暂停", 'system("pause")')
    line = line.replace(">", " > ")
    line = line.replace("<", " < ")
    line = line.replace("!", " ! ")
    line = line.replace("=", " = ")
    line = line.replace("&&", " && ")
    line = line.replace("<<", " << ")
    line = line.replace("||", " || ")
    line = line.replace("析构", "~")
    line = line.replace("声明类型", "")
    line = line.replace("定义类型", "")
    line = line.replace("创建类型", "")
    find_class = re.search("，模板类型", line)
    if find_class:
        line = line.replace("，参数", ">(")
    line = line.replace("，模板类型", "<")
    line = line.replace("否则如果", "else 如")
    line = line.replace("否则", "otherwise")
    line = line.replace("取模", "取余")
    line = line.replace("查看", "switch (")
    line = line.replace("匹配", "case ")
    line = line.replace("默认", "default")
    line = line.replace("大于等于", " >= ")
    line = line.replace("小于等于", " <= ")
    line = line.replace("大于", " > ")
    line = line.replace("小于", " < ")
    line = line.replace("不是", " ! ")
    line = line.replace("非", " ! ")
    line = line.replace("不等于", " != ")
    line = line.replace("赋值", " = ")
    line = line.replace("等于", " = ")
    line = line.replace("别名替换", "typedef ")
    line = line.replace("引用", "&")
    line = line.replace("实例", "*new ")
    line = line.replace("释放数组", "delete() ")
    line = line.replace("释放", "delete ")
    line = line.replace("虚函数", "函数virtual ")
    line = line.replace("模板函数", "函数template<typename T>")
    line = line.replace("结构体", "struct ")
    line = line.replace("结构变量", "} structVar ")
    line = line.replace("宏定义", "define ")
    line = line.replace(",", ", ")
    line = line.replace("如果", "如")
    line = line.replace("且", " && ")
    line = line.replace("及", " << ")
    line = line.replace("或", " || ")
    line = line.replace("字符串数组", "char **")
    line = line.replace("字符串", "string ")
    line = line.replace("字符", "char ")
    line = line.replace("长", "long ")
    line = line.replace("友元类", "friend ")
    line = line.replace("友元", "friend ")
    line = line.replace("尝试", "try{")
    line = line.replace("抛出", "throw ")
    line = line.replace("短整型", "short ")
    line = line.replace("整型数组", "int []")
    line = line.replace("双精度浮点数数组", "double []")
    line = line.replace("浮点数数组", "float []")
    line = line.replace("小数数组", "float []")
    line = line.replace("整型", "int ")
    line = line.replace("自动变量", "auto ")
    line = line.replace("整数", "int ")
    line = line.replace("双精度浮点数", "double ")
    line = line.replace("浮点数", "float ")
    line = line.replace("浮点型", "float ")
    line = line.replace("命名空间", "命名间")
    line = line.replace("std", "using namespace std")
    line = line.replace("循环，", "循环")
    line = line.replace("为真", " = true")
    line = line.replace("为假", " = false")
    line = line.replace("真", "true")
    line = line.replace("假", "false")
    line = line.replace("打印", "cout << ")
    line = line.replace("输出", "cout << ")
    line = line.replace("接受输入", "cin >> ")
    line = line.replace("接受", "cin >> ")
    line = line.replace("输入", "cin >> ")
    line = line.replace("导入", "#include <")
    line = line.replace("！", "")
    line = line.replace("开始", "int main(){")
    line = line.replace("结束", "}")
    line = line.replace("，无参数", "(")
    line = line.replace("，参数", "(")
    line = line.replace("参数", "(")
    line = line.replace("，元素", "元素 = {")
    line = line.replace("写文件", "ofstream ")
    line = line.replace("读文件", "ifstream ")
    line = line.replace("内联", "inlinee")
    line = line.replace("指针取值", "*")
    line = line.replace("指针取址", "&")
    line = line.replace("取值", "*")
    line = line.replace("取址", "&")
    line = line.replace("静态", "static ")
    line = line.replace("常量", "const ")
    line = line.replace("带符号", "signed ")
    line = line.replace("无符号", "unsigned ")
    line = line.replace("中止", "continue")
    line = line.replace("公共继承", " :public ")
    line = line.replace("公有继承", " :public ")
    line = line.replace("保护继承", " :protected ")
    line = line.replace("私有继承", " :public ")
    line = line.replace("公共", "public: \n")
    line = line.replace("公有", "public: \n")
    line = line.replace("私有", "private: \n")
    line = line.replace("保护", "protected: \n")
    line = line.replace("退出", "break")
    line = line.replace("，返回值", "传回")
    line = line.replace("，返回类型", "回型")
    line = line.replace("返回", "return ")
    line = line.replace("左移", " << ")
    line = line.replace("右移", " >> ")
    line = line.replace("空", "void")
    line = line.replace("枚举", "enum ")
    line = line.replace("举值为", " {")
    line = line.replace("的数据成员", ".")
    line = line.replace("创建类", "class ")
    line = line.replace("定义类", "class ")
    line = line.replace("声明类", "class ")
    line = line.replace("自增", "++")
    line = line.replace("指针", "*")

    find_equal = re.search('=', line)
    find_if = re.search('如', line)
    find_while = re.search('当', line)
    find_array1 = re.search('第', line)
    find_array2 = re.search('个', line)
    used_string_len = 0
    # 将中文表述的“数组第n个”，替换为n-1
    while find_array1 and find_array2:
        array1_pos = line[used_string_len:-1].find('第')
        array2_pos = line[used_string_len:-1].find('个')
        string2 = line[array1_pos + 1 + used_string_len:array2_pos + used_string_len]
        pattern = re.compile(r'\d')
        result = pattern.findall(string2)
        array_size = str(int(result[0]) - 1)
        string2 = re.sub(result[0], array_size, string2, 1)
        line = line[0:array1_pos + used_string_len + 1] + string2 + line[used_string_len + array2_pos:-1] + line[-1]
        used_string_len = array2_pos + 1 + used_string_len
        find_array1 = re.search('第', line[used_string_len:-1])
        find_array2 = re.search('个', line[used_string_len:-1])

    # “如果”和“等于”同时出现时，“等于”意味着“==”，而非“=”
    while find_if:
        if_pos = line.find('如')
        ch_comma_pos = line.find('，')
        while ch_comma_pos < if_pos:
            line = line.replace("，", "@", 1)
            ch_comma_pos = line.find('，')
        for j in range(if_pos, ch_comma_pos):
            if line[j] == '=':
                line = line[:j] + '$' + line[j + 1:]
        line = line.replace("如", "if1 ", 1)
        line = line.replace("，", "@", 1)
        find_if = re.search('如', line)
    line = line.replace("@", "，")

    # “当”和“等于”同时出现时，“等于”意味着“==”，而非“=”
    while find_while:
        if_pos = line.find('当')
        ch_comma_pos = line.find('，')
        while ch_comma_pos < if_pos:
            line = line.replace("，", "@", 1)
            ch_comma_pos = line.find('，')
        for j in range(if_pos, ch_comma_pos):
            if line[j] == '=':
                line = line[:j] + '$' + line[j + 1:]
        line = line.replace("当", "while(", 1)
        line = line.replace("，", "@", 1)
        find_while = re.search('当', line)

    line = line.replace("@", "，")
    find_if = re.search('，', line)
    if_pos = 0
    ch_comma_pos = line.find('，')
    cnt = line.count('，')

    # 中文逗号作为分割句子的标识，根据不同关键字进行不同处理
    for j in range(cnt + 1):
        string = line[if_pos:ch_comma_pos]
        find_if1 = re.search('if1', string)
        find_for = re.search('循环', string)
        find_while1 = re.search('while', string)
        find_modulus = re.search('取余', string)
        find_class1 = re.search('class', string)
        find_cin = re.search('cin', string)
        find_period = re.search('。', string)
        find_func = re.search('函数', string)
        find_return = re.search('传回', string)
        find_define_func = re.search('定义函数', string)
        find_func_type = re.search('回型', string)
        find_left_bracket = re.search(']', string)
        find_array = re.search('数组', string)
        find_element = re.search('元素 = {', string)
        if ch_comma_pos is not -1:
            string = string + '\n'
        if ch_comma_pos == -1:
            string = string + line[ch_comma_pos]

        # 实现对数组的代码转换
        if find_array:
            string = string.replace("第", '[')
            string = string.replace("个", ']')
        if find_element:
            string = string.replace("\n", '};\n')
        if find_left_bracket:
            pattern = re.compile(r'[个0-9]')
            result = pattern.findall(string)
            if result:
                str1 = ""
                for i in result:
                    if i == '个':
                        break
                    str1 = str1 + i
                    array_size_pos = string.find(i)
                    string = string[:array_size_pos] + string[array_size_pos + 1:]
                string = string.replace('[', '[' + str1, 1)
            find_while = string.rfind(']')
            str2 = string[find_while + 1:-1]
            #
            pattern = re.compile(r'[元A-Za-z0-9]')
            result = pattern.findall(str2)
            str1 = ""
            for i in result:
                if i == '元':
                    break
                str1 = str1 + i
                array1_pos = string.rfind(i)
                string = string[:array1_pos] + string[array1_pos + 1:]
            string = string.replace("[", str1 + '[', 1)

        # 实现输入的代码转换
        if find_cin:
            string = string.replace("<<", ">>", 1)

        # 实现函数的代码转换
        if find_func:
            string = string.replace("\n", ")\n", 1)
            if ch_comma_cnt == 0:
                string = string.replace(")\n", "()\n", 1)

        # 实现返回值的代码转换
        if find_return:
            pattern = re.compile(r'[\(,A-Za-z0-9]')
            result = pattern.findall(string, find_return.span()[0] + 2)
            if result:
                str1 = ""
                for i in result:
                    if i is '(':
                        break
                    str1 = str1 + i
                    if '(' not in result:
                        array_size_pos = string.rfind(i)
                    else:
                        array_size_pos = find_ch_comma + string[find_ch_comma:].find(i)
                    string = string[:array_size_pos] + string[array_size_pos + 1:]
                string = string.replace(" (", "(", 1)
                string = str1 + " = " + string
        # 实现定义函数的代码转换
        if find_define_func:
            string = string.replace(")", "){", 1)

        # 实现声明函数返回类型的代码转换
        if find_func_type:
            pattern = re.compile(r'[\(,A-Za-z0-9]')
            result = pattern.findall(string, find_func_type.span()[0] + 1)
            if result:
                str1 = ""
                for i in result:
                    if i is '(':
                        break
                    str1 = str1 + i
                    if '(' not in result:
                        array_size_pos = string.rfind(i)
                    else:
                        array_size_pos = find_ch_comma + string[find_ch_comma:].find(i)
                    string = string[:array_size_pos] + string[array_size_pos + 1:]
                string = string.replace(" (", "(", 1)
                string = str1 + " " + string

        # 实现if的代码转换
        if find_if1:
            string = string.replace("$", "==")
            string = string.replace("if1 ", "if (", 1)
            string = string.replace("\n", "){\n", 1)

        # 实现class的代码转换
        if find_class1:
            string = string.replace("\n", "{\n", 1)
        # 实现class的代码转换
        if find_for:
            string = string.replace("循环", "for (", 1)
            string = string.replace("至", "; ", 1)
            string = string.replace("\n", ";){\n", 1)
        # 实现while的代码转换
        if find_while1:
            string = string.replace("$", "==")
            string = string.replace("\n", "){\n", 1)
        # 实现取余的代码转换
        if find_modulus:
            string = string.replace("/", "%")
        # 句号为块结束的标识
        string = string.replace("。", "\n}\n")
        interphase_file.write(string)
        if_pos = ch_comma_pos + 1
        line = line.replace("，", "@", 1)
        ch_comma_pos = line.find('，')
        line = line.replace("otherwise", "else {")

interphase_file.close()

interphase_file = open("interphase.txt", "r", encoding='utf-8')
interphase2_file = open("interphase2.txt", "w+", encoding='utf-8')
lines = interphase_file.readlines()

for line in lines:
    find_if2 = re.search('if ', line)
    find_right_brace = re.search('}', line)
    find_hash = re.search('#', line)
    find_left_brace = re.search('{', line)
    find_public = re.search('public', line)
    find_protected = re.search('protected', line)
    find_private = re.search('private', line)
    find_enum = re.search('enum', line)
    find_virtual = re.search('virtual', line)
    find_template = re.search('template', line)
    define = re.search('define', line)
    find_main = re.search('main', line)
    line = line.replace(" )", ")")
    line = line.replace("inlinee", "inline ")

    line = re.sub(r'[\u4E00-\u9FA5]', "", line)

    line = line.replace("@", '"')
    line = line.replace("!==", "!=")
    line = line.replace("<==", "<=")
    line = line.replace(">==", ">=")
    # 实现导入库的代码转换
    if find_hash:
        line = line.replace("\n", ">\n")
    if line[0] == ';':
        line = line.replace(';', "\n")
    if line[0] == '\n':
        line = line.replace("\n", "", 1)
    if find_main:
        line = line.replace("int", "\nint")
    # 在合适的位置添加;
    if not find_if2 and not find_right_brace and not find_hash and not find_left_brace and not find_public and not find_private and not define and not find_protected and len(
            line) > 1:
        line = line.replace("\n", ";\n")
    # 实现枚举的代码转换
    if find_enum and find_left_brace:
        line = line.replace("\n", "};\n")
    # 实现虚函数的代码转换
    if find_virtual:
        line = line.replace(" virtual", "")
        line = "virtual " + line
    # 实现马模板函数的代码转换
    if find_template:
        line = line.replace("template<typename T>", "")
        line = "template<typename T> " + line
    find_new = re.search('new', line)
    # 实现实例化类的代码转换
    if find_new:
        pattern = re.compile(r'([a-zA-Z]+)')
        result = pattern.findall(line)
        line = result[-1] + " " + line
        line = line.replace(";", "();")
    interphase2_file.write(line)
input_file.close()
interphase_file.close()
interphase2_file.close()

interphase2_file = open("interphase2.txt", "r", encoding='utf-8')

output_file = open("output.txt", "w+", encoding='utf-8')
lines = interphase2_file.readlines()
indent = 0
switch_indent = 0

for line in lines:
    line = line.replace("\t;\n", "")
    line = line.replace("inline", "\ninline")
    line = line.replace("class", "\nclass")
    line = line.replace("struct ", "\nstruct ")
    line = line.replace("struct ", "\nstruct ")
    line = line.replace("friend", "friend class")
    line = line.replace("define", "#define")
    line = line.replace('"~', "/*")
    line = line.replace('~";', "*/")
    line = line.replace('~"', "*/")
    find_new = re.search(';', line)
    find_for2 = re.search('for', line)
    if find_new and not find_for2:
        line = line.replace(" < ", "<")
        line = line.replace(" > ", ">")

    # 实现结构体的代码转换
    find_structVal = re.search('structVar', line)
    if find_structVal:
        line = line.replace("structVar", "")
        line = line.replace("\n", ";\n")
    find_struct = re.search('struct', line)
    if find_struct:
        line = line.replace(";", "{")
    find_switch = re.search('switch', line)
    # 实现switch的代码转换
    if find_switch:
        line = line.replace(";", "){")
    find_case = re.search('case', line)
    find_default = re.search('default', line)
    if find_case or find_default:
        line = line.replace(";\n", " :\n")
    line = line.replace("delete()", "delete[]")
    # 实现倒序赋值的代码转化，如5+2等于b
    if line[0].isdigit():
        ttt = line.find('=')
        line = line[ttt + 2:-2] + " = " + line[0:ttt - 1] + ";\n"

    find_right_brace = re.search('}', line)
    find_left_brace = re.search('{', line)
    find_case2 = re.search('case', line)
    find_default2 = re.search('default', line)
    # 记录switch内部的代码缩进
    if find_case2 or find_default2:
        switch_indent = 0
    find_case2 = re.search('}', line)
    if find_case2:
        switch_indent = 0
    # 记录全局缩进
    if find_right_brace and not find_left_brace:
        indent = indent - 1

    if indent > 0:
        for i in range(indent):
            line = '\t' + line

    if switch_indent > 0:
        for i in range(switch_indent):
            line = '\t' + line

    if find_left_brace and not find_right_brace:
        indent = indent + 1
    find_case3 = re.search('case', line)
    find_default3 = re.search('default', line)
    if find_case3 or find_default3:
        switch_indent = 1
    # 针对类可见性的缩进修改
    line = line.replace("	public", "public")
    line = line.replace("	protected", "protected")
    line = line.replace("	private", "private")
    # 写回双引号内的内容
    pattern = re.compile(r'""')
    result = pattern.findall(line)
    for i in range(len(result)):
        if quotation_list[quotation_pos] == '""':
            quotation_list[quotation_pos] = '@"@"@'
        line = re.sub(r'""', quotation_list[quotation_pos], line, 1)
        quotation_pos = quotation_pos + 1

    # 写回注释
    pattern = re.compile(r'\￥\￥')
    result1 = pattern.findall(line)
    for i in range(len(result1)):
        line = re.sub(r'\￥\￥', annotation_list[annotation_pos], line, 1)
        annotation_pos = annotation_pos + 1
    line = line.replace("￥;", "*/")
    line = line.replace("￥", "/*")
    line = line.replace('@"@"@', '""')
    line = line.replace('`', "")
    line = line.replace(r"\\n", r'\n')
    output_file.write(line)
output_file.close()
