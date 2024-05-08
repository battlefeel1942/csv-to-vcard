
# Employee QR Code Generator

This project generates QR codes for each employee using their detailed contact information and saves each QR code as an image file.

## Requirements

- Python 3.8 or higher
- Libraries: `pandas` and `qrcode`. Install them using:
```bash
pip install pandas qrcode[pil]
```

## Usage

1. Prepare your CSV file containing employee data with the following columns: Firstname, Lastname, Organization, Position (Work), Phone (Work), Phone (Private), Phone (Mobile), Fax (Work), Fax (Private), Email, Website, Street, Zipcode, City, State, Country.
2. Place the CSV file in the same directory as the script.
3. Run the script. QR codes will be saved in the same directory with the naming format `Firstname-Lastname.png`.

## Detailed Information

Each QR code is generated containing a vCard with the following details:
- Full name
- Organization and position
- Work, private, and mobile phone numbers
- Work and private fax numbers
- Email and website
- Work address (street, city, state, zip, country)

The generated QR codes can be used to easily share and scan employee contact information using mobile devices.

## Contributing

Contributions to this project are welcome. Please fork the repository and submit a pull request with your enhancements.

## License

This project is open source and available under the MIT License.
