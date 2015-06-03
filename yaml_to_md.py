import yaml
from io import StringIO


def md_from_yaml_file(file_path, main_field, fields_to_leave):
    s = StringIO()
    l = yaml.load(open(file_path).read())
    for d in l:
        s.write('* {0}\n'.format(str(d[main_field])))
        for f in fields_to_leave:
            s.write('  * {0}: {1}\n'.format(f, str(d[f])))

    return s.getvalue()

if __name__ == '__main__':
    with open('books.md', 'w') as f:
        f.write(md_from_yaml_file('books', 'title', ['author', 'score']))
    with open('films.md', 'w') as f:
        f.write(md_from_yaml_file('films', 'title', ['score']))
    with open('vg.md', 'w') as f:
        f.write(md_from_yaml_file('vg', 'title', ['score']))

    with open('quotes.md', 'w') as f:
        l = yaml.load(open('quotes').read())
        for d in l:
            f.write('* ' + d['quote'].replace('\n', '  \n').rstrip() + '\n')
            f.write('  * ~' + d['source'] + '\n')
