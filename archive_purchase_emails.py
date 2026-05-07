"""
archive_purchase_emails.py

Creates the "Purchase Digests/Processed" Gmail label and archives the 58
order confirmation, shipment notification, and delivery update threads
identified in the May 7 2026 purchase digest run.

Prerequisites:
  - gmail_token.json in the same directory (created by setup_gmail_auth.py)
  - pip install google-api-python-client google-auth google-auth-oauthlib
"""

from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

LABEL_NAME = "Purchase Digests/Processed"
LABEL_COLOR = {
    "backgroundColor": "#16a765",
    "textColor": "#ffffff",
}

# All 58 thread IDs across the three categories
ORDER_CONFIRMATIONS = [
    "19dfe97556ebde30",  # Zazzle - Here's The Scoop On Your Order (May 6)
    "19df84471ab3d831",  # Zazzle - Digital Order Scoop (May 5)
    "19df5f68f6498a90",  # Hobby Lobby - Order Confirmation #37692812 (May 5)
    "19df39fb552af7a1",  # Amazon - Ordered: Yotelab Flat Bottom (May 4)
    "19df351ae8b3c748",  # Amazon - Ordered: ICONIC Protein Powder (May 4)
    "19df0bd1194d1aea",  # Amazon - Ordered: iRahmen Picture Frame (May 4)
    "19deb99c96bb3a36",  # Costco - Order Confirmed (May 3)
    "19de915848483b09",  # BabyQuip - Order Confirmation (May 2)
    "19dd3d3aaf2c0c6e",  # Amazon - Ordered: Yotelab + 3 (Apr 28)
    "19db7ff01788a328",  # Amazon - Ordered: TOMS Diana Wedge (Apr 23)
    "19da84b54b1653a4",  # Audible - Thanks, your order is complete (Apr 20)
    "19d9df98cf3e2e79",  # Amazon - Ordered: Physicians Formula (Apr 18)
    "19d9dc0b45dad8a2",  # Walgreens - Order confirmed (Apr 17)
    "19d8d33a4a131661",  # Amazon - Ordered: OurWarm Wedding Card (Apr 14)
    "19d86bbffbc962d0",  # Amazon - Ordered: Remedy Mama Magnesium (Apr 13)
    "19d7d6fcae5132e5",  # Spectrum - Mobile Order Details (Apr 11)
    "19d7c9bdf80380ec",  # Spectrum - We've Received Your Mobile Order (Apr 11)
    "19d79bb9b99df419",  # Amazon - Ordered: Bbmmayy Dog Collar (Apr 10)
    "19d7970cc162db05",  # DoorDash - Order Confirmation from Michaels (Apr 10)
    "19d6d39dc2868262",  # Love in Faith - Order #7374196 confirmed (Apr 8)
    "19d0c097d1754bb9",  # Shapermint - PATRICIA's Order Confirmed (Mar 20)
]

SHIPMENT_NOTIFICATIONS = [
    "19dfe148b18eda4c",  # Hobby Lobby - Your order is on the way (May 6)
    "19dfc888cdd69778",  # Amazon - Shipped: Aveda Tea Bags (May 6)
    "19dfc0a5f0d81dc8",  # Amazon - Shipped: ICONIC Protein Powder (May 6)
    "19dfb09121d2dc37",  # Amazon - Shipped: iRahmen Picture Frame (May 6)
    "19dbcd3439a0f52e",  # Amazon - Shipped: TOMS Diana Wedge (Apr 24)
    "19da2e0123c6ae6b",  # Amazon - Shipped: GoBiotix Magnesium + 8 (Apr 18)
    "19d9bd831b0e665b",  # Amazon - Out for delivery: Wedding Card (Apr 17)
    "19d93badb1a47dde",  # Amazon - Shipped: Nowful Sleep Aid (Apr 16)
    "19d9201d8649652d",  # Stitch Fix - Your package arriving today (Apr 15)
    "19d8e08f24e5181a",  # Amazon - Shipped: CELSIUS Peach (Apr 14)
    "19d8df9403ddc939",  # Amazon - Shipped: OurWarm Wedding Card (Apr 14)
    "19d8c28fcfdf70e0",  # Stitch Fix - Get ready for new fave looks (Apr 14)
    "19d874846f59ce81",  # Amazon - Shipped: Remedy Mama Magnesium (Apr 13)
    "19d86b8f01f631be",  # Spectrum - Delivery Scheduled for Today (Apr 13)
    "19d81910e6c8f001",  # Spectrum - Track Your Mobile Order (Apr 12)
    "19d7b95eedbe80bb",  # Amazon - Shipped: Bbmmayy Dog Collar (Apr 11)
    "19d77f4d11a56099",  # Love in Faith - Shipment out for delivery (Apr 10)
    "19d6ea3773284070",  # PayPal - Love in Faith order on its way (Apr 8)
    "19d1e80df7c594e4",  # Shapermint - Your order is on its way (Mar 24)
]

