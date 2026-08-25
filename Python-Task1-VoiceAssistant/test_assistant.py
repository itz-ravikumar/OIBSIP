import voice_assistant
import time
import sys
import os

# We'll inject these voice commands sequentially to simulate a user speaking.
# We are skipping sleep/shutdown/lock to prevent the automated test from disrupting the PC.
commands_to_test = [
    "hello",
    "battery",
    "wikipedia artificial intelligence",
    "volume down",
    "volume up",
    "open calc",
    "screenshot",
    "exit"
]

def mock_listen():
    """Mock the microphone to return test commands."""
    if commands_to_test:
        cmd = commands_to_test.pop(0)
        print(f"\n---> [AUTOMATED TEST] Injecting voice command: '{cmd}'")
        time.sleep(2) # brief pause to simulate human interaction
        return cmd
    return "exit"

def run_tests():
    print("==================================================")
    print("Starting automated tests for Advanced Voice Assistant...")
    print("==================================================")
    
    # Temporarily replace the microphone function with our mock
    voice_assistant.listen = mock_listen
    
    # Run the main loop
    try:
        voice_assistant.main()
        print("\n==================================================")
        print("All automated tests completed successfully!")
        print("==================================================")
    except Exception as e:
        print(f"\n[ERROR] An error occurred during testing: {e}")
        sys.exit(1)

if __name__ == "__main__":
    run_tests()
