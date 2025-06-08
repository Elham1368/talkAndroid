from configs.appium_config import initialize_driver

try:
    driver = initialize_driver()
    print("Driver initialized successfully!")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    if 'driver' in locals():
        print("hiiiiiiiiiiiiiiiii")
