x = [ [5,2,3], [10,8,9] ] 

x[1] = [15,8,9]
print(x)

# # //////////////////////////////

students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
students[0]['last_name'] = 'Bryant'
print(students[0])


# # /////////////////////////////////

sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
sports_directory['soccer'][0]= 'Andres'
print(sports_directory['soccer'])

# # /////////////////////////////////////

z = [ {'x': 10, 'y': 20} ]
z [0]['y'] = 30
print(z)

# # /////////////////////////////////


students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ] 

def iterate_Dictionary(list):
    for i in range(0, len(list)):
        output = ""
        for key,val in list[i].items():
            output += f" {key} - {val} "
        print(output)   

iterate_Dictionary(students)


def iterate_Dictionary2(key_name,list):
    for i in range(0, len(list)):
        for key,val in list[i].items():
            if key == key_name:
                print(val)

iterate_Dictionary2('first_name',students)
iterate_Dictionary2('last_name',students)

# /////////////////////////////////////////

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(dict):
    for key,val in dict.items():
        print('----------------') 
        print(f"{len(val)} {key}")
        for i in range(0,len(val)):
            print(val[i])
printInfo(dojo)