import sys
import json
import untangle


def file_reading():
    """
    reads the file that is after the < symbol
    :return: the headers list and the data list
    """
    return sys.stdin.read().strip()


def xml2csv(file):
    """
    :return:
    """
    xml = untangle.parse(file)

    header = xml.file.headers.cdata

    header1 = header.split(",")
    header1 = [header1[i].replace(" ", "_") for i in range(len(header1))]

    data = []
    for record in xml.file.data.record:
        data.append(",".join([getattr(record, item).cdata for item in header1]))

    return header, data


def json2csv(file):
    """
    :return:
    """
    data = json.loads(file)

    headers = data['headers']
    header = ','.join(i for i in headers)

    jmain = data['data']
    # a = data['data'][0]

    main_d = []
    for i in range(len(jmain)):
        main_d.append(",".join(data['data'][i][item] for item in headers))

    return header, main_d


if __name__ == "__main__":
    argument = sys.argv[1]

    if argument == 'xml':
        file = file_reading()
        header, data = xml2csv(file)
        print(header)
        for i in data:
            print(i)

    elif argument == 'json':
        file = file_reading()
        header, data = json2csv(file)
        print(header)
        for i in data:
            print(i)

    else:
        print('Check argument, only html, xml or json are acceptable')
