import socket
import subprocess
import sys

# === USER CONFIGURATION ===

WALLET = input("Enter your Worker Name (e.g., binanceuser.001): ")
POOL_URL = input("Enter your pool URL (e.g., stratum+tcp://etc.poolbinance.com:1800): ")
GPU_ID = input("Enter your GPU ID (e.g., 0): ")
COIN = input("Enter the coin you want to mine (e.g., ETC): ")

# Path to lolMiner — MUST be correct
# ---------------------------------------------------------------
# 🔧 How to download and set up lolMiner (Windows):
# 1. Go to: https://github.com/Lolliedieb/lolMiner-releases
# 2. Download the latest ZIP file, e.g., lolMiner_v1.xx_Win64.zip
# 3. Extract the ZIP to a folder, e.g., C:\Miners\lolMiner\
# 4. Copy the full path to lolMiner.exe and paste it below
# ---------------------------------------------------------------
MINER = r"C:\Path\To\lolMiner.exe"  # <- ← ← Provide full path to lolMiner.exe

# === CHECKING CONNECTION TO POOL ===

try:
    host, port = POOL_URL.replace("stratum+tcp://", "").split(":")
    socket.create_connection((host, int(port)), timeout=5).close()
    print("Connection to pool successful.")
except Exception as err:
    print("Connection to pool failed:", err)
    sys.exit(1)

# === STARTING MINER ===

cmd = [
    MINER,
    "--coin", COIN,
    "--pool", POOL_URL,
    "--user", WALLET,
    "--pass", "x",
    "--tls", "0",
    "--devices", GPU_ID,
    "--apiport", "42000"
]

print("Starting miner...")
proc = subprocess.Popen(cmd)
print(f"Miner is running (PID: {proc.pid})")
print("Stats available at: http://127.0.0.1:42000/summary")
