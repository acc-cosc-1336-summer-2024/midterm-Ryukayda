
# Global variable
global_var = 0

def use_global():
    global global_var
    global_var += 1

def demonstrate_global_variable_change():
    global global_var
    # Reset the global variable before demonstration
    global_var = 0
    print(f"Initial value of global_var: {global_var}")
    use_global()
    print(f"Value of global_var after calling use_global: {global_var}")

if __name__ == "__main__":
    demonstrate_global_variable_change()

#write functions here, don't add input('') statements here!
def test_config():
    return True
