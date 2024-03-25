import ansible_runner

# Function to load and list inventory
def load_and_list_inventory():
    # Using ansible-runner to execute the ping playbook and gather hosts
    r = ansible_runner.run(private_data_dir='.', playbook='ping.yml')
    if r.status == "successful":
        print("Inventory hosts ping results:", r.stats)
    else:
        print("Failed to run playbook")

load_and_list_inventory()