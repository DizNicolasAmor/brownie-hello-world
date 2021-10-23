from brownie import accounts, config, HelloWorld

def main():
    account = accounts[0]
    helloWorldDeployed = HelloWorld.deploy({ "from": account })
    greeting = helloWorldDeployed.sayHelloWorld()
    print(greeting)
