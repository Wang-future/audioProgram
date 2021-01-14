import ast

src = '''
ial = 10
'''

ast_node = ast.parse(src, "msg.log", mode="exec")

print(ast.dump(ast_node))