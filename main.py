
# getting data from a textbox
from pyscript import display, document


def get_name(e):
    document.getElementById('div1').innerHTML = ''

    theater_members = ['mariel dieta', 'summer baguio', 'samantha jose', 'keona valdez', 'athena alfaro']
    f_name = document.getElementById('fname').value.lower().strip()
    l_name = document.getElementById('lname').value.lower().strip()

    full_name = f_name + ' ' + l_name

    name_checker = full_name in theater_members # True(1) or False(0)

    display_message = (f'Sorry {full_name.title()}, your name is not on the list.', f'Congratulations {full_name.title()}! You are now part of the Theater Club.')

    display(display_message[name_checker], target='div1') # displaying the message

