def my_home(name, *people, **mask):
    print(name)
    print(people)
    print(mask)


my_home('我家', 'Dad', 'Mom', 'Bro', 'Sis', Adult=100, child=50)