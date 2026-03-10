def tower_of_hanoi(n, source, target, path):
    if n == 1:
        print(f"move the disk 1 from {source} to {target}")
        return
    tower_of_hanoi(n-1, source, path, target)
    print(f"move the disk {n} from {source} to {target}")
    tower_of_hanoi(n-1, path, target, source)
num_disks = int(input("Enter the number of disks: "))
tower_of_hanoi(num_disks, 'A', 'B' , 'C')