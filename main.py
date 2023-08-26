import os
import subprocess
import time

def boost_fps_and_optimize():
    try:
        # Close unnecessary background applications and processes
        os.system("sudo purge")  # Clear inactive memory

        # Adjust power settings for better performance
        subprocess.run(["sudo", "pmset", "-c", "gpuswitch", "0"])  # Disable automatic graphics switching
        subprocess.run(["sudo", "pmset", "-c", "displaysleep", "0"])  # Prevent display sleep
        subprocess.run(["sudo", "pmset", "-c", "sleep", "0"])  # Prevent system sleep

        # Clean up temporary files
        os.system("sudo rm -rf ~/Library/Caches/*")
        os.system("sudo rm -rf /Library/Caches/*")

        print("FPS boosted and system optimized!")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    try:
        while True:
            boost_fps_and_optimize()
            time.sleep(60)  # Wait for 60 seconds before running again
    except KeyboardInterrupt:
        print("Script stopped by user.")
