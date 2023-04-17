import csv
import datetime


def read_csv_file(file_name):
    data = []
    with open(file_name, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            data.append(row)
    return data


def generate_html_elements(data):
    sorted_data = sorted(data, key=lambda x: x['BirthDate'])
    html_elements = []
    for entry in sorted_data:
        if entry['DeathDate'] == '':
            entry['DeathDate'] = 'Unknown'
        elif entry['DeathDate'] == 'alive':
            entry['DeathDate'] = 'Present'
        else:
            entry['DeathDate'] = datetime.datetime.strptime(entry['DeathDate'], '%m/%d/%Y').strftime('%Y')
        entry['BirthDate'] = datetime.datetime.strptime(entry['BirthDate'], '%m/%d/%Y').strftime('%Y')
        if entry['DebutDate'] == '':
            entry['DebutDate'] = 'Unknown'
        if entry['LastFilmDate'] == '':
            entry['LastFilmDate'] = 'Unknown'
        if entry['Movies'] != '':
            entry['Movies'] = "<p>Movies: " + entry['Movies'] + "</p>"
        else:
            entry['Movies'] = ''
        html_element = f'''
  <div class="entry">
    <div class="title big">{entry['Name']}</div>
    <div class="body">
        <p>{entry['BirthDate']} - {entry['DeathDate']}</p>
      <p>Debut: {entry['DebutDate']}</p>
      <p>Last Film: {entry['LastFilmDate']}</p>
      {entry['Movies']}
    </div>
  </div>'''
        html_elements.append(html_element)
    return html_elements


def write_html_file(html_elements, output_file):
    with open(output_file, 'w') as file:
        for element in html_elements:
            file.write(element + '\n')


if __name__ == '__main__':
    csv_file_name = 'actors.csv'
    output_html_file = 'output.html'
    csv_data = read_csv_file(csv_file_name)
    html_elements = generate_html_elements(csv_data)
    write_html_file(html_elements, output_html_file)
