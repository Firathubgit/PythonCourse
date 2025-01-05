import requests
from pprint import pprint

API_Key = "12161~wJcBPCvzMB8UX7aZNYKP4ckTPXcYfDRmFEHrLwcy38THyF8Dz7nr6JRCaPx9RkkU"

base_url = "https://hv.instructure.com/"

headers = {
    "Authorization": f"Bearer {API_Key}"
}

profile_pic_full_path = r"C:\Users\loki_\Documents\FiratDevFolder\PythonCourse\Facepic128x128.jpg"

url_request_file_upload = f"{base_url}api/v1/users/self/files"

canvas_filename = "my_new_fancy_profile_pic.jpg"

print("=== [1] Begär uppladdnings-URL ===")
data = {
    "name": canvas_filename,
    "parent_folder_path": "profile pictures"
}
resp = requests.post(url_request_file_upload, headers=headers, data=data)

print("[DEBUG] Statuskod:", resp.status_code)
print("[DEBUG] Text:", resp.text)
print()

try:
    resp_json = resp.json()
except Exception as e:
    print("[FEL] Kunde inte tolka JSON:", e)
    exit()

upload_url = resp_json.get("upload_url")
upload_params = resp_json.get("upload_params")
if not upload_url or not upload_params:
    print("Fel: kunde inte hitta 'upload_url'/'upload_params'. Avbryter.")
    exit()

print("=== [2] Ladda upp filen ===")
with open(profile_pic_full_path, "rb") as f:
    files = {"file": f}
    upload_resp = requests.post(upload_url, data=upload_params, files=files)

print("[DEBUG] Statuskod:", upload_resp.status_code)
print("[DEBUG] Text:", upload_resp.text)
print()

try:
    upload_json = upload_resp.json()
except Exception as e:
    print("[FEL] Kunde inte tolka JSON (upload):", e)
    exit()

pprint(upload_json)

file_id = upload_json.get("id")
file_uuid = upload_json.get("uuid")
file_url = upload_json.get("url")

print("\n=== [2b] Uppladdad filinfo ===")
print("file_id:  ", file_id)
print("file_uuid:", file_uuid)
print("file_url:", file_url)
print()

if not file_id:
    print("Fel: ingen 'id' från uppladdningen – avbryter.")
    exit()

url_update_profile = f"{base_url}api/v1/users/self"

def try_avatar_update(payload_description, payload_dict):
    """
    Hjälpfunktion för att skicka PUT /api/v1/users/self
    med en viss data = payload_dict.
    """
    print(f"=== [3] Sätter avatar via: {payload_description} ===")
    print("[DEBUG] data =", payload_dict)
    put_resp = requests.put(url_update_profile, headers=headers, data=payload_dict)
    print("[DEBUG] Statuskod:", put_resp.status_code)

    try:
        put_json = put_resp.json()
        print("[DEBUG] JSON-svar:")
        pprint(put_json)
    except Exception as e:
        print("[DEBUG] Rå text:", put_resp.text)
        print("[FEL] Kunde inte tolka JSON (PUT):", e)

    print()

    return put_resp.status_code

status_1 = try_avatar_update(
    "user[avatar][token] = file_id",
    {"user[avatar][token]": file_id}
)
if 200 <= status_1 < 300:
    print("[INFO] Det verkar ha lyckats med 'token=file_id'")
    print("Kolla i Canvas-profilen om bilden syns!")
    exit()

status_2 = try_avatar_update(
    "user[avatar][token] = file_uuid",
    {"user[avatar][token]": file_uuid}
)
if 200 <= status_2 < 300:
    print("[INFO] Det verkar ha lyckats med 'token=file_uuid'")
    print("Kolla i Canvas-profilen om bilden syns!")
    exit()

status_3 = try_avatar_update(
    "user[avatar][url] = file_url",
    {"user[avatar][url]": file_url}
)
if 200 <= status_3 < 300:
    print("[INFO] Det verkar ha lyckats med 'url=file_url'")
    print("Kolla i Canvas-profilen om bilden syns!")
    exit()

print("[SLUT] Alla tre varianter gav icke-200-svar. Kolla debug-utskriften ovan.")