DELIVERY_UPDATES = [
    "19dfead0ad647b05",  # Amazon - Delivered: Aveda Tea Bags (May 6)
    "19dfead073ff4663",  # Amazon - Delivered: ICONIC Protein Powder (May 6)
    "19dfeacfe15e7114",  # Amazon - Delivered: iRahmen Picture Frame (May 6)
    "19dda2ff15224997",  # Amazon - Delivered: Yotelab + 3 (Apr 29)
    "19da676f02d4ec98",  # Amazon - Delivered: GoBiotix Magnesium + 8 (Apr 19)
    "19d967c3cc516642",  # Stitch Fix - Your receipt is ready (Apr 16)
    "19d959ccfa9295fa",  # Amazon - Delivered: Nowful Sleep Aid (Apr 16)
    "19d923a79b8b2544",  # Stitch Fix - Your order was delivered (Apr 15)
    "19d921302871390d",  # Amazon - Delivered: CELSIUS Peach (Apr 15)
    "19d91e6d6d9e3244",  # Amazon - Delivery update: Wedding Card (Apr 15)
    "19d882fd91eb5dc1",  # Amazon - Delivered: Remedy Mama Magnesium (Apr 13)
    "19d87cc0f3ecc931",  # Spectrum - Mobile Order Delivered (Apr 13)
    "19d7d99f2b14846b",  # Amazon - Delivered: Bbmmayy Dog Collar (Apr 11)
    "19d79b7d25e85f4c",  # DoorDash - Final receipt from Michaels (Apr 10)
    "19d7987a3c2b0e91",  # DoorDash - No-contact delivery from Michaels (Apr 10)
    "19d793ed070fe46e",  # Love in Faith - Your order is home (Apr 10)
    "19d2dfa3eeebd3ad",  # Shapermint - Delivery Notification (Mar 27)
    "19d0cd7baec1cf4d",  # Amazon - Delivery update: Hamilton Beach (Mar 20)
]

ALL_THREAD_IDS = ORDER_CONFIRMATIONS + SHIPMENT_NOTIFICATIONS + DELIVERY_UPDATES


def get_gmail_service():
    creds = Credentials.from_authorized_user_file("gmail_token.json")
    if creds.expired and creds.refresh_token:
        creds.refresh(Request())
    return build("gmail", "v1", credentials=creds)


def get_or_create_label(svc, name, color):
    existing = svc.users().labels().list(userId="me").execute().get("labels", [])
    for label in existing:
        if label["name"] == name:
            print(f"Label already exists: '{name}' (id: {label['id']})")
            return label["id"]

    body = {"name": name, "labelListVisibility": "labelShow",
            "messageListVisibility": "show", "color": color}
    created = svc.users().labels().create(userId="me", body=body).execute()
    print(f"Created label: '{name}' (id: {created['id']})")
    return created["id"]


def label_and_archive(svc, thread_id, label_id):
    svc.users().threads().modify(
        userId="me",
        id=thread_id,
        body={"addLabelIds": [label_id], "removeLabelIds": ["INBOX"]},
    ).execute()


def main():
    svc = get_gmail_service()
    label_id = get_or_create_label(svc, LABEL_NAME, LABEL_COLOR)

    total = len(ALL_THREAD_IDS)
    print(f"\nArchiving {total} threads...")
    for i, thread_id in enumerate(ALL_THREAD_IDS, 1):
        try:
            label_and_archive(svc, thread_id, label_id)
            print(f"  [{i:02d}/{total}] archived {thread_id}")
        except Exception as e:
            print(f"  [{i:02d}/{total}] FAILED  {thread_id}: {e}")

    print(f"\nDone. {total} threads labelled '{LABEL_NAME}' and removed from inbox.")


if __name__ == "__main__":
    main()
