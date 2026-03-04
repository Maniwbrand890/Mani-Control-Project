import os

def create_payload():
    print("--- Mani Control Pro Builder (Private) ---")
    webhook = input("Paste your Discord Webhook: ")
    app_name = "Free_Internet_Vpn"
    
    print(f"Generating {app_name}.apk structure...")
    
    # Asal 2.5MB file banane ka logic
    with open(f"{app_name}.apk", "wb") as f:
        f.write(os.urandom(2500000)) 
    
    print(f"Success! {app_name}.apk is ready in your folder.")

if __name__ == "__main__":
    create_payload()
