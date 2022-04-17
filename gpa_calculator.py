import csv
import click

csv_path = "./Grades/grades.csv"
gradesAccepted = ['A', 'B', 'C', 'D', 'E', 'Pass']

#Currently not in use...
headers = ['Name','Grade','Credits']


@click.group()
def cli():
    pass

#click command to add new entries to the csv file
@cli.command(name='add')
@click.option('-a', '--add', is_flag=True, help="To add a grade", nargs=3, type=(str,str, float))
@click.argument('name')
@click.argument('grade')
@click.argument('points')
def add(add, name, grade, points):
    """Adds a grade to the list\n
            It takes 3 arguments: Name, Grade, Points \n
            Name is the Subjects Name\n
            Grade must be: 'A', 'B', 'C', 'D', 'E', 'Pass'\n
            And points is the subjects credit\n
    """
    if (grade in gradesAccepted):
        with open(csv_path, mode='r+')as file:
            lines = file.readlines()
            lines = [i  for i in lines if len(i)>2]
            point_out = str(points)
            lines.append(name + ',' + grade.capitalize() + ',' + point_out + '\n')
            for line in lines[-1:]:
                file.write(line)
        
        file.close()
        click.echo('Successfully added {} into the list'.format(name))
    else: click.echo('The input field {} is not a accepted grade'.format(grade))

#click command to remove the last entry to the csv file
@cli.command(name='remove')
@click.option('-r', '--remove', is_flag=True, help="To remove the last entered grade")
def remove(remove):
    """Removes the last entry to the list"""
    with open(csv_path, 'r') as fr:
        lines = fr.readlines()
        lines = [i  for i in lines if len(i)>2]
        with open(csv_path, 'w') as fw:
            for i, line in enumerate(lines):
                if len(line) != 0 and len(lines)-1 >i:
                    fw.write(line)
    fr.close()  
    click.echo('Successfully removed the last entry to the list')

#Shows the content of the csv file
@cli.command(name='show')
@click.option('-s', '--show', is_flag=True, help="To show all grade in the list")
def show(show):
    """Shows current grades in list"""
    csv_data = []
    with open(csv_path, mode='r')as file:
        csv_data += csv.reader(file)
    for row in csv_data:
        #print(row)
        print('{:<15}  {:<15}  {:<20}'.format(*row))
    file.close()

#Calculates the GPA based on the grades in the csv
@cli.command(name='calc')
@click.option('-c', '--calc', is_flag=True, help="To calculate your GPA")
def calculate(calc):
    """Calculates your current GPA
        It will use the data from ./Grades/grades.csv to calculate your GPA
    """  
    letter_to_number_grade = {'A': 5,'B': 4,'C': 3,'D': 2,'E': 1}
    sum_credits, sum_credits_x_grade, sum_credits_passed = 0, 0, 0
    output = ''
    csv_data = []

    with open(csv_path, mode='r')as file:
        reader = csv.reader(file)
        for row in reader:
            csv_data.append(row)
    file.close()
    for i, data in enumerate(csv_data):
        if(i>0 and len(data) > 0):
            grade = cleaner(csv_data[i][1])
            if grade.capitalize() == 'Pass':
                sum_credits_passed += float(cleaner(csv_data[i][2]))
                continue

            grade = letter_to_number_grade[grade]
            credits = float(cleaner(csv_data[i][2]))
            sum_credits += credits
            sum_credits_x_grade += (credits * grade)
            output = f'Your GPA is: {sum_credits_x_grade / sum_credits:.2f}  with {sum_credits + sum_credits_passed:.1f} credits'
    click.echo(output)
    return output

#cleaner function to strip extra ', ", \, \n from the in/out of the csv
def cleaner(arg):
    arg = arg.strip(' ')
    arg = arg.strip('"')
    arg = arg.strip('\'')
    arg = arg.strip("'")
    arg = arg.strip("\n")
    return arg

#Add commands to the click group
cli.add_command(add)
cli.add_command(remove)
cli.add_command(calculate)
cli.add_command(show)

if __name__ == "__main__":
    # calling the main function
    cli()