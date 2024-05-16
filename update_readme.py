
# template readme
with open('Readme_text.md') as f:
    readme_stub = f.read()
with open('Mermaid_Diagramm.md') as f_2:
    readme_stub_2 = f_2.read()
# simple replacement, use whatever stand-in value is useful for you.
readme = readme_stub.replace('{TOC}',readme_stub_2)

with open('README.md','w') as f:
    f.write(readme)