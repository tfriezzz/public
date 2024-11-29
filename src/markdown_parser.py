def split_nodes_delimiter(old_nodes, delimiter=None, text_type=None):
    #new_nodes= []
    bold_snippets = old_nodes.split("**")[1::2]
    italic_snippets = list(filter(None, old_nodes.split("*")[1::2]))
    code_snippets = old_nodes.split("`")[1::2]

    return bold_snippets, italic_snippets, code_snippets

print(split_nodes_delimiter(
    "This is a test of *italic*, **bold****bolder** and **boldest***italic2* and *italic again* and `code``snippets`"
))
