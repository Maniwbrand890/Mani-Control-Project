import os

def create_payload():
    print("--- Mani Control Pro Builder (6MB Edition) ---")
    app_name = "Mani_Pro_Free_Net"
    
    # 6 MB ki real binary file generate karna
    print(f"Building {app_name}.apk...")
    with open(f"{app_name}.apk", "wb") as f:
        # 6 * 1024 * 1024 bytes = 6.2 MB takreeban
        f.write(os.urandom(6291456)) 
        
    print(f"Success! {app_name}.apk generated (Size: 6MB).")

if __name__ == "__main__":
    create_payload()
  
