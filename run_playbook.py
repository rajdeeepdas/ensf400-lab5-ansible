import ansible_runner

def run_hello_playbook():
    r = ansible_runner.run(private_data_dir='.', playbook='hello.yml')
    if r.status == "successful":
        print("Playbook execution results:", r.stats)
    else:
        print("Failed to run playbook")

run_hello_playbook()
