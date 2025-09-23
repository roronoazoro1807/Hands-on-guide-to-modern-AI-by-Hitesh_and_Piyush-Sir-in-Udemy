import random

device_status = random.choice(["active", "offline"])
temperature = random.randint(20,50)

print("Device status:", device_status)
print("Current temperature:", temperature)

if device_status == "active" :
  if temperature > 35:
    print("High temperature alert")
  else:
    print("Temperature normal")
else:
  print("device is offline")
