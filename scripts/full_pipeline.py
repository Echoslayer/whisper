import subprocess

def run_voice2transcripts():
    subprocess.run(["python", "SELF/scripts/voice2transcripts.py"], check=True)

def run_time_stamp_cleaner():
    subprocess.run(["python", "SELF/scripts/time_stamp_cleaner.py"], check=True)

def run_transcripts_summary():
    subprocess.run(["python", "SELF/scripts/transcripts_summary.py"], check=True)

if __name__ == "__main__":
    print("🚀 Starting full pipeline...")
    
    run_voice2transcripts()
    run_time_stamp_cleaner()
    # run_transcripts_summary()
    print("🎉 Full pipeline completed!")
