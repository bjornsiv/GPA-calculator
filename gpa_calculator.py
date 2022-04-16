import csv
import click

csv_path = "./Grades/grades.csv"
gradesAccepted = ['A', 'B', 'C', 'D', 'E', 'Pass']
headers = ['Name','Grade','Credits']
format_of_CSV = """The file needs to have the following format:"""


@click.group()
def cli():
    pass

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
    with open(csv_path, mode='r+')as file:
        lines = file.readlines()
        lines = [i  for i in lines if len(i)>2]
        point_out = str(points)
        lines.append(name + ',' + grade.capitalize() + ',' + point_out + '\n')
        for line in lines[-1:]:
            file.write(line)
       
    file.close()
    click.echo('Successfully added {} into the list'.format(name))

#WIP
@cli.command(name='remove')
@click.option('-r', '--remove', is_flag=True, help="To remove the last entered grade")
def remove(remove):
    """Removes the last entry to the list to the list"""
    with open(csv_path, 'r') as fr:
        lines = fr.readlines()
        lines = [i  for i in lines if len(i)>2]
        with open(csv_path, 'w') as fw:
            for i, line in enumerate(lines):
                if len(line) != 0 and len(lines)-1 >i:
                    fw.write(line)
    fr.close()  
    click.echo('Successfully removed the last entry to the list')

@cli.command(name='show')
@click.option('-s', '--show', is_flag=True, help="To show all grade in the list")
def show(show):
    """Shows current grades list"""
    csv_data = []
    with open(csv_path, mode='r')as file:
        csv_data += csv.reader(file)
    for row in csv_data:
        print(row)
    file.close()


@cli.command(name='calc')
@click.option('-c', '--calc', is_flag=True, help="To calculate your GPA")
def calculate(calc):
    """Calculates your current GPA"""

    letter_to_number_grade = {
            'A': 5,
            'B': 4,
            'C': 3,
            'D': 2,
            'E': 1
        }
    sum_of_credits, sum_of_credits_x_grade, sum_of_credits_from_passed_subjects = 0, 0, 0
    output = ''
    csv_data = []

    with open(csv_path, mode='r')as file:
        reader = csv.reader(file)
        for row in reader:
            csv_data.append(row)
    file.close()
    for i, key in enumerate(csv_data):
        
        if(i>0 and len(key) > 0):
            
            grade = cleaner(csv_data[i][1])
           
            if grade.capitalize() == 'Pass':
                sum_of_credits_from_passed_subjects += float(cleaner(csv_data[i][2]))
                continue

            grade = letter_to_number_grade[grade]
            credits = float(cleaner(csv_data[i][2]))
            sum_of_credits += credits
            sum_of_credits_x_grade += (credits * grade)
            output = f'Your GPA is: {sum_of_credits_x_grade / sum_of_credits:.2f}  with {sum_of_credits + sum_of_credits_from_passed_subjects:.1f} credits'
    click.echo(output)
    
    return output
    


def cleaner(arg):
    arg = arg.strip(' ')
    arg = arg.strip('"')
    arg = arg.strip('\'')
    arg = arg.strip("'")
    arg = arg.strip("\n")
    return arg



cli.add_command(add)
cli.add_command(remove)
cli.add_command(calculate)
cli.add_command(show)


if __name__ == "__main__":
#    # calling the main function
    cli()
