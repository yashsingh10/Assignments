def a(b):
    try:
        return [float(x) for x in b.split(',')]
    except ValueError:
        return []

def z(c, d):
    e = sum(c)
    f = len(c)
    return e / f if f else 0

def y(g):
    if g >= 90:
        return 'A'
    elif g >= 80:
        return 'B'
    elif g >= 70:
        return 'C'
    elif g >= 60:
        return 'D'
    return 'F'

def p():
    i = input("Enter number of learners: ")
    try:
        j = int(i)
    except ValueError:
        j = 0

    k = {}
    for l in range(j):
        m = input(f"Name of student {l + 1}: ").strip()
        n = input(f"Scores for {m} (comma-separated): ").strip()
        o = a(n)
        if o:
            k[m] = o
    return k

def q(k):
    s = []
    t = None
    for u, v in k.items():
        w = z(v)
        x = max(v)
        y_ = min(v)
        z_ = y(w)
        s.append((u, v, w, x, y_, y_))
        if not t or w > t[2]:
            t = (u, w)
    return s, t

def r():
    s = p()
    t, u = q(s)
    print("\n-- RESULTS --")
    for v in t:
        print(f"{v[0]}: Scores={v[1]}, Avg={v[2]:.2f}, Max={v[3]}, Min={v[4]}, Grade={v[5]}")
    print(f"\nTop student: {u[0]} with Avg={u[1]:.2f}")
    try:
        with open('output.txt', 'w') as f:
            for v in t:
                f.write(f"{v[0]}: Scores={v[1]}, Avg={v[2]:.2f}, Max={v[3]}, Min={v[4]}, Grade={v[5]}\n")
            f.write(f"\nTop student: {u[0]} with Avg={u[1]:.2f}")
        print("Saved to output.txt")
    except Exception as e:
        print(f"Error writing to file: {e}")

if __name__ == "__main__":
    r()
