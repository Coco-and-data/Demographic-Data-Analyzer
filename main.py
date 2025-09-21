from demographic_data_analyzer import calculate_demographic_data

print("Testing demographic data analyzer...")
print("=" * 50)

try:
    result = calculate_demographic_data(print_data=True)
    
    print("\n" + "=" * 50)
    print("SUCCESS: All calculations completed!")
    print("=" * 50)
        print("\nReturned values:")
    print("-" * 30)
    for key, value in result.items():
        print(f"{key}: {value}")
        
except Exception as e:
    print(f"\nERROR: {e}")
    print("Check your internet connection and try again.")
