import sqlite3
from app.service.database import DB_PATH


def get_connection():
    return sqlite3.connect(DB_PATH)


def add_vendor(
    vendor_name,
    contact_person,
    phone,
    email,
    gst,
    pan,
    address,
    payment_terms,
    category,
    currency,
    bank_details
):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO vendors (
            vendor_name,
            contact_person,
            phone,
            email,
            gst,
            pan,
            address,
            payment_terms,
            category,
            currency,
            bank_details
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        vendor_name,
        contact_person,
        phone,
        email,
        gst,
        pan,
        address,
        payment_terms,
        category,
        currency,
        bank_details
    ))

    conn.commit()
    conn.close()


def get_all_vendors():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM vendors
        ORDER BY vendor_name
    """)

    rows = cursor.fetchall()

    conn.close()

    return rows


def delete_vendor(vendor_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM vendors WHERE id=?",
        (vendor_id,)
    )

    conn.commit()
    conn.close()