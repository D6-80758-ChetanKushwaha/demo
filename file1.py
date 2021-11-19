print("Hello World")

def main():
    print("Hello World")
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

# generate random data for training
def generate_data(n):
    data = []
    for i in range(n):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        label = 1 if x**2 + y**2 < 1 else 0
        data.append((x, y, label))
    return data