users = [
    {"id": 0, "name": "Hero"},
    {"id": 1, "name": "Dunn"},
    {"id": 2, "name": "Sue"},
    {"id": 3, "name": "Chi"},
    {"id": 4, "name": "Thor"},
    {"id": 5, "name": "Clive"},
    {"id": 6, "name": "Hicks"},
    {"id": 7, "name": "Devin"},
    {"id": 8, "name": "Kate"},
    {"id": 9, "name": "Klein"},
]

#print (users)


friendships = [
    (0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4), 
    (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)
]

for user in users:
    user["friends"] = []

#(0, 1)
#users[0]["friends"].append(users[1])
#users[1]['friends'].append(users[0])

#for friendship in friendships:
#    users[friendship[0]]["friends"].append(users[friendship[1]])
#    users[friendship[1]]["friends"].append(users[friendship[0]])

#tuple unpacking
for i, j in friendships:
    users[i]["friends"].append(users[j])
    users[j]["friends"].append(users[i])
   
#print (users[0])

def number_of_friends (user):
    return len(user["friends"])

#print (number_of_friends(users[2]))

#[2, 3, 3, 3, 2, 3]

#lista = [number_of_friends(user) for user in users]
#print (lista)
total_connections = sum (number_of_friends(user) for user in users)
#print (total_connections)


num_users = len (users)
avg_connections = total_connections / num_users

#print (avg_connections)


#[(0, 2), (1, 3), (2, 3)]

num_friends_by_id = [(user["id"], number_of_friends(user)) for user in users]

#print (num_friends_by_id)

lista_ordenada = sorted (num_friends_by_id, key = lambda num_friends: num_friends[1], reverse=True)
#print (lista_ordenada)

def friends_of_friends_ids_bad (user):
    return [
        foaf["id"]
        for friend in user["friends"]
        for foaf in friend["friends"]
    ]
def not_the_same (user, other_user):
    return user["id"] != other_user["id"]




#exercicio 01
for user in users:
    user["sex"] = []
    user["age"] = []

#print (users)

   
#exercicio 02
dic = {} 
sex = []
friends = []
totalM=0
totalF=0
for user in users: 
    dic["friendsM"] = []
    dic["friendsF"] = []
    dic["id"] = []
    id = user["id"]
    if id %2 ==0 : 
        user["sex"]= "M"
        totalM  += 1 
        dic["friendsM"] = user["sex"]
    else:
        user["sex"] = "F"     
        dic["friendsF"] = user["sex"]
        totalF  += 1 
     
dic["id"] = id

dic[friends][0] = totalM
dic[friends][1] = totalF

print (str(dic))




