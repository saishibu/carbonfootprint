import random

# Generate a random float between 0 and 600
s1 = round(random.uniform(0, 600),2)
s2 = round(random.uniform(0, 600),2)
s3 = round(random.uniform(0, 600),2)
l1 = random.choice([0, 20])
l2 = random.choice([0, 20])
l3 = random.choice([0, 20])
l4 = random.choice([0, 20])
f1 = random.choice([0, 25, 50, 75])

p1 = (s1 + l1)*0.8
p2 = (s2 + l3)*0.8
p3 = (s3 + l3)*0.8
total = p1+p2+p3+(l4x0.8)+(f1*0.8)

data = {'s1':s1, 's2':s2, 's3':s3, 'l1':l1, 'l2':l2, 'l3':l3, 'l4':l4, 'f1':f1, 'p1':p1, 'p2':p2, 'p3':p3, 'total':total}
print(data)
