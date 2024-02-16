import json
print("Interface Status")
print("================================================================================")
print("DN                                     Description           Speed    MTU  ")
print("-------------------------------------------------- --------------------  ------  ------")

file = open("sample-data.json", "r")
data = json.load(file)
for item in data['imdata']:
    print(f"{item['l1PhysIf']['attributes']['dn']}                               {item['l1PhysIf']['attributes']['speed']}  {item['l1PhysIf']['attributes']['mtu']}")