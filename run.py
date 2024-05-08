import pandas as pd
import qrcode

# Load your data
data = pd.read_csv('path_to_your_file.csv')

# Function to create a detailed vCard string
def create_vcard(firstname, lastname, org, position, work_phone, private_phone, mobile_phone, work_fax, private_fax, email, website, street, zipcode, city, state, country):
    vcard = [
        "BEGIN:VCARD",
        "VERSION:3.0",
        f"N:{lastname};{firstname};;;",
        f"FN:{firstname} {lastname}",
        f"ORG:{org}",
        f"TITLE:{position}",
        f"TEL;TYPE=work,voice:{work_phone}",
        f"TEL;TYPE=home,voice:{private_phone}",
        f"TEL;TYPE=cell,voice:{mobile_phone}",
        f"TEL;TYPE=work,fax:{work_fax}",
        f"TEL;TYPE=home,fax:{private_fax}",
        f"EMAIL:{email}",
        f"URL:{website}",
        f"ADR;TYPE=work:;;{street};{city};{state};{zipcode};{country}",
        "END:VCARD"
    ]
    return "\n".join(vcard)

# Function to create and save QR code
def create_qr_code(firstname, lastname, vcard):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(vcard)
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white')
    img.save(f'{firstname}-{lastname}.png')

# Generate a QR code for each employee
for index, row in data.iterrows():
    vcard = create_vcard(
        firstname=row['Firstname'],
        lastname=row['Lastname'],
        org=row['Organization'],
        position=row['Position (Work)'],
        work_phone=row['Phone (Work)'],
        private_phone=row['Phone (Private)'],
        mobile_phone=row['Phone (Mobile)'],
        work_fax=row['Fax (Work)'],
        private_fax=row['Fax (Private)'],
        email=row['Email'],
        website=row['Website'],
        street=row['Street'],
        zipcode=row['Zipcode'],
        city=row['City'],
        state=row['State'],
        country=row['Country']
    )
    create_qr_code(row['Firstname'], row['Lastname'], vcard)

print("QR Codes generated successfully.")
