import subprocess

data = subprocess.check_output(
    ['netsh', 'wlan', 'show', 'profiles'],
    text=True,
    errors='backslashreplace'
).split('\n')

profiles = []

for line in data:
    if "All User Profile" in line:
        profiles.append(line.split(":")[1].strip())

print("{:<30} | {}".format("WiFi Name", "Password"))
print("-" * 50)

for profile in profiles:
    try:
        results = subprocess.check_output(
            ['netsh', 'wlan', 'show', 'profile', f'name={profile}', 'key=clear'],
            text=True,
            errors='backslashreplace'
        ).split('\n')

        password = ""
        for line in results:
            if "Key Content" in line:
                password = line.split(":")[1].strip()
                break

        print("{:<30} | {}".format(profile, password))

    except Exception:
        print("{:<30} | ERROR".format(profile))