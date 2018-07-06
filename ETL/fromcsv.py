import sys
from jinja2 import Environment

HTML = """
<html>
<body>
<table>
<tr>{% for j in title %}<th>{{j}}</th>{% endfor %}</tr>
{% for i in range(rows) %}<tr>{% for j in range(cols) %}<td>{{main[i][j]}}</td>{% endfor %}</tr>
{% endfor %}</table>
</body>
</html>
"""

JSON = """{
  "headers":[{{title}}],
  "data":[
    {% for i in range(rows-1) %}{
      {% for j in range(cols-1) %}{{header[j]}}:"{{main[i][j]}}", {% endfor %}{{header[cols-1]}}:"{{main[i][cols-1]}}"
    },
    {% endfor %}
    {
      {% for j in range(cols-1) %}{{header[j]}}:"{{main[rows-1][j]}}", {% endfor %}{{header[cols-1]}}:"{{main[rows-1][cols-1]}}"
    }
  ]
}
"""

XML = """<?xml version="1.0"?>
<file>
  <headers>{% for j in range(cols) %}{{header[j]}}{% endfor %}</headers>
  <data>{% for i in range(rows) %}
    <record>
      {% for j in range(cols) %}<{{title[j]}}>{{main[i][j]}}</{{title[j]}}>{% endfor %}
    </record>{% endfor %}
  </data>
</file>
"""


def file_reading():
    """
    reads the file that is after the < symbol
    :return: the headers list and the data list
    """
    data = sys.stdin.read().strip().split("\n")
    header = data[0].rstrip().split(',')
    data = [data[i].rstrip().split(',') for i in range(1, len(data))]

    return header, data


def csv2html(header, data, HTML):
    """
    :return:
    """
    print(header)
    print(data)
    return Environment().from_string(HTML).render(title=header,
                                                  main=data,
                                                  rows=len(data),
                                                  cols=len(header))


def csv2json(header, data, JSON):
    """
    :return:
    """
    title = ', '.join(map(lambda x: '"' + x + '"', header))
    json_header = ['"' + header[i] + '"' for i in range(len(header))]
    return Environment().from_string(JSON).render(title=title,
                                                  main=data,
                                                  header=json_header,
                                                  rows=len(data),
                                                  cols=len(header))


def csv2xml(header, data, XML):
    """
    :return:
    """
    xml_header = [header[i].replace(" ", "_") for i in range(len(header))]

    header_ = header[len(header) - 1]
    header = [header[i] + "," for i in range(len(header) - 1)]
    header.append(header_)

    return Environment().from_string(XML).render(title=xml_header,
                                                 header=header,
                                                 main=data,
                                                 rows=len(data),
                                                 cols=len(header))


if __name__ == "__main__":
    argument = sys.argv[1]

    if argument == 'html':
        header, data = file_reading()
        print(csv2html(header, data, HTML))

    elif argument == 'xml':
        header, data = file_reading()
        print(csv2xml(header, data, XML))

    elif argument == 'json':
        header, data = file_reading()
        print(csv2json(header, data, JSON))

    else:
        print('Check argument, only html, xml or json are acceptable')
