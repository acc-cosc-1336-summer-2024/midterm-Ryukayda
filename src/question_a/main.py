from question_a import test_config, use_global, global_var

if __name__ == "__main__":
    # Demonstrate the use of test_config and use_global functions
    print("Testing configuration:", test_config())
    
    global_var = 0
    print("Initial global_var:", global_var)
    use_global()
    print("Global_var after use_global:", global_var)
#add import